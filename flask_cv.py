from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'MI-PYT je nejlepší předmět na FITu!'

if __name__ == '__main__':
    app.run(debug=True)


    ##########################3333

    python anywhere.
    #treba virtualenv.
    virtualenv --python=python3.5 env
