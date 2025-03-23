
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Referer": "https://www.google.com/",
}

url=""
response = requests.get(url, headers=headers)


if response.status_code == 200:

    soup = BeautifulSoup(response.content, "html.parser")

 
    print(soup.get_text())
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
