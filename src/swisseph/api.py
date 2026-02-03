# from sweph.c
# [ ] swe_version
# [ ] swe_get_library_path
# [ ] swe_calc
# [ ] swe_calc
# [x] swe_calc_ut
# [ ] swe_calc_pctr
# [ ] swe_solcross
# [ ] swe_solcross_ut
# [ ] swe_mooncross
# [ ] swe_mooncross_ut
# [ ] swe_mooncross_node
# [ ] swe_mooncross_node_ut
# [ ] swe_helio_cross
# [ ] swe_helio_cross_ut
# [ ] swe_fixstar
# [ ] swe_fixstar_ut
# [ ] swe_fixstar_mag
# [ ] swe_fixstar2
# [ ] swe_fixstar2_ut
# [ ] swe_close
# [ ] swe_set_ephe_path
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
# [ ] swe_julday
# [ ] swe_revjul
# [ ] swe_utc_to_jd
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

# from swecl.c
# [ ] swe_gauquelin_sector
# [ ] swe_sol_eclipse_where
# [ ] swe_lun_occult_where
# [ ] swe_sol_eclipse_how
# [ ] swe_lun_occult_when_loc
# [ ] swe_lun_occult_when_glob
# [ ] swe_lun_eclipse_how
# [ ] swe_lun_eclipse_when
# [ ] swe_lun_eclipse_when_loc

# from swephlib.c
# [ ] swe_deltat
# [ ] swe_deltat_ex
# [ ] swe_time_equ
# [ ] swe_lmt_to_lat
# [ ] swe_lat_to_lmt
# [ ] swe_sidtime0
# [ ] swe_sidtime
# [ ] swe_set_interpolate_nut
# [ ] swe_cotrans
# [ ] swe_cotrans_sp
# [ ] swe_get_tid_acc
# [ ] swe_set_tid_acc
# [ ] swe_set_delta_t_userdef
# [ ] swe_degnorm
# [ ] swe_radnorm
# [ ] swe_rad_midp
# [ ] swe_deg_midp
# [ ] swe_split_deg

from ._pysweph import ffi, lib

class SwissephError(RuntimeError):
    pass

# --- constants ---

FLG_SWIEPH = int(lib.get_SEFLG_SWIEPH())
SE_GREG_CAL = int(lib.get_SE_GREG_CAL())

# --- helpers ---

def _read_errbuf(errbuf):
    s = ffi.string(errbuf)
    if s:
        return s.decode('utf-8')
    else:
        return None

def _to_double_array(seq, length):
    if not hasattr(seq, "__len__") or len(seq) < length:
        raise TypeError(f"sequence must have length >= {length}")
    arr = ffi.new(f"double[{length}]")
    for i in range(length):
        try:
            arr[i] = float(seq[i])
        except Exception as exc:
            raise TypeError(f"item {i} is not numeric") from exc
    return arr

# --- from sweph.c ---

def calc_ut(tjd_ut, ipl, flags=FLG_SWIEPH):
    out = ffi.new("double[6]")
    serr = ffi.new("char[256]")
    ret = lib.swe_calc_ut(tjd_ut, ipl, flags, out, serr)
    err = _read_errbuf(serr)

    out_list = []
    for i in range(6):
        out_list.append(out[i])

    return {
        "longitude": out[0],
        "latitude": out[1],
        "distance": out[2],
        "speed_long": out[3],
        "speed_lat": out[4],
        "speed_dist": out[5],
        "status": ret,
        "error": err
    }

# --- from swedate.c ---

def julday(year, month, day, hour=12.0, cal=SE_GREG_CAL):
    return float(lib.swe_julday(year, month, day, hour, cal))

# --- from swehouse.c ---

def houses(tjd_ut, geolat, geolon, hsys=ord('W')):
    """
    Calculates house cusps from Julian day (UT), geocentric coordinates, and house system.

    Parameters
    ----------
    tjd_ut : float
        Julian day (UT)
    geolat : float
        Geocentric latitude (degrees)
    geolon : float
        Geocentric longitude (degrees)
    hsys : int
        House system or byte code

    Returns
    -------
    dict
        Dictionary with the following keys:

        - cusps: list of house cusps as 13 or 37 floats where index 0 is empty (37 for Gauquelin)
        - ascmc: list of angles as 10 floats:
            - ascmc[0]: ascendnat
            - ascmc[1]: MC
            - ascmc[2]: ARMC
            - ascmc[3]: Vertex
            - ascmc[4]: "equatorial ascendnant"
            - ascmc[5]: "co-ascendant" (Walter Koch)
            - ascmc[6]: "co-ascendant" (Michael Munkasey)
            - ascmc[7]: "polar ascendant" (Munkasey)
            - ascmc[8] and ascmc[9]: reserved for use with houses_armc() and houses_armc_ex2()
        - status: integer
    """
    cusps = ffi.new("double[37]")
    ascmc = ffi.new("double[10]")
    ret = lib.swe_houses(tjd_ut, geolat, geolon, hsys, cusps, ascmc)

    cusps_list = []
    for i in range(37):
        cusps_list.append(cusps[i])

    ascmc_list = []
    for i in range(10):
        ascmc_list.append(ascmc[i])

    return {
        "cusps": cusps_list,
        "ascmc": ascmc_list,
        "status": ret
    }
