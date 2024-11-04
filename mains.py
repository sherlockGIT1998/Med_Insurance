from flask import Flask,render_template,request

from utils import MedicalInsurance

app = Flask(__name__)

@app.route('/')

def hello_flask():
    print('Medical Insurance Prediction')
    return render_template('index.html')

@app.route('/predict_charges',methods=['POST','GET'])

def get_predicted_charges():
    
    if request.method == 'GET':
        
        print('GET Method')
        
        data = request.form 
        age = eval(data[age])
        sex = data[sex]
        bmi = eval(data[bmi])
        children = eval(data[children])
        smoker = data[smoker]
        region = data[region]
        
        species = MedicalInsurance(age,sex,bmi,children,smoker,region)
        
        predict = species.get_predicted_charges()
        
        return f'Charges is : {round(predict,2)} /-'
    
print('__name__ :',__name__)

if __name__ == '__main__':
    
    app.run()
    
    