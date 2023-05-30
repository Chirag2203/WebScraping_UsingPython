import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.example.com/table.html"  #URL of the page with the table
response = requests.get(url)

# BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Finding the table element
table = soup.find("table")

# Extracting data from the table
data = []
for row in table.find_all("tr"):
    row_data = []
    for cell in row.find_all("td"):
        row_data.append(cell.text.strip())
    if row_data:
        data.append(row_data)

# Printing the extracted data
for row in data:
    print(row)
