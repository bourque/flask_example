import glob

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    """The 'telescope' project homepage"""

    return render_template('index.html')


@app.route('/instruments/')
def instruments():
    """Return the instrument template"""

    instruments = ['ACS', 'WFC3', 'STIS']
    return render_template('instruments.html', instrument_list=instruments)


@app.route('/documentation/<instrument>/')
def documentation(instrument):
    """Return the documentation template for the given instrument"""

    return render_template('{}.html'.format(instrument))


@app.route('/images/')
def images():
    """Return the images template"""

    image_dict = {}
    image_dict['nebulae'] = glob.glob('static/img/nebulae/*')
    image_dict['planets'] = glob.glob('static/img/planets/*')
    image_dict['comets'] = glob.glob('static/img/comets/*')

    return render_template('images.html', image_dict=image_dict)


if __name__ == '__main__':
    app.run()