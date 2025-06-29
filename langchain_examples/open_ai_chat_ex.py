import os
import config
from langchain_openai import OpenAI

config = config.ConfigReader("../config.yaml")
os.environ["OPENAI_API_KEY"] = config.get_config_value("OPENAI_API_KEY")

chat_client = OpenAI(model = "gpt-3.5-turbo")
res = chat_client.invoke("Hello")
print(res)