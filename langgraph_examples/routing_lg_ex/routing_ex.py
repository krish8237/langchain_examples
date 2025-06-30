from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.messages import AnyMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.graph.message import add_messages
from typing import TypedDict, List, Annotated

import os

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
def add(a: int, b: int):
    '''
    add two integers a and b
    :param a:
    :param b:
    :return: result
    '''
    return a + b

class MessageState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]

llm_with_tools = llm.bind_tools([add])

def tooled_llm(state: MessageState):
    return {"messages" : [llm_with_tools.invoke(state["messages"])]}

graph = StateGraph(MessageState)

graph.add_node("calc_model", tooled_llm)
graph.add_node("tools", ToolNode([add]))

graph.add_edge(START, "calc_model")
graph.add_edge("calc_model", "tools")
graph.add_conditional_edges("tools", tools_condition)
graph.add_edge("tools", END)

graph = graph.compile()