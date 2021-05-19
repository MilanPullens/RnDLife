from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def process_form():
    if request.method == 'POST':
        if int(request.form['partID']) == 1:
            return render_template('Part1.html')
        elif int(request.form['partID']) == 2:
            return render_template('Part2.html')
    return render_template('LifeQ.html')

if __name__ == '__main__':
   app.run(debug=True)