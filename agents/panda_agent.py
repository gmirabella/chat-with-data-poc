from langchain_openai import ChatOpenAI as langOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import streamlit as st
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI as pandaOpenAI

''' TODO 
The gpt version is hardcoded because it is necessary to check
 whether other versions chosen by the user can be used with upgrades
'''
def create_panda_df_agent(df: str):
    llm = langOpenAI(model="gpt-3.5-turbo", temperature=0)
    #llm = langOpenAI(openai_api_key="KEY")

    # Create a Pandas DataFrame agent.
    return create_pandas_dataframe_agent(
        llm, 
        df, 
        verbose=True, 
        agent_type="openai-tools"
        )

def create_pandas_ai_agent():
    llm = pandaOpenAI(api_token=st.session_state.get("OPENAI_API_KEY"))
    pandas_ai = PandasAI(llm, verbose=True, conversational=True)
    #llm = pandaOpenAI(api_token='KEY')
    # Create a PandasAI agent.
    return pandas_ai