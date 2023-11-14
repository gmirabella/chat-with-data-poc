import streamlit as st
import pandas as pd
from services.query_service import handle_sample_query
from services.chart_service import handle_chart_query
from services.lida_service import handle_lida_chart_query
from components.sidebar import sidebar
from components.button_panel import generate_buttons
from components.tutorial import tutorial
from utils import get_data, chart_framework_selector
from components.tutorial import tutorial

# Suppress deprecation warnings related to Pyplot's global use
st.set_option("deprecation.showPyplotGlobalUse", False)
st.set_page_config(page_title="Chat With Data", page_icon="📖", layout="wide")

# Cache the header of the app to prevent re-rendering on each load
@st.cache_resource
def display_app_header():
    """Display the header of the Streamlit app."""
    st.header("🤖 Chat With Data 🤖", divider='red')


# Display the header of the app
display_app_header()
sidebar()
tutorial()

df = get_data()

# If data is uploaded successfully
if df is not None:
     # Extract column names for further processing
     column_names = ", ".join(df.columns)
     generate_buttons(df, column_names)

     # Check if the uploaded DataFrame is not empty
     if not df.empty:
         # Handle the OpenAI query and display results in a text
        handle_sample_query(df=df, column_names=column_names)

         # Handle the OpenAI query and display results in a chart
        st.header('📈 Generate a Chart 📈', divider='red')
        chart_framework_selector(df=df, column_names=column_names)
     else:
        st.write("Warning")



