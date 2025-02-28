# -*- coding: utf-8 -*-
"""calculator app .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F6Z-7qIK47g0VTU_jRkiAvMwN4NZtA2_
"""

import streamlit as st

st.title("Simple Calculator")

st.write("Enter two numbers and select an operator to perform a calculation.")

num1 = st.number_input("enter first number", value=0.0)
num2 = st.number_input("enter second number", value=0.0)

operator = st.selectbox("select an operator", ("+", "-", "*", "/"))

if st.button("Calculate"):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Division by zero error"


st.write(f"Result:", result)

st.markdown("Developed by David Olusomidomo")





