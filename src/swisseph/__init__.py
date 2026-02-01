from .api import SwissEph

_inst = SwissEph()
set_ephe_path = _inst.set_ephe_path
close = _inst.close
version = _inst.version
calc = _inst.calc
calc_ut = _inst.calc_ut
calc_pctr = _inst.calc_pctr
fixstar = _inst.fixstar
fixstar_ut = _inst.fixstar_ut
julday = _inst.julday
revjul = _inst.revjul
utc_to_jd = _inst.utc_to_jd
houses = _inst.houses
