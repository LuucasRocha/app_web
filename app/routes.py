from flask import request, jsonify
from .services import get_all_tasks, create_task, update_task, delete_task

"""
Arquivo responsável por definir as rotas (endpoints) da aplicação.

As rotas recebem requisições HTTP e chamam as funções
responsáveis pelas regras de negócio (services).
"""

def register_routes(app):
    """
    Função responsável por registrar todas as rotas
    no objeto principal da aplicação.
    """
    @app.route("/tasks", methods=["GET"])
    def list_tasks():
        return jsonify(get_all_tasks())

    @app.route("/tasks", methods=["POST"])
    def add_task():
        data = request.get_json()
        if not data or "title" not in data:
            return jsonify({"error": "Title is required"}), 400
        return jsonify(create_task(data["title"])), 201

    @app.route("/tasks/<int:task_id>", methods=["PUT"])
    def edit_task(task_id):
        data = request.get_json()
        updated = update_task(task_id, data)
        if not updated:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(updated)

    @app.route("/tasks/<int:task_id>", methods=["DELETE"])
    def remove_task(task_id):
        delete_task(task_id)
        return jsonify({"message": "Task deleted"})