import os
from cffi import FFI
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
SWE_DIR = BASE_DIR / "libswe"

ffibuilder = FFI()

ffibuilder.cdef("""
    void swe_set_ephe_path(char *path);
    void swe_close(void);
    char *swe_version(char *);
    int swe_calc(double tjd, int ipl, int iflag, double *xx, char *serr);
    int swe_calc_ut(double tjd_ut, int ipl, int iflag, double *xx, char *serr);
    int swe_calc_pctr(double tjd, int ipl, int iplctr, int iflag, double *xxret, char *serr);
    int swe_fixstar(char *star, double tjd, int iflag, double *xx, char *serr);
    int swe_fixstar_ut(char *star, double tjd_ut, int iflag, double *xx, char *serr);
    double swe_julday(int year, int month, int day, double hour, int gregflag);
    void swe_revjul(double jd, int gregflag, int *jyear, int *jmon, int *jday, double *jut);
    int swe_utc_to_jd(int iyear, int imonth, int iday, int ihour, int imin, double dsec, int gregflag, double *dret, char *serr);
    int swe_houses(double tjd_ut, double geolat, double geolon, int hsys, double *cusps, double *ascmc);
""")

ffibuilder.set_source("_pysweph",
    '#include "swephexp.h"',
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
