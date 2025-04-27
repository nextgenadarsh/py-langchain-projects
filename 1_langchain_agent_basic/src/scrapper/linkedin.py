import os
import requests


def scrape_linkedin_profile(profile_url: str, mock: bool = False):
    if mock is True:
        profile_url = "https://gist.githubusercontent.com/nextgenadarsh/c9713e27e2f38f4fca0aea3e2b703ea8/raw/9bcc60134f87fc819cf47e86198590fe532fced1/linkedin_nextgenadarsh.json"
        response = requests.get(profile_url, timeout=10)
    else:
        api_endpoint = f"https://api.scrapin.io/enrichment/profile"
        params = {"apikey": os.environ["SCRAPIN_API_KEY"], "linkedInUrl": profile_url}
        response = requests.get(api_endpoint, params=params, timeout=10)

    data = response.json().get("person")
    data = {
        key: value
        for key, value in data.items()
        if value not in ([], "", None) and key not in ["certifications"]
    }
    return data


# print(scrape_linkedin_profile("http://linkedin.com/in/nextgenadarsh/", True))
