import re

def is_valid_mac(mac):
    # Prüft, ob valide MAC vom Format E88088A47C9A (ohne Doppelpunkte oder Bindestriche) übergeben wurde
    mac_pattern = re.compile(r'^([0-9A-Fa-f]{2})([:-]?[0-9A-Fa-f]{2}){5}$')
    return bool(mac_pattern.match(mac))

print(is_valid_mac("E8-80-88-A4-79-5A"))