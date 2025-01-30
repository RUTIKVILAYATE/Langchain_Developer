from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os 


from dotenv import load_dotenv
load_dotenv()


# Langsmith Tracking 
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot With OPENAI"


# Prompt Template 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user query")
        ("user", "Question: {question}")
    ]
)

def generate_response(question,llm,temperature,max_tokens):
    llm = ollama(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({"question":question})
    return answer



# Title of the App
st.title("Enhanced Q&A Chatbot With Ollama")


st.sidebar.title("Settings")
# api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")


# Drop Down to select various openai models 
engine = st.sidebar.selectbox("Select an OpenAI Model", ["mistral"])

# Adjust response parameter 
temperature = st.sidebar("Temperature", min_value=0.0, max_value= 1.0,value= 0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)


# Main Interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,engine,temperature,max_tokens)
    st.write(response)
else: 
    st.write("Please provide the query ")