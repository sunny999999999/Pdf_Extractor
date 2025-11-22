import pandas as pd
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv
from autogen_agentchat.ui import Console 
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from Prompt import system_message
import streamlit as st

api_key = st.secrets["GEMINI-API-KEY"]
#load env variables - GEMINI_API_KEY
load_dotenv()

#Create a list for agent output structure via pydantic
class AgentOutput(BaseModel):
    data: List

#create the midel-client in this case gemini
model_client = OpenAIChatCompletionClient(model="gemini-2.5-flash",api_key=api_key)

#Create the agent via assistant agent
agent = AssistantAgent(name="structure_agent",
                       model_client=model_client,
                       system_message=system_message,  #from prompt.py
                       output_content_type=AgentOutput) #the output structure list of dicts

#run the agent with input data
async def Agent_Run(text:str):
    result = await Console(agent.run_stream(task=f"This the input text : {text} Start your process now."),output_stats=True)
    data = result.messages[-1].content.data #extract the last message that is the task output
    df = pd.DataFrame(data, columns=["Key", "Value", "Comment"]) #create a dataframe with required columns
    df.to_excel("output.xlsx", index=False) #convert it into .xlsx file
    print("Output.xlsx Created Successfully")


