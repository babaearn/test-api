import sys
import time
import requests

print("--- [DUAL-SDK VALIDATION TEST: KALSHI + POLYMARKET] ---")
print(f"Python Version: {sys.version}")

# --- TEST 1: POLYMARKET (via REST API - Most Robust) ---
print("\n--- Testing Polymarket Data Layer ---")
try:
    # Polymarket Gamma API Endpoint
    POLY_GAMMA_URL = "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=10"
    response = requests.get(POLY_GAMMA_URL, timeout=10)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ [SUCCESS] Polymarket API reached directly! Found {len(data)} events.")
        for event in data[:2]:
            print(f"   Market: {event.get('title')}")
    else:
        print(f"❌ [FAIL] Polymarket Status Code: {response.status_code}")
except Exception as ep:
    print(f"❌ [FATAL] Polymarket Request Error: {ep}")


# --- TEST 2: KALSHI (via REST API - Most Robust) ---
print("\n--- Testing Kalshi Data Layer ---")
try:
    # Kalshi V2 Public API Endpoint
    KALSHI_API_URL = "https://trading-api.kalshi.com/trade-api/v2/markets?status=open&limit=5"
    response = requests.get(KALSHI_API_URL, timeout=10)
    if response.status_code == 200:
        data = response.json()
        markets = data.get('markets', [])
        print(f"✅ [SUCCESS] Kalshi API reached directly! Found {len(markets)} markets.")
        for m in markets[:2]:
            print(f"   Market: {m.get('title')}")
    else:
        print(f"❌ [FAIL] Kalshi Status Code: {response.status_code}")
except Exception as ek:
    print(f"❌ [FATAL] Kalshi Request Error: {ek}")

print("\n--- [SDK TEST FINISHED] ---")
time.sleep(300) # Keep log alive
