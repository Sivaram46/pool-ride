import requests

from flask import Flask, request, render_template, session, redirect, url_for
from polyline import Polyline

from const import API_KEY

app = Flask(__name__, template_folder="template")
counter = 0
polyline = Polyline()

app.secret_key = b's/,mdnfklsadn'

@app.route('/', methods=['GET', 'POST'])
def index():
    global counter
    if request.method == 'GET':
        counter += 1
        session['id'] = counter
        return render_template('index.html')

    if request.method == 'POST':
        name = request.form.get("name")
        ph_no = request.form.get("ph_no")
        session['name'] = name
        session['ph_no'] = ph_no

    return redirect(url_for('ride'))

@app.route('/ride', methods=['GET', 'POST'])
def ride():
    if request.method == 'GET':
        return render_template('ride.html')

    if request.method == 'POST':
        source_name = request.form.get("source")
        dest_name = request.form.get("dest")
        
        source_name = source_name.replace(' ', '+')

        # call HERE api's to get lat and lng
        url = f'https://geocode.search.hereapi.com/v1/geocode?q={source_name}&apiKey={API_KEY}'
        source_res = requests.get(url).json()
        url = f'https://geocode.search.hereapi.com/v1/geocode?q={dest_name}&apiKey={API_KEY}'
        dest_res = requests.get(url).json()

        # get lat and lng from request return objects
        if source_res['items']:
            source = [source_res['items'][0]['position']['lat'], source_res['items'][0]['position']['lng']]
            dest = [dest_res['items'][0]['position']['lat'], dest_res['items'][0]['position']['lng']]

            print(source, dest)

            polyline.add(session['id'], source, dest)

        else:
            print("Please provide full address")

    return redirect(url_for('pending'))

@app.route('/pending', methods=['GET'])
def pending():
    res = polyline.check_status(session['id'])

    if res == [-1, -1]:
        return render_template('pending.html')
    
    return redirect(url_for('success'))

@app.route('/success', methods=['GET'])
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)