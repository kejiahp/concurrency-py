import requests
import time


def download_sites(url: str):
    with requests.Session() as session:
        with session.get(url) as response:
            print(f"Read {len(response.content)} from {url}")

def download_all_sites():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    for i in sites:
        download_sites(i)


if __name__ == "__main__":
    start_time = time.time()
    download_all_sites()
    duration = time.time() - start_time
    print(f"{duration} seconds") #100.85387945175171 seconds