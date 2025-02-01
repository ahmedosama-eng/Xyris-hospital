
from ingestion.vectorization import *
from retrieval.llm_interaction import *



def retrive_the_vector(cheak_path,vdb_path):   
    data_loaded=doc_loader(processed_data)
    data =text_spliter(data_loaded) 
    if check_file_exists(cheak_path)==True:
        vectordb= q_chat_with_retrive_embedings(vdb_path)
    else:
        vectordb= q_chat_with_create_embedings(data,vdb_path)
    return vectordb
    


