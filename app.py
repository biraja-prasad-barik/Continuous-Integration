import streamlit as st

#streamlit UI
st.title("Power calculator")
st.write("Enter a number to calculate its square , cube and fifth power")

#Get user input 
n=st.number_input("Enter an integer", value=1,step=1)

#Calculate results
square=n**2
cube=n**3
fifth_power=n**5

#display results
st.write(f"the square of {n} is : {square}")
st.write (f"the cube of {n} is : {cube}")
st.write(f"the fifth power of {n} is :{fifth_power}")