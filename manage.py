import os
from flask_script import Manager
from flask_migrate import Migrate
from app import create_app
from flask_cors import CORS


env = os.getenv("FLASK_ENV") or "dev"

print(f"Active environment: * {env} *")


app, mongo_db = create_app(env)

migrate = Migrate(app, mongo_db)

manager = Manager(app)

# CORS enabling

CORS(app)


@manager.command
def run():
    app.run(debug=True, host="0.0.0.0")


if __name__ == "__main__":
    manager.run()


