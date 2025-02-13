import requests
from bs4 import BeautifulSoup
import webbrowser
import os

# URL to scrape
url = "https://www.ebay.com/deals?_trkparms=parentrq%3Af8afcd011940a60c4e3c6515ffffc4f0%7Cpageci%3A66c433ae-e904-11ef-8703-46859dd65244%7Ciid%3A1%7Cvlpname%3Avlp_homepage"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all div elements with class "dne-itemtile-detail"
    jfy_divs = soup.find_all('div', class_='dne-itemtile-detail')

    # Check if any divs were found
    if not jfy_divs:
        print("No divs found with class 'dne-itemtile-detail'")

    # Create an HTML file and write the output
    output_file = "webscraper.html"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("<html>\n<head>\n<title>Scraped Content</title>\n</head>\n<body>\n")
        file.write("<h1>Scraped Content</h1>\n")

        for div in jfy_divs:
            file.write(f"<p>{div.get_text(strip=True)}</p>\n")

        file.write("</body>\n</html>")

    # Open the HTML file in the default web browser
    webbrowser.open(f"file://{os.path.abspath(output_file)}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")