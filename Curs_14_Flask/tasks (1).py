from flask import Blueprint, abort, jsonify
from repository import tasks as tasks_repo

bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.route("/")
def get_all():
    tasks = tasks_repo.get_tasks()
    if not tasks:
        abort(404)
    return jsonify(tasks)
