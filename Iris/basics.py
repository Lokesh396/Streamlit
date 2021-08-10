import streamlit as st
import pandas as pd
import numpy as np

data={
        'a':[1,2,3],
        'b':[4,5,6],
        'c':[7,8,9]
    }
data=pd.DataFrame(data)
#data


if st.checkbox('check box'):
    data={
        'a':[1,2,3],
        'b':[4,5,6],
        'c':[7,8,9]
    }
    data=pd.DataFrame(data)
    data

st.slider('slider',1,24,12)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

st.selectbox('selectbox',np.arange(10,30))

option=st.selectbox('choose',data.a)
' selected value is' ,   option 

st.write('[Google](www.google.in)')