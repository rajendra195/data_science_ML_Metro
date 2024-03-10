import multiprocessing
import requests
from program_timer import timer
from multiprocessing import Pool, freeze_support

URL = "https://httpbin.org/uuid"

def fetch_uuid(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])

# print(multiprocessing.cpu_count())

@timer(1, 1)      
def main():
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch_uuid, [(session, URL) for _ in range(100)])

# if __name__ == "__main__":
#     main()
# raise error in window vs code but run in gollab collab