from flask import Flask, jsonify, request, Response
from flask_socketio import SocketIO
from flask_cors import CORS
import json
import time
import sys
sys.path.append('widgets/')
sys.path.append('db/')
import db

app = Flask(__name__)
socketio = SocketIO(app)

# <-- Allow CORS
app.config['DEFAULT_PARSERS'] = [
    'flask.ext.api.parsers.JSONParser',
    'flask.ext.api.parsers.URLEncodedParser',
    'flask.ext.api.parsers.FormParser',
    'flask.ext.api.parsers.MultiPartParser'
]
cors = CORS(app,resources={r"/*":{"origins":"*"}})
# -->

@app.route("/news", methods=["GET"])
def get_news():
    result = db.getEntry("news")
    if result is not None:
        return Response(result, status=200, mimetype='application/json')
    else:
        return not_found()

@app.route("/news", methods=["PUT"])
def put_news():
    data = request.get_json()
    db.updateEntry("news", data)
    emitUpdate("updateNews", data)
    return "200"

@app.route("/news", methods=["POST"])
def post_news():
    data = request.get_json()
    db.addEntry("news", data)
    return "200"

@app.route("/current_weather", methods=["GET"])
def get_current_weather():
    result = db.getEntry("current_weather")
    if result is not None:
        return Response(result, status=200, mimetype='application/json')
    else:
        return not_found()

@app.route("/current_weather", methods=["PUT"])
def put_current_weather():
    data = request.get_json()
    db.updateEntry("current_weather", data)
    emitUpdate("updateCurrentWeather", data)
    emitUpdate("updateSuntimes", data)
    return "200"

@app.route("/current_weather", methods=["POST"])
def post_current_weather():
    data = request.get_json()
    db.addEntry("current_weather", data)
    return "200"

@app.route("/weather_forecast", methods=["GET"])
def get_weather_forecast():
    result = db.getEntry("weather_forecast")
    if result is not None:
        return Response(result, status=200, mimetype='application/json')
    else:
        return not_found()

@app.route("/weather_forecast", methods=["PUT"])
def put_weather_forecast():
    data = request.get_json()
    db.updateEntry("weather_forecast", data)
    emitUpdate("updateWeatherForecast", data)
    return "200"

@app.route("/weather_forecast", methods=["POST"])
def post_weather_forecast():
    data = request.get_json()
    db.addEntry("weather_forecast", data)
    return "200"

@app.route("/departures", methods=["GET"])
def get_departures():
    result = db.getEntry("departures")
    if result is not None:
        return Response(result, status=200, mimetype='application/json')
    else:
        return not_found()

@app.route("/departures", methods=["POST"])
def post_departures():
    data = request.get_json()
    db.addEntry("departures", data)
    return "200"

@app.route("/departures", methods=["PUT"])
def update_departures():
    data = request.get_json()
    db.updateEntry("departures", data)
    emitUpdate("updateDepartures", data)
    return "200"


@app.route("/temperature", methods=["GET"])
def get_temperature():
    result = db.getEntry("temperature")
    if result is not None:
        return Response(result, status=200, mimetype='application/json')
    else:
        return not_found()

@app.route("/temperature", methods=["POST"])
def post_temperature():
    data = request.get_json()
    db.addEntry("temperature", data)
    return "200"

@app.route("/temperature", methods=["PUT"])
def update_temperature():
    data = request.get_json()
    db.updateEntry("temperature", data)
    emitUpdate("updateRoomTemperature", data)
    return "200"

@app.route("/light", methods=["GET"])
def get_light():
    result = db.getEntry("light")
    if result is not None:
        return Response(result, status=200, mimetype='application/json')
    else:
        return not_found()

@app.route("/light", methods=["POST"])
def post_light():
    data = request.get_json()
    db.addEntry("light", data)
    return "200"

@app.route("/light", methods=["PUT"])
def update_light():
    data = request.get_json()
    db.updateEntry("light", data)
    emitUpdate("updateLight", data)
    return "200"

@app.errorhandler(404)
def not_found(error=None):
    message = {
        "status": 404,
        "message": "Not Found: " + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@socketio.on('connect')
def onConnect():
    print("client is connected")

@socketio.on('disconnect')
def onDisconnect():
    print('Client disconnected')

def emitUpdate(emitFunc, payload):
    print(payload)
    socketio.emit(emitFunc, {'data': payload})

@socketio.on_error()
def errorHandler(e):
    print(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    socketio.run(app)
