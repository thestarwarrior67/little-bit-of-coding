import streamlit as st

st.title("unitconverter")
st.write("converts weight, length, temperature in seconds!")

#sidebar

category = st.sidebar.selectbox("Select a category", ["Weight", "Length", "Temperature"]) 

#weight conversion

if category == "Weight":
    st.header("Weight Conversion")
    weight_value = st.number_input("Enter weight:", min_value=0.0)
    weight_from = st.selectbox("Convert from:", ["Kilograms", "Pounds", "grams"])
    weight_to = st.selectbox("Convert to:", ["Kilograms", "Pounds", "grams"])
    if st.button("Convert weight"):
        if weight_from == "Kilograms":
            kg_value = weight_value
        elif weight_from == "grams":
            kg_value = weight_value / 1000
        elif weight_from == "Pounds":
            kg_value = weight_value / 2.20462

            #convert to target unit

        if weight_to == "Kilograms":
            result = kg_value
        elif weight_to == "grams":
            result = kg_value * 1000
        elif weight_to == "Pounds":
            result = kg_value * 2.20462
        st.write(f"Result: {result} {weight_to}")

        