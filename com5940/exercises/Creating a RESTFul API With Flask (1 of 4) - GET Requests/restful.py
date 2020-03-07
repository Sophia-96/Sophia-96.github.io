from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]
students = [{'name':'Mike','id':'1155131888','city':'Hong Kong'}, {'name':'John','id':'1155131800','city':'Guilin'}, {'name':'Mike','id':'1155131811','city':'Lipu'}, {'name':'Tony','id':'1155131819','city':'Beijing'}]

#GET Method

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})  #return messages it runs in JSON form

@app.route('/lang', methods=['GET'])  #get the list of dict above
def returnAll():
	return jsonify({'languages' : languages})   #still in JSON format; the key is 'language', the value is language

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

@app.route('/students', methods=['GET'])
def returnstu():
	return jsonify({'students' : students})

@app.route('/students/<string:name>', methods=['GET'])
def returnTwo(name):
	studs = [student for student in students if student['name'] == name]
	return jsonify({'student' : studs[0]})   
	#students/Mike
	#return jsonify({'student' : studs[1]}) 

#POST Method

@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name' : request.json['name']}
	languages.append(language)
	return jsonify({'languages' : languages})

#PUT Method

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [language for language in languages if language['name'] == name]
	langs[0]['name'] = request.json['name']
	return jsonify({'language' : langs[0]})

#DELETE Method

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
	lang = [language for language in languages if language['name'] == name]
	languages.remove(lang[0])
	return jsonify({'languages' : languages})

if __name__ == '__main__':
	app.run(debug=True, port=9084) #run app on port 9084 in debug mode