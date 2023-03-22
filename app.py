import streamlit as st
import machine_learning as ml
import feature_extraction as fe
from bs4 import BeautifulSoup
import requests as me
import matplotlib.pyplot as plt
import re
from multiapp import MultiApp
from apps import data,prevent # import your app modules here


# col1, col2 = st.columns([1, 3])
st.title('JT Hunters')
st.header('Phishing Website Detection using Machine Learning')


with st.expander('EXAMPLE PHISHING URLs:'):
    st.write('_https://rtyu38.godaddysites.com/_')
    st.write('_https://karafuru.invite-mint.com/_')
    st.write('_https://defi-ned.top/h5/#/_')
    st.caption('REMEMBER, PHISHING WEB PAGES HAVE SHORT LIFECYCLE! SO, THE EXAMPLES SHOULD BE UPDATED!')
st.subheader('here we use "Random forest" ML model ')


model = ml.rf_model


url = st.text_input('Enter the URL')

# check the url is valid or not
if st.button('Check!'):
    try:
        response = me.get(url, verify=False, timeout=4)
        if response.status_code != 200:
            print(". HTTP connection was not successful for the URL: ", url)
        else:
            soup = BeautifulSoup(response.content, "html.parser")
            vector = [fe.create_vector(soup)]  # it should be 2d array, so I added []
            result = model.predict(vector)
            if result[0] == 0:
                st.success("This web page seems a legitimate!")
                st.balloons()
            else:
                st.warning("Attention! This web page is a potential PHISHING!")
                st.snow()

    except me.exceptions.RequestException as e:
        print("--> ", e)



app = MultiApp()


# Add all your application here

app.add_app("STORIES & EXAMPLES", data.app)
app.add_app("how to prevent phising", prevent.app)
# The main app
app.run()




