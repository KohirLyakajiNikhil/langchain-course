import os
from dotenv import load_dotenv
from langchain_perplexity import ChatPerplexity
from langchain_core.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Get the API key
api_key = os.getenv("PERPLEXITY_API_KEY")
if not api_key:
    raise ValueError("PERPLEXITY_API_KEY environment variable is not set.")



information = """Clearer classification of vehicles and auto parts will cut down disputes, improve compliance, and support growth in Indian automotive manufacturing and exports.

Small cars, two-wheelers ≤350cc: 28% → 18%.
Buses, trucks, three-wheelers, all auto parts: 28% → 18%."""

summary_template = """
Given the information {{information}} about tax cut ,If the petrol variant Nexon car is currently priced at on-road ₹14,26,000, what would be the estimated on road price in Hyderabad after the tax reduction?
"""

# Create prompt and invoke
summary_prompt_template = PromptTemplate(
    input_variables=["information"],
    template = summary_template
)
# Initialize Perplexity model
llm = ChatPerplexity(model="sonar", temperature=0.7, pplx_api_key=api_key)

chain = summary_prompt_template | llm
response = chain.invoke(input=
    {"input": information}
)
print(response.content)

def main():
  if __name__ == "__main__":
     main()