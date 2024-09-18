"""Views > Cores"""
# Imports
from flask import render_template, Blueprint, request, redirect, url_for

from controllers.test_connection_controller import test_connection


# Blueprint
core_bp = Blueprint('core', __name__)


# Route - Homepage
@core_bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Landing Page
    Functionality:
      - User adds the API endpoint and Bearer token to test the connection and
        ExplainationOfBenefit resource
    """

    if request.method == 'POST':
        base_url = request.form.get('base_url')

        # Ensure the URL starts with https:// and ends with a slash
        if not base_url.startswith('https://'):
            base_url = f'https://{base_url}'
        if not base_url.endswith('/'):
            base_url = f'{base_url}/'

        api_endpoint = f"{base_url}fhir/ExplainationOfBenefit"

        connection_result = test_connection(api_endpoint)

        if connection_result['success']:
            return redirect(url_for('claim_results',
                                    base_url=base_url))
        else:
            return render_template('results/index.html',
                                   title='Claim Results',
                                   connection_result=(
                                       connection_result['message']))

    return render_template('index.html',
                           title='H3O-FHIR-CLAIM-COMPARE')

