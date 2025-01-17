import streamlit as st
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader

load_dotenv()

loader = CSVLoader(file_path='./assets/amadeus_dados.csv')
documents = loader.load()

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(documents, embeddings)


def retrieve_info(query):
    similar_response = db.similarity_search(query, k=3)
    return [doc.page_content for doc in similar_response]


llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')

template = """
Você é um assistente virtual de uma empresa chamada Amadeus AI, que vende serviços de inteligência artificial para outras empresas.
Sua função será responder e-mails que recebemos de potenciais clientes.

Siga todas as regras abaixo:
1/ Tenha uma linguagem humanizada. 
2/ Assine os e-mails com o nome de Maria Eduarda Borges.
3/ Alguns dos e-mails podem conter links e informações irrelevantes. Preste atenção apenas ao conteúdo útil da mensagem.

Aqui esta uma mensagem recebida de um novo cliente.
{message}

Aqui está uma lista de informações úteis sobre a empresa. Este histórico irá servir como base para que você compreenda sobre nossos serviços.
{best_practice}

Escreva a melhor resposta que eu deveria enviar para este potencial cliente:
"""

prompt = PromptTemplate(
    input_variables=['message', 'best_practice'], template=template
)

chain = LLMChain(llm=llm, prompt=prompt)


def generate_response(message):
    best_practice = retrieve_info(message)
    response = chain.run(message=message, best_practice=best_practice)
    return response


response = generate_response(
    """
    Olá, boa tarde!
                  
    Encontrei vocês no Google e gostaria de saber mais sobre o que vocês fazem, quais serviços vocês prestam para empresa. Tenho uma empresa de agência de marketing, como vocês poderiam me ajudar?
"""
)

print(response)
