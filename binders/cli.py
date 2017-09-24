#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from colorama import Fore, Style
from flask_script import Manager
from subprocess import Popen

from binders import app

config = app.config

manager = Manager(app)


@manager.option(
    '-d', '--debug', action='store_true',
    help="Start the web server in debug mode")
@manager.option(
    '-n', '--no-reload', action='store_false', dest='no_reload',
    default=config.get("FLASK_USE_RELOAD"),
    help="Don't use the reloader in debug mode")
@manager.option(
    '-a', '--address', default=config.get("BINDERS_WEBSERVER_ADDRESS"),
    help="Specify the address to which to bind the web server")
@manager.option(
    '-p', '--port', default=config.get("BINDERS_WEBSERVER_PORT"),
    help="Specify the port on which to run the web server")
def runserver(debug, no_reload, address, port):
    """Starts a Superset web server."""
    debug = debug or config.get("DEBUG")
    if debug:
        print(Fore.BLUE + '-=' * 20)
        print(
            Fore.YELLOW + "Starting Superset server in " +
            Fore.RED + "DEBUG" +
            Fore.YELLOW + " mode")
        print(Fore.BLUE + '-=' * 20)
        print(Style.RESET_ALL)
        app.run(
            host='0.0.0.0',
            port=int(port or 8080),
            threaded=False,
            debug=True,
            use_reloader=no_reload)
    else:
        addr_str = " {address}:{port} "
        cmd = (
            "gunicorn "
            "-b " + addr_str +
            "--limit-request-line 0 "
            "--limit-request-field_size 0 "
            "binders:app").format(**locals())
        print(Fore.GREEN + "Starting server with command: ")
        print(Fore.YELLOW + cmd)
        print(Style.RESET_ALL)
        Popen(cmd, shell=True).wait()


@manager.command
def list_routes():
    import urllib
    from flask import url_for

    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:25s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    print(Fore.YELLOW + "{:50s} {:25s} {}".format("Views/Endpoints", "Methods", "URL"))
    for line in sorted(output):
        print(Fore.GREEN + line)
