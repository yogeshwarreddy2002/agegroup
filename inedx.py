import streamlit as st
st.title("🕒User Age Group Filter")
f=st.sidebar
with f:
    i=st.radio("choose your age option",("1-25","26-51","52-75","76-100")) 
if i=="1-25":
     users = [
     # 1–25
     {"name": "Aarav", "age": 18, "gender": "Male", "age_group": "1-25"},
     {"name": "Priya", "age": 22, "gender": "Female", "age_group": "1-25"},
     {"name": "Rahul", "age": 24, "gender": "Male", "age_group": "1-25"},
     {"name": "Sneha", "age": 19, "gender": "Female", "age_group": "1-25"},
     {"name": "Kiran", "age": 25, "gender": "Male", "age_group": "1-25"},
     ]
     st.table(users)  

if i=="26-51":
    users = [
    {"name": "Vikram", "age": 30, "gender": "Male", "age_group": "26-50"},
    {"name": "Meera", "age": 35, "gender": "Female", "age_group": "26-50"},
    {"name": "Raj", "age": 40, "gender": "Male", "age_group": "26-50"},
    {"name": "Pooja", "age": 45, "gender": "Female", "age_group": "26-50"},
    {"name": "Amit", "age": 50, "gender": "Male", "age_group": "26-50"},
    ]
    st.dataframe(users)
if i=="52-75":    
    users = [
    {"name": "Karthik", "age": 55, "gender": "Male", "age_group": "51-75"},
    {"name": "Anjali", "age": 60, "gender": "Female", "age_group": "51-75"},
    {"name": "Rajesh", "age": 65, "gender": "Male", "age_group": "51-75"},
    {"name": "Lakshmi", "age": 70, "gender": "Female", "age_group": "51-75"},
    {"name": "Sundar", "age": 75, "gender": "Male", "age_group": "51-75"},
    ]
    st.dataframe(users)
if i=="76-100":    
    users = [
    {"name": "Suresh", "age": 80, "gender": "Male", "age_group": "76-100"},
    {"name": "Kamala", "age": 85, "gender": "Female", "age_group": "76-100"},
    {"name": "Mohan", "age": 90, "gender": "Male", "age_group": "76-100"},
    {"name": "Leela", "age": 95, "gender": "Female", "age_group": "76-100"},
    {"name": "Raman", "age": 100, "gender": "Male", "age_group":"76-100"},
  ]
    st.dataframe(users)

  


