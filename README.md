# [experiment] pysweph CFFI rewrite

> [!CAUTION]
**This branch is not a functional library.** It is an orphan branch with scaffolding for a long-term, solo CFFI refactor. Commits may not be pushed for weeks or months at a time.

- **Do NOT use this.** As of writing, only three of 86 Swiss Ephemeris functions have been bound.
- **Do not report bugs**. If a function is missing or broken, I am aware.
- **Namespace change**: To separate from Pyswisseph, the import name of this rewrite will be `import sweph`.
- **Versioning**: Once feature-complete, releases will start from `pysweph==0.1.0`.

## Why

The purpose of this work is to replace the legacy CPython extensions with CFFI, resolving drift from the upstream C library's bindings.

[**Return to the default branch for stable**](https://github.com/sailorfe/pysweph).
