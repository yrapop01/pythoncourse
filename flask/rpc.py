from flask import request, jsonify

def expose(app):
    def inner(func):
        @app.route('/' + func.__name__, methods=['GET', 'POST'])
        def wrapper():
            data = request.get_json(silent=True)
            args = data.get('args', [])
            kwargs = data.get('kwargs', {})
            return jsonify(func(*args, **kwargs))

        return wrapper

    return inner
