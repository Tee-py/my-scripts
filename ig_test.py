import imp
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import time

load_dotenv()

IG_USER = os.getenv("IG_USER")
IG_PASS = os.getenv("IG_PASS")

def main(p_len):
    url = f"https://api.ticketswitch.com/f13/events.v1?country_code=uk&page_number=0&page_length={p_len}"
    response = requests.get(url, auth=HTTPBasicAuth(IG_USER, IG_PASS))
    return response.json()

if __name__ == "__main__":
    p_lens = [10, 20, 50, 100, 200, 500]
    for l in p_lens:
        start = time.monotonic()
        main(l)
        print(f"It took {time.monotonic()-start}MS to Call Api for Page Len {l}")