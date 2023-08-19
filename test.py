import streamlit as st
import time
from PIL import Image
tab1, tab2,tab3 = st.tabs(["Home", "About","Contact us"])
tab1.markdown("<h1 style='text-align: center; color: grey;'>KIITEE 2023</h1>", unsafe_allow_html=True)
tab1.write("this is tab 1")
tab2.write("this is tab 2")
tab3.image('./pp.jpg')
with st.sidebar:
    st.image('./log.png',width=200)
    url = 'http://kiit.ac.in'
    st.markdown(f'''<a href={url}><button style="background-color:grey;">Home Page</button></a>''',unsafe_allow_html=True)
    ur = 'http://admission.kiit.ac.in'
    st.markdown(f'''<a href={ur}><button style="background-color:grey;">Admissions</button></a>''',unsafe_allow_html=True)
    u = 'https://kiit.ac.in/academics/'
    st.markdown(f'''<a href={u}><button style="background-color:grey;"></button></a>''',unsafe_allow_html=True)
    
query =tab1.text_input("enter your query")
tab1.write("my name is sheetal")