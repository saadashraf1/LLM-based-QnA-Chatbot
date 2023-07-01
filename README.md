# LLM Powered Chatbot

This repository contains code files for an LLM (Language Model) powered chatbot. The chatbot utilizes the OpenAI/Cohere and Langchain libraries to provide a conversational interface for answering questions and providing information based on text data.

## Overview

The code files in this repository include a Streamlit application that serves as the user interface for the chatbot. The chatbot leverages the power of LLMs provided by Cohere and Langchain to understand user queries and generate appropriate responses.

## Dependencies

To run the code in these files, you need to have the following dependencies installed:

- Python 3.x
- Streamlit
- Cohere
- Langchain
- Qdrant
- pandas

## Code Files

1. `app.py`: This Python file contains the main code for the LLM powered chatbot. It imports necessary modules, sets up the Streamlit user interface, initializes the LLM models from Cohere or OpenAI, handles user queries, and generates responses using the LLM models.

2. `text_load_utils.py`: This Python file contains utility functions for parsing text files and PDF files. It includes functions for parsing plain text files (`parse_txt`) and PDF files (`parse_pdf`), as well as a function for converting text to Langchain documents (`text_to_docs`).

3. `df_chat.py`: This Python file defines the `user_message` and `bot_message` classes, which are used for displaying user and bot messages in the Streamlit user interface.

## Getting Started

To get started with the LLM powered chatbot, you can follow these steps:

1. Install the required dependencies listed above.

2. Clone or download the repository containing the code files.

3. Open the `app.py` file in a Python IDE or text editor.

4. Update the API keys for Cohere and OpenAI, if necessary, by replacing the placeholders `cohere_api_key` and `openai_api_key` with your own API keys.

5. Run the `app.py` file. This will start the Streamlit application and open it in your default web browser.

6. Use the text input field in the web interface to type your message or query for the chatbot.

7. The chatbot will process your query using the LLM models and generate a response based on the provided text data.

## Additional Resources

- [Cohere Documentation](https://docs.cohere.com/docs/): Official documentation for the Cohere library.

- [Langchain Documentation](https://python.langchain.com/en/latest/index.html): Official documentation for the Langchain library.

## License

The code in this repository is licensed under the MIT License. You can find the full license text in the [LICENSE](https://github.com/cohere-ai/notebooks/blob/main/LICENSE) file.

Feel free to explore and modify the code to enhance the functionality of the chatbot! If you have any questions or feedback, please reach out to the repository owners.