import os

from flask import Flask, render_template

from data_fetch import get_jwt_token, get_activity_parameters


basedir = os.path.abspath(os.path.dirname(__file__))


template_dir = os.path.join(basedir, '..', 'templates')
app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def dashboard():
    try:
        login = os.getenv("LOGIN")
        password = os.getenv("PASSWORD")

        jwt_token = get_jwt_token(login, password)

        activity_parameters = get_activity_parameters(jwt_token)

        return render_template('dashboard.html', activity_parameters=activity_parameters)

    except Exception as e:
        return f"Failed to fetch data: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)

