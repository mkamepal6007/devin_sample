from flask import Flask, jsonify, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index() -> str:
        return render_template("index.html", message="Hello, World!")

    @app.route("/api/hello")
    def api_hello():
        return jsonify(message="Hello, World!")

    @app.route("/health")
    def health():
        return jsonify(status="ok")

    return app
