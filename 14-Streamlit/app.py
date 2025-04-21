import streamlit as st
import pandas as pd
import numpy as np

##Tile of the application
st.title("Hello Streamlit")

##Display Simple test
st.write ("This is a sample text")

##Create simple Dataframe
df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column': [10 , 20 , 30 , 40]

})
##Simple DataFrame
st.write("Here is the dataframe")
st.write(df)

#create line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c',]
)
st.line_chart(chart_data)