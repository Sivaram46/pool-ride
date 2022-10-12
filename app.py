from flask import Flask, request, render_template

app = Flask(__name__, template_folder="template")

@app.route('/', methods=['GET', 'POST'])
def index():
    result = [None, None]
    if request.method == 'POST':
        source = (request.form.get("source-lon"), request.form.get("source-lat"))
        dest = (request.form.get("dest-lon"), request.form.get("dest-lat"))
        result = [source, dest]

    return render_template('index.html', data=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)