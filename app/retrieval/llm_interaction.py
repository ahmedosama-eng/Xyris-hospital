from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI

from retrieval.retrieval import retrive_the_vector


vdb_path=r'F:\xyris test\xyris_HIS_test\ingestion\vectorstore'
cheak_path=r"F:\xyris test\xyris_HIS_test\ingestion\vectorstore\index.faiss"

def chatbot_model(docsearch):
    print("\n\n  here in chatbot_model \n\n") 
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
    chat_memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    qa = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=docsearch.as_retriever(),
        memory=chat_memory
    )
    return qa


def intilalize_the_caht(cheak_path,vdb_path):
    chat=chatbot_model(retrive_the_vector(cheak_path,vdb_path))
    return chat
