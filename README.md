# pysweph
[![pypi](https://img.shields.io/pypi/v/pysweph.svg)](https://pypi.org/project/pysweph/) [![license: agpl v3](https://img.shields.io/badge/license-agpl--3-blue.svg)](./LICENSE)

Modern Python bindings for the [Swiss Ephemeris](https://www.astro.com/swisseph/swephinfo_e.htm), a high-precision astronomical computation library for astrology developed and maintained since 1997.

`pysweph` continues the work of [`pyswisseph`](https://github.com/astrorigin/pyswisseph) with updated documentation, bug fixes, and ongoing community maintenance.

## Background

In mid-2025, the documentation for `pywisseph` (`https://astrorigin.com/pyswisseph`) became inaccessible, and the maintainer has been unresponsive to issues and pull requests. This fork, `pysweph`, aims to keep the Python interface stable, documented, and installable for users who rely on it.

### Versioning

This project follows the versioning scheme: `<swe_major>.<swe_minor>.<swe_patch>.<wrapper_increment>`

- The first three numbers match the Swiss Ephemeris C library version, [v2.10.03](https://github.com/aloistr/swisseph/releases/tag/v2.10.03) (2022-09-09).
- The fourth number increments for Python wrapper changes.

`pysweph` starts from [`pyswisseph==2.10.3.2`](https://github.com/astrorigin/pyswisseph/releases/tag/v2.10.03.2) (2023-06-04). The first release of this fork is `2.10.3.3`. If the original maintainer of `pyswisseph` returns, this project will coordinate or merge changes as appropriate.

### Upstream

`pysweph` links directly to the official [Swiss Ephemeris C library](https://github.com/aloistr/swisseph) maintained by Alois Treindl and Astrodienst.

`pyswisseph` included the author's auxiliary repositories ([`swephelp`](https://github.com/astrorigin/swephelp), [`sqlite3`](https://github.com/astrorigin/sqlite3), and related utilities). These have been intentionally removed in `pysweph` to reduce complexity and depend only on the canonical Swiss Ephemeris source code.

## Changes in `pysweph`

- [**Documentation**](https://sailorfe.github.io/pysweph):
    * Rebuilt with Sphinx and MyST Markdown, hosted on GitHub Pages with continuous integration via GitHub Actions.
    * Generated API reference directly from `pyswisseph.c` docstrings with `sphinx-autodoc`.
    * Includes original tutorials and conceptual guides intended for both astrologers and developers.
- **C library parity**:
    * [2.10.3.3](https://github.com/sailorfe/pysweph/releases/tag/2.10.3.3): Exposed string errors in `swe.calc()`, `swe.calc_pctr()`, `swe.calc_ut()`, and `swe.deltat_ex()`.
    * [2.10.3.4](https://github.com/sailorfe/pysweph/releases/tag/v2.10.3.4): The `swe_houses` function family now returns house cusps as a 13 or 37-item tuple where index 0 is empty.

### Status

- As of 2026-02-06, the test suite is deprecated due to `calc` and `houses` function patches.
- A CFFI refactor is in progress: [cffi-rewrite](https://github.com/sailorfe/pysweph/tree/cffi-rewrite).

## Installation

Install from [PyPI](https://pypi.org/project/pysweph): `pip install pysweph`

Build from source:
```
git clone https://github.com/sailorfe/pysweph.git
cd pysweph
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

`pysweph` retains the same import name from `pyswisseph`:

```py
import swisseph as swe
```

The documentation includes a detailed `pyswisseph` to `pysweph` [Migration Guide](https://sailorfe.github.io/pysweph/concepts/migration_guide.html) for existing projects.

## Credits

- **Alois Treindl**, creator of the Swiss Ephemeris
- **Stanislas Marquis**, author of the original Python bindings (`pyswisseph`)
- **sailorfe**, maintainer of `pysweph` continuation

## License

`pysweph` is licensed under the GNU Affero General Public License version 3, whose text you can read at [LICENSE](./LICENSE).
