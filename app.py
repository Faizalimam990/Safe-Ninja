from flask import Flask,redirect,render_template
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)

app.secret_key = 'S4F3-N1NJA-1$O9@*&6FA@^%@9180'
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/employeelogin/')
def employeelogin():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        employee = db.session.query(Employee).filter_by(email=email).first()

        if employee and check_password_hash(employee.password, password):
            session['employee_id'] = employee.id
            session['is_admin'] = employee.is_admin
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # Replace with your route
        else:
            flash('Invalid email or password', 'danger')

    return render_template('employeelogin.html')


@app.route('/businesslogin/')

def businesslogin():

    return render_template('businesslogin.html')

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