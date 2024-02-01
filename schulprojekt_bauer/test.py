import re

def is_valid_mac(mac):
    mac_pattern = re.compile(r'^([0-9A-Fa-f]{2})([:-]?[0-9A-Fa-f]{2}){5}$')
    return bool(mac_pattern.match(mac))

print(is_valid_mac("00:AA:2B:3C:4D:5E"))