# Chat-UI

**Tax-Related Question Interface**

A simple web interface for asking tax-related questions. This system uses Flask for the backend and the OpenAI GPT model to fetch answers. The main aim is to help users get quick responses to their tax queries.

**Table of Contents**
* Features

1. Web Interface: Users can ask tax-related questions through a browser.

1. Flask Backend: Handles web requests and interacts with OpenAI's API.

1. Error Handling: Ensures that users receive helpful error messages if something goes wrong.

* Setup and Installation
 
1. Clone the Repository
```
git clone https://github.com/krushikagujarati/Chat-UI.git
cd Chat-UI
```
2. Install Dependencies
```
pip install Flask openai
```
3. Run the Server
```
python app.py
```

* Usage

1. Ask a Question: Navigate to the main page. You will see a text area where you can type your tax-related question. After submitting, the answer will be displayed below.

1. Error Messages: If the system encounters an error, it will display an error message. This might include issues like quota exceedance or non-tax-related questions.

* Error Handling

1. Questions that aren't related to taxes will be flagged.
1. If the OpenAI quota is exceeded, a message will be shown to inform the user.
1. General and OpenAI-specific errors are also caught and appropriate messages are shown.

* UI

![WhatsApp Image 2023-10-18 at 12 16 30 PM](https://github.com/krushikagujarati/Chat-UI/assets/48424819/31d4d91b-2556-4d8a-871c-72c30581d603)

Limit prompts only to Tax related questions

![WhatsApp Image 2023-10-18 at 12 12 03 PM](https://github.com/krushikagujarati/Chat-UI/assets/48424819/43848897-ada9-4684-9a92-2e5074b5fbc5)

