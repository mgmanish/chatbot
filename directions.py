#calculates the directions from origin to destination
import googlemaps
import webbrowser
import location
import urllib.request
import json
import os
import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req): 
	result = urllib.request.urlopen(baseurl).read()
	origin = req.get("result").get("parameters").get("origin")
	destinatreq.get("result").get("parameters").get("destination")
	gmaps = googlemaps.Client(key='AIzaSyDK7i8tLOzpfgaSVg1bZ-4cQGOXfi_IfTg')
	# origin = str(input("Enter the origin location: "))
	# destination = str(input("Enter the destination location: "))
	result = gmaps.directions(origin,destination) #other attributes
	address = "origin="+origin+"&"+"destination="+destination
	address = address.lower()
	address = address.replace(" ","+")
	url = "https://www.google.com/maps/dir/?api=1&"
	result_url = url+address
	print(result_url)
	webbrowser.open_new(result_url)
	return{
	"fulfillmentText": result_url
	}