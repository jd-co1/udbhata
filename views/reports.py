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

# find API key in console at app.pinecone.io old
# YOUR_API_KEY = "0c63694c-7756-401b-a897-03616f43acf9"
YOUR_API_KEY="ee98367a-b03f-4caf-b83f-7086934e6f00"

# find ENV (cloud region) next to API key in console
YOUR_ENV = "gcp-starter"
index_name = 'udbhata'
embeddings = OpenAIEmbeddings()
pinecone.init(
    api_key=YOUR_API_KEY,
    environment=YOUR_ENV,
)
index = pinecone.Index(index_name)
# index=index(namespace="Divislabs")
vectorstore = Pinecone(
    index, embeddings.embed_query, text_key="text"
)

# model_name = "gpt-3.5-turbo"
model_name="gpt-4"
llm = ChatOpenAI(model_name=model_name,temperature=0,top_p=0.8)
# Build prompt
template = """You are an assistant of a company and you are generating annual  report for 2023 year about profit,loss and revenue ,etc .
Use the following pieces of context to answer the question at the end. If you don't know the answer,
just say that you don't know, don't try to make up an answer.Dont give Description or any other details in the responses,If any answer has Yes or No, just say that.
 
{context}
Question: {question}
Helpful Answer:"""
# retriever=vectorstore.as_retriever(
#     search_kwargs={ "namespace": "Divislabs"}, 
# )
#generate the accurate values along with corresponding currency and generate only the values and currency type, Example: 123,874 INR ,if come across a question which has YES or NO type then just give YES or NO answer,if you don't have value just say NA. 
#  and the answer should be from the context given below and it should be exact match. And dont forget to give currency type for the questions which has currency type.
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)# Run chain
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

# questions=[
# "caliculate the board industry experience of the company?",
# "Revenue",
# "Revenue from operations",
# "PBT or Profit before tax",
# "Total assets",
# "Total Liabilities",
# "EBITDA or Earnings before tax",
# "Net debt",
# "Total equity",
# "Current Investments",
# "Return on capital employed",
# "Debt-equity ratio",
# "Does the company have a formal board diversity policy that clearly requires diversity factors such as gender, race, ethnicity, country of origin, nationality or cultural background in the board nomination process?",
# "Has the company conducted a materiality analysis to identify the most important material issues (economic, environmental, or social) for the company's performance?",
# "Does the company publicly disclose details of the materiality analysis, including information on how they conduct the materiality analysis process and progress towards targets or metrics?",
# "Does the company have Risk Management Committee.",
# "Does the company identify emerging risks, and give the mitigation plans for the risks",
# "Does the company have a Supplier Code of Conduct and is it publicly available?",
# "Awards for Finance, Risk management, Sustainability and Governance",
# "Board experience in Risk Management",
# "what is the values of EBITDA for net sales"

# ]
# print("Running",len(questions))
results=[]
def run_question(question):
    resp = qa_chain(question)
    answer=resp["result"]
    source_docs = resp["source_documents"]
    return answer, source_docs[:3]
# with ThreadPoolExecutor(max_workers=3) as executor:
#         # Submit tasks to the executor
#         t1=executor.submit(run_question, questions[0])
#         t2=executor.submit(run_question, questions[1])
#         t3=executor.submit(run_question, questions[2])
#         t4=executor.submit(run_question, questions[3])
#         t5=executor.submit(run_question, questions[4])
#         t6=executor.submit(run_question, questions[5])
#         t7=executor.submit(run_question, questions[6])
#         t8=executor.submit(run_question, questions[7])
#         t9=executor.submit(run_question, questions[8])
#         t10=executor.submit(run_question, questions[9])
#         t11=executor.submit(run_question, questions[10])
#         t12=executor.submit(run_question, questions[11])
#         t13=executor.submit(run_question, questions[12])
#         t14=executor.submit(run_question, questions[13])
#         t15=executor.submit(run_question, questions[14])
#         t16=executor.submit(run_question, questions[15])
#         t17=executor.submit(run_question, questions[16])
#         t18=executor.submit(run_question, questions[17])
#         t19=executor.submit(run_question, questions[18])
#         t20=executor.submit(run_question, questions[19])
#         t21=executor.submit(run_question, questions[20])
#         concurrent.futures.wait([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20,t21])
#         if t1.done() & t2.done() & t3.done() & t4.done() & t5.done() & t6.done() & t7.done() & t8.done() & t9.done() & t10.done() & t11.done() & t12.done() & t13.done() & t14.done() & t15.done() & t16.done() & t17.done() & t18.done() & t19.done() & t20.done() & t21.done():
#             results.append({"Annual_Report":questions[0],"Value":t1.result()})
#             results.append({"Annual_Report":questions[1],"Value":t2.result()})
#             results.append({"Annual_Report":questions[2],"Value":t3.result()})
#             results.append({"Annual_Report":questions[3],"Value":t4.result()})
#             results.append({"Annual_Report":questions[4],"Value":t5.result()})
#             results.append({"Annual_Report":questions[5],"Value":t6.result()})
#             results.append({"Annual_Report":questions[6],"Value":t7.result()})
#             results.append({"Annual_Report":questions[7],"Value":t8.result()})
#             results.append({"Annual_Report":questions[8],"Value":t9.result()})
#             results.append({"Annual_Report":questions[9],"Value":t10.result()})
#             results.append({"Annual_Report":questions[10],"Value":t11.result()})
#             results.append({"Annual_Report":questions[11],"Value":t12.result()})
#             results.append({"Annual_Report":questions[12],"Value":t13.result()})
#             results.append({"Annual_Report":questions[13],"Value":t14.result()})
#             results.append({"Annual_Report":questions[14],"Value":t15.result()})
#             results.append({"Annual_Report":questions[15],"Value":t16.result()})
#             results.append({"Annual_Report":questions[16],"Value":t17.result()})
#             results.append({"Annual_Report":questions[17],"Value":t18.result()})
#             results.append({"Annual_Report":questions[18],"Value":t19.result()})
#             results.append({"Annual_Report":questions[19],"Value":t20.result()})
#             results.append({"Annual_Report":questions[20],"Value":t21.result()})
#             print("Done")
#    Risk management, Sustainability and Governance
def load_reports():
    st.header("Reports Generator")
#     # st.table(results)       
# question=""" does this award 'CDP Supplier Engagement Leaderboard 2023' come under the Finance?.
#          """
# result, source_documents = run_question(question)
# st.write("Question:", question)
# st.write("Answer:", result)
# st.write("Source Documents:")
# for doc in source_documents:
#     st.write(doc.page_content+"\n"+"Page number:\n"+str(int(doc.metadata["page"]+1))+"   \n  "+doc.metadata['source'])
#     # st.write(doc)
