from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

def render_page(flavour, flavours):
    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Ice Cream</title>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <h1>The Ice Cream Shop</h1>
        <div id="flavours">
        {% for flavour in flavours %}
            <div class="flavour" >
                <a href="/?flavour={{ flavour }}">{{ flavour }}</a>
            </div>
        {% endfor %}
        </div>

        {% if flavour %}
        <div id="order">
                <h3>Flavour: ''' +  flavour + '''</h3>
                <button onclick="">Order  ></button>
        </div>
        {% endif %}
    </body>
    </html>
    '''
    return render_template_string(template, flavour=flavour, flavours=flavours)

flavours = ['vanilla', 'chocolate', 'strawberry', 'coffee', 'caramel']
blacklist = ['kill','die','rm']

@app.route("/", methods=["GET"])
def index():
    flavour = request.args.get("flavour") or ''
    if any(word in flavour for word in blacklist):
        return render_page(flavour="Hey, don't hack me!", flavours=flavours)
    return render_page(flavour=flavour.capitalize(), flavours=flavours)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
