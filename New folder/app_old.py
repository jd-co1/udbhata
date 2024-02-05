import streamlit as st
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from concurrent.futures import ThreadPoolExecutor
import concurrent


load_dotenv()

model_name = 'text-embedding-ada-002'

embed = OpenAIEmbeddings(
    model=model_name,
   
)

# find API key in console at app.pinecone.io
YOUR_API_KEY = "0c63694c-7756-401b-a897-03616f43acf9"
# find ENV (cloud region) next to API key in console
YOUR_ENV = "gcp-starter"
index_name = 'udbhata'
embeddings = OpenAIEmbeddings()
pinecone.init(
    api_key=YOUR_API_KEY,
    environment=YOUR_ENV
)
index = pinecone.Index(index_name)

vectorstore = Pinecone(
    index, embeddings.embed_query, text_key="text"
)


model_name = "gpt-3.5-turbo"
llm = ChatOpenAI(model_name=model_name,temperature=0)
# Build prompt
template = """You are an assistant of a company and you are generating annual  report for current year about profit,loss and revenue ,etc .
Use the following pieces of context to answer the question at the end. If you don't know the answer,
just say that you don't know, don't try to make up an answer. 
 generate the accurate values along with corresponding currency and don't generate description for the question,generate only the values and currency type Example: Profit before tax : 123,874 INR ,if you don't have value just say NA
 and the answer should be from the context given below and it should be exact match.
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)# Run chain
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

questions=[
"what is the dividend per share",
"Revenue",
"Revenue from operations",
"Total Liabilities",
# "EBITDA or Earnings before tax",
# "Net debt"
]
results=[]
def run_question(question):
    # print(f"Question: {question}")
    resp = qa_chain(question)
    return resp["result"]
with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor
        t1=executor.submit(run_question, questions[0])
        t2=executor.submit(run_question, questions[1])
        t3=executor.submit(run_question, questions[2])
        t4=executor.submit(run_question, questions[3])
        concurrent.futures.wait([t1,t2,t3,t4])
        if t1.done() & t2.done() & t3.done() & t4.done():
            results.append({"Annual_Report":questions[0],"Value":t1.result()})
            results.append({"Annual_Report":questions[1],"Value":t2.result()})
            results.append({"Annual_Report":questions[2],"Value":t3.result()})
            print(t1.result())
      
            

st.title("Reports Generator")

st.table(results)


    