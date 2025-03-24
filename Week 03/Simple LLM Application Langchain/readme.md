# LangChain Translation App

## Overview
This project is a simple translation application built using **LangChain**, **Groq's LLM**, and **FastAPI**. The app allows users to input text and specify a target language, and it returns the translated text.

## Features
- Uses **LangChain** to structure and process translation requests.
- Integrates **Groq's LLM** for efficient translation.
- Supports **FastAPI** for API deployment.
- Provides an endpoint (`/chain`) for easy integration with frontend applications.

## Installation

### Prerequisites
Make sure you have **Python 3.8+** installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-repo/langchain-translation-app.git
cd langchain-translation-app
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set API Key
Obtain an API key from [Groq](https://groq.com/) and set it as an environment variable:
```bash
export GROQ_API_KEY="your_api_key"
```
(On Windows, use `set GROQ_API_KEY="your_api_key"` instead.)

## Running the Application
To start the FastAPI server, run:
```bash
python serve.py
```
The API will be available at `http://localhost:8000/chain`.

## API Usage
### Endpoint: `/chain`
#### Request (POST)
```json
{
  "language": "italian",
  "text": "hello"
}
```
#### Response (JSON)
```json
"ciao"
```

### Testing via cURL
```bash
curl -X POST "http://localhost:8000/chain" \
     -H "Content-Type: application/json" \
     -d '{"language": "italian", "text": "hello"}'
```
Moreover the frontend is created on plain html css you can also access that or use the application using the langchain playground.