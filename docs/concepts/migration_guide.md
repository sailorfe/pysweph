# `pyswisseph` to `pysweph` Migration Guide

This guide is intended to help migrate existing projects from [`pyswisseph` v2.10.3.2](https://github.com/astrorigin/pyswisseph/releases/tag/v2.10.03.2) to `pysweph`, which wraps [Swiss Ephemeris 2.10.03](https://github.com/aloistr/swisseph/releases/tag/v2.10.0).

If you are starting a new project with `pysweph`, please see [Installation](../installation.md).

## Dependency swap

### pip

Assuming you are in an virtual environment, run `pip list` to verify that `pyswisseph` is installed.

```{code-block} shell
$ pip list
Package    Version
---------- --------
pyswisseph 2.10.3.2
```

To replace `pyswisseph`, run:

```{code-block} shell
$ pip uninstall pyswisseph && pip install pysweph
```

```{code-block} shell
# Example output
Found existing installation: pyswisseph 2.10.3.2
Uninstalling pyswisseph-2.10.3.2:
  Would remove:
    /home/user/../.venv/lib/python3.13/site-packages/pyswisseph-2.10.3.2.dist-info/*
    /home/user/../.venv/lib/python3.13/site-packages/swisseph.cpython-313-x86_64-linux-gnu.so
Proceed (Y/n)?
  Successfully uninstalled pyswisseph-2.10.3.2
Collecting pysweph
  Using cached pysweph-2.10.3.3-cp313-cp313-manylinux_2_34_x86_64.whl.metadata (4.3 kB)
Using cached pysweph-2.10.3.3-cp313-cp313-manylinux_2_34_x86_64.whl (770 kB)
Installing collected packages: pysweph
Successfully installed pysweph-2.10.3.3
```

Verify and update project requirements with:

```
$ pip freeze > requirements.txt
```

Update your `pyproject.toml` or `setup.py` accordingly.

### uv

In your project directory, run `uv pip list` to verify that `pyswisseph` is installed.

```{code-block} shell
$ uv pip list
Package    Version
---------- --------
pyswisseph 2.10.3.2
```

To replace `pyswisseph`, run:

```{code-block} shell
$ uv remove pyswisseph && uv add pysweph
```

```{code-block} shell
# Example output
Resolved 1 package in 6ms
Uninstalled 1 package in 0.51ms
 - pyswisseph==2.10.3.2
Resolved 2 packages in 5ms
Installed 1 package in 4ms
 + pysweph==2.10.3.3
```

These commands update your `pyproject.toml` for you:

```{code-block} toml
[project]
...
dependencies = [
    "pysweph>=2.10.3.3",
]
```

## Core changes

The primary divergence in `pysweph` 2.10.3.3+ is a return to C-parity.

### String errors

While `pyswisseph` attempted to hide C-style error handling, `pysweph` exposes it to ensure you know exactly why a calculation failed (e.g., `"SwissEph file 'sepl_18.se1' not found in PATH '/usr/share/swisseph:/usr/local/share/swisseph/' \nusing Moshier eph.; "`).


| Function          | Legacy `pyswisseph` return    | New `pysweph` return      |
| ----------------- | ----------------------------- | ------------------------- |
| `swe.calc()`      | `(int, retflags)`             | `(int, retflags, serr)`   |
| `swe.calc_pctr`   | `(int, retflags)`             | `(int, retflags, serr)`   |
| `swe.calc_ut()`   | `(int, retflags)`             | `(int, retflags, serr)`   |
| `swe.deltat_ex()` | `(float)`                     | `(float, serr)`           |
