
import numpy as np
import pandas as pd
import joblib
import streamlit as st 
from PIL import Image

# model = joblib.load('classifier.joblib')

image = Image.open('dollar.png')
st.image(image.resize((1000, 300)))
# st.image(image, caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="auto")

# new_image = image.resize((1000, 300))
# st.image(new_image)

# Display image on Streamlit app with custom height
#st.image(image, use_column_width=True, height=50)

def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = model.predict([[variance, skewness, curtosis, entropy]])
    return prediction

def main():
    st.title("Banknote Authentication Classifier")
    variance = st.text_input("variance", placeholder="Type Here")
    skewness = st.text_input("skewness", placeholder="Type Here")
    curtosis = st.text_input("curtosis", placeholder="Type Here")
    entropy = st.text_input("entropy", placeholder="Type Here")

    if st.button("Get Prediction"):
        output = predict_note_authentication(variance, skewness, curtosis, entropy)
        st.success(f'Result: {output}.')
        st.write('0 = banknote is forged')
        st.write('1 = banknote is genuine')

   # if st.button("About"):
        # st.text("SRM - 3rd SEM Internship Project")
        # st.text("Built by Suraj R. Yadav")

if __name__ == '__main__':
    main()
