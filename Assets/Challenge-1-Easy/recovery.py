import time
import base64

def system_boot():
    print("--- PUP-STC LAB 2: EMERGENCY RECOVERY SYSTEM ---")
    time.sleep(1)
    print("[!] Warning: System integrity compromised.")
    print("[!] Author: Juan Dela Cruz (BSIT 2-1)")
    print("-----------------------------------------------")

def check_access():
    access_key = "ADMIN_PROMPT_2026"
    
    print("\nAttempting to recover encrypted session data...")
    time.sleep(2)
    
    encoded_flag = "ZWR1Q1RGe3c0c19pdF8zYXN5X200cjFhaD9fOTQyOH0="
    decoded_flag = base64.b64decode(encoded_flag).decode('utf-8')

    print(f"\n[SUCCESS] Session Key Recovered: {decoded_flag}")
    print("\nLOG ENTRY: 'Someone is definitely outside. - Juan'")

if __name__ == "__main__":
    system_boot()
    check_access()