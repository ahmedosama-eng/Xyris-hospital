from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from ingestion.data_ingestion  import *
import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())



db_path = r'F:\xyris test\xyris_HIS_test\app\data\output_db\hospital.db'
processed_data = retrieve_and_process_data(db_path)

def doc_loader(data_dict):
    documents = []
    for filename, df in data_dict.items():
        text = "\n".join(df.astype(str).apply(lambda x: ", ".join(x), axis=1))
        documents.append(Document(page_content=text, metadata={"source": filename}))
    return documents


def text_spliter(data):           
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(data)
    return text_chunks


def create_Embeddings_and_vectordb(text_chunks,DB_FAISS_PATH):
    print("\n\n  here in create_Embeddings_and_vectordb \n\n")     
    embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    docsearch = FAISS.from_documents(text_chunks, embedding)
    docsearch.save_local(DB_FAISS_PATH)
    return docsearch


def retrive_vectordb(vdb_path):
    print("\n\n  here in retrive_vectordb \n\n") 
    docsearch = FAISS.load_local(vdb_path,embeddings=OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY")),allow_dangerous_deserialization=True)
    return docsearch

def q_chat_with_create_embedings(data_path,vdb_path):
    print("\n\n  here in q_chat_with_create_embedings \n\n") 
    q_chat=create_Embeddings_and_vectordb(text_spliter(data_path),vdb_path)
    return q_chat


def q_chat_with_retrive_embedings(vdb_path):
    print("\n\n  here in q_chat_with_retrive_embedings \n\n") 
    q_chat=(retrive_vectordb(vdb_path))
    return q_chat

def check_file_exists(index_path):
    return os.path.exists(index_path)
 