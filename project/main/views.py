# project/main/views.py


#################
#### imports ####
#################
from flask import render_template, Blueprint
import os
import subprocess

################
#### config ####
################

main_blueprint = Blueprint('main', __name__, )


################
#### routes ####
################


@main_blueprint.route('/')
def home():
    return render_template('main/home.html')


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")


@main_blueprint.route('/shoot/')
def shoot():
    mUrl = "www.hust.edu.cn"
    path = os.path.dirname(os.path.realpath(__file__)) + "/shoot.py"
    subprocess.check_output("python " + path + " " + mUrl, shell=True)
    return 'hello'
