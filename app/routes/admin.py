from flask import Blueprint, request, redirect, session, render_template
from app.forms import AddProjectForm
from app.models import create_project, parse_choices

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/add-project', methods=['GET', 'POST'])
def add_project():
  form = AddProjectForm()
  if form.validate_on_submit():
    create_project(
      request.form.get('title'),
      request.form.get('desc'),
      request.form.get('url'),
      request.form.get('img'),
      request.form.get('category')
		)
    return redirect(request.referrer)
  return render_template('/admin/new-project.html', form=form)