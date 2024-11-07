import sys
import os
import streamlit as st

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from chatbot import GenAIChatbot
from data_processing import fetch_data

st.title("GenAI Chatbot")

# Initialize the chatbot
chatbot = GenAIChatbot()

# Fetch data from GitLab's Handbook and Direction pages
handbook_url = "https://about.gitlab.com/handbook/"
direction_url = "https://about.gitlab.com/direction/"
handbook_company_url = "https://handbook.gitlab.com/handbook/company/"
about_company_url = "https://about.gitlab.com/company/"
context = "Inspired by companies like GitLab, which embody a “build in public” philosophy, this project aims to foster transparency, collaboration, and learning. GitLab openly shares its strategies, roadmaps, and internal processes, encouraging community feedback and improvement."


handbook_data = fetch_data(handbook_url)
direction_data = fetch_data(direction_url)
about_company_data = fetch_data(about_company_url)
handbook_company_data = fetch_data(handbook_company_url)

# remoing empty lines
handbook_data = "\n".join([line for line in handbook_data.split("\n") if line.strip()])
direction_data = "\n".join([line for line in direction_data.split("\n") if line.strip()])
about_company_data = "\n".join([line for line in about_company_data.split("\n") if line.strip()])
handbook_company_data = "\n".join([line for line in handbook_company_data.split("\n") if line.strip()])

initial_context = context + handbook_data + direction_data + about_company_data+ handbook_company_data


# Initialize session state for chat history and context
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'context' not in st.session_state:
    st.session_state.context = initial_context

# Function to handle user input and generate response
def handle_input(user_input):
    response = chatbot.get_answer(user_input, st.session_state.context)
    if isinstance(response, dict) and 'answer' in response:
        st.session_state.chat_history.append({"user": user_input, "bot": response['answer']})
        # Update context with the new question and answer
        st.session_state.context += f"\nUser: {user_input}\nBot: {response['answer']}"
    else:
        st.session_state.chat_history.append({"user": user_input, "bot": "No answer available."})

# User input
user_input = st.text_input("Ask me anything about GitLab:")

# Handle user input
if user_input:
    handle_input(user_input)

# Option to clear chat history
if st.button("Start New Chat"):
    st.session_state.chat_history = []
    st.session_state.context = initial_context

# Display chat history in a collapsible section
with st.expander("Show Chat History"):
    st.write("### Chat History")
    for chat in st.session_state.chat_history:
        st.write(f"**User:** {chat['user']}")
        st.write(f"**Bot:** {chat['bot']}")

# Option to save chat history temporarily
if 'saved_history' not in st.session_state:
    st.session_state.saved_history = []

if st.button("Save Current Chat"):
    st.session_state.saved_history.append(st.session_state.chat_history.copy())
    st.session_state.chat_history = []

# Display saved chat history in a collapsible section
with st.expander("Show Saved Chat History"):
    st.write("### Saved Chat History")
    for idx, history in enumerate(st.session_state.saved_history):
        st.write(f"**Chat {idx + 1}:**")
        for chat in history:
            st.write(f"**User:** {chat['user']}")
            st.write(f"**Bot:** {chat['bot']}")

# Option to restore a saved chat
if st.button("Restore Last Saved Chat"):
    if st.session_state.saved_history:
        st.session_state.chat_history = st.session_state.saved_history.pop()