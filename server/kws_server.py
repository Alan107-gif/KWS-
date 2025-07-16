import argparse
import ssl
import socket
import threading

clients = set()


def handle_client(conn, addr, debug):
    try:
        username = conn.recv(1024).decode()
        if debug:
            print(f"{username} connected from {addr}")
        clients.add(conn)
        while True:
            data = conn.recv(4096)
            if not data:
                break
            msg = f"{username}: {data.decode()}"
            for c in list(clients):
                if c is not conn:
                    try:
                        c.sendall(msg.encode())
                    except Exception:
                        clients.discard(c)
    finally:
        clients.discard(conn)
        conn.close()
        if debug:
            print(f"{addr} disconnected")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store_true', help='debug output')
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((args.host, args.port))
        s.listen()
        if args.d:
            print(f"Server listening on {args.host}:{args.port}")
        while True:
            conn, addr = s.accept()
            conn = context.wrap_socket(conn, server_side=True)
            threading.Thread(target=handle_client, args=(conn, addr, args.d), daemon=True).start()

if __name__ == '__main__':
    main()
