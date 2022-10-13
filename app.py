from flask import Flask, request, render_template, session, redirect, url_for
from polyline import Polyline

app = Flask(__name__, template_folder="template")
counter = 0
polyline = Polyline()

app.secret_key = b's/,mdnfklsadn'

@app.route('/', methods=['GET', 'POST'])
def new_user():
    global counter
    if request.method == 'GET':
        counter += 1
        session['id'] = counter
        return render_template('new_user.html')

    if request.method == 'POST':
        name = request.form.get("name")
        ph_no = request.form.get("ph_no")
        session['name'] = name
        session['ph_no'] = ph_no

    return redirect(url_for('index'))

@app.route('/ride', methods=['GET', 'POST'])
def index():
    global counter
    if request.method == 'GET':
        counter += 1
        session['id'] = counter
        return render_template('index.html')

    if request.method == 'POST':
        source = (request.form.get("source-lon"), request.form.get("source-lat"))
        dest = (request.form.get("dest-lon"), request.form.get("dest-lat"))
        polyline.add(session['id'], source, dest)

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