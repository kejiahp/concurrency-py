import requests
import time
import threading
import concurrent.futures

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session

def download_sites(url: str):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites():
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_sites, sites)


if __name__ == "__main__":
    start_time = time.time()
    download_all_sites()
    duration = time.time() - start_time
    print(f"{duration} seconds") # 8.932958602905273 seconds 😮