from typing import Any

from flask import Flask, request


class FlaskExercise:
    @staticmethod
    def configure_routes(app: Flask) -> None:
        db: dict = {}

        @app.post("/user")
        def new_user() -> Any:
            username = request.json.get("name")
            if not username:
                return {"errors": {"name": "This field is required"}}, 422
            db[username] = username
            return {"data": f"User {db[username]} is created!"}, 201

        @app.get("/user/<name>")
        def find_user(name: str) -> Any:
            if db.get(name):
                return {"data": f"My name is {db[name]}"}, 200
            return "User not found", 404

        @app.patch("/user/<name>")
        def update_user(name: str) -> Any:
            new_name = request.json.get("name")
            if not new_name:
                return "User not found", 404
            db[name] = new_name
            return {"data": f"My name is {db[name]}"}, 200

        @app.delete("/user/<name>")
        def delete_user(name: str) -> Any:
            if name not in db.keys():
                return "User not found", 404
            db.pop(name)
            return "User was deleted", 204
