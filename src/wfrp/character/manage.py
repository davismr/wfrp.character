from wfrp.character.app import create_app
from wfrp.character.database import init_db


def main():
    app = create_app()
    init_db(app)
    app.run(debug=False, port=6543)


if __name__ == "__main__":
    main()
