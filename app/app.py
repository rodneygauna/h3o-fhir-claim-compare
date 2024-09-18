"""
H3O-FHIR-CLAIM-COMPARE
Author: Rodney Gauna
GitHub: https://github.com/rodneygauna/h3o-fhir-claim-compare
"""
# Imports
from flask import Flask

# Flask Blueprints - Imports
from views.core_views import core_bp


# Flask initialization
app = Flask(__name__)

# Flask Blueprints - Register
app.register_blueprint(core_bp)

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
