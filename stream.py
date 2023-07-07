import streamlit as st

# Set the title of the webpage
st.title('Image Searcher')

# Set the page layout with columns
left_column, right_column = st.beta_columns(2)

# Left column
with left_column:
    # Create an input box for users to enter text
    written_input = st.text_input('Enter text')

    # Display the written input
    st.write('You entered:', written_input)

# Right column
with right_column:
    # Add borders and colorfulness
    st.markdown('<style>.stButton>button{background-color:#ffcc00;border-color:#000;color:#000;border-radius:10px;padding:10px 16px;font-size:16px;font-weight:bold;}</style>', unsafe_allow_html=True)

    # Add a button with colorful style
    if st.button('Search', key='search_button'):
        # Add a colorful message when the button is clicked
        st.markdown('<p style="color:#ffcc00;font-size:20px;">Searching for images...</p>', unsafe_allow_html=True)

# Add a footer with border and color
st.markdown('<hr style="border: 2px solid #ffcc00;">', unsafe_allow_html=True)
st.markdown('<p style="color:#ffcc00;">Powered by Image Searcher</p>', unsafe_allow_html=True)
