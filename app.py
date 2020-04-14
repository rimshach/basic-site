from flask import Flask, render_template

app = Flask(__name__,template_folder='')

@app.route('/')
def render_home_page():
    return render_template('home.html')


if __name__ == '__main__':
   app.run()