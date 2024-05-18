import os

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

from flask import (
    Flask,
    render_template,
    url_for,
    Response,
    make_response,
    send_file
)

DOCUMENTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'documents')
CV_PDF_PATH = os.path.join(DOCUMENTS_DIR, 'CV.pdf')    
FRESHIFE_PDF_PATH = os.path.join(DOCUMENTS_DIR, 'freshlife_writeup.pdf')


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        
        context = {
            'work_experiences': WORK_EXPERIENCES,
            'pet_projects': PET_PROJECTS,
            'academic_projects': ACADEMIC_PROJECTS,
            'education_experiences': EDUCATION_EXPERIENCES,
            'research_experiences': RESEARCH_EXPERIENCES # + [SELF_ATTACHMENT_TECHNIQUE_MENG_PROJECT],
        }
        return render_template('index.html', **context)

    @app.route('/cv')
    def cv():
        response = make_response(send_file(CV_PDF_PATH))
        response.headers['Content-Type'] = 'application/pdf'
        return response
    
    @app.route('/freshlife-writeup')
    def freshlife_writeup():
        response = make_response(send_file(FRESHIFE_PDF_PATH))
        response.headers['Content-Type'] = 'application/pdf'
        return response

    @app.route('/scaling-extreme-startup')
    def scaling_extreme_startup():
        context = {
            'project': ACADEMIC_PROJECTS[0]
        }
        return render_template('articles/scaling_extreme_startup.html', **context)

    # @app.route('/blog/hobbies')
    # def hobbies():
    #     return render_template('blog/hobbies/hobby_index.html')

    # @app.route('/icmodules')
    # def icmodules():
    #     return render_template('experiences/imperial/icmodules.html')

    return app

