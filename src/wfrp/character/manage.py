from wfrp.character.app import create_app
from wfrp.character.database import init_db
from wfrp.character.routes import register_routes


def main():
    app = create_app()
    init_db(app)
    with app.app_context():
        register_routes(app)
    app.run(debug=False, port=6543)


if __name__ == "__main__":
    main()
