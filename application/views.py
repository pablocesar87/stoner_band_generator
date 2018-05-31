from flask import render_template, request, session
from application import app

from .utils import generate_random_band_name, get_adjetive


@app.route('/', methods=["GET", "POST"])
def generate_band_name(generated_band_name=''):
    name_generated = False
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'Generate a band name':
            generated_band_name = generate_random_band_name()
            session['previous_band_name'] = generated_band_name
            name_generated = True
        elif action == 'Make it metalier!' and session.get(
            'previous_band_name',
        ):
            adjetive = get_adjetive()
            generated_band_name = '{} {}'.format(
                adjetive,
                session.get('previous_band_name'),
            )
            name_generated = True
        else:
            pass
    return render_template(
        'index.html',
        generated_band_name=generated_band_name,
        name_generated=name_generated,
    )
