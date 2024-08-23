import streamlit as st
import pickle

st.title("🎈 car co2 emssion")
f1=st.number_input('feature_1',min_value=1,max_value=10)
f2=st.number_input('feature_2',min_value=1,max_value=10)
f3=st.number_input('feature_3',min_value=1,max_value=10)
image = Image.open('path_to_your_image.jpg')
st.sidebar.image(image, caption="Sample Image")
with open('model.pkl','rb')as file:
  model=pickle.load(file)
res=model.predict([[f1,f2,f3]])
st.write(res[0][0])
  
