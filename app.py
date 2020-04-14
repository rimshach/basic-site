from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def render_home_page():
    return render_template_string('HELLO WORLD')


if __name__ == '__main__':
   app.run()
