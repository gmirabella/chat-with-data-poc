import streamlit as st
import pandas as pd
from services.lida_service import handle_lida_chart_query
from services.chart_service import handle_chart_query

def get_data():
    """
    Upload data via a file.

    Returns:
    - df: DataFrame containing the uploaded data or None if no data was uploaded
    """
    
    # File uploader for data file
    file_types = ["csv", "xlsx", "xls"]
    data_upload = st.file_uploader("Upload a data file", type=file_types)
    
    if data_upload:
        path_to_save = "filename.csv"
        with open(path_to_save, "wb") as f:
            f.write(data_upload.getvalue())
        # Check the type of file uploaded and read accordingly
        if data_upload.name.endswith('.csv'):
            df = pd.read_csv(data_upload)
        elif data_upload.name.endswith('.xlsx') or data_upload.name.endswith('.xls'):
            df = pd.read_excel(data_upload)
        else:
            df = None
        return df
    
    return None


def persona_selector():
    persona = st.sidebar.selectbox( 'Select User 👤',("CEO with finance background",
                                                        "CEO with business analysis background",
                                                        "CEO with no specific background",
                                                        "CFO with strong analysis background",
                                                        "Sales Manager with strong commercial background"
                                                        "CTO with development background",
                                                        "Standard user with no specific skills"))    
    return persona


def chart_framework_selector(df, column_names):
    selected_framework = st.selectbox('Select framework to generate charts ', ("Lida", "Pandas"))
    st.write('You use:', selected_framework)
    query = st.text_area(
        "Enter your Prompt:",
        placeholder="Prompt tips: Use plotting related keywords such as 'Plots' or 'Charts' or 'Subplots'. Prompts must be concise and clear, example 'Bar plot for the first ten rows.'",
        help="""
            How an ideal prompt should look like? *Feel free to copy the format and adapt to your own dataset.*
            
            ```
            - Subplot 1: Line plot of the whole spectra.
            - Subplot 2: Zoom into the spectra in region 1000 and 1200.
            - Subplot 3: Compare the area of whole spectra and zoom spectra as Bar Plot.
            - Subplot 4: Area curve of the zoom spectra.
            ```
            """,
    )

    # If the "Generate Chart" button is clicked
    if st.button("Generate Chart", type="primary"):
        if selected_framework == "Lida":
         handle_lida_chart_query(query)
    
        elif selected_framework == "Pandas":
         handle_chart_query(df, column_names, query)
