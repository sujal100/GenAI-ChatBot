# GenAI Chatbot Project

## Objective

Inspired by companies like GitLab, which embody a “build in public” philosophy, this project aims to foster transparency, collaboration, and learning. GitLab openly shares its strategies, roadmaps, and internal processes, encouraging community feedback and improvement.

The challenge for this project is to develop an interactive chatbot that allows users—employees or aspiring employees—to easily access information from GitLab’s Handbook and Direction pages. By providing an engaging interface, the chatbot will retrieve relevant information based on user queries and help users learn in an accessible and engaging way.

## Project Structure

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Project

1. Run the Streamlit app:
    ```sh
    streamlit run ui/app.py
    ```

## File Descriptions

### `context.txt`
Contains the initial context data used by the chatbot to answer questions. This file includes information from GitLab’s Handbook and Direction pages.

### `dotenv.py`
Contains environment variables for the project. Currently, it includes:
```py
TF_ENABLE_ONEDNN_OPTS=0
```

### `requirements.txt`
Lists all the dependencies required for the project:

- streamlit
- gradio
- transformers
- torch
- requests
- beautifulsoup4
- tf-keras

### `src/`
Contains the source code for the chatbot.

### `src/chatbot.py`
Defines the GenAIChatbot class, which uses a pre-trained model from the transformers library to answer questions based on the provided context.

### `src/data_processing.py`
Contains functions to fetch and process data from GitLab’s Handbook and Direction pages.

### `tests/`
Contains unit tests for the chatbot.

### `tests/test_chatbot.py`
Defines unit tests for the GenAIChatbot class to ensure it functions correctly.

### `ui/`
Contains the frontend code for the chatbot.

### `ui/app.py`
Defines the Streamlit app that provides the user interface for interacting with the chatbot.