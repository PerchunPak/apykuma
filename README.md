# apykuma

[![Support Ukraine](https://badgen.net/badge/support/UKRAINE/?color=0057B8&labelColor=FFD700)](https://www.gov.uk/government/news/ukraine-what-you-can-do-to-help)

[![Build Status](https://github.com/PerchunPak/apykuma/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/PerchunPak/apykuma/actions?query=workflow%3Atest)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python support versions badge (from pypi)](https://img.shields.io/pypi/pyversions/apykuma)](https://www.python.org/downloads/)

Small library to notify Uptime Kuma that the service is up.
Only async applications are supported.

## Usage

Create a new Push monitor on your Kuma instance:

![image](https://github.com/PerchunPak/apykuma/assets/68118654/f50bbcbc-5717-40a3-8e1c-759b57d3f87a)

Then, install the library:

```bash
pip install apykuma
```

And include it in your code:

```python
import logging
import apykuma

await apykuma.start(
    # Required; URL copied from the image above
    url="https://kuma.example.com/api/push/63MlSOY4CM?status=up&msg=OK&ping=",
    # Optional; default is 60 seconds
    interval=60,
    # Optional; sleeps for N seconds before pinging Kuma, in case if you run `apykuma` right before starting your service
    #           (if service fails, `apykuma` won't start as well). The recommended value is 10 seconds
    delay=0,
    # Optional; function that is called when during ping we encourage an error
    #           it is done to notify you about (e.g.) network errors, and to not
    #           stop the process of pinging kuma on such errors
    #
    #           by default, it logs an error using `logging` library (default value is shown below),
    #           also supports async functions
    handle_exception=lambda e: logging.getLogger("apykuma").exception(e),
)
```

It is important to start `apykuma` after your service starts.

## Differences from `pykuma`

https://github.com/oliverstech/pykuma

That library is great, but it has some problems:

- It uses globals, which I personally don't like
- It blocks the loop every time it sends a request, because it uses `requests` library instead of `aiohttp`. See also https://github.com/oliverstech/pykuma/issues/2.

## Installing for local developing

```bash
git clone https://github.com/PerchunPak/apykuma.git
cd apykuma
```

### Installing `poetry`

Next we need install `poetry` with [recommended way](https://python-poetry.org/docs/master/#installation).

If you use Linux, use command:

```bash
curl -sSL https://install.python-poetry.org | python -
```

If you use Windows, open PowerShell with admin privileges and use:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### Installing dependencies

```bash
poetry install --no-dev
```

### Configuration

All configuration happens in `config.yml`, or with enviroment variables.

### If something is not clear

You can always write me!

## Thanks

This project was generated with [python-template](https://github.com/PerchunPak/python-template).
