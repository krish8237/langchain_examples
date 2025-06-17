from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from config import ConfigReader
import sys

config = ConfigReader("config.yaml")

class SampleChat:
    def __init__(self, template):
        self.model = ChatGoogleGenerativeAI(
            model = 'gemini-2.0-flash',
            google_api_key = config.get_config_value('GOOGLE_API_KEY'),
            max_tokens = 50
        )
        self.prompt_template = PromptTemplate.from_template(template = template)

    def get_prompt_value(self, data):
        return self.prompt_template.invoke(data)
    def chat(self, data):
        return self.model.invoke(self.get_prompt_value(data)).content

sample_chat = SampleChat("Answer the following question : {question}")
data = {"question" : "What is the current stock price of Google ?"}
print(data, sample_chat.chat(data))

print("Start asking questions. To exit press q | Q and then Enter")
while(True):
    user_in = input("Question :>")
    if(user_in in ["q", "Q"]):
        sys.exit(0)
    print("Response :>", sample_chat.chat({'question' : user_in}))

'''
> python sample_chat.py 
{'question': 'What is the current stock price of Google ?'} I cannot give you the exact, real-time stock price of Google (Alphabet Inc. - GOOGL or GOOG). Stock prices change constantly throughout the trading day.

However, here's how you can find the current stock price:
Start asking questions. To exit press q | Q and then Enter
Question :>what is an array ?
Response :> An array is a fundamental data structure in computer programming that stores a collection of elements of the **same data type** in contiguous memory locations.  Think of it like a numbered list where each item on the list has a specific position.

Here'
Question :>what is your name ?
Response :> I am a large language model, trained by Google.
Question :>how much computing capacity does it needs for training you ?
Response :> The exact computing capacity required to train me is not publicly disclosed by Google. It's a closely guarded secret due to its competitive value and the complexity of the calculation. However, we can make some educated estimations based on what is known about large language
Question :>Thank you
Response :> You're welcome! How can I help you? What is your question?
Question :>q

Process finished with exit code 0
'''