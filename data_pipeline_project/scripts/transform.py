# scripts/transform.py
import sys
import os
sys.path.append(os.path.abspath("scripts"))

from extract import extract_exchange_rates

def transform_exchange_rates(raw_data):
    base = raw_data.get("base_code")
    date = raw_data.get("time_last_update_utc")
    rates = raw_data.get("rates", {})

    transformed = []
    for currency, rate in rates.items():
        transformed.append({
            "base": base,
            "date": date,
            "currency": currency,
            "rate": rate
        })
    return transformed

if __name__ == "__main__":
    raw = extract_exchange_rates()
    data = transform_exchange_rates(raw)
    print(data[:5])
