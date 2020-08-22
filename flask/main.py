import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request
		
@app.route('/add', methods=['POST'])
def add_user():
	try:
		_json = request.json
		_name = _json['name']
		_email = _json['email']
		_university = _json['university']
		# validate received values
		if _name and _email and _university and request.method == 'POST':
			# insert data to the students table
			sql = "INSERT INTO students(student_name, student_email, university) VALUES(%s, %s, %s)"
			data = (_name, _email, _university,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/users', methods=['GET'])
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		#get data from the students table via select statement
		cursor.execute("SELECT student_id id, student_name name, student_email email, university university FROM students")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/user/<int:id>')
def user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		#get data from the students table via select statement for specific user via WHERE clause
		cursor.execute("SELECT student_id id, student_name name, student_email email, university university FROM students WHERE student_id=%s", id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

@app.route('/update', methods=['PUT'])
def update_user():
	try:
		_json = request.json
		_id = _json['id']
		_name = _json['name']
		_email = _json['email']
		_university= _json['university']		
		# validate the received values
		if _name and _email and _university and _id and request.method == 'PUT':
			#update information in the students table via UPDATE statement
			sql = "UPDATE students SET student_name=%s, student_email=%s, university=%s WHERE student_id=%s"
			data = (_name, _email, _university, _id,)
			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
		
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		#delete student from the students table
		cursor.execute("DELETE FROM students WHERE student_id=%s", (id,))
		conn.commit()
		resp = jsonify('User deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

#custom error pages: https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

#run flask instance on port 5000		
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
