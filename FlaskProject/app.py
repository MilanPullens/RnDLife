from flask import Flask
from flask import render_template
from flask import request
import pandas
import matplotlib.pyplot as plt
from io import BytesIO
import base64
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
            global screen
            screen = input['screen']
            global smoke
            smoke = input['smoke']
            global cig
            cig = input['cig']
            plot_urls=data()
            plot1=plot_urls[0]
            plot2=plot_urls[1]
            return render_template('End.html', smoke=smoke, plot1=plot1, plot2=plot2  )

    return render_template('LifeQ.html')

def data():
    pandas.options.mode.chained_assignment = None # None|'warn'|'raise'

    demData = pandas.read_csv("RnD/demographic.csv")
    dietData = pandas.read_csv("RnD/diet.csv")
    exmData = pandas.read_csv("RnD/examination.csv")
    labData = pandas.read_csv("RnD/labs.csv")
    medData = pandas.read_csv("RnD/medications.csv",usecols=[0,12])
    quesData = pandas.read_csv("RnD/questionnaire.csv")
    newData = pandas.read_sas("RnD/DEMO_I.xpt", format='xport')
    deathData = pandas.read_csv("RnD/Deaths.txt", sep='\t')

    filteredDemData = demData[['SEQN','RIAGENDR','RIDAGEYR','INDFMPIR']]
    filteredDietData = dietData[['SEQN','DR1TALCO','DR1TCAFF','DR1TKCAL']]
    filteredExmData = exmData[['SEQN','BPXPLS','BMXWT','BMXHT','BMXBMI']]
    filteredLabData = labData[['SEQN','LBXHGB','LBXWBCSI','LBXRBCSI']]
    filteredMedData = medData[['SEQN','RXDCOUNT']]
    filteredQuesData = quesData[['SEQN','MCQ220','PAD680']]
    filteredNewData = newData[['SEQN','RIAGENDR','RIDAGEYR','INDFMPIR']]
    filteredDeathData = deathData[['Gender','Single-Year Ages Code','Crude Rate']]

    filteredDemData.dropna(inplace = True)
    filteredDietData.dropna(inplace = True)
    filteredExmData.dropna(inplace = True)
    filteredLabData.dropna(inplace = True)
    filteredMedData.dropna(inplace = True)
    filteredNewData.dropna(inplace = True)

    filteredQuesData['ACTLIG'] = quesData['PAD645'].fillna(0)
    filteredQuesData['ACTMOD'] = quesData['PAD630'].fillna(0) + quesData['PAD675'].fillna(0)
    filteredQuesData['ACTVIG'] = quesData['PAD615'].fillna(0) + quesData['PAD660'].fillna(0)
    filteredQuesData['ACTTOT'] = filteredQuesData['ACTLIG'] + filteredQuesData['ACTMOD'] + filteredQuesData['ACTVIG']
    filteredQuesData['SCRTOT'] = quesData['PAQ710'].fillna(0) + quesData['PAQ715'].fillna(0)
    filteredQuesData['100CIG'] = quesData['SMQ020']
    filteredQuesData['CIGDAY'] = quesData['SMD650'].fillna(0)
    filteredQuesData.dropna(inplace = True)

    filteredData1 = pandas.merge(filteredDemData, filteredDietData, on="SEQN")
    filteredData2 = pandas.merge(filteredData1, filteredExmData, on="SEQN")
    filteredData3 = pandas.merge(filteredData2, filteredLabData, on="SEQN")
    filteredData4 = pandas.merge(filteredData3, filteredMedData, on="SEQN")
    filteredData5 = pandas.merge(filteredData4, filteredQuesData, on="SEQN")
    filteredFinalData = filteredData5.drop_duplicates(subset=['SEQN'])
    filteredDeathData.drop(filteredDeathData.index[1])
    #filteredFinalData.size/24
    #filteredFinalData.head(100)
    #filteredNewData.round(3)
    #filteredDeathData.head
    #filteredNewData.head(100)
    
    deathrate=(filteredDeathData['Crude Rate'][filteredDeathData['Gender']==gender][filteredDeathData['Single-Year Ages Code']==age]).to_csv(header=None, index=False).rstrip("\r\n")
    if ((weight and height)!=""):
        BMI=(int(weight))/(((int(height)/100)*(int(height)/100)))
    variables=["DR1TKCAL", "BMXBMI"]
    youG = 1
    youA = 30.0
    ages = [youA-5, youA-4, youA-3, youA-2, youA-1, youA, youA+1, youA+2, youA+3, youA+4, youA+5]
    fig, ax = plt.subplots(figsize=(12,6))
    names=["Distribution of ", "BMI"]
    xlabel=["calories", "BMI"]
    plots=[]
    you=[2500, BMI]
    for i in range(len(names)):
        temp2 = filteredFinalData[variables[i]]
        #you = temp2.iloc[5]
        f, axs = plt.subplots(1, 1)
        axs.hist(x=temp2, bins=100)
        axs.axvline(x=temp2.mean(), color='RED')
        axs.axvline(x=you[i], color='GREEN')
        plt.title(names[i])
        plt.xlabel(xlabel[i])
        plt.ylabel("frequency")
        img=BytesIO()
        plt.savefig(img, format='png')
        plots.append(base64.b64encode(img.getvalue()).decode('utf8'))
        # temp = filteredFinalData.loc[(filteredFinalData['RIAGENDR']== youG) 
                                #& (filteredFinalData['RIDAGEYR'].isin(ages))] 
    return plots
    

    
    '''plt.hist(x=temp2, bins=100)
    #plt.ylim((None, temp.size/25))
    plt.axvline(x=temp2.mean(), color='RED')
    plt.axvline(x=you, color='GREEN')
    plt.title("Distribution of")
    ax[0].xlabel("Calories a day")
    plt.ax[0].ylabel("frequency")
    img=BytesIO()
    plt.savefig(img, format='png')
    count = 0
    for i in temp2 :
        if i >= you :
            count = count + 1
    print(you,':' ,  round(count/temp2.size*100, 2),'%')'''   

if __name__ == '__main__':
   app.run(debug=True)







