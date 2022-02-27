import sys
from flask import Flask, request
from models.index import moveAvater, stopAvater, judgeShouldSkip

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('presentation/html/index.html')

@app.route('/move', methods=['POST'])
def move():
        try:
            req = request.json
            top = req.get("top")
            left = req.get("left")
            if judgeShouldSkip(top, left) == True:
                return 'OK, different is tiny, so skipped process', 204

            moveAvater(top, left)
            return 'OK, successfully sent your position', 204

        except TypeError:
            return TypeError.args[0], 503
        except:
            print(sys.exc_info()[0])
            return '', 503

@app.route('/stop', methods=['POST'])
def stop():
    stopAvater()
    return 'successfully called stop process', 204

app.run(port=8000, debug=True)