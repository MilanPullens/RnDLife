from typing import final
from flask import Flask
from flask import render_template
from flask import request
import pandas
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np

app = Flask(__name__)

gender = ""
age = ""
income = ""
country=""

alcohol = ""
coffee = ""
health=""
bmi=""

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

cigRG=False
healthRG=False
drinkRG=False
bmiRG=False
physRG=False
lowRG=0

LifeExpectancyvalue1=0
LifeExpectancyvalue2=0

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
            global country
            country=input['country']
            return render_template('Part2.html')
        elif int(input['partID']) == 3:
            global alcohol
            alcohol = input['alcohol']
            global coffee 
            coffee = input['coffee']
            global health
            health=input['health']
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
            plots=data()
            global drinkRG
            global bmiRG
            global physRG
            global cigRG
            global LifeExpectancyvalue1
            global LifeExpectancyvalue2
            global healthRG
            global bmi
            cigfeedback=""
            physfeedback=""
            drinkfeedback=""
            bmifeedback=""
            healthfeedback=""
            goodfeedback=""
            
            cigfeedback="""Non-smoker = 0 cigarettes per day\n Light smoker = 1-10 cigarettes per day\n Moderate smoker = 11-19 cigarettes per day\n
                                Heavy smoker = 20+ cigarettes per day\n
                            Smoking is one of the greatest contributors to life expectancy. Smoking causes cancer, heart disease, stroke, lung diseases, diabetes, and more. It is estimated that more that approximately 70% of smokers, die from smoking related illness.
                            A heavy smoker has a life expectancy that is 13 years shorter than that of a non-smoker. This is  9 years for moderate smokers, and 5 years for light smokers."""
            cigfeedback=cigfeedback.replace("\n", "<br />")

            if (not drinkRG):
                drinkfeedback="""Lifetime never or infrequent drinker = 0 drinks per week
                                Light drinker = 1-6 drinks per week\n
                                Moderate drinker = 7-14 drinks per week\n
                                Heavy drinker = 14-25 drinks per week\n
                                Very heavy drinker = 25+ drinks per week\n

                                These are some of the common negative health consequences of excessive alcohol consumption:
                                Liver disease; a higher risk of high blood pressure, heart failure, and dementia; a higher risk of certain cancers; a higher risk of injury (drunk driving or falls for example); and alcohol poisoning.\n

                                These factors and others make it that a very heavy drinker at the age of 40, has a life expectancy that is 4 to 5 years shorter than that of a non-drinker. This is 1 to 2 years for heavy drinkers, and 6 months for moderate drinkers.\n

                                While the list of health risks related to excessive alcohol consumption is long, there may also be health benefits associated with light drinking. Studies suggest that light drinking may be linked with a lower risk of: heart attack, the most common type of stroke, death due to cardiovascular disease, and diabetes.
                                Despite these potential health benefits, most doctors don’t recommend that someone who doesn’t drink start drinking, or for a light drinker to drink more. That’s because these are only correlations (which does not necessarily mean causation). Many of these benefits are quite small, and it’s hard to predict who will actually benefit and who may be harmed more than helped by alcohol consumption.
                                    """
            else: drinkfeedback="Your drinking habits are fine. Surprisingly, a small amount of alcohol (5-30g for men, 5-15g for women) can be better than no alcohol."
            if (not physRG):
                physfeedback="You should try to get some more activity. It has a big impact on your life, so try to encorporate some exercise into your lifestyle."
            else: physfeedback="You get a good amount of activity, so keep it up!"
            if (not healthRG):
                healthfeedback="You should try to eat healthier!"
            else: healthfeedback="Your eating habits are good."
            if (not bmiRG):
                if(bmi<18.5):bmifeedback="Talk with your healthcare provider to determine possible causes of underweight and if you need to gain weight. A BMI lesser than 18.5 leads to a life expectancy shortened by 4.3 years for men, and 4.5 years for women, compared to people with a healthy BMI of 18.5-24.9"
                elif(bmi>=18.5 and bmi<25): bmifeedback="Maintaining a healthy weight may reduce the risk of chronic diseases associated with overweight and obesity."
                elif(bmi>=25 and bmi<30): bmifeedback="People who are overweight or obese are at higher risk for chronic conditions such as high blood pressure, diabetes, and high cholesterol. A BMI of 25-29.9 leads to a 1.0 years shorter life expectancy for men, and 0.8 years shorter for women, compared to people with a healthy BMI of 18.5-24.9"
                elif(bmi>=30): bmifeedback="People who are overweight or obese are at higher risk for chronic conditions such as high blood pressure, diabetes, and high cholesterol. A BMI greater than 30 leads to a 4.2 years shorter life expectancy for men, and 3.5 years shorter for women, compared to people with a healthy BMI of 18.5-24.9"
            else: bmifeedback="Your bmi is good."
            if (cigRG and drinkRG and physRG and healthRG and bmiRG):
                goodfeedback="Your lifestyle is very well and "
            plot1=plots[0]
            plot2=plots[1]
            plot3=plots[2]
            plot4=plots[3]
            plot5=plots[4]
            return render_template('End.html', LifeExpectancyvalue1=LifeExpectancyvalue1, LifeExpectancyvalue2=LifeExpectancyvalue2, cigfeedback=cigfeedback, 
            physfeedback=physfeedback, drinkfeedback=drinkfeedback, bmifeedback=bmifeedback, healthfeedback=healthfeedback, goodfeedback=goodfeedback,
            plot1=plot1, plot2=plot2, plot3=plot3, plot4=plot4, plot5=plot5)

    return render_template('LifeQ.html')

