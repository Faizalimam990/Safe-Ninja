from flask import Flask, flash,redirect,render_template,session,url_for,request,jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import Employee,Business
from database import session as db
from sqlalchemy.exc import IntegrityError

app=Flask(__name__)

app.secret_key = 'S4F3-N1NJA-1$O9@*&6FA@^%@9180'
@app.route('/')

def index():
    business = db.query(Business).filter_by(id=1).first()
    print(business.name)

    
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



@app.route('/api/createbusiness/create', methods=['POST'])
def create_business():
    data = request.get_json()

    # Validate required fields
    required_fields = ['email', 'password', 'name']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'error': f'{field} is required'}), 400

    email = data['email']
    raw_password = data['password']
    name = data['name']

    # Hash password
    hashed_password = generate_password_hash(raw_password)

    # Create Business object
    new_business = Business(
        email=email,
        password=hashed_password,
        name=name
    )

    try:
        db.add(new_business)
        db.commit()
        return jsonify({'message': 'Business created successfully', 'business_id': new_business.id}), 201
    except IntegrityError:
        db.rollback()
        return jsonify({'error': 'Business name or email already exists'}), 409
    except Exception as e:
        db.rollback()
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500
if __name__ == "__main__":
    app.run(debug=True)  