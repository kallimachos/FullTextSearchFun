from bottle import request, route, run, static_file, template

@route('/custom.css')
def serve_static():
    return static_file("custom.css", root='.')


@route('/')
def index():
    return template('search')


run(host='localhost', port=8080, debug=True)
