import requests
from bs4 import BeautifulSoup
import os

# Function to download an image from a URL
def download_image(url, directory):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded: {file_name}")
    else:
        print(f"Failed to download image from: {url}")

# Function to scrape images from a website
def scrape_images(url, directory):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        img_tags = soup.find_all('img')

        if not os.path.exists(directory):
            os.makedirs(directory)

        for img in img_tags:
            if 'src' in img.attrs:
                img_url = img['src']
                if img_url.startswith('http'):
                    download_image(img_url, directory)
    else:
        print(f"Failed to scrape images from: {url}")


# Example usage
website_url = "https://thepetwala.com"  #Website to download images from.
download_directory = " "  # Add your own directory here to download the images to.

scrape_images(website_url, download_directory)
