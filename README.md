# Arcade

A pure Python Phaser webapp.

![Review](https://img.shields.io/github/actions/workflow/status/JoelLefkowitz/arcade/review.yml)
![Version](https://img.shields.io/pypi/v/arcade)
![Downloads](https://img.shields.io/pypi/dw/arcade)
![Quality](https://img.shields.io/codacy/grade/ef1f0bc7a29c40dbafa33d69163694fe)
![Coverage](https://img.shields.io/codacy/coverage/ef1f0bc7a29c40dbafa33d69163694fe)

## Motivation

Modern tools for extending Python's capabilities are emerging for both the server and client side. AIOHTTP provides support for asynchronous request handling whilst Brython permits Python scripts to access javascript libraries. As a demonstration of these technologies, this Phaser webapp is entirely written in Python.

[Try it out!][webapp]

## Design

![Architecture][architecture]

## Installation

```bash
pip install arcade
```

## Documentation

Documentation and more detailed examples are hosted on [Github Pages](https://joellefkowitz.github.io/arcade).

## Tooling

### Dependencies

To install dependencies:

```bash
yarn install
pip install .[all]
```

### Tests

To run tests:

```bash
thx test
```

### Documentation

To generate the documentation locally:

```bash
thx docs
```

### Linters

To run linters:

```bash
thx lint
```

### Formatters

To run formatters:

```bash
thx format
```

## Contributing

Please read this repository's [Code of Conduct](CODE_OF_CONDUCT.md) which outlines our collaboration standards and the [Changelog](CHANGELOG.md) for details on breaking changes that have been made.

This repository adheres to semantic versioning standards. For more information on semantic versioning visit [SemVer](https://semver.org).

Bump2version is used to version and tag changes. For example:

```bash
bump2version patch
```

### Contributors

- [Joel Lefkowitz](https://github.com/joellefkowitz) - Initial work

## Remarks

Lots of love to the open source community!

<div align='center'>
    <img width=200 height=200 src='https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif' alt='Be kind to your mind' />
    <img width=200 height=200 src='https://media.giphy.com/media/KEAAbQ5clGWJwuJuZB/giphy.gif' alt='Love each other' />
    <img width=200 height=200 src='https://media.giphy.com/media/WRWykrFkxJA6JJuTvc/giphy.gif' alt="It's ok to have a bad day" />
</div>
