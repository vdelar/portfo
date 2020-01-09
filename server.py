from flask import Flask, render_template, request, redirect
import json
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<file>.html')
def other_files(file):
    return render_template(file + '.html')

def write_to_file(data):
    # with open('')
    pass

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    data = request.form.to_dict()
    with open('./messages/msg1.json', 'r') as file:
        records = file.read()
        records = records.replace('\n]','')
    with open('./messages/msg1.json', 'w') as file:
        file.write(records + ',\n' + json.dumps(data) + '\n]')
    return redirect('thankyou.html')
