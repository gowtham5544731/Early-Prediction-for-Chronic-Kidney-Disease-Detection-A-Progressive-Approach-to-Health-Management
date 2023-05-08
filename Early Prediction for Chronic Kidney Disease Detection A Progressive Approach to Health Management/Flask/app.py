#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pickle
pickle.dump(lgr,open('CKD.pkl','wb'))
from flask import Flask, render_template, request
import numpy as np
import pickle
app = Flask(_name_)
model = pickle.load(open('CKD.pkl','rb'))
app.route('/')
def home():
    return render_template('home.html')
app.route('/prediction',methods=['POST','GET'])

def prediction():
    return render_template('indexnew','html')
app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_teplate('home.html')
app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in requrest.form.values()]  
    features_value = [np.array(input_features)]
    
    features_name = ['blood_urea', 'blood glouse random', 'anemia',
        'coronary_artery_disease', 'pus_cell', 'red_blood_cells',
        'diabetemellitus', 'pedal_edema']
    df = pd.DataFrame(features_values, columns=features_name)
    
    output = model.predict(df) 
    return render_template('result.html', prediction_text=output)
if _name_ == '_main_':
    app.run(debug=True)


# In[ ]:




