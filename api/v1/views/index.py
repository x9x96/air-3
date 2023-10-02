#!/usr/bin/python3
"""
Module for route/endpoint status
"""
from flask import Flask
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)

def status():
    """
    Outputs the JSON status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)

def count():
    """
    Collects each objects number
    """
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
