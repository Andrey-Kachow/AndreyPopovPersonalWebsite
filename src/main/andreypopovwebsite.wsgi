#!/usr/bin/python
import sys, os
sys.path.append(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        '..'
    )
)

from main import create_app
application = create_app()
