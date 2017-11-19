import os, json, recognition, base64
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/cans', methods=['POST'])
def cans():
	data = json.loads(request.data)
	data = data['img']
	data = base64.b64decode(data)
	response_dict = recognition.predict(data)
	# response_dict = {'result': 'popo'}
	response_json = json.dumps(response_dict)
	response = Response(response=response_json, status=200, mimetype="application/json")
	return response

@app.route('/hello', methods=['GET'])
def hello():
	return 'hello'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)