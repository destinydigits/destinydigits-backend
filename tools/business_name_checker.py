from datetime import datetime
from tools.numerology_core import numerology_values, extract_full_numerology

def business_name_checker(data):
    """
    Inputs expected from frontend:
      - name / clientName         => client's personal name (shown on UI as 'name')
      - businessName              => business/trade name (used for expression number)
      - dob                       => client's DOB (used for destiny number)

    Output keys align with DestinyDigits Tool Result expectations.
    """

    # ---- Read inputs (gracefully) ----
    client_name   = (data.get("name") or data.get("clientName") or "").strip()
    business_name = (data.get("businessName") or "").strip()
    dob           = (data.get("dob") or "").strip()

    # ---- Basic validation / graceful fallback ----
    missing = []
    if not client_name:
        missing.append("name")
    if not business_name:
        missing.append("businessName")
    if not dob:
        missing.append("dob")

    if missing:
        miss_str = ", ".join(missing)
        return {
            "tool": "business-name-checker",
            "name": client_name,
            "businessName": business_name,
            "dob": dob,
            "score": 0,
            "emoji": "❌",
            "summary": f"Missing required field(s): {miss_str}. Please provide all inputs.",
            "title": "Business Name Compatibility",
            "mainNumber": 0,
            "mainPercentage": 0,
            "vibe": "",
            "syncScore": "0/100",
            "syncMessage": ""
        }

    # ---- Helper to read both snakeCase & camelCase keys safely ----
    def _pick(d, *keys, default=None):
        for k in keys:
            if k in d and d[k] is not None:
                return d[k]
        return default

    try:
        # 1) Expression number from BUSINESS NAME (not client name)
        name_data = numerology_values(business_name)
        expression_number = _pick(
            name_data,
            "expression_number", "expressionNumber",
            default=None
        )

        if expression_number is None:
            raise ValueError("Expression number could not be derived from business name.")

        # 2) Destiny number from CLIENT (DOB; some cores also use name)
        #    Pass client_name + dob for maximum compatibility with your core.
        core_data = extract_full_numerology(client_name, dob)
        destiny_number = _pick(
            core_data,
            "destiny_number", "destinyNumber",
            default=None
        )

        if destiny_number is None:
            raise ValueError("Destiny number could not be derived from DOB.")

        # ---- Compatibility logic (simple diff model) ----
        diff = abs(int(expression_number) - int(destiny_number))
        if diff == 0:
            score = 92
            vibe = "Perfect Match"
            emoji = "🌟"
            message = "Your business name is in perfect alignment with your destiny. Full steam ahead!"
        elif diff == 1:
            score = 85
            vibe = "Strong Compatibility"
            emoji = "✅"
            message = "The name strongly supports your path. Success flows with ease."
        elif diff == 2:
            score = 75
            vibe = "Moderately Aligned"
            emoji = "⚖️"
            message = "Good energy overall. You may consider enhancing the name's impact slightly."
        else:
            score = 62
            vibe = "Needs Adjustment"
            emoji = "🔄"
            message = "There may be clashes between your name and core path. Small changes can help."

        # ---- Final payload (Frontend-friendly) ----
        return {
            "tool": "business-name-checker",
            "name": client_name,                 # ✅ show client name on UI
            "businessName": business_name,       # ✅ also return business name explicitly
            "dob": dob,
            "score": score,
            "emoji": emoji,
            "summary": (
                f"‘{business_name}’ ka expression number {expression_number} hai, "
                f"jo aapke destiny number {destiny_number} (DOB ke base par) se compare hota hai. {message}"
            ),
            "title": "Business Name Compatibility",
            "mainNumber": score,                 # ✅ frontend expects this
            "mainPercentage": score,             # ✅ frontend expects this
            "vibe": vibe,
            "syncScore": f"{score}/100",
            "syncMessage": message
        }

    except Exception as e:
        return {
            "tool": "business-name-checker",
            "name": client_name,
            "businessName": business_name,
            "dob": dob,
            "score": 0,
            "emoji": "❌",
            "summary": f"Something went wrong: {str(e)}",
            "title": "Business Name Compatibility",
            "mainNumber": 0,
            "mainPercentage": 0,
            "vibe": "",
            "syncScore": "0/100",
            "syncMessage": ""
        }
