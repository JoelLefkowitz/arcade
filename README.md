# Arcade

A pure Python Phaser webapp.

[Try it out!][webapp]

## Status

| Source     | Shields                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------ |
| Project    | ![release][release_shield] ![license][license_shield]                                                              |
| Health     | ![travis][travis_shield] ![codacy][codacy_shield] ![coverage][coverage_shield] ![readthedocs][readthedocs_shield]  |
| Repository | ![issues][issues_shield] ![pulls][pulls_shield]                                                                    |
| Activity   | ![contributors][contributors_shield] ![monthly_commits][monthly_commits_shield] ![last_commit][last_commit_shield] |

## Motivation

Modern tools for extending Python's capabilities are emerging for both the server and client side. AIOHTTP provides support for asyncronous request handling whilst Brython permits Python scripts to access javascript libraries. As a demonstration of these technologies, this Phaser webapp is entirely written in Python.

## Architecture

![Architecture][architecture]


## Installation

```bash
git clone https://github.com/JoelLefkowitz/arcade
```

## Tests

To run unit tests:

```bash
grunt tests:unit
```

To generate a coverage report:

```bash
grunt tests:coverage
```

## Documentation

This repository's documentation is hosted on [readthedocs][readthedocs].

To generate the sphinx configuration:

```bash
grunt docs:generate
```

Then build the documentation:

```bash
grunt docs:build
```

## Tooling

To run linters:

```bash
grunt lint
```

To run formatters:

```bash
grunt format
```

Before commiting new code:

```bash
grunt precommit
```

This will run linters, formaters, generate a test coverage report and the sphinx configuration.

## Versioning

This repository adheres to semantic versioning standards.
For more inforamtion on semantic versioning visit [SemVer][semver].

Bump2version is used to version and tag changes.
For example:

```bash
bump2version patch
```

## Changelog

Please read this repository's [CHANGELOG](CHANGELOG.md) for details on changes that have been made.

## Contributing

Please read this repository's guidelines on [CONTRIBUTING](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Contributors

- **Joel Lefkowitz** - _Initial work_ - [Joel Lefkowitz][joellefkowitz]

[![Buy Me A Coffee][coffee_button]][coffee]

## Remarks

Lots of love to the open source community!

![Be kind][be_kind]

<!-- Github links -->

[pulls]: https://github.com/JoelLefkowitz/arcade/pulls
[issues]: https://github.com/JoelLefkowitz/arcade/issues
[architecture]: https://github.com/JoelLefkowitz/arcade/raw/master/architecture.png

<!-- External links -->

[readthedocs]: https://joellefkowitz-arcade.readthedocs.io/en/latest/
[webapp]: https://arcade.joellefkowitz.co.uk
[semver]: http://semver.org/
[coffee]: https://www.buymeacoffee.com/joellefkowitz
[coffee_button]: https://cdn.buymeacoffee.com/buttons/default-blue.png
[be_kind]: https://media.giphy.com/media/osAcIGTSyeovPq6Xph/giphy.gif

<!-- Acknowledgments -->

[joellefkowitz]: https://github.com/JoelLefkowitz

<!-- Project shields -->

[release_shield]: https://img.shields.io/github/v/tag/joellefkowitz/arcade
[license_shield]: https://img.shields.io/github/license/joellefkowitz/arcade

<!-- Health shields -->

[travis_shield]: https://img.shields.io/travis/joellefkowitz/arcade
[codacy_shield]: https://img.shields.io/codacy/coverage/arcade
[coverage_shield]: https://img.shields.io/codacy/grade/arcade
[readthedocs_shield]: https://img.shields.io/readthedocs/joellefkowitz-arcade

<!-- Repository shields -->

[issues_shield]: https://img.shields.io/github/issues/joellefkowitz/arcade
[pulls_shield]: https://img.shields.io/github/issues-pr/joellefkowitz/arcade

<!-- Activity shields -->

[contributors_shield]: https://img.shields.io/github/contributors/joellefkowitz/arcade
[monthly_commits_shield]: https://img.shields.io/github/commit-activity/m/joellefkowitz/arcade
[last_commit_shield]: https://img.shields.io/github/last-commit/joellefkowitz/arcade
