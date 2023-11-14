import openai
import streamlit as st
from lida import Manager, TextGenerationConfig, llm
from langchain.llms import OpenAI as langOpenAI


def create_openai_agent( messages):
    openai.api_key = st.session_state.get("OPENAI_API_KEY")
    modelName=st.session_state.get("MODEL_NAME")
    #openai.api_key = 'API_KEY'
    return openai.ChatCompletion.create(
                        model=modelName, messages=messages, stream=True
                    )
