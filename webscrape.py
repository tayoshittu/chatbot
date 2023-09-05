import requests
from bs4 import BeautifulSoup

# List of Siemens related URLs to scrape to build corpus
urls = ['https://en.wikipedia.org/wiki/Siemens','https://www.sw.siemens.com/en-US','https://eda.sw.siemens.com/en-US', 'https://eda.sw.siemens.com/en-US/ic',
'https://eda.sw.siemens.com/en-US/ic/products', 'https://eda.sw.siemens.com/en-US/ic-packaging', 'https://eda.sw.siemens.com/en-US/ic-packaging/software',
'https://eda.sw.siemens.com/en-US/pcb','https://eda.sw.siemens.com/en-US/trending-technologies',
'https://eda.sw.siemens.com/en-US/trending-technologies/artificial-intelligence-machine-learning','https://eda.sw.siemens.com/en-US/consulting-services',
'https://eda.sw.siemens.com/en-US/cloud-solutions','https://eda.sw.siemens.com/en-US/eda-training']

# Initialize an empty string to store the scraped content
scraped_content = ''

# Iterate over each URL
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the specific elements on the page that contain the content you want to scrape
        # Customize this based on the structure of each website's HTML
        content_elements = soup.find_all('p')

        # Extract the text content from the elements and append it to the scraped_content string
        scraped_content += '\n\n'.join(element.get_text() for element in content_elements)
        scraped_content += '\n\n'  # Add a separator between each website's content
    else:
        print(f"Failed to retrieve content from URL: {url}")

# Save the scraped content into a text file
with open('siemens_content.txt', 'w', encoding='utf-8') as file:
    file.write(scraped_content)

print('Scraping and saving content complete.')
