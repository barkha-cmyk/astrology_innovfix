from datetime import date

SIGN_DATES = [
    ("Capricorn",  (12, 22), (1, 19)),
    ("Aquarius",   (1, 20),  (2, 18)),
    ("Pisces",     (2, 19),  (3, 20)),
    ("Aries",      (3, 21),  (4, 19)),
    ("Taurus",     (4, 20),  (5, 20)),
    ("Gemini",     (5, 21),  (6, 20)),
    ("Cancer",     (6, 21),  (7, 22)),
    ("Leo",        (7, 23),  (8, 22)),
    ("Virgo",      (8, 23),  (9, 22)),
    ("Libra",      (9, 23),  (10, 22)),
    ("Scorpio",    (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21)),
]

def sun_sign(dob: date) -> str:
    md = (dob.month, dob.day)
    for sign, start, end in SIGN_DATES:
        # Capricorn wraps the year boundary (Dec 22 – Jan 19), so start > end
        if start > end:
            if md >= start or md <= end:
                return sign
        elif start <= md <= end:
            return sign
    raise ValueError(f"Could not determine sun sign for {dob}")
