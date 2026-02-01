# from sweph.c
# [x] swe_version
# [ ] swe_get_library_path
# [ ] swe_calc
# [x] swe_calc
# [x] swe_calc_ut
# [x] swe_calc_pctr
# [ ] swe_solcross
# [ ] swe_solcross_ut
# [ ] swe_mooncross
# [ ] swe_mooncross_ut
# [ ] swe_mooncross_node
# [ ] swe_mooncross_node_ut
# [ ] swe_helio_cross
# [ ] swe_helio_cross_ut
# [x] swe_fixstar
# [x] swe_fixstar_ut
# [ ] swe_fixstar_mag
# [ ] swe_fixstar2
# [ ] swe_fixstar2_ut
# [x] swe_close
# [x] swe_set_ephe_path
# [ ] swe_set_jpl_file
# [ ] swe_get_planet_name
# [ ] swe_set_topo
# [ ] swe_set_sid_mode
# [ ] swe_get_ayanamsa_ex
# [ ] swe_get_ayanamsa_ex_ut
# [ ] swe_get_ayanamsa
# [ ] swe_get_ayanamsa_ut
# [ ] swe_get_ayanamsa_name
# [ ] swe_get_current_file_data

# from swedate.c
# [ ] swe_date_conversion
# [x] swe_julday
# [x] swe_revjul
# [x] swe_utc_to_jd
# [ ] swe_jdet_to_utc
# [ ] swe_jdut1_to_utc
# [ ] swe_utc_time_zone

# from swehouse.c
# [x] swe_houses
# [ ] swe_houses_ex
# [ ] swe_houses_ex2
# [ ] swe_houses_armc
# [ ] swe_houses_armc_ex2
# [ ] swe_house_pos
# [ ] swe_house_name

from ._pysweph import ffi, lib
import os

