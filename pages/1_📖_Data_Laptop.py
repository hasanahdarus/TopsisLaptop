import streamlit as st
from dbmanagement import DbManagement

db = DbManagement('laptopsis.db')

def init():
    # Import tables needed
    db = DbManagement('laptopsis.db')
    data = db.get_laptop_data(for_topsis=True)

    criteria = db.get_criteria()
    criteria = criteria.set_index('criteria')

    subcrit = db.get_sub_criteria()

    return data, criteria, subcrit

def edit_data(selected_row):
    # Placeholder: Implement logic to edit the selected row in the database
    st.write(f"Editing data for row {selected_row}")
    
    # Example: You might want to use st.text_input to get updated values
    new_values = st.text_input("Enter updated values separated by commas")
    
    # Example: Replace the following line with your actual logic to update the database
    # Assuming data is a list of dictionaries
    if selected_row - 1 < len(data):
        updated_values = new_values.split(',')
        for key, value in zip(data[selected_row - 1].keys(), updated_values):
            data[selected_row - 1][key] = value

def input_data():
    # Placeholder: Implement logic to collect user input and add new data to the database
    st.write("Collecting user input for new data")
    
    # Example: You might want to use st.text_input, st.selectbox, etc.
    new_values = st.text_input("Enter new values separated by commas")
    
    # Example: Replace the following line with your actual logic to update the database
    # Assuming data is a list of dictionaries
    new_values_dict = {key: value for key, value in zip(data[0].keys(), new_values.split(','))}
    data.append(new_values_dict)

def delete_data(selected_row):
    # Placeholder: Implement logic to delete the selected row from the database
    st.write(f"Deleting data for row {selected_row}")
    
    # Example: Replace the following line with your actual logic to update the database
    # Assuming data is a list of dictionaries
    if selected_row - 1 < len(data):
        del data[selected_row - 1]

st.set_page_config(page_title="Data Laptop", page_icon="📖")
st.markdown("# Data Laptop")
st.sidebar.header("Data Laptop")

# Display the laptop data
data, criteria, subcrit = init()
st.write(data)

# Add buttons for "Edit," "Input," and "Hapus"
if st.button("Edit"):
    # Collect user input for the row to be edited
    selected_row = st.number_input("Enter the row number to edit:", min_value=1, max_value=len(data))
    edit_data(selected_row)

if st.button("Input"):
    # Collect user input for new data
    input_data()

if st.button("Hapus"):
    # Collect user input for the row to be deleted
    selected_row = st.number_input("Enter the row number to delete:", min_value=1, max_value=len(data))
    delete_data(selected_row)
