from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import config

config_data = config.ConfigReader('../config.yaml')

prompt = PromptTemplate.from_template("Answer the following question : {question}")

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    google_api_key = config_data.get_config_value('GOOGLE_API_KEY'),
    max_tokens = 50
)

chain = prompt | model

print(chain.invoke({"question" : "What is the largest prime number ?"}))