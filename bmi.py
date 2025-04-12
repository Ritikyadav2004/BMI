import streamlit as st
import pandas as pd
import time
# MAIN TITLE
st.title("BMI Calculator") #
# SLIDER FOR USER INPUT
height = st.slider("Enter Your Height (in cm)",100,250,175)
weight = st.slider("Enter Your Weight (in kg)",40,200,75)
# CALCULATION PART
bmi = weight/((height/100)**2)
#CHECKING WHETHER CLICK OR NOT
button1 = st.button("Click Me")

# SOME FANCY THINGS
if(button1):
    with st.spinner("In Progress..."):
        time.sleep(1)
        st.success("Done",icon="✅")
    st.write(f"### Your BMI is {bmi:.2f} ###")
    if(bmi<18.5):
        st.write("Take a Protein Rich Diet")
    elif(18.5<=bmi<=24.9):
        st.snow()
        st.success("Keep it up and Maintain Your Spirit",icon="🔥")
    elif(25<=bmi< 29.9):
        st.warning("You are Overweight, Do Physical Activity",icon="⚠️")
    else:
        st.error("You are Overweight, Do Physical Activity",icon="🚨")

# DESCRIPTION ABOUT BMI
st.write("### BMI Categories ###")
st.write("- Underweight : BMI less than 18.5 ")
st.write("- Normal Weight : BMI between 18.5 and 24.9")
st.write("- Overweight : BMI between 25 and 29.9")
st.write("- Obesity : BMI 30 or greater")
st.markdown("Thanks for Visiting my BMI Calculator App")