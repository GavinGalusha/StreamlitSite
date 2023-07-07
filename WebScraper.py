import requests
from bs4 import BeautifulSoup

def count_word_occurrences(url, word):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all text elements on the page
        text_elements = soup.find_all(text=True)
        
        # Count the occurrences of the word
        count = 0
        for element in text_elements:
            if word.lower() in element.lower():
                count += 1
        
        return count
    else:
        print('Error: Failed to retrieve the website content.')
        return 0

# Specify the URL of the website you want to scrape
url = 'https://www.example.com/'

# Specify the word you want to count occurrences of
word = 'example'

# Call the function to get the count
occurrence_count = count_word_occurrences(url, word)

# Print the result
print(f'The word "{word}" was found {occurrence_count} times on the website.')
