from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ''
    greeting = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
        if name:
            greeting = f'Hello, {name}! Welcome to Azure hosting.'
    return render_template_string('''
        <!doctype html>
        <title>Flask App on Azure</title>
        <h2>Flask App on Azure</h2>
        <form method="post">
            Enter your name: <input type="text" name="name" value="{{ name }}">
            <input type="submit" value="Submit">
        </form>
        <p>{{ greeting }}</p>
    ''', name=name, greeting=greeting)

if __name__ == '__main__':
    app.run()
