import streamlit as st
import joblib

model = joblib.load('regression.joblib')

# size, number of bedrooms and whether a house has a garden

size = st.number_input(label="bedroom size",min_value=0,value=0)
nOfrooms = st.number_input(label="number of bedroom",min_value=0 ,value=0)
hasGarden = st.number_input(label="has garden",value=0,min_value=0,max_value=1)

res = model.predict([[size, nOfrooms, hasGarden]])

st.write(res)