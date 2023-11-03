from flask import Blueprint, abort, jsonify, request, Response
from repository import tasks as task_repo

bp = Blueprint('tasks', __name__, url_prefix='/tasks')


@bp.route("/")
def get_all():
    tasks = task_repo.get_tasks()
    if not tasks:
        abort(404)
    return jsonify(tasks)


@bp.route('/', methods=["POST"])
def add_task():
    task_data = request.json
    task_repo.add_task(task_data)
    return Response("OK", 201)
