#!/usr/bin/bash

export FLASK_APP=src/main
export FLASK_ENV=development
export FLASK_APP_SECRET_KEY='some_secret_key_for_tests'
flask run -h localhost -p 5000

## Windows
#
# $Env:FLASK_APP = 'src/main'
# $Env:FLASK_ENV = 'development'
# flask run
# or
# flask run -h localhost -p 5001 --debug
# or
# SET FLASK_APP='src/main'
# SET FLASK_ENV='development'
# flask run
#    or
# python -m flask run -h localhost -p 5001 --debug