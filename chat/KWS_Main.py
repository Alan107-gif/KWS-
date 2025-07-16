import os
import ssl
import socket
import threading
import sys
from pathlib import Path

import kws_setup

HOME_DIR = Path.home() / 'KWS'
CONFIG_FILE = HOME_DIR / 'config.cfk'

DEFAULT_SERVER = 'localhost:5000'

def ensure_setup():
    if not HOME_DIR.exists():
        kws_setup.setup()
        sys.exit(0)


def load_config():
    server = DEFAULT_SERVER
    username = 'user'
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            for line in f:
                if line.startswith('server='):
                    server = line.strip().split('=', 1)[1]
                if line.startswith('username='):
                    username = line.strip().split('=', 1)[1]
    else:
        with open(CONFIG_FILE, 'w') as f:
            f.write(f'server={server}\nusername={username}\n')
    host, port = server.split(':')
    return username, host, int(port)


def recv_loop(sock):
    while True:
        data = sock.recv(4096)
        if not data:
            break
        print('\n<', data.decode(), '>')


def send_loop(sock):
    try:
        while True:
            msg = input('> ')
            if msg:
                sock.sendall(msg.encode())
    except EOFError:
        pass


def main():
    ensure_setup()
    username, host, port = load_config()
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    with socket.create_connection((host, port)) as raw_sock:
        with context.wrap_socket(raw_sock, server_hostname=host) as sock:
            sock.sendall(username.encode())
            threading.Thread(target=recv_loop, args=(sock,), daemon=True).start()
            send_loop(sock)


if __name__ == '__main__':
    main()
