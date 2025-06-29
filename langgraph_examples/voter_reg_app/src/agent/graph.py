
from langgraph.graph import StateGraph, START, END
#%% md
# #### State
# 
# - This is the first thing to define while creating a Graph.
# - State schema serves as an Input schema for all the Nodes and Edges in the Graph.
#%%
from typing import TypedDict

class State(TypedDict):
    g_state : str
    age : int
#%% md
# #### Nodes
#
# - **Nodes** are the python functions and they are operated on the State.
# - By default, each node will override the previous state value
#%%
def node1(state: State):
    state["g_state"] = f"Hello {state['g_state']}"
    return state
#%%
def node2(state: State):
    state["g_state"] = f"{state['g_state']}. Redirecting to fill the Voting Application !"
    return state
#%%
def node3(state: State):
    state["g_state"] = f"{state['g_state']}. You are not eligible for Voting !"
    return state
#%%
def node4(state: State):
    state["g_state"] = f"{state['g_state']}. Age Limit Exceeded !"
    return state
#%% md
# #### Edges
# Edges are of two types
#
# - **Normal** : These are connected to the other node without any connection
# - **Conditional Edge** : These are connected to the other nodes with a condition
#%%
from typing import Literal

def conditional_edge(state: State) -> Literal["node2", "node3", "node4"]:
    
    age = state["age"]
    if(age in range(1, 18)):
        return "node3"
    elif(age in range(18, 121)):
        return "node2"
    else:
        return "node4"
#%%
graph_builder = StateGraph(State)
#%%
graph_builder.add_node("node1", node1)
graph_builder.add_node("node2", node2)
graph_builder.add_node("node3", node3)
graph_builder.add_node("node4", node4)
#%%
from IPython.display import Image, display

def get_graph(graph: StateGraph):
    voting_graph = graph.compile()
    return voting_graph, Image(voting_graph.get_graph().draw_mermaid_png())
#%%
graph_builder.add_edge(START, "node1")
#%%
graph_builder.add_conditional_edges("node1", conditional_edge)
#%%
graph_builder.add_edge("node2", END)
graph_builder.add_edge("node3", END)
graph_builder.add_edge("node4", END)
#%%
graph, img = get_graph(graph_builder)
#%%
display(img)
#%%
graph.invoke({"g_state" : "Vamsi", "age" : 18})
#%%
graph.invoke({"g_state" : "Krishna", "age" : 17})
#%%
graph.invoke({"g_state" : "Vamsi Krishna", "age" : 200})