#!/usr/bin/bash

export FLASK_APP=src/main
export FLASK_ENV=development
flask run -h localhost -p 5001

## Windows
#
# $Env:FLASK_APP = 'src/main'
# $Env:FLASK_ENV = 'development'
# flask run -h localhost -p 5001 --debug
#    or
# python -m flask run -h localhost -p 5001 --debug