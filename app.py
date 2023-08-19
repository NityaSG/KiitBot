# The code is a Python script that creates a chatbot for KIIT University using Streamlit and various
# natural language processing tools such as OpenAI and FAISS. The chatbot is designed to help users
# find information about the university, including admissions, academics, and general queries related
# to KIITEE exam. The script also includes information about the university and contact details for
# further inquiries.
# The line `from langchain.chains.question_answering import load_qa_chain` is importing the
# `load_qa_chain` function from the `question_answering` module of the `langchain.chains` package.
# This function is used to load a pre-trained question answering model that can be used to answer
# questions based on a given input document or set of documents.
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
import os
import streamlit as ss
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] =os.getenv("OPENAI_API_KEY")

reader = PdfReader('./KIITEE.pdf')

raw_text = ''
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        raw_text += text

text_splitter = CharacterTextSplitter(        
    separator = "\n",
    chunk_size = 1000,
    chunk_overlap  = 200,
    length_function = len,
)
texts = text_splitter.split_text(raw_text)
from PIL import Image
from matplotlib import style
with ss.sidebar:
    col1, col2, col3 = ss.columns([1,2, 1])

    with col1:
        ss.write(' ')

    with col2:
        ss.image("./log.png")

    with col3:
        ss.write(' ')
    ss.write("Welcome to the KIIT University chatbot! Our bot is designed to help you quickly and easily find the information you need about the university. Whether you're a student, faculty member, or staff member, our bot is here to assist you with a wide range of tasks, from course selection to IT support. Our bot is built using Large language model, which is a popular and sophisticated machine learning model, providing you with an interactive and user-friendly experience. We hope our chatbot can help make your experience at KIIT University as smooth and successful as possible.")
    url = 'http://kiit.ac.in'
    ss.markdown(f'''<a href={url}><button style="background-color:grey;">Home Page</button></a>''',unsafe_allow_html=True)
    ur = 'http://admission.kiit.ac.in'
    ss.markdown(f'''<a href={ur}><button style="background-color:grey;">Admissions</button></a>''',unsafe_allow_html=True)
    u = 'https://kiit.ac.in/academics/'
    ss.markdown(f'''<a href={u}><button style="background-color:grey;">Academics</button></a>''',unsafe_allow_html=True)
    
st, tab2,tab3 = ss.tabs(["Home", "About","Contact us"])

tab2.image('./campus.jpg')
tab2.subheader("About KIIT")
tab2.write("KIIT is a private academic institution dedicated to providing educational opportunities for the intellectual, social, and professional development of a diverse student population. To achieve this purpose, the institution offers focused and balanced curricula at Undergraduate, Master’s and Doctoral levels. A broad-based core curriculum is offered, promoting critical thinking, effective verbal and written communication, and skills for life-long learning. KIIT’S approach to higher education and the resulting varied academic experiences provide students with the intellectual acumen and pragmatic approach necessary to create the foundation for personal and professional fulfillment.")
tab2.image('./stat.jpg')
tab2.image('./stat1.jpg')
embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(texts, embeddings)
st.markdown("<h1 style='text-align: center; color: white;'>KIITEE 2023</h1>", unsafe_allow_html=True)
st.image('./pp.jpg')
st.subheader('KIITEE query solver')
chain = load_qa_chain(OpenAI(), chain_type="stuff")
query =st.text_input("enter your query")

try:
    docs = docsearch.similarity_search(query)
    s=chain.run(input_documents=docs, question=query)
    st.write(s)
except:
    print("ok")
tab3.header("Contact us")
tab3.image('./camp.jpg')
tab3.subheader("Website : ")
tab3.write("https://www.kiitee.com/")

tab3.subheader("Email : ")
tab3.write("admission@kiit.ac.in")

tab3.subheader("Phone : ")

tab3.write("+918080735735")

