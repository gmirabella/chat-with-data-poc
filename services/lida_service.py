# Add necessary imports
import streamlit as st
from lida import Manager, TextGenerationConfig, llm
import openai
from PIL import Image
from io import BytesIO
import base64
from dotenv import load_dotenv
import os

#load_dotenv()
#openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key=st.session_state.get("OPENAI_API_KEY")
modelName=st.session_state.get("MODEL_NAME")

#Handlers
def handle_lida_summary(persona):
    st.write(lida_summary_service(persona))

def handle_lida_chart_query(query):
         lida_chart_service(query)


#private function
def base64_to_image(base64_string):
        byte_data = base64.b64decode(base64_string)
        return Image.open(BytesIO(byte_data))


def lida_summary_service(persona):

    text_gen = llm("openai")
    lida = Manager(text_gen)

    textgen_config = TextGenerationConfig(n=1, temperature=0.5, model=modelName, use_cache=True)
    summary = lida.summarize("filename.csv", summary_method="default", textgen_config=textgen_config)
    #st.write(summary)
    goals = lida.goals(summary, n=15, textgen_config=textgen_config, persona= persona)
    i = 0
    while i < (len(goals)):
        st.write(goals[i])
        library = "seaborn"
        textgen_config = TextGenerationConfig(n=1, temperature=0.2, use_cache=True)
        try:
            charts = lida.visualize(summary=summary, goal=goals[i], textgen_config=textgen_config, library=library)
            img_base64_string_summary = charts[0].raster
            img_summary = base64_to_image(img_base64_string_summary)
            st.image(img_summary)
        except:
            st.warning("An exception occurred. Cannot generate chart")
        i+= 1


def lida_chart_service(user_query):
    text_gen = llm("openai")
    lida = Manager(text_gen)
    textgen_config = TextGenerationConfig(n=1, temperature=0.2, model=modelName, use_cache=True)
    summary = lida.summarize("filename.csv", summary_method="default", textgen_config=textgen_config)
    try:
        charts = lida.visualize(summary=summary, goal=user_query, textgen_config=textgen_config)  
        img_base64_string = charts[0].raster
        img = base64_to_image(img_base64_string)
        st.image(img)
    except:
        st.warning("An exception occurred. Cannot generate chart")