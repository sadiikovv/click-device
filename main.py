import json
import os
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

TARGET_URL = "https://my.click.uz/"
PHONE_SELECTOR = '[data-testid="auth-phone-input"]'
LOGIN_BTN_SELECTOR = '[data-testid="auth-login-button"]'
TRUST_BTN_OFF_SELECTOR = '[data-testid="sms-page-trust-device-btn-off"]'
TRUST_BTN_ON_SELECTOR = '[data-testid="sms-page-trust-device-btn-on"]'
CODE_INPUT_SELECTOR = '[data-testid="sms-page-code-input"]'
CONFIRM_BTN_SELECTOR = '[data-testid="sms-page-confirm-btn"]'
PIN_INPUT_SELECTOR = '[data-testid="pin-page-pin-input"]'
PIN_ENTER_BTN_SELECTOR = '[data-testid="pin-page-enter-btn"]'
API_CONTAINS = "/evo/"

def pretty_print_request_response(entry, idx=None):
    if idx is not None:
        print(f"\n--- #{idx} URL: {entry.get('url')} status: {entry.get('status')} ---")
    else:
        print(f"\n--- URL: {entry.get('url')} status: {entry.get('status')} ---")
    print("Request POST data:")
    rb = entry.get("request_body")
    if rb is None:
        print("  <no request body captured>")
    else:
        try:
            parsed = json.loads(rb)
            print(json.dumps(parsed, indent=2, ensure_ascii=False))
        except Exception:
            print(str(rb)[:4000])
    print("\nResponse body:")
    resp = entry.get("response_body")
    if resp is None:
        print("  <no response body captured>")
    else:
        if isinstance(resp, (dict, list)):
            print(json.dumps(resp, indent=2, ensure_ascii=False))
        else:
            print(str(resp)[:8000])

def save_captured_json(captured):

    try:
        with open("responses.json", "w", encoding="utf-8") as f:
            json.dump(captured, f, ensure_ascii=False, indent=2)
        print("[+] All captured requests/responses saved to responses.json")
    except Exception as e:
        print("[!] Failed to save responses.json:", e)

def run(phone_number: str, headless=True):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=not (str(headless).lower() in ("false","0","no")),
            args=["--no-sandbox"]
        )
        context = browser.new_context()
        page = context.new_page()

        captured = []

        def on_response(response):
            try:
                url = response.url
                if API_CONTAINS in url:
                    try:
                        req = response.request
                        req_body = None
                        try:
                            req_body = req.post_data
                        except Exception:
                            req_body = None
                        try:
                            text = response.text()
                        except Exception as e:
                            text = f"<error reading body: {e}>"
                        try:
                            parsed = json.loads(text)
                        except Exception:
                            parsed = text
                        captured.append({
                            "url": url,
                            "status": response.status,
                            "request_body": req_body,
                            "response_body": parsed
                        })
                    except Exception:
                        pass
            except Exception:
                pass

        page.on("response", on_response)

        print("[*] Opening page:", TARGET_URL)
        page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=30000)


        try:
            page.wait_for_selector(PHONE_SELECTOR, timeout=20000)
            page.fill(PHONE_SELECTOR, phone_number)
            print("[+] Phone input filled.")
        except PWTimeout:
            print("[!] Phone input not found within timeout.")
            browser.close()
            return

        try:
            page.click(LOGIN_BTN_SELECTOR, timeout=10000)
            print("[+] Login/submit clicked.")
        except PWTimeout:
            print("[!] Login button not clickable / not found.")
            browser.close()
            return

        page.wait_for_timeout(3000)

        try:
            page.wait_for_selector(TRUST_BTN_OFF_SELECTOR, timeout=3000)
            try:
                page.click(TRUST_BTN_OFF_SELECTOR)
                print("[+] Clicked TRUST device checkbox.")
            except Exception:
                el = page.query_selector(TRUST_BTN_OFF_SELECTOR)
                if el:
                    page.evaluate("(el)=>el.click()", el)
                    print("[+] Clicked TRUST via JS.")
            page.wait_for_timeout(500)
        except PWTimeout:
            if page.query_selector(TRUST_BTN_ON_SELECTOR):
                print("[*] Trust checkbox already ON.")
            else:
                print("[*] Trust checkbox not present; continuing.")

        token = input("SMS kodni kiriting (yoki confirm_token): ").strip()
        if not token:
            print("No token provided; exiting.")
            browser.close()
            return

        try:
            page.wait_for_selector(CODE_INPUT_SELECTOR, timeout=5000)
            page.fill(CODE_INPUT_SELECTOR, token)
            try:
                page.click(CONFIRM_BTN_SELECTOR)
                print("[+] Confirm clicked.")
            except Exception:
                page.press(CODE_INPUT_SELECTOR, "Enter")
                print("[+] Pressed Enter on code input.")
        except PWTimeout:
            print("[!] Code input not found on page.")

        page.wait_for_timeout(3000)

        try:
            page.wait_for_selector(PIN_INPUT_SELECTOR, timeout=5000)
            print("[*] PIN input detected.")
            pin_code = input("PIN kodni kiriting (yoki ENTER qoldiring): ").strip()
            if pin_code:
                page.fill(PIN_INPUT_SELECTOR, pin_code)
                try:
                    page.click(PIN_ENTER_BTN_SELECTOR)
                    print("[+] PIN Enter button clicked.")
                except Exception:
                    page.press(PIN_INPUT_SELECTOR, "Enter")
                page.wait_for_timeout(3000)
        except PWTimeout:
            print("[*] No PIN input found; skipping PIN stage.")

        try:
            cookies = context.cookies()
            with open("cookies.json", "w", encoding="utf-8") as f:
                json.dump(cookies, f, ensure_ascii=False, indent=2)
            print("[+] Cookies saved.")
        except Exception as e:
            print("[!] Could not save cookies:", e)

        save_captured_json(captured)

        browser.close()

if __name__ == "__main__":
    phone = os.environ.get("CLICK_PHONE") or input("Telefon raqamini kiriting. Misol uchun(998909009090): ").strip()
    run(phone, headless=True)


