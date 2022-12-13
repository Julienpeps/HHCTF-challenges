from flask import Flask, render_template,send_from_directory,make_response

app = Flask(__name__)

# flag: HHCTF{tHiS_1s_A_r3a11y_lOo00Oo0o00on9_FlaG}

# flag-1: HHCTF{tHiS_1s
# flag-2: _A_r3a11y
# flag-3: _lOo00Oo0
# flag-4: o00on9_FlaG}

@app.route("/")
def index():
    resp = make_response(render_template("index.html"))
    resp.set_cookie("flag-1","HHCTF{tHiS_1s")
    return resp

@app.route("/<path:path>")
def static_file(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
