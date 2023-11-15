import streamlit as st

from dotenv import load_dotenv
import os

# Setting up the api key
import environ

env = environ.Env()
environ.Env.read_env()

#comment this line in local env, because this work only for streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

load_dotenv()



def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below 🔑\n"  # noqa: E501
            "2. Upload a csv file 📄\n"
            "3. Ready to Roll! 🚀"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )
        model_name = st.selectbox('Select Model',("gpt-3.5-turbo-0301","gpt-3.5-turbo", "gpt4-turbo", "-"), help="OpenAI models are advanced language models designed for various tasks. Versions like GPT-3.5 provide powerful natural language processing. Newer versions may offer improved capabilities, training on diverse data for better performance. Explore the right version for your needs!")    


        st.session_state["OPENAI_API_KEY"] = api_key_input
        st.session_state["MODEL_NAME"] = model_name
