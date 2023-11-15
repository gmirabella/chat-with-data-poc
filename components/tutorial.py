import streamlit as st

def tutorial():
    expander = st.expander("## Tutorial: How Chat with Data works?")
    expander.write("""
                Our application allows you to query the Excel file you choose to upload in various ways.\n
               ## 1. Deep Summary: \n
               Let the system analyze the data for you. \n
               Just specify your user level—whether you're a data newbie or an expert—to get a tailored result. \n
               The analysis includes 15 goals, or questions, answered with corresponding graphs. \n
               If the generated goals don't quite hit the mark, feel free to input your own prompt.\n
             """)
    expander.image("images/example-lida.png")

    expander.write(""" \n
                ## 2. Quick Summary: \n
                   If you're short on time and want a 5-line snapshot of the document, opt for the Quick Summary. \n """)
    expander.image("images/quick-summary.png")

    expander.write(""" \n
                   For experienced users, our chatbox allows you to interact with the document. Ask any question and receive a textual response. 
                   Keep in mind that this feature is in beta, so responses may not always be accurate. \n
                   ##  3. Get Simple Answer: \n
                   Write down your query and chat with data, litterally! \n""")
    
    expander.image("images/simple-answer.png")              
                
    expander.write(""" \n
                   ## 4. Generate Chart: \n
                   Need a quick visual? Use the Generate Chart function. Choose between two experimental frameworks, but remember, they are works in progress.\n
                   Be specific, and use available helpers if needed. \n""")
                
    expander.image("images/generate-chart-generic.png") 
    expander.image("images/generate-chart-specific.png")



    expander.write(""" \n Explore the possibilities and feel free to reach out if you encounter any issues. Happy querying!""")
