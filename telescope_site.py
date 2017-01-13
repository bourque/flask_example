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


if __name__ == '__main__':
    app.run()