from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('usuario.html',)

@app.route('/user')
def user(): 
    return render_template('home.html')
  

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/bonifica')
def bonifica():
    return render_template('bonificacion.html')

if __name__ == '__main__':
    app.run(debug=True)