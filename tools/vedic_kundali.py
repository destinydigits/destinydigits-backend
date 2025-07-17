# tools/vedic_kundali.py
from tools.vedic_numerology_kundali import generate_vedic_kundali

def get_vedic_kundali(data):
    name = data.get("name")
    dob = data.get("dob")
    return generate_vedic_kundali(name, dob)
