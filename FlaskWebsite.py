from flask import Flask
app = Flask(__name__, static_url_path='', static_folder='website')

@app.route("/")
@app.route("/website")
def website():
    return app.send_static_file('index.html')

@app.route("/contactus")
def contactus():
    return '''<!doctype html>
    <html><style> body {background-color:powderblue; text-align:center; type=text/css"} 
    h1 {color:darkblue;} p {color:darkgreen;}  </style>
    <title>Flask Web-Site (Course 55264A)</title>
    <p><h1 style="color:blue;">Contact Us:<hr></h1>
    <a href="mailto:myemail@host.com">Email us your feedback</a></p>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True)

