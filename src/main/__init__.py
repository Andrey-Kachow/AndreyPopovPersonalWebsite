import os

from main.experiences import (
    WORK_EXPERIENCES,
    EDUCATION_EXPERIENCES
)

from flask import (
    Flask,
    render_template,
    url_for,
    Response,
    make_response,
    send_file
)

CV_PDF_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'documents')
CV_PDF_PATH = os.path.join(CV_PDF_DIR, 'CV.pdf')    


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def index():
        context = {
            'work_experiences': WORK_EXPERIENCES,
            'education_experiences': EDUCATION_EXPERIENCES,
        }
        return render_template('index.html', **context)

    @app.route('/cv')
    def cv():
        response = make_response(send_file(CV_PDF_PATH))
        response.headers['Content-Type'] = 'application/pdf'
        return response

    return app

