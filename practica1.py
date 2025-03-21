from flask import Flask

app = Flask(__name__)
#@app.route('/wellcome/<name>')
#@app.route('/wellcome <int:ncontrol>')
#@app.route('/wellcome/<name>/<int:ncontrol>')
#def hello(name, ncontrol):
# return f'Bienvenido {name}, tu número de control es: {ncontrol}'

#if __name__ == '__main__':
#    app.run(debug=True)

@app.route('/wellcome/')

@app.route('/wellcome/<name>')

@app.route('/wellcome/<int:ncontrol>')

@app.route('/wellcome/<name>/<int:ncontrol>')

def bienvenido(name=None,ncontrol=None):

    if name== None and ncontrol==None:

        return 'Bienvenido '

    if name!= None and ncontrol == None:

        return f'Bienvenido {name}'

    if name == None and ncontrol != None:

        return f'El número recibido es: {ncontrol}'

    else:

        return f'Bienvenido {name} tu numero de control es: {ncontrol}'
    
    a=8

    print(a)

    print(type(a))

    a='mexicali'

    print(a)

    print(type(a))

    a=4.5

    print(a)

    print(type(a))

    a=None

    print(a)

    print(type(a))