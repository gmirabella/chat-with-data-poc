from agents.panda_agent import create_panda_df_agent, create_pandas_ai_agent
import streamlit as st

#Handlers
def handle_sample_query(df, column_names):
    query = st.text_area(
        "Enter your Prompt:",
        placeholder="Prompt tips: Receive an answer to a question regarding the excel file in text format.'",
        help="""
            How an ideal prompt should look like? *Feel free to copy the format and adapt to your own dataset.*
            ```
            - What is the best-selling book this year?
            - Who is the player with the most points on the X team?
            - How many lines does the file contain and what line 12 contains?
            ```
            """,
    )
    if st.button("Get Simple Answer", type="primary"):
        if query:
            with st.spinner("Generating Response..."):
           # Create an agent from the CSV file.
               agent = create_panda_df_agent(df)
               response = query_service(agent=agent, query=query)
               st.write(response)
        else:
            st.warning("Please enter a valid query")

def handle_quick_summary(df, column_names):
    agent_quick= create_panda_df_agent(df)
    st.write(quick_summary_service(agent=agent_quick, column_names=column_names))

def handle_deep_summary(df, column_names):
    agent_deep= create_pandas_ai_agent()
    st.write(deep_summary_service(
        df=df,
        agent=agent_deep, 
        column_names=column_names)
        )

def handle_suggest_query(df, column_names):
    agent_suggest= create_pandas_ai_agent()
    st.write(suggest_query_service(
        df=df, 
        agent=agent_suggest, 
        column_names=column_names)
        )

#private functions

def query_service(agent, query):
    prompt = f"""
             The dataset is ALREADY loaded into a DataFrame named 'df'. 
             DO NOT load the data again.
             You are a text assistant chatbot that response to query always in a conversation way.
       
             Lets think step by step.
            
             Below is the query.
             Query: 
            """ + query
    

    # Run the prompt through the agent.
    response = agent.run(prompt)

    # Convert the response to a string.
    return response

def quick_summary_service(agent, column_names):
    prompt = f"""            
              The dataset is ALREADY loaded into a DataFrame named 'df'. 
              DO NOT load the data again.
              You are a text assistant that response to queries based on the following columns: {column_names}.
              you are a text assistant who give an accurate recap of 500 words based on the on the following columns: {column_names}.
              IMPORTANT: the recap must concern the data of the document inserted
            
            Lets think step by step. 
            """

    # Run the prompt through the agent.
    response = agent.run(prompt)

    # Convert the response to a string.
    return response.__str__()

def deep_summary_service(agent, df, column_names):
    prompt = f"""
              The dataset is ALREADY loaded into a DataFrame named 'df'. 
              DO NOT load the data again.
              You are a text assistant who give an accurate recap of 500 words based on the on the following data and columns: {column_names}.
              IMPORTANT: the recap must concern the data of the document inserted
        """

    # Run the prompt through the agent.
    response = agent.run(df,prompt)

    # Convert the response to a string.
    return response.__str__()

def suggest_query_service(agent, df, column_names):
    prompt =f"""
              The dataset is ALREADY loaded into a DataFrame named 'df'. 
              DO NOT load the data again.
              You are a text assistant that return 10 suggestion for query prompt based on the following columns: {column_names}.
              - prompt 1: 
              - prompt 2:
              - prompt 3: 
              """

    # Run the prompt through the agent.
    response = agent.run(df,prompt)

    # Convert the response to a string.
    return response