from langchain.prompts import PromptTemplate, ChatPromptTemplate
from generic_chain import GenericChainInvoker

prompt = PromptTemplate(
    inputs = ["query"],
    template = "You're an intelligent system. please, answer the following query.\n{query}"
)

messenger = GenericChainInvoker(prompt)
print(messenger.chat({"query" : "Where is the largest building located ?"}))

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'you are an intelligent system that responds about the largest building in trems of height'),
        ('human', 'Which is the large building in india'),
        ('ai', 'Country: India, Building: ABC, Height: 120 feets'),
        ('human', "Answer this question : {country}")
    ]
)

messenger = GenericChainInvoker(prompt)
print(messenger.chat({"country" : "America"}))