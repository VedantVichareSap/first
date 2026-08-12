import streamlit as st
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

st.set_page_config(page_title="Calculator", page_icon="🧮")
st.title("Calculator")

col1, col2, col3 = st.columns(3)
with col1:
    num1 = st.number_input("First number", value=0.0, format="%g")
with col2:
    op = st.selectbox("Operator", ["+", "-", "*", "/"])
with col3:
    num2 = st.number_input("Second number", value=0.0, format="%g")

if st.button("Calculate", use_container_width=True):
    try:
        ops = {"+": add, "-": subtract, "*": multiply, "/": divide}
        result = ops[op](num1, num2)
        st.success(f"**Result:** {num1} {op} {num2} = **{result}**")
    except ValueError as e:
        st.error(str(e))
