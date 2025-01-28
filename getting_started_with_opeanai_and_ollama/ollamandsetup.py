# To setup and loading all the environment variables
import os 
from dotenv import load_dotenv
load_dotenv.load()

from langchain_community.llms import ollama
import streamlit as st 
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser



# Setting up Lanchain API Keys in os environment

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv["LANGCHAIN_PROJECT"]


# Prompt Template 
prompt = ChatMessagePromptTemplate.from_message(
    [
    ("system", "You are a helpful assistant. Please respond to the question asked "),
    ("user","Question:{question}")
    ]
    )

# streamlit framework 
st.title("Langchain Demo with Gemma model")
input.text = st.text_input("What question you have in mind?")

# ollama gemma model
llm = Ollama(model="gemma:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser 



if input_text:
    st.write(chain.invoke({"question":input_text}))

