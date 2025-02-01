from flask import Flask, request,jsonify

from app.ingestion.data_ingestion import get_db_connection
from retrieval.llm_interaction import intilalize_the_caht


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
   

@app.route('/add_to_physicians', methods=['POST'])
def add_to_physicians():
    try:
        # Get JSON data from the request
        request_data = request.get_json()
        name = request_data.get("name")
        speciality = request_data.get("speciality")
        degree = request_data.get("degree")

        # Validate the input data
        if not name or not speciality or not degree:
            return jsonify({"error": "Missing required fields (name, speciality, degree)"}), 400

        # Insert data into the Physicians table
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Physicians (name, speciality, degree)
            VALUES (?, ?, ?)
        ''', (name, speciality, degree))
        conn.commit()
        conn.close()
        return jsonify({"message": "Data added to Physicians table successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


@app.route('/add_to_physicians', methods=['POST'])
def add_to_physicians():
    try:
        request_data = request.get_json()
        name = request_data.get("name")
        speciality = request_data.get("speciality")
        degree = request_data.get("degree")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Physicians (name, speciality, degree)
            VALUES (?, ?, ?)
        ''', (name, speciality, degree))
        conn.commit()
        conn.close()
        return jsonify({"message": "Data added to Physicians table successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500




@app.route('/add_to_schedules', methods=['POST'])
def add_to_schedules():

    try:
        request_data = request.get_json()
        doctor_name = request_data.get("doctor_name")
        monday = request_data.get("monday")
        tuesday = request_data.get("tuesday")
        wednesday = request_data.get("wednesday")
        thursday = request_data.get("thursday")
        friday = request_data.get("friday")
        saturday = request_data.get("saturday")
        sunday = request_data.get("sunday")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Schedules (doctor_name, monday, tuesday, wednesday, thursday, friday, saturday, sunday)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (doctor_name, monday, tuesday, wednesday, thursday, friday, saturday, sunday))
        conn.commit()
        conn.close()
        return jsonify({"message": "Data added to Schedules table successfully"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500




@app.route('/add_to_Specialities', methods=['POST'])
def add_to_Specialities():
    try:
      
        request_data = request.get_json()
        id = request_data.get("id")
        speciality_name = request_data.get("speciality_name")
        definition = request_data.get("definition")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Specialities (id, speciality_name, definition)
            VALUES (?, ?, ?)
        ''', (id, speciality_name, definition))
        conn.commit()
        conn.close()
        return jsonify({"message": "Data added to Specialities table successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/add_to_Policy', methods=['POST'])
def add_to_Policy():
    try:
      
        request_data = request.get_json()
        id = request_data.get("id")
        name = request_data.get("name")
        policy_description = request_data.get("policy_description")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Policy (id, name, policy_description)
            VALUES (?, ?, ?)
        ''', (id, name, policy_description))
        conn.commit()
        conn.close()
        return jsonify({"message": "Data added to Policy table successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/add_to_Pricelist', methods=['POST'])
def add_to_Pricelist():
    try:
      
        request_data = request.get_json()
        id = request_data.get("id")
        service_name = request_data.get("service_name")
        price_usd = request_data.get("price_usd")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Pricelist (id, service_name, price_usd)
            VALUES (?, ?, ?)
        ''', (id, service_name, price_usd))
        conn.commit()
        conn.close()
        return jsonify({"message": "Data added to Pricelist table successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    start_the_caht()
    app.run(host='0.0.0.0', port=6000) 



 