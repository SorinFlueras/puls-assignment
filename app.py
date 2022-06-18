from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/healthcheck',methods=['GET'])
def getAllEmp():
    return jsonify({"status":"ok"})

if __name__ == '__main__':
 app.run()