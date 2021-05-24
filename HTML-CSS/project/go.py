from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

gender = ""
age = ""
income = ""

alcohol = ""
coffee = ""

weight = ""
height = ""
heartrate = ""

hemoglobine = ""
wbc = ""
rbc = ""

drugs = ""

cancer = ""
sed = ""
ligACT = ""
modACT = ""
vigACT = ""
totACT = ""
screen = ""
smoke = ""
cig = ""

@app.route('/',methods=['POST','GET'])
def process_form():
    if request.method == 'POST':
        input=request.form
        if int(input['partID']) == 1:
            return render_template('Part1.html')
        elif int(input['partID']) == 2:
            global gender
            gender = input['gender']
            global age
            age = input['age']
            global income
            income = input['income']
            return render_template('Part2.html')
        elif int(input['partID']) == 3:
            global alcohol
            alcohol = input['alcohol']
            global coffee 
            coffee = input['coffee']
            return render_template('Part3.html')
        elif int(input['partID']) == 4:
            global weight
            weight = input['weight']
            global height 
            height = input['height']
            global heartrate
            heartrate = input['heartrate']
            return render_template('Part4.html')
        elif int(input['partID']) == 5:
            global hemoglobine
            hemoglobine = input['hemoglobine']
            global wbc 
            wbc = input['wbc']
            global rbc
            rbc = input['rbc']
            return render_template('Part5.html')
        elif int(input['partID']) == 6:
            global drugs
            drugs = input['drugs']
            return render_template('Part6.html')
        elif int(input['partID']) == 7:
            global cancer
            cancer = input['cancer']
            global sed
            sed = input['sed']
            global ligACT
            ligACT = input['ligACT']
            global modACT
            modACT = input['modACT']
            global vigACT
            vigACT = input['vigACT']
            global totACT
            totACT = input['totACT']
            global screen
            screen = input['screen']
            global smoke
            smoke = input['smoke']
            global cig
            cig = input['cig']
            data()
            return render_template('End.html')

    return render_template('LifeQ.html')

def data():
    print("Part 1:")
    print(gender)
    print(age)
    print(income)
    print("Part 2:")
    print(alcohol)
    print(coffee)
    print("Part 3:")
    print(weight)
    print(height)
    print(heartrate)
    print("Part 4:")
    print(hemoglobine)
    print(wbc)
    print(rbc)
    print("Part 5:")
    print(drugs)
    print("Part 6:")
    print(cancer)
    print(sed)
    print(ligACT)
    print(modACT)
    print(vigACT)
    print(totACT)
    print(screen)
    print(smoke)
    print(cig)

if __name__ == '__main__':
   app.run(debug=True)