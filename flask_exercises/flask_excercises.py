from typing import Any

from flask import Flask, request


class FlaskExercise:
    @staticmethod
    def configure_routes(app: Flask) -> None:
        db: dict = {}

        @app.route("/user", methods=["POST"])
        def new_user() -> Any:
            username = request.json.get("name")
            if username:
                db[username] = username
                return {"data": f"User {username} is created!"}, 201
            return {"errors": {"name": "This field is required"}}, 422

        @app.route("/user/<name>", methods=["GET", "PATCH", "DELETE"])
        def modify_user(name: str) -> Any:
            if request.method == "GET":
                if db.get(name):
                    return {"data": f"My name is {db[name]}"}, 200
                return "User not found", 404
            if request.method == "PATCH":
                new_name = request.json.get("name")
                db[name] = new_name
                return {"data": f"My name is {new_name}"}, 200
            if request.method == "DELETE":
                db.pop(name)
                return "User was deleted", 204
            return "", 500
