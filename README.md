# KWS Chat System

This repository provides a minimal implementation of the KWS chat concept.
It consists of two parts:

* `chat/` – client scripts including `KWS_Main.py` and `kws_setup.py`.
* `server/` – the relay server script `kws_server.py`.

Run the client using Python. On first start it installs itself under `~/KWS`
and creates the required data files. After the setup message
"Installation Done, Need to restart the Script." restart the client to use the
chat.

The server can be started with `python kws_server.py` and kept running
permanently. Use the `-d` flag for verbose output.
