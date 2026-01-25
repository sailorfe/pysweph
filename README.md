# pysweph

Modern Python bindings for the [Swiss Ephemeris](https://www.astro.com/swisseph/swephinfo_e.htm), a high-precision astronomical computation library for astrology developed and maintained since 1997.

`pysweph` continues the work of [astrorigin/pyswisseph](https://github.com/astrorigin/pyswisseph) with updated documentation, bug fixes, and ongoing community maintenance.

## Background

In mid-2025, the documentation for Pyswisseph (`astrorigin.com/pyswisseph`) became inaccessible, and the maintainer has been unresponsive to issues and pull requests. This fork, `pysweph`, aims to keep the Python interface stable, documented, and installable for users who rely on it.

## Upstream and scope

`pysweph` links directly to the official [Swiss Ephemeris C library](https://github.com/aloistr/swisseph) maintained by Alois Treindl and Astrodienst.

The previous Python package (`astrorigin/pyswisseph`) included Stanislas Marquis' (astrorigin's) auxiliary repositories (`[swephelp](https://github.com/astrorigin/swephelp)`, `[sqlite3](https://github.com/astrorigin/sqlite3)`, and related utilities). These have been intentionally removed in `pysweph` to reduce complexity and depend only on the canonical Swiss Ephemeris source.

## What's new in pysweph

- Full documentation rebuild using Sphinx and MyST Markdown, following the Diataxis framework
- Regenerated API reference directly from Python docstrings
- Original tutorials and conceptual guides.
- Bug fixes improving error handling in `swe.calc()` functions and `swe.deltat_ex`
- Continuous integration and Github Pages documentation hosting
- Compatible with the upstream Swiss Ephemeris C library

You can browse the documentation here: [https://sailorfe.github.io/pysweph](https://sailorfe.github.io/pysweph).

### Development status

To fix critical bugs in the C-FFI layer and align with the upstream Swiss Ephemeris, the legacy test suite has been deprecated. We are currently rewriting the test suite from the ground up to ensure 100% parity with the upstream C outputs.

- [ ] **Core test suite rewrite:** In progress.
- [x] **C-FFI bug fixes:** Completed.

## Installation

`pyswisseph` is available directly from [PyPI](https://pypi.org/project/pysweph).

```sh
uv pip install pysweph
# or
pip install pysweph
```

`pysweph` is a drop-in replacement for `pyswisseph`. As long as you uninstall `pyswisseph` from any existing project first, your import should still be

```py
import swisseph as swe
```

## Versioning

This project follows the versioning scheme: `<swe_major>.<swe_minor>.<swe_patch>.<wrapper_increment>`

- The first three numbers match the Swiss Ephemeris C library version.
- The fourth number increments for Python wrapper changes.
- Current C library version: 2.10.3 (released 2022).

`pysweph` starts from `pyswisseph==2.10.3.2`. The first release of this fork is `2.10.3.3`.

If the original maintainer of `pyswisseph` returns, this project will coordinate or merge changes as appropriate.

## Credits

- **Alois Treindl**, creator of the Swiss Ephemeris
- **Stanislas Marquis**, author of the original Python bindings (`pyswisseph`)
- **sailorfe**, maintainer of `pysweph` continuation

## License

`pysweph` is licensed under the GNU Affero General Public License version 3, whose text you can read at [LICENSE](./LICENSE).
