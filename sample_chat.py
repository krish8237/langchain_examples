from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from config import ConfigReader

config = ConfigReader("config.yaml")

template = "Answer the following question :\n{question}"
prompt_template = PromptTemplate.from_template(template = template)

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.0-flash',
    google_api_key = config.get_config_value('GOOGLE_API_KEY'),
    max_tokens = 50
)

question = "What is an Array ?"
prompt_value = prompt_template.invoke({"question" : question})
res = model.invoke(prompt_value)
print(res.content)