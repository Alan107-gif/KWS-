# KWS Server

This directory contains a simple relay server for the KWS chat system.

Run the server permanently on a host machine:

```bash
python kws_server.py [-d]
```

Use the `-d` option to print detailed debug output.

The server accepts TLS connections from clients and relays messages between them.
