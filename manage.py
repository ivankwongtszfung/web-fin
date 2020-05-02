import os
import unittest

import pytest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
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

# Ipython setting
banner = ''

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


@manager.command
def test():
    """Runs the unit tests."""
    pytest.main(["-x", "app/test", "-vv", "--pdb"])
    return 1


@manager.command
def shell():
    from IPython import embed
    from IPython.terminal.ipapp import load_default_config
    config_colors = load_default_config().InteractiveShell.colors
    colors = config_colors if isinstance(config_colors, str) else "NoColor"
    embed(banner1=banner, user_ns={'app': app}, colors=colors)

# @manager.command
# def shell():
#     import IPython
#     from IPython.terminal.ipapp import load_default_config
#     c = load_default_config()
#     c.InteractiveShellEmbed = c.TerminalInteractiveShell
#     c.InteractiveShellApp.exec_lines = [
#         'load_ext autoreload', '%autoreload 2', ]
#     IPython.start_ipython(config=c, argv=[])


if __name__ == "__main__":
    manager.run()
