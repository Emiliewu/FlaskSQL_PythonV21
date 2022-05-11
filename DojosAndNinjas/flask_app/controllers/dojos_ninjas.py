
from contextlib import nullcontext
import re
from flask_app import app
from flask import render_template,redirect,request,session,get_flashed_messages
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app.models.course import Course
from flask_app.models.registration import Registration

@app.route("/dojo")
@app.route("/")
def index():
    
    # call the get all classmethod to get dojos
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("index.html", dojos = dojos)

# create new dojo
@app.route("/dojo/new", methods=['POST'])
def createdojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect("/dojo")

@app.route("/ninja")
def newninja():
    # create new ninja
    dojos = Dojo.get_all()
    return render_template("newninja.html", dojos = dojos)

@app.route("/ninja/new", methods=['POST'])
def createninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojos_id': request.form['dojo']
    }
    Ninja.save(data)
    return redirect("/")

@app.route("/dojo/<int:id>")
def dojodetail(id):
    # display dojo detail
    data = {
        "id": id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("dojodetail.html", dojo = dojo)

@app.route("/course")
def newcourse():
    # create new course
    courses = Course.get_all()
    return render_template("newcourse.html", courses = courses)

@app.route("/course/new", methods=['POST'])
def createcourse():
    data = {
        'name': request.form['name'],
    }
    Course.save(data)
    return redirect("/course")

@app.route("/register")
def newregister():
    if not session.get("error"):
        session['error'] = " "
    courses = Course.get_all()
    ninjas = Ninja.get_all()
    print(ninjas)
    return render_template("/newregister.html", courses = courses, ninjas = ninjas)

@app.route("/register/new", methods=['POST'])
def registercourse():
    
    data = {
        'ninja_id': request.form['ninja'],
        'course_id': request.form['course']
    }
    validationdata = {
        'id': request.form['course']
    }
    course = Course.get_course_with_ninjas(validationdata)
    if course != "not found":
        for ninja in course.ninjas:
            if ninja.id == int(request.form['ninja']):
                session['error'] = "ninja already registered"
                return redirect('/register')
            else:
                session.clear()
    Registration.register_ninja_to_course(data)
    return redirect('/register')

@app.route("/course/<int:id>")
def coursedetail(id):
    data = {
        'id': id
    }
    course = Course.get_course_with_ninjas(data)
    return render_template("coursedetail.html", course = course)