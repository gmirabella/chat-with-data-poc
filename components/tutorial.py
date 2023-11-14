import streamlit as st

def tutorial():
    expander = st.expander("## Tutorial: How Chat with Data works?")
    expander.write("""
                Our application allows you to query the Excel file you choose to upload in various ways.
                1. ## I Have No Idea What's in the File:
               Deep Summary Button:
               Let the system analyze the data for you. 
               Just specify your user level—whether you're a data newbie or an expert—to get a tailored result. 
               The analysis includes 15 goals, or questions, answered with corresponding graphs. 
               If the generated goals don't quite hit the mark, feel free to input your own prompt.

               
""")
    expander.image("images/example-lida.png")

    expander.write("""
                Quick Summary Button:
                   If you're short on time and want a 5-line snapshot of the document, opt for the Quick Summary.

                   
                2. ## Expert mode - Chatbox:
                    For experienced users, our chatbox allows you to interact with the document. Ask any question and receive a textual response. 
                   Keep in mind that this feature is in beta, so responses may not always be accurate.
                Generate Chart:

                Need a quick visual? Use the Generate Chart function. Choose between two experimental frameworks, but remember, they are works in progress. Be specific, and use available helpers if needed.
                Explore the possibilities and feel free to reach out if you encounter any issues. Happy querying!"               
""")
