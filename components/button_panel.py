import streamlit as st
from services.query_service import handle_quick_summary
from services.lida_service import handle_lida_summary
from utils import persona_selector

def generate_buttons(data, column_names):
    on = st.sidebar.toggle('View Table Data')
    if on:
        st.write(data) 
        if data.isnull().sum().any():
                st.warning("There are missing values in the dataset. Consider handling them.")
                
    st.sidebar.write("📊 Explore CSV with a click! Choose your user type and unlock insights: spot patterns, create graphs, find connections, and get personalized tips.")
    persona=persona_selector()
    if st.sidebar.button("Deep Summary", type="primary"):
       handle_lida_summary(persona=persona)

    st.sidebar.write("📜 Short on time? Get instant insights in a snapshot! Ideal for a brief summary of key data points.")
    if st.sidebar.button("Quick Summary", type="primary"):
       handle_quick_summary(df=data, column_names=column_names)
  
   

   