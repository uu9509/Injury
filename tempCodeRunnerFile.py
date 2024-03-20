@app.route("/verify_signin", methods=["POST"])
def verify_signin():
    if request.method == 'POST':
        field = str(request.form.get('field'))
        number = int(request.form.get('mobile'))
        password = request.form.get('password')
        if field=='student':
            if db.execute(text("SELECT number FROM student WHERE number = :number", {"number": number})).rowcount == 0:
                return render_template('login-system/signup.html',msg="Enter mobile number not exist, Register first!")
            else:
                raw = db.execute(text("SELECT password,name FROM student WHERE number = :number", {"number": number})).fetchone()
                password_db = raw[0]
                if(password == password_db):
                    return 'tranfer student to academy or online video'
                else:
                    return render_template('login-system/signin.html',msg="Your enter incorrect password, Try again!")