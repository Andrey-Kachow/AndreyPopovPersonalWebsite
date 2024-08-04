from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

bp = Blueprint('apps', __name__, url_prefix='/apps')

@bp.route('/ntictactoe')
def ntictactoe():
    return render_template('apps/ntic_tac_toe/ntictactoe.html')