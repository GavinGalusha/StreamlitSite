import streamlit as st
from googlesearch import search
from WebScraper import count_word_occurrences


# Initialize session state
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

# Set the background color to dark blue
st.markdown(
    """
    <style>
    body {
        background-color: #192A56;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the title of the webpage with contrasting color
st.title('Web Scraper')
st.markdown('<p style="color:#ffcc00;">Scrape a Website for Word Occurrences</p>', unsafe_allow_html=True)

# Set the page layout with columns
left_column, right_column = st.columns(2)

# Left column
with left_column:
    # Create an input box for users to enter text with contrasting color
    written_input = st.text_input('Enter a website name or URL', key='website_input')
    st.markdown('<p style="color:#ffcc00;">You entered:</p>', unsafe_allow_html=True)
    st.write(written_input)

# Right column
with right_column:
    # Save search to history
    if st.button('Search', key='search_button'):
        searching_placeholder = st.empty()
        searching_placeholder.markdown(
            '<p style="color:#ffcc00;font-size:20px;">Searching the web...</p>', unsafe_allow_html=True)

        query = written_input

        for j in search(query, tld="co.in", num=3, stop=3, pause=2):
            st.write(j)

        # Save the search query to the search history
        st.session_state.search_history.append(query)

        searching_placeholder.empty()

# Display search history for the user
st.write('Search History:')
selected_queries = st.multiselect('Select Previous Searches', st.session_state.search_history)
if selected_queries:
    st.write('You selected:', ', '.join(selected_queries))

# Add a footer with border and contrasting color
st.markdown('<hr style="border: 2px solid #ffcc00;">', unsafe_allow_html=True)

# Set the header for the word occurrence section with contrasting color
st.header('Word Occurrence Counter')
st.markdown('<p style="color:#ffcc00;">Enter a URL and a word to count its occurrences on the website</p>', unsafe_allow_html=True)

# Create input boxes for URL and word with contrasting color
url_input = st.text_input('Enter URL', key='url_input')
word_input = st.text_input('Enter Word', key='word_input')

# Create the "Webscrape" button with contrasting color
if st.button('Webscrape'):
    # Call the function to get the count
    occurrence_count = count_word_occurrences(url_input, word_input)

    # Print the result with contrasting color
    st.markdown(f'<p style="color:#ffcc00;">The word "{word_input}" was found {occurrence_count} times on the website.</p>',
                unsafe_allow_html=True)
