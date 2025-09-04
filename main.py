from dotenv import load_dotenv

"""from langchain_core.prompts import PromptTemplate
from langchain_perplexity import ChatPerplexity
load_dotenv()


def main():
    print("Hello from langchain-course!")



if __name__ == "__main__":
    main()"""
import os

# from dotenv import load_dotenv
from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()

# Get the API key
api_key = os.getenv("PERPLEXITY_API_KEY")
if not api_key:
    raise ValueError("PERPLEXITY_API_KEY environment variable is not set.")

# Initialize Perplexity model
llm = ChatPerplexity(model="sonar", temperature=0.7, pplx_api_key=api_key)

# Create prompt and invoke
prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."), ("human", "{input}")]
)

chain = prompt | llm
response = chain.invoke(
    {"input": "I am reaching you over API call. How do you feel about it?"}
)
print(response.content)
