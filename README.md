# Description
This is a very simple library designed to be able to easily accept actions in a
json format and then return the average time each action takes. This is designed
to be very simple, with caching to be easy to implement if necessary. This was
not planned to have massive distribution, but to be run on a handful of machines
in a performant way. If I wanted this to be massively distributed I would have
written an API with a library to send requests and handled concurrency that way.

## Concurrency
The library I used is inherently thread safe, and postgres can easily handle
concurrency in most cases.
http://initd.org/psycopg/docs/usage.html#thread-and-process-safety

# Setup
## Database
1. Install postgres
1. Add your TEST_DB_CONN to .env if necessary. Look at .env.example for reference.

## Install Python 3.7.3
```
pip install pyenv
pyenv install
```

### OSX
```
CFLAGS="-I$(brew --prefix readline)/include -I$(brew --prefix openssl)/include -I$(xcrun --show-sdk-path)/usr/include" \
LDFLAGS="-L$(brew --prefix readline)/lib -L$(brew --prefix openssl)/lib" \
PYTHON_CONFIGURE_OPTS=--enable-unicode=ucs2 \
pyenv install
```

## Install dependencies for testing
```
pip install pipenv
pipenv install --dev
```

# Test
## Setup test db
```
python ./bin/setup_test_db.py
```

## Run tests
```
pipenv run pytest
```

