from flask import Flask, request

from retrieval.llm_interaction import intilalize_the_caht
#from  retrieval.llm_interaction import *


app = Flask(__name__)

q_chat=None

def start_the_caht():
    global q_chat
    vdb_path=r'F:\xyris test\xyris_HIS_test\ingestion\vectorstore'
    cheak_path=r"F:\xyris test\xyris_HIS_test\ingestion\vectorstore\index.faiss"
    q_chat=intilalize_the_caht(cheak_path,vdb_path)


@app.route('/hospital', methods=['POST'])
def Hospital_chat():
   try: 
        request_data = request.get_json()
        user_query = request_data.get("message")
        response = q_chat(user_query)
        return {"response": response['answer']}
   except Exception as e:
        return {"error": str(e)}, 500
   


if __name__ == '__main__':
    start_the_caht()
    app.run(host='0.0.0.0', port=6000)



 