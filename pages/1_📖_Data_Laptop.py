import pickle
from pathlib import Path
import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
from topsis import Topsis
from dbmanagement import DbManagement
db = DbManagement('laptopsis.db')

def init():
    #Import tabel-tabel yang diperlukan
    db = DbManagement('laptopsis.db')
    data =  db.get_laptop_data(for_topsis=True)

    criteria = db.get_criteria()
    criteria = criteria.set_index('criteria')

    subcrit = db.get_sub_criteria()

    return data, criteria, subcrit

st.set_page_config(page_title="Data Laptop", page_icon="📖")
st.markdown("# Data Laptop")
st.sidebar.header("Data Laptop")

st.write("""
    ## Rekomendasi laptop berdasarkan input user menggunakan TOPSIS

    Di bawah adalah daftar laptop yang tersedia      
    """)


data, criteria, subcrit = init()
st.write(db.get_laptop_data())

# db = DbManagement('laptopsis.db')
data_categorization = db.read_categorization()

st.set_page_config(page_title='DATA CATEGORIZATION', page_icon= "📓")
st.markdown("# DATA CATEGORIZATION")

id = []
specification= []
criteria = []
class = []
for data in data_categorization:
    data_id = data[2]
    data_specification = data[0]
    data_criteria = data[3]
    data_class = data[3]

    names.append(data_names)
    usernames.append(data_usernames)
    passwords.append(data_passwords)
    class.append(data_class)
    
    st.subheader("BACA DATA CATEGORIZATION")
    read_data_categorization = pd.DataFrame(data_categorization,columns=["id","specification","criteria", "class"])
    st.write(read_data_categorization)
