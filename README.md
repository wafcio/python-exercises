# Python Exercises

## Overview

This repo contains programming exercises in Python language.

- [Project Euler](https://projecteuler.net/)
- [Advent of Code](https://adventofcode.com/)

## Check code style

```
pylint $(pwd)/exercises
pylint $(pwd)/test
```

## Verification

Every exercise contains test written in unittest.

```
pytest
```

### Check test coverage

```
coverage run -m pytest
coverage report -m
coverage html
```
