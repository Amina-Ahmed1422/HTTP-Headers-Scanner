import requests

SECURITY_HEADERS = { 
    "Content-Security-Policy": 
        "Helps prevent XSS and other code injection attacks.",

    "Strict-Transport-Security":
        "Forces browsers to use HTTPS.",

    "X-Content-Type-Options":
        "Helps prevent MIME-type sniffing.",

    "X-Frame-Options":
        "Helps protect against clickjacking.",

    "Referrer-Policy":
      "Controls how much referrer information is shared.",

    "Permissions-Policy":
        "Controls access to browser features."
}
def scan_headers(url): 
    try: 
        response = requests.get(url, timeout=10)

        print("\nHTTP Headers Scanner")
        print("=" * 40)
        print(f"Target: {url}")
        print(f"Status Code: {response.status_code}")
        print("=" * 40)

        for header, description in SECURITY_HEADERS.items():

            if header in response.headers:
                 print(f"[+] {header}: PRESENT")

            else:
             print(f"[-] {header}: MISSING")
             print(f"    {description}")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")
url = input("Enter website URL: ")

if not url.startswith(("http://", "https://")): 
    url = "https://" + url
scan_headers(url)