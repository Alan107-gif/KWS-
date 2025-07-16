# KWS Chat Client

This directory contains the client portion of the KWS chat system.

## Usage

1. Run `python KWS_Main.py` to start the client.
2. On first run the script creates `~/KWS` and moves the client files there.
3. After setup you need to restart the script. On subsequent runs the chat
   connects to the server and allows encrypted communication.

The client communicates with the server via TLS (using Python's `ssl` module).