def data():
    if (smoke=="no"):
        smoked=2
    else: smoked=1
    act=int(modACT)+int(vigACT)
    global bmi
    if ((weight and height)!=""):
        bmi=round((int(weight))/(((int(height)/100)*(int(height)/100))), 1)
    LowRisks=[range(5,30), range(17,25), range(45,1280), range(2,3)]
    gramAlcohol=(int(alcohol)*15)/7
    global drinkRG
    global bmiRG
    global physRG
    global cigRG
    LowRiskData = [gramAlcohol, bmi, act, smoked]
    LowRiskGroups=[drinkRG, bmiRG, physRG, cigRG]
    index = 0
    global lowRG
    for i in LowRiskData :
        if int(i) in LowRisks[index]:
            if (lowRG<5):
                lowRG=lowRG+1
            LowRiskGroups[index]=True
        index = index+1
    global cig
    
    drinkRG=LowRiskGroups[0]
    bmiRG=LowRiskGroups[1]
    physRG=LowRiskGroups[2]
    cigRG=LowRiskGroups[3]
    global healthRG
    if (health=="Yes"):
        healthRG=True
        if(lowRG<5):
            lowRG=lowRG+1

    finalLifeExpectancy=0

    if (not drinkRG):
        if (gender=="Male"):
            if (gramAlcohol==0):
                AlcoholTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleAlcohol4.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(AlcoholTable['Y'].loc[(AlcoholTable['X']==int(age))].values)
            elif (gramAlcohol>0 and gramAlcohol<5):
                AlcoholTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleAlcohol2.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(AlcoholTable['Y'].loc[(AlcoholTable['X']==int(age))].values)
            elif (gramAlcohol>=30):
                AlcoholTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleAlcohol3.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(AlcoholTable['Y'].loc[(AlcoholTable['X']==int(age))].values)
        elif (gender=="Female"):
            if (gramAlcohol==0):
                AlcoholTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleAlcohol3.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(AlcoholTable['Y'].loc[(AlcoholTable['X']==int(age))].values)
            elif (gramAlcohol>0 and gramAlcohol<5):
                AlcoholTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleAlcohol1.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(AlcoholTable['Y'].loc[(AlcoholTable['X']==int(age))].values)
            elif (gramAlcohol>=15 and gramAlcohol<30):
                AlcoholTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleAlcohol2.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(AlcoholTable['Y'].loc[(AlcoholTable['X']==int(age))].values)
            elif (gramAlcohol>=30):
                AlcoholTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleAlcohol4.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(AlcoholTable['Y'].loc[(AlcoholTable['X']==int(age))].values)
    
    if (not bmiRG):
        if (gender=="Male"):
            if (bmi>=25 and bmi<30):
                bmiTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleBmi2.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(bmiTable['Y'].loc[(bmiTable['X']==int(age))].values)
            elif (bmi>=30 and bmi<35):
                bmiTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleBmi3.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(bmiTable['Y'].loc[(bmiTable['X']==int(age))].values)
            elif (bmi>=35):
                bmiTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleBmi4.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(bmiTable['Y'].loc[(bmiTable['X']==int(age))].values)
        elif (gender=="Female"):
            if (bmi>=25 and bmi<30):
                bmiTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleBmi1.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(bmiTable['Y'].loc[(bmiTable['X']==int(age))].values)
            elif (bmi>=30 and bmi<35):
                bmiTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleBmi3.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(bmiTable['Y'].loc[(bmiTable['X']==int(age))].values)
            elif (bmi>=35):
                bmiTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleBmi4.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(bmiTable['Y'].loc[(bmiTable['X']==int(age))].values)

    if (not cigRG):
        if (gender=="Male"):
            if (int(cig)>0 and int(cig)<15):
                cigTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleSmoking2.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(cigTable['Y'].loc[(cigTable['X']==int(age))].values)
            elif(int(cig)>=15 and int(cig)<25):
                cigTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleSmoking3.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(cigTable['Y'].loc[(cigTable['X']==int(age))].values)
            elif(int(cig)>24):
                cigTable=pandas.read_csv("CSV_expanded/CSV expanded/MaleSmoking4.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(cigTable['Y'].loc[(cigTable['X']==int(age))].values)
        elif(gender=="Female"):
            if (int(cig)>0 and int(cig)<15):
                cigTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleSmoking2.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(cigTable['Y'].loc[(cigTable['X']==int(age))].values)
            elif(int(cig)>=15 and int(cig)<25):
                cigTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleSmoking3.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(cigTable['Y'].loc[(cigTable['X']==int(age))].values)
            elif(int(cig)>24):
                cigTable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleSmoking4.csv")
                finalLifeExpectancy=finalLifeExpectancy+float(cigTable['Y'].loc[(cigTable['X']==int(age))].values)

    yourCountry = country
    LifeExpectancyTable = pandas.read_csv("CSV_expanded/CSV expanded/LifeExpectancy.csv")
    yourLife = LifeExpectancyTable[gender].loc[(LifeExpectancyTable['Age']== int(age))].values
    predAge=1
    excel = pandas.read_excel(open('CSV_expanded/CSV expanded/'+gender+'50.xlsx', 'rb')).to_numpy()
    col1 = [item[0] for item in excel]
    col2 = [item[1] for item in excel]
    BaseUSA = [col2[i] for i in range(len(col1))if col1[i]=='UNITED STATES']
    BaseYou = [col2[i] for i in range(len(col1))if col1[i]==yourCountry]
    LSData = pandas.read_csv("CSV_expanded/CSV expanded/"+gender+"Healty"+str(lowRG)+".csv")
    LSAge = float(LSData['Y'].loc[(LSData['X']== int(age))].values)
    yourCoefficient = round((float(BaseYou[0])-50)/(float(BaseUSA[0])-50),3)
    predAge=round(float((yourLife+LSAge+finalLifeExpectancy)*yourCoefficient+int(age)),3)
    print(round(0.975 * predAge,2), 'to' , round(1.025*predAge,2))

    filteredFinalData=pandas.read_csv("CSV_expanded/CSV expanded/TheFinalData.csv")
    global LifeExpectancyvalue1
    global LifeExpectancyvalue2
    LifeExpectancyvalue1=int(0.975*predAge)
    LifeExpectancyvalue2=int(1.025*predAge)

    names=["Alcohol", "Bmi", "Smoking", "Total activity", "Expected age"]
    variables=["DR1TALCO","BMXBMI","CIGDAY", "ACTTOT", "AGEPRED"]
    xlabel=["g/dl", "Bmi", "Cig/day", "min/day", "Life expectancy"]
    you=[gramAlcohol, bmi, int(cig), act, predAge]
    bins=[30, 100, 20, 50, 10]
    plots=[]
    for i in range(len(names)):
        temp1 = filteredFinalData[variables[i]] 
        #temp1 = [temp1[i] for i in range(len(temp1))if temp1[i]>0]
       
        f, axs = plt.subplots(1, 1, figsize=(16,9) )
        axs.hist(x=temp1, bins=bins[i])
        axs.axvline(x=np.mean(temp1), color='RED')
        axs.axvline(x=you[i], color='GREEN')
        
        plt.title(names[i])
        plt.xlabel(xlabel[i])
        plt.ylabel("frequency")
        img=BytesIO()
        plt.savefig(img, format='png')
        plots.append(base64.b64encode(img.getvalue()).decode('utf8'))

    return plots

    '''pandas.options.mode.chained_assignment = None # None|'warn'|'raise'

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
    
    deathrate=(filteredDeathData['Crude Rate'][filteredDeathData['Gender']==gender][filteredDeathData['Single-Year Ages Code']==age]).to_csv(header=None, index=False).rstrip("\r\n")
    if ((weight and height)!=""):
        BMI=round((int(weight))/(((int(height)/100)*(int(height)/100))), 1)
    variables=["DR1TKCAL", "BMXBMI"]
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
            
    count = 0
    for i in temp2 :
        if i >= you[1] :
            count = count + 1
    print(you[1],':' ,  round(count/temp2.size*100, 2),'%')
    return plots
    for hel in range(1,5):

        CurveData = pandas.read_csv("CSV_expanded/CSV expanded/FemaleBmi"+str(hel)+".csv")
        Curve = CurveData.interpolate()
        Curve2 = Curve.interpolate(method ='linear', limit_direction='backward', order = 1)
        Curve2.to_csv(r'RnD/FemaleBmi'+str(hel)+'.csv', index = False)
        plt.plot(Curve2['X'], Curve2['Y'])

    plt.hist(x=temp2, bins=100)
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
    print(you,':' ,  round(count/temp2.size*100, 2),'%')
     youG = 1
    youA = 30.0
    ages = [youA-5, youA-4, youA-3, youA-2, youA-1, youA, youA+1, youA+2, youA+3, youA+4, youA+5]
     # temp = filteredFinalData.loc[(filteredFinalData['RIAGENDR']== youG) 
                                #& (filteredFinalData['RIDAGEYR'].isin(ages))]    
                                 
    if (gender=="Male"):
        if (lowRG==0):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/MaleHealty0.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
        elif (lowRG==1):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/MaleHealty1.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
        elif (lowRG==2):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/MaleHealty2.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
        elif (lowRG==3):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/MaleHealty3.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
        elif (lowRG==4):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/MaleHealty4.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
    elif(gender=="Female"):
        if (lowRG==0):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleHealty0.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
        elif (lowRG==1):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleHealty1.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
        elif (lowRG==2):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleHealty.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
        elif (lowRG==3):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleHealty.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)
        elif (lowRG==4):
            healthytable=pandas.read_csv("CSV_expanded/CSV expanded/FemaleHealty.csv")
            finalLifeExpectancy=finalLifeExpectancy+float(healthytable['Y'].loc[(healthytable['X']==int(age))].values)'''
        
if __name__ == '__main__':
   app.run(debug=True)







