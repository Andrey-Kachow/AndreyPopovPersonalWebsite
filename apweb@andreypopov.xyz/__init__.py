import main.apps as apps
from main.experiences import (
    WORK_EXPERIENCES,
    EDUCATION_EXPERIENCES,
    RESEARCH_EXPERIENCES,
)
from main.projects import (
    PET_PROJECTS,
    ACADEMIC_PROJECTS,
    SELF_ATTACHMENT_TECHNIQUE_MENG_PROJECT
)
from main.constants import *

import os

from flask import (
    Flask,
    render_template,
    url_for,
    Response,
    make_response,
    send_file
)


def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
    )
    app.config['DEBUG'] = os.environ.get('FLASK_ENV') == 'development'

    app.register_blueprint(apps.bp)

    @app.route('/')
    def index():
        context = {
            'is_index': True,
            'featured': SELF_ATTACHMENT_TECHNIQUE_MENG_PROJECT,
            'work_experiences': WORK_EXPERIENCES,
            'pet_projects': PET_PROJECTS,
            'academic_projects': ACADEMIC_PROJECTS,
            'education_experiences': EDUCATION_EXPERIENCES,
            'research_experiences': RESEARCH_EXPERIENCES # + [SELF_ATTACHMENT_TECHNIQUE_MENG_PROJECT],
        }
        return render_template('index.html', **context)

    @app.route('/cv')
    def cv():
        response = make_response(send_file(Paths.CV_PDF_PATH))
        response.headers['Content-Type'] = 'application/pdf'
        return response
    
    @app.route('/freshlife-writeup')
    def freshlife_writeup():
        response = make_response(send_file(Paths.FRESHIFE_PDF_PATH))
        response.headers['Content-Type'] = 'application/pdf'
        return response

    @app.route('/scaling-extreme-startup')
    def scaling_extreme_startup():
        context = {
            'project': ACADEMIC_PROJECTS[0]
        }
        return render_template('articles/scaling_extreme_startup.html', **context)

    @app.route('/sat-protocol-online-article')
    def sat_protocol_online_article():
        context = {
            'project': SELF_ATTACHMENT_TECHNIQUE_MENG_PROJECT
        }
        return render_template('articles/imperial/sat/sat_protocol_online.html', **context)

    # @app.route('/blog/hobbies')
    # def hobbies():
    #     return render_template('blog/hobbies/hobby_index.html')

    # @app.route('/icmodules')
    # def icmodules():
    #     return render_template('experiences/imperial/icmodules.html')

    return app

