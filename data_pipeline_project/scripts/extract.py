# scripts/extract.py
import requests

def extract_exchange_rates(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code}")
    
    return response.json()

if __name__ == "__main__":
    data = extract_exchange_rates()
    print(data)
