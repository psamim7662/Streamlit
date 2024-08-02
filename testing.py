import streamlit as st
st.markdown("#Streamlit:red[Tutorial]")
st.markdown("Here are some of the most used database:")
db_list=["Oracle DB","My SQL","PostgreSQL"]

if st.button("show",type="primary"):
    st.write(db_list)
st.title("welcome")