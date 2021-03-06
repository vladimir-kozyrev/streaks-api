[![Build Status](https://travis-ci.com/vladimir-kozyrev/streaks-api.svg?branch=master)](https://travis-ci.com/vladimir-kozyrev/streaks-api)

# STREAKS API

An impression of what a simplified version of [STREAKS](https://streaksapp.com/) API could look like.
This is a practice project that will help me learn FastAPI.

## Installation

```shell
$ pipenv install
$ pipenv shell
```

## Run it

```shell
$ uvicorn main:app --reload
```

## TODO

- Initialize the database and apply migrations using [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- Improve directory structure
- Hash user passwords
