from langchain.prompts import ChatPromptTemplate
from generic_chain import GenericChainInvoker
from pprint import pprint

prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are responsible to browse and list out the products (with given specifications) for the current date using google search'),
        ('human', 'list out the laptops under 500$'),
        ('ai', '''
                [
                    "name : ABC, url : https://www.amazon.com/xxxx, price : 400",
                    "name : DEF, url : https://www.amazon.com/xxxx, price : 300"
                ]
            '''
        ),
        ('human', 'list out the {product} under {price}$')
    ])

product_looker = GenericChainInvoker(prompt, 200)
pprint(product_looker.chat({'product' : 'Lenovo Laptops', 'price' : 400}).content)