import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__, template_folder='templates')
model = load('hms.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/bmi.html')
def bmi():
    return render_template('bmi.html')

@app.route('/checkup.html',methods=['POST','GET'])
def checkup():
    '''
    For rendering results on HTML GUI
    '''
    if request.method == 'POST':
     x_test = [[int(x) for x in request.form.values()]]
     print(x_test)
     prediction = model.predict(x_test)
     print(prediction)
     output=prediction[0]
     if(output == 0):
         text = "Patient is healthy. No medications are required.But we would recomend you to control your alcohol consumption and smoking habits if any. Stay Safe, we care for you!"
     elif(output == 1):
         text = "Patient is not completely healthy. Needs to take care of his/her diet. If any symptom persists after 3-4 days, consult a Doctor. Also consumption of alcohol and smoking habits should not be entertained. Stay Safe, we care for you! "
     elif(output == 2):
         text = "Patient is sick! He/She needs immediate medical attention. We recommend you to consult a doctor as soon as possible. Also consumption of alcohol and smoking habits should not be entertained. Stay Safe, we care for you!"
     
     return render_template('checkup.html', prediction_text='Level {}'.format(output), medic=format(text))
    else:
        return render_template('checkup.html')


if __name__ == "__main__":
    app.run(debug=True)
