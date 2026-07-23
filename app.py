import streamlit as st
import pandas as pd
import numpy as np
st.title("My First Streamlit App")
st.write("Hello Aryan")
st.text("Lets Start")
name = st.text_input("Enter name: ")
if st.button("Greet"):
    st.success(f"Hello, {name}!")
