import streamlit as st

st.write("Hello guys. How are you today?")
st.write("How do I stop this session")

st.write('try again')
st.write('kita cuba')

#Text Formatting
st.header('This is header')
st.header('This is sub header')
st.caption('this is caption')

st.markdown('*Streamlit* is **really** ***cool***')

st.markdown(''' :red[Streamlit] :orange[Streamlit] :green[Streamlit]''')
st.markdown("Here's a bouduet &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("good")
st.warning('bad')
st.info('info')
st.error('Error')

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;"> This is advanced font manipulation!</p>'
st.markdown(new_title, unsafe_allow_html=True) 

#selection BOX
st.selectbox("Kuala Lumpur is located at",['Malaysia', 'Thailand', 'UK'])
st.multiselect("Select 2 states",['Selangor','Johor','Kedah'])

#Button
st.button("Click Here to Proceed")
st.slider("Select the length of stay", 1,10, value=3)

#Input Box
number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write("The current number is ", number)

#Insert Graphic
from PIL import Image 
im = Image.open('shrdc_logo.png')
st.image(im, width=500)

#Data Frame
import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

#Bar Chart
st.bar_chart(df, x="Location", y="Income")

#Line Chart
st.line_chart(df, x="Household", y="Income")

#Scatter Chart
st.scatter_chart(df, x="Household", y="Income")

#Creating Multiple Page
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
 st.header("A cat")
 st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
 st.header("An owl")
 st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

#Create Multi Column
col1, col2, col3 = st.columns(3)
with col1:
 st.slider("Select the length of stay", 1,5, value=3)
 st.header("A cat")
 st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
 st.header("A dog")
 st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
 st.header("An owl")
 st.image("https://static.streamlit.io/examples/owl.jpg")




