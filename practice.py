import streamlit as st

st.title("🧮 Basic Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Choose operation
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate based on operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

# Show result
st.write(f"### Result: {result}")