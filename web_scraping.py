import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

# URL of the subreddit r/programming
url = 'https://www.reddit.com/r/programming/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = []
    scores = []
    links = []

    # Find all div elements with the specified class for titles
    divs = soup.find_all('div', class_='font-semibold text-neutral-content-strong text-16 xs:text-18 mb-2xs xs:mb-xs')
    for div in divs:
        titles.append(div.get_text(strip=True))

    # Find all shreddit-post elements for scores
    shreddit_posts = soup.find_all('shreddit-post')
    for post in shreddit_posts:
        score = post['score']
        scores.append(score)

        # Get the relative link and convert it to an absolute URL
        relative_link = post['permalink']
        absolute_link = urljoin(url, relative_link)
        links.append(absolute_link)

    # Write the extracted data to a CSV file
    with open('reddit_programming.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write data row by row
        for title, score, link in zip(titles, scores, links):
            csv_writer.writerow([title, score, link])

    print("Data saved successfully to the 'reddit_programming.csv' file.")
else:
    print("Unable to retrieve the page.")