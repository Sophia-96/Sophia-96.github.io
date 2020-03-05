from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

languages = [{'name' : 'JavaScript'}, {'name' : 'Python'}, {'name' : 'Ruby'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'It works!'})  #return messages it runs in JSON form

@app.route('/lang', methods=['GET'])  #get the list of dict above
def returnAll():
	return jsonify({'languages' : languages})   #still in JSON format; the key is 'language', the value is languages

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languages if language['name'] == name]
	return jsonify({'language' : langs[0]})

if __name__ == '__main__':
	app.run(debug=True, port=9084) #run app on port 9084 in debug mode