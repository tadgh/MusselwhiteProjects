import bottle



app = bottle.Bottle()


@app.route('/')
def index():
    return 'hello!!'

@app.route('/static/:path#.+#', name='static')
def static(path):
    return bottle.static_file(path, root='./static/')


if __name__ == '__main__':
    bottle.run(app,host='0.0.0.0', port='8083', server='cherrypy')