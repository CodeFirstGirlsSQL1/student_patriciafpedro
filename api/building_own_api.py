from flask import Flask, jsonify, request
from flights_data import flights
from utils import search_flight, get_index

# creating new app
app = Flask(__name__)


# GETTING INFORMATION
# after / we add the endpoint(londontoibiza) or if it is a link we leave empty
@app.route('/')
def hello():
    return {'hello': 'Universe'}


@app.route('/flights')
def get_flights():
    return jsonify(flights)

# we add access for the user to delete a particular flight
@app.route('/flights/<int:id>')
def get_flight_by_id(id):
    flight = search_flight(id, flights)
    return jsonify(flight)


if __name__ == '__main__':
    app.run(debug=True)
