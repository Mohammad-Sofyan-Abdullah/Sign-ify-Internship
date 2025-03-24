from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.chat_models import ChatGroq  # Use ChatGroq instead of ChatOpenAI
from langchain_groq import ChatGroq
from langserve import add_routes
from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware


# Set your Groq API key
os.environ["GROQ_API_KEY"] = "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"  # Replace with your actual API key

# Create a prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Use Groq's chat model
model = ChatGroq(model="llama3-8b-8192")  # Use the correct model name
 # Replace with the correct Groq model name

# Create a parser
parser = StrOutputParser()

# Create a chain
chain = prompt_template | model | parser

# Create a FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces"
)


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change to specific frontend URL for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Add a route for the chain
add_routes(app, chain, path="/chain")

if __name__ == "__main__":  # Fixed typo (_name_ → __name__)
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
