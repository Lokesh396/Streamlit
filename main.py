import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Streamlit application')
st.write("Hello Everyone")

data=pd.read_csv('modified.csv')

sns.scatter(data.Hobbyist,data.Age)

