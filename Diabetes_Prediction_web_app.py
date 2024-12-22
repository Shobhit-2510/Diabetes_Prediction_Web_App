import numpy as np
import pickle
import streamlit as st

# Update the model file path for your environment
#filename = 'C:/Users/sshob/Downloads/trained_model.sav'
filename = 'trained_model.sav'


# loading the saved model
loaded_model = pickle.load(open(filename, 'rb'))

def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Prediction
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    st.title('Diabetes Prediction Web App')
    
    # Getting the input data from the user
    Pregnancies = st.text_input('No of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('Body Mass Index')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of Person')
    
    # Validate the inputs and ensure they are numbers
    try:
        input_data = [
            float(Pregnancies),
            float(Glucose),
            float(BloodPressure),
            float(SkinThickness),
            float(Insulin),
            float(BMI),
            float(DiabetesPedigreeFunction),
            float(Age)
        ]
    except ValueError:
        st.error("Please enter valid numerical values.")
        return

    # Code for Prediction
    diagnosis = ''
    
    if st.button('Diabetes test prediction'):
        diagnosis = diabetes_prediction(input_data)
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()
