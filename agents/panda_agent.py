from langchain import OpenAI as langOpenAI
from langchain.agents import create_pandas_dataframe_agent, AgentType
import streamlit as st
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI as pandaOpenAI


def create_panda_df_agent(df: str):
    llm = langOpenAI(openai_api_key=st.session_state.get("OPENAI_API_KEY"))
    #llm = langOpenAI(openai_api_key="KEY")

    # Create a Pandas DataFrame agent.
    return create_pandas_dataframe_agent(
        llm, 
        df, 
        verbose=True, 
        agent_type=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION
        )

def create_pandas_ai_agent():
    llm = pandaOpenAI(api_token=st.session_state.get("OPENAI_API_KEY"))
    pandas_ai = PandasAI(llm, verbose=True, conversational=True)
    #llm = pandaOpenAI(api_token='KEY')
    # Create a PandasAI agent.
    return pandas_ai