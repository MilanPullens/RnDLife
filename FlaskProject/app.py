from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

weight=""
country=""
cig=""
gender=""
@app.route('/',methods=['POST','GET'])
def process_form():
    if request.method == 'POST':
        input=request.form
        print(input)
        if int(input['partID']) == 1:
            return render_template('Part1.html')
        elif int(input['partID']) == 2:
            return render_template('Part2.html')
        elif int(input['partID']) == 3:
            return render_template('Part3.html')
        elif int(input['partID']) == 4:
            return render_template('Part4.html')
            
    return render_template('LifeQ.html')


def data():
    print(gender, country, weight, cig)
    
if __name__ == '__main__':
   app.run(debug=True)