class SwissEph:
    def __init__(self, ephe_path=None):
        if ephe_path:
            self.set_ephe_path(ephe_path)

    # exports from sweph.c

    def set_ephe_path(self, path):
        """Sets the path to the ephemeris files.

        Parameters
        ----------
        path : str
            Path to the ephemeris files.
        """
        path_bytes = os.path.abspath(path).encode('utf-8')
        lib.swe_set_ephe_path(path_bytes)

    def close(self):
        """Closes the Swiss Ephemeris."""
        lib.swe_close()

    def version(self):
        """Returns the version of Swiss Ephemeris."""
        buf = ffi.new("char[256]")
        lib.swe_version(buf)
        return ffi.string(buf).decode('utf-8')

    def calc(self, tjd_et, planet, flags=2):
        """Calculates planet positions for a given Julian day from ephemeris time (ET), or more accurately terrestrial time (TT).

        Parameters
        ----------
        tjd_et : float
            Truncated Julian day (TJD) from ephemeris time/terrestrial time.
        planet : int
            Planet number.
        flags : int
            Calculation flags.

        Returns
        -------
        longitude : float
            Longitude in degrees.
        latitude : float
            Latitude in degrees.
        distance : float
            Distance in AU.
        speed_long : float
            Speed in longitude direction in AU/day.
        speed_lat : float
            Speed in latitude direction in AU/day.
        speed_dist : float
            Speed in distance direction in AU/day.
        status : int
            Status code.
        """
        xx = ffi.new("double[6]")
        err_buf = ffi.new("char[256]")

        status = lib.swe_calc(tjd_et, planet, flags, xx, err_buf)

        if status < 0:
            raise RuntimeError(ffi.string(err_buf).decode('utf-8'))

        return {
            "longitude": xx[0],
            "latitude": xx[1],
            "distance": xx[2],
            "speed_long": xx[3],
            "speed_lat": xx[4],
            "speed_dist": xx[5],
            "status": status
        }

    def calc_ut(self, tjd_ut, planet, flags=2):
        """Calculates planet positions for a given Julian day from universal time (UT).

        Parameters
        ----------
        tjd_ut : float
            Truncated Julian day (TJD) from universal time.
        planet : int
            Planet number.
        flags : int
            Calculation flags.

        Returns
        -------
        longitude : float
            Longitude in degrees.
        latitude : float
            Latitude in degrees.
        distance : float
            Distance in AU.
        speed_long : float
            Speed in longitude direction in AU/day.
        speed_lat : float
            Speed in latitude direction in AU/day.
        speed_dist : float
            Speed in distance direction in AU/day.
        status : int
            Status code.
        """
        xx = ffi.new("double[6]")
        err_buf = ffi.new("char[256]")

        status = lib.swe_calc_ut(tjd_ut, planet, flags, xx, err_buf)

        if status < 0:
            raise RuntimeError(ffi.string(err_buf).decode('utf-8'))

        return {
            "longitude": xx[0],
            "latitude": xx[1],
            "distance": xx[2],
            "speed_long": xx[3],
            "speed_lat": xx[4],
            "speed_dist": xx[5],
            "status": status
        }

    def calc_pctr(self, tjd, planet, planet_counter, flags=2):
        """Calculates planetocentric positions of a planet observed from another, e.g. Jupiter-centric ephmerides, for a given Julian day.

        Parameters
        ----------
        tjd : float
            Truncated Julian day.
        planet : int
            Planet number.
        planet_counter : int
            Planet number of the planet observed from.
        flags : int
            Calculation flags.

        Returns
        -------
        longitude : float
            Longitude in degrees.
        latitude : float
            Latitude in degrees.
        distance : float
            Distance in AU.
        speed_long : float
            Speed in longitude direction in AU/day.
        speed_lat : float
            Speed in latitude direction in AU/day.
        speed_dist : float
            Speed in distance direction in AU/day.
        status : int
            Status code.
        """
        xx = ffi.new("double[6]")
        err_buf = ffi.new("char[256]")

        status = lib.swe_calc_pctr(tjd, planet, planet_counter, flags, xx, err_buf)

        if status < 0:
            raise RuntimeError(ffi.string(err_buf).decode('utf-8'))

        return {
            "longitude": xx[0],
            "latitude": xx[1],
            "distance": xx[2],
            "speed_long": xx[3],
            "speed_lat": xx[4],
            "speed_dist": xx[5],
            "status": status
        }

    def fixstar(self, star, tjd_et, flags=2):
        """Calculates position of a fixed star for a given Julian day in ephemeris time (ET), or more accurately terrestrial time (TT).

        Parameters
        ----------
        star : str
            Fixed star name.
        tjd_et : float
            Julian day from ephemeris time/terrestrial time.
        flags : int
            Calculation flags.

        Returns
        -------
        longitude : float
            Longitude in degrees.
        latitude : float
            Latitude in degrees.
        distance : float
            Distance in AU.
        speed_long : float
            Speed in longitude direction in AU/day.
        speed_lat : float
            Speed in latitude direction in AU/day.
        speed_dist : float
            Speed in distance direction in AU/day.
        status : int
            Status code.
        """
        xx = ffi.new("double[6]")
        err_buf = ffi.new("char[256]")

        status = lib.swe_fixstar(star, tjd_et, flags, xx, err_buf)

        if status < 0:
            raise RuntimeError(ffi.string(err_buf).decode('utf-8'))

        return {
            "longitude": xx[0],
            "latitude": xx[1],
            "distance": xx[2],
            "speed_long": xx[3],
            "speed_lat": xx[4],
            "speed_dist": xx[5],
            "status": status
        }

    def fixstar_ut(self, star, tjd_ut, flags=2):
        """Calculates position of a fixed star for a given Julian day in universal time (UT).

        Parameters
        ----------
        star : str
            Fixed star name.
        tjd_ut : float
            Julian day from universal time.
        flags : int
            Calculation flags.

        Returns
        -------
        longitude : float
            Longitude in degrees.
        latitude : float
            Latitude in degrees.
        distance : float
            Distance in AU.
        speed_long : float
            Speed in longitude direction in AU/day.
        speed_lat : float
            Speed in latitude direction in AU/day.
        speed_dist : float
            Speed in distance direction in AU/day.
        status : int
            Status code.
        """
        xx = ffi.new("double[6]")
        err_buf = ffi.new("char[256]")

        status = lib.swe_fixstar_ut(star, tjd_ut, flags, xx, err_buf)

        if status < 0:
            raise RuntimeError(ffi.string(err_buf).decode('utf-8'))

        return {
            "longitude": xx[0],
            "latitude": xx[1],
            "distance": xx[2],
            "speed_long": xx[3],
            "speed_lat": xx[4],
            "speed_dist": xx[5],
            "status": status
        }

    # exports from swedate.c

    def julday(self, year, month, day, hour, gregflag=1):
        """Calculates Julian day from year, month, day, and hour.

        Parameters
        ----------
        year : int
            Year.
        month : int
            Month.
        day : int
            Day.
        hour : float
            Hour.
        gregflag : int
            Gregorian calendar flag.

        Returns
        -------
        jd : float
            Julian day.
        """
        return lib.swe_julday(year, month, day, hour, gregflag)

    def revjul(self, jd, gregflag=1):
        """Calculates year, month, day, and hour from Julian day.

        Parameters
        ----------
        jd : float
            Julian day.
        gregflag : int
            Gregorian calendar flag.

        Returns
        -------
        year : int
            Year.
        month : int
            Month.
        day : int
            Day.
        ut : float
            Hour.
        """
        jyear = ffi.new("int*")
        jmon = ffi.new("int*")
        jday = ffi.new("int*")
        jut = ffi.new("double*")

        lib.swe_revjul(jd, gregflag, jyear, jmon, jday, jut)

        return {
            "year": jyear[0],
            "month": jmon[0],
            "day": jday[0],
            "ut": jut[0]
        }

    def utc_to_jd(self, year, month, day, hour, minute, second, gregflag=1):
        """Calculates Julian day from UTC date and time.

        Parameters
        ----------
        year : int
            Year.
        month : int
            Month.
        day : int
            Day.
        hour : float
            Hour.
        minute : float
            Minute.
        second : float
            Second.
        gregflag : int
            Gregorian calendar flag.

        Returns
        -------
        jd : float
            Julian day.
        status : int
            Status code.
        """
        dret = ffi.new("double*")
        err_buf = ffi.new("char[256]")

        status = lib.swe_utc_to_jd(year, month, day, hour, minute, second, gregflag, dret, err_buf)

        if status < 0:
            raise RuntimeError(ffi.string(err_buf).decode('utf-8'))

        return {
            "jd": dret[0],
            "status": status
        }

    def houses(self, tjd_ut, latitude, longitude, hsys=0):
        """Calculates house cusps from Julidan day (UT), latitude, longitude, and house system.

        Parameters
        ----------
        tjd_ut : float
            Truncated Julian day (TJD) from universal time.
        latitude : float
            Latitude in degrees.
        longitude : float
            Longitude in degrees.
        hsys : int
            House system number.

        Returns
        -------
        cusps : tuple
            House cusps as a tuple of 13 (or 37, for Gauquelin) values where index 0 is empty, index 1 is the first house cusp, and so on.
        ascmc : tuple
            Tuple of 8 values where ascmc[0] is the asendant, asmc[1] is the midheaven, and asmc[2:7] are additional and hypothetical points.
        """
        cusps = ffi.new("double[4]")
        ascmc = ffi.new("double[4]")

        lib.swe_houses(tjd_ut, latitude, longitude, hsys, cusps, ascmc)

        return {
            "cusps": cusps,
            "ascmc": ascmc
        }
