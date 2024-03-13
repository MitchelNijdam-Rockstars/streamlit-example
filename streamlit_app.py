import streamlit as st
import requests

# Function to fetch GitHub user data
def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

st.title('GitHub Profile Viewer')

username = st.text_input('Enter GitHub username:', '')

# TODO: Use the fetch_github_user function to get user data
# and display the user's name, bio, and avatar.
# Hint: Use st.image for the avatar, st.write or st.markdown for text.

if username:
    user_data = fetch_github_user(username)
    if user_data:
        st.image(user_data['avatar_url'])
        # Display the GitHub user's details
        # Participants will fill in these parts using AI tools.
        pass  # Replace this with code to display user data
    else:
        st.error("User not found")
