from flask import render_template, request
from application import app

from .utils import generate_random_band_name


@app.route('/', methods=["GET", "POST"])
def generate_band_name(generated_band_name=''):
    if request.method == 'POST':
        generated_band_name = generate_random_band_name()
    return render_template(
        'index.html', generated_band_name=generated_band_name,
    )
