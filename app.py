import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Loading the env variables
load_dotenv()

# Setting the title of the app
st.title("Experimenting with Gemini and Streamlit")

# Creating the document loader
loader = PyPDFLoader("my_paper.pdf")
data = loader.load()

# Creating chunks of text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000
)
docs = text_splitter.split_documents(data)

# Creating the vectorstore
vectorstore = Chroma.from_documents(
    documents = docs, 
    embedding = GoogleGenerativeAIEmbeddings( model = "models/embedding-001"
))

retriver = vectorstore.as_retriever(search_type = "similarity",
                                     search_kwargs={"k":4})

# Creating the llm 
llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-pro",
    temperature = 0,
    max_tokens = None, 
    timeout =None
)

# Creating the system prompt
query = st.chat_input("Ask me anything")

# Creating the prompt template, with context placeholder
# They get replaced with the actual context when the chain is invoked
system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}") # Just a placeholder for the user input
    ]
)

# If user has entered a query, we will create the chain and get the response
if query:
    # Combines prompt(context, input) to the llm
    question_answer_chain =  create_stuff_documents_chain(llm, prompt)
    
    # Connects the retriver(contianing 4 docs) to the LLM
    # Retriver gets relevant chunks and passes these chunks as context to the LLM 
    # Then generates the answer based on facts
    rag_chain = create_retrieval_chain(retriver, question_answer_chain)

    # Passing the query to the chain
    response = rag_chain.invoke({"input":query})
    print(response['answer'])
    st.write(response['answer'])
