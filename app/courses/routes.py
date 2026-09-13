from flask import Blueprint, render_template, abort
from flask_login import login_required
from app.courses.data import COURSES

courses_bp = Blueprint("courses", __name__, url_prefix="/courses")

@courses_bp.route("/")
@login_required
def list_courses():
    return render_template("courses.html", courses=COURSES)

@courses_bp.route("/<slug>")
@login_required
def module_detail(slug):
    # Find the module and the parent course
    for course in COURSES:
        for module in course["modules"]:
            if module["slug"] == slug:
                return render_template("course_detail.html", course=course, module=module)
    
    # If module not found
    abort(404)
