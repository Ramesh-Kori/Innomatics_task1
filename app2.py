import streamlit as st 
st.title(":red[Innomatics] Data App :sunglasses:")

st.header("Data Science Internship")

st.subheader("Feb 2023")

CODE = '''print("Hello world")'''

st.code(CODE, language="python")
st.snow()

btn_click = st.button("Click Me!")
st.write(btn_click)

if btn_click == True:
    st.subheader("You clicked me :joy:")
    st.balloons()
    github="https://github.com/Ramesh-Kori"
    var1=st.write("Github Link: {}".format(github))
