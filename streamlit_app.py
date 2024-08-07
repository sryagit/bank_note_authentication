import numpy as np
import pandas as pd
import joblib
import streamlit as st
from PIL import Image

model = joblib.load('classifier.joblib')

image = Image.open('dollar.png')
st.image(image.resize((1000, 300)))

def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    return prediction

def main():
    st.title("Bank Note Authentication Web APP")
    variance = st.text_input("Variance", placeholder="Type Here")
    skewness = st.text_input("Skewness", placeholder="Type Here")
    curtosis = st.text_input("Curtosis", placeholder="Type Here")
    entropy = st.text_input("Entropy", placeholder="Type Here")

    if st.button("Get Prediction"):
        output = predict_note_authentication(variance, skewness, curtosis, entropy)
        st.session_state['prediction'] = output

    if 'prediction' in st.session_state:
        if st.session_state['prediction'] == 0:
            st.markdown("<h3>Result :<span style='color:red'> 0 </span></h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3>Result :<span style='color:LawnGreen'> 1 </span></h3>", unsafe_allow_html=True)
            
        st.markdown("<h5 style='color:red'> 0<span style='color:white'> =</span> banknote is forged</h5>", unsafe_allow_html=True)
        st.markdown("<h5 style='color:LawnGreen'> 1<span  style='color:White'> =</span> banknote is genuine</h5>", unsafe_allow_html=True)
        
    if st.button("About"):
        st.text("Classifier : Random Forest")
        st.text("Accuracy : 99.27 %")
        st.text("Built by : Suraj R. Yadav")

if __name__ == '__main__':
    main()
