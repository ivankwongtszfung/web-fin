import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
from app.main.resources import *
from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

# Expand the Swagger UI when it is loaded: list or full
app.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
# Globally enable validating
app.config['RESTPLUS_VALIDATE'] = True
# Enable or disable the mask field, by default X-Fields
app.config['RESTPLUS_MASK_SWAGGER'] = False
# Enable or disable the 404 default message
app.config['ERROR_404_HELP'] = False

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()