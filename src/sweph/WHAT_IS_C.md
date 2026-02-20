# cheat sheet

| C                 | Python                    |
| ----------------- | ------------------------- |
| double            | float                     |
| int32             | int                       |
| char * (input)    | path.encode('utf-8')      |
| char * (output)   | ffi.new("char[256]")      |
| double * (output) | fif.new("double[size]")   |

- double[37], double[10] = lists of 37 and 10 floats
- char[256] = strings, need encoding
