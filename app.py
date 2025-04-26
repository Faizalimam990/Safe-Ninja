from flask import Flask,redirect,render_template

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')
'''''''

@app.route('/admin')

def admin():
    return render_template('admin.html')

@app.route('/incidents')

def incidents():
    return render_template("incidents.html")

@app.route('/report-incident/')

def report_incident():
    return render_template('report_incident.html')



if __name__ == "__main__":
    app.run(debug=True)  