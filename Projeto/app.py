from flask import Flask, render_template
import extendmap

app = Flask(__name__)

def extend_map():
    

@app.route('/')
def home():
    result = extend_map()
    return render_template('projeto.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)