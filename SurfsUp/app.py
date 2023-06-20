# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine)

# reflect the tables
Base.metadata.tables
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
baseRoute = "/api/v1.0"
route_percip = f"{baseRoute}/percipitation"
route_stations = f"{baseRoute}/stations"
route_tobs = f"{baseRoute}/tobs"
route_startstop = f"{baseRoute}/<start>/<stop>"

@app.route("/")
def index():
    """List all available routes"""
    return (
        f"Available Routes:<br/>"
        f"{route_percip}<br/>"
        f"{route_stations}<br/>"
        f"{route_tobs}<br/>"
        f"{route_startstop}"
    )

@app.route(route_percip)
def percip():
    

@app.route(route_stations)

@app.route(route_tobs)

@app.route(route_startstop)



