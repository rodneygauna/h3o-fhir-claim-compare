"""Views > Cores"""
# Imports
from flask import render_template, Blueprint


# Blueprint
core_bp = Blueprint('core', __name__)


# Route - Homepage
@core_bp.route('/')
def index():
    """Homepage"""

    return render_template('index.html',
                           title='H3O-FHIR-CLAIM-COMPARE')
