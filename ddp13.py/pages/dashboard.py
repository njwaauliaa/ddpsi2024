import streamlit as st 

st.title("INI HALAMAN DASHBOARD!")
st.session_state['Nabung']

jumlah = 0
for session in st.session_state['Nabung']:
   jumlah += session['Nominal'] 
   
st.write("Total nominal menabung sebesar", jumlah)