import os
from cffi import FFI
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
SWE_DIR = BASE_DIR / "libswe"

ffibuilder = FFI()

ffibuilder.cdef("""
    /* from swpeh.c */
    int swe_calc_ut(double tjd_ut, int ipl, int iflag, double *xx, char *serr);

    /* from swedate.c */
    double swe_julday(int year, int month, int day, double hour, int gregflag);

    /* from swehouse.c */
    int swe_houses(double tjd_ut, double geolat, double geolon, int hsys, double *cusps, double *ascmc);

    /* constants */
    int get_SEFLG_SWIEPH(void);
    int get_SE_GREG_CAL(void);
""")

ffibuilder.set_source("_pysweph",
    r'''
    #include "swephexp.h"
    int get_SEFLG_SWIEPH(void) { return SEFLG_SWIEPH; }
    int get_SE_GREG_CAL(void) { return SE_GREG_CAL; }
    ''',
    include_dirs=[str(SWE_DIR)],
    sources=[str(SWE_DIR / f) for f in [
        "sweph.c",
        "swephlib.c",
        "swedate.c",
        "swemmoon.c",
        "swemplan.c",
        "swejpl.c",
        "swehel.c",
        "swehouse.c",
        "sweephe4.c",
        "swecl.c",
    ]],
)

if __name__ == "__main__":
    package_dir = BASE_DIR / "swisseph"
    os.chdir(str(package_dir))
    ffibuilder.compile(target="./_pysweph.*", verbose=True)
    print(f"binary successfully generated in {package_dir}!")
