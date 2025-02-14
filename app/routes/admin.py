from flask import Blueprint, request, redirect, flash, render_template, render_template_string, url_for
from app.forms import AddProjectForm
from app.models import create_project, delete_project_by_id, parse_choices

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/add-project', methods=['GET', 'POST'])
def add_project():
  form = AddProjectForm()
  if form.validate_on_submit():
    project = create_project(
      request.form.get('title'),
      request.form.get('desc'),
      request.form.get('url'),
      request.form.get('img'),
      request.form.get('category')
		)
    flash(f'New project "{ project["title"] }" added to { parse_choices(project["category"]) }.')
    return redirect(request.referrer)
  return render_template('/admin/new-project.html', form=form)

@admin_blueprint.route('/projects/remove/<string:id>', methods=['GET', 'POST'])
def delete_project(id: str):
  delete_project_by_id(id)
  return redirect(url_for('pages.projects'))