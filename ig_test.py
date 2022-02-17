import imp
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth
import time

load_dotenv()

IG_USER = os.getenv("IG_USER")
IG_PASS = os.getenv("IG_PASS")

def ig_main(p_len):
    url = f"https://api.ticketswitch.com/f13/events.v1?country_code=uk&page_number=0&page_length={p_len}&req_media_triplet_one=true&req_media_marquee=true&req_extra_info=true&req_cost_range=true&sort_order=true&req_avail_details=true&req_avail_details_with_perfs=true"
    response = requests.get(url, auth=HTTPBasicAuth(IG_USER, IG_PASS))
    return response.json()

def t7e_main():
    url = "https://stage.triple7events.com/api/v2.0/event/get_events/?at_location=London,+UK&lat=51.5073509&long=-0.1277583&per_page=5&next_page=0"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    p_lens = [10, 20, 50, 100, 200, 500]
    start = time.monotonic()
    t7e_main()
    print(f"It took {time.monotonic()-start} S to Call T7E Api.\n\n")
    
    for l in p_lens:
        start = time.monotonic()
        ig_main(l)
        print(f"It took {time.monotonic()-start}Seconds to Call Api for Page Len {l}")