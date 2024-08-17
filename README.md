# devicecheck-repro

Reproduces a bug in `devicecheck` causing duplicate log lines in clients.

## Steps to reproduce

1. Clone this repository: `git clone https://github.com/athyuttamre/devicecheck-repro.git`.
2. Create a virtual environment: `python3 -m venv .venv`.
3. Install dependencies: `pip install .`.
4. Run the script: `python devicecheck_repro/main.py`.

Observe that you get duplicate logs.

```
$ python devicecheck_repro/main.py
INFO:root:This is a log message from the client application.
MY LOGS - INFO - This is a log message from the client application.
```
