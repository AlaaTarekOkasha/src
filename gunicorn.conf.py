import multiprocessing

bind = ":8000"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = "gunicorn_landingpages.log"
# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "landing_api.wsgi:emarketing"
# The granularity of Error log outputs
# loglevel = "debug"
# The number of worker processes for handling requests
# workers = 2
# The socket to bind
# bind = "0.0.0.0:8000"
# Restart workers when code changes (development only!)
# reload = True
# Write access and error info to /var/log
# accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "gunicorn.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = True