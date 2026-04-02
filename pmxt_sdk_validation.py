import sys
import os
import time

print("--- [ULTIMATE SDK VALIDATION TEST: CLOUD ONLY] ---")
print(f"Python Environment: {sys.version}")

try:
    import pmxt
    print("✅ [SDK TEST] pmxt successfully imported in the cloud!")

    # 🧪 TEST 1: KALSHI PUBLIC API
    print("\n--- Trying Kalshi Public Data ---")
    try:
        kalshi = pmxt.Kalshi()
        # Non-auth fetch (just public markets)
        markets = kalshi.fetch_markets(params={"status": "open", "search_query": "Bitcoin"})
        if markets:
             print(f"✅ [SDK TEST] Kalshi Connected! Found {len(markets)} Bitcoin markets.")
             print(f"   Sample Question: {markets[0].get('question')}")
        else:
             print("⚠️ [SDK TEST] Kalshi reachable, but returned 0 Bitcoin markets.")
    except Exception as e:
        print(f"❌ [SDK TEST] Kalshi Failed: {e}")

    # 🧪 TEST 2: POLYMARKET CLOB PUBLIC API
    print("\n--- Trying Polymarket Public Data ---")
    try:
        poly = pmxt.Polymarket()
        markets = poly.fetch_markets(params={"active": True})
        if markets:
             print(f"✅ [SDK TEST] Polymarket Connected! Found {len(markets)} active markets.")
        else:
             print("⚠️ [SDK TEST] Polymarket reachable, but returned 0 markets.")
    except Exception as e:
         print(f"❌ [SDK TEST] Polymarket Failed: {e}")

except ImportError as e:
    print(f"❌ [SDK TEST] pmxt is NOT installed correctly: {e}")
except Exception as e:
    print(f"❌ [SDK TEST] Fatal Error: {e}")

print("\n--- [SDK TEST FINISHED] ---")

# Keep the worker alive for a few minutes so you can see the log
time.sleep(300) 
