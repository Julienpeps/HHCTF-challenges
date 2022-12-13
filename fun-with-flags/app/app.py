from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route("/")
def index():

    # Get the file from the URL parameter
    country = request.args.get('country', default=None)

    try:
        include = open(f'static/countries/{country}', 'r').read()
    except:
        include = ''

    # Get the special flag from program's arguments
    # TODO: Display it
    try:
        special_flag = str(sys.argv[1])
    except:
        special_flag = ''

    return render_template('index.html', include=include)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
