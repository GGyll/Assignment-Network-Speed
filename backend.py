from flask import Flask, render_template
from solution import *


app = Flask(__name__)

@app.route("/")
def solution():    
    # Delete existing Devices and Network Stations
    Device._devices = []
    NetworkStation._stations = []
    stations = input_network_stations()
    devices = input_devices()
    data = initialize(stations, devices)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

