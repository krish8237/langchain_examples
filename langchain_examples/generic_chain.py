from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import BasePromptTemplate
import config

conf = config.ConfigReader('../config.yaml')

class GenericChainInvoker():

    def __init__(self, prompt : BasePromptTemplate, max_tokens = 50):

        self.model = ChatGoogleGenerativeAI(
            model = 'gemini-2.0-flash',
            google_api_key = conf.get_config_value('GOOGLE_API_KEY'),
            max_tokens = max_tokens
        )

        self.chain = prompt | self.model

    def chat(self, inputs):
        return self.chain.invoke(inputs)