from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def render_home_page():
    return render_template_string('HELLO WORLD')


if __name__ == '__main__':
   if len(sys.argv) == 1:
        port = 5000
    else:
        port = int(float(sys.argv[1])) #the custom port you want
    app.run(host='0.0.0.0', port=port)
