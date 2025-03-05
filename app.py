import requests

def fetch_url(url):
    response = requests.get(url)
    return response.status_code

if __name__ == "__main__":
    print(fetch_url("https://www.google.com"))
