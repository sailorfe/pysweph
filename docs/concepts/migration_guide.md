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

## Changes

The primary divergence in `pysweph` 2.10.3.3+ is a return to C-parity, which diverges from `pyswisseph` in subtle-to-breaking ways.

### 🔧 `swe.calc` family string errors

While `pyswisseph` attempted to hide C-style error handling, `pysweph` exposes it to ensure you know exactly why a calculation failed (e.g., `"SwissEph file 'sepl_18.se1' not found in PATH '/usr/share/swisseph:/usr/local/share/swisseph/' \nusing Moshier eph.; "`).


| Function          | Legacy `pyswisseph` return    | New `pysweph>=2.10.3.3` return      |
| ----------------- | ----------------------------- | ------------------------- |
| `swe.calc()`      | `(int, retflags)`             | `(int, retflags, serr)`   |
| `swe.calc_pctr`   | `(int, retflags)`             | `(int, retflags, serr)`   |
| `swe.calc_ut()`   | `(int, retflags)`             | `(int, retflags, serr)`   |
| `swe.deltat_ex()` | `(float)`                     | `(float, serr)`           |


### ⚠️ `swe.houses` family `cusps` tuple

```{warning}
This is a **breaking change** with `pyswisseph`. If you mean to migrate, you will need time to rewrite any portions of your code that use the `cusps` outpuet of `swe.houses()`, `swe.houses_armc()`, `swe.houses_armc_ex2()`, `swe.houses_ex()`, or `swe.houses_ex2()`.
```

In the `houses` function family, Swiss Ephemeris indexes the house cusps or Gauquelin sectors in 13-item and 37-item arrays where index `0` is empty, which is logical for the domain of astrology. `pyswisseph` changed these to 12- and 36-item tuples, where index `0` was the first house cusp. `pysweph` restores the Swiss Ephemeris' empty `0` index.

| House cusp [^1]   | `pyswisseph`  | `pysweph>=2.10.3.4`       |
| ----------------- | ------------- | ------------------------- |
| -                 | -             | `cusps[0]`                |
| 1st               | `cusps[0]`    | `cusps[1]`                |
| 2nd               | `cusps[1]`    | `cusps[2]`                |
| 3rd               | `cusps[2]`    | `cusps[3]`                |
| 4th               | `cusps[3]`    | `cusps[4]`                |
| 5th               | `cusps[4]`    | `cusps[5]`                |
| 6th               | `cusps[5]`    | `cusps[6]`                |
| 7th               | `cusps[6]`    | `cusps[7]`                |
| 8th               | `cusps[7]`    | `cusps[8]`                |
| 9th               | `cusps[8]`    | `cusps[9]`                |
| 10th              | `cusps[9]`    | `cusps[10]`               |
| 11th              | `cusps[10]`   | `cusps[11]`               |
| 12th              | `cusps[11]`   | `cusps[12]`               |

[^1]: For every house system but Gauquelin (71 or `b'G'`).
