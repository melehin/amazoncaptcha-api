from amazoncaptcha import AmazonCaptcha
from flask import Flask, request, abort
import base64
import random
import os

app = Flask('app')

@app.route('/createTask', methods=['POST'])
def createTask():
    taskId = random.randint(10000, 100000)
    
    r = request.get_json()

    image = "{}.jpeg".format( taskId )
    with open(image, 'wb') as f:
        f.write( base64.b64decode( r['task']['body'] ) )
    
    solution = AmazonCaptcha(image).solve()

    result = "{}_result.txt".format( taskId )
    with open(result, 'w') as f:
        f.write( solution )
    
    return {
        "errorId": 0,
        "taskId": taskId
    }

@app.route('/getTaskResult', methods=['POST'])
def getTaskResult():
    r = request.get_json()

    try:
        taskId = int( r['taskId'] )
    except:
        return abort(403)
    
    result = "{}_result.txt".format( taskId )
    image = "{}.jpeg".format( taskId )
    if os.path.isfile( result ):
        solution = ""
        with open(result) as f:
            solution = f.read()
        
        os.remove( result )
        os.remove( image )

        return {
            'status': 'ready',
            'solution': {
                'text': solution
            }
        }
    else:
        return abort(404)

if __name__ == "__main__":
    app.run()