import os
import config
from langchain.tools.tavily_search import TavilySearchResults

config = config.ConfigReader("../config.yaml")
os.environ["TAVILY_API_KEY"] = config.get_config_value("TAVILY_API_KEY")

search_client = TavilySearchResults()
search_client.max_results = 3
res_docs = search_client.invoke("Explain about the difference between LangGraph and MCP")
print(res_docs)