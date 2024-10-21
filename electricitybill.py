import streamlit as st 
def calculate_electricity_bill(units):
    fixed_charge = 0
    if units > 500:
        fixed_charge = 100
    elif units > 0:
        fixed_charge = 50
    if units <= 100:
        return fixed_charge  
    elif units <= 200:
        bill = (units - 100) * 3.50
    elif units <= 500:
        bill = (100 * 3.50) + (units - 200) * 4.60
    else:
        bill = (100 * 3.50) + (300 * 4.60) + (units - 500) * 6.60
    
    total_bill = bill + fixed_charge
    return total_bill

st.title("Electricity Bill Generator")
st.header("Explanation :")
st.write("Free units: The first 100 units are free.")
st.write ("101-200 units: Billed at ₹3.50 per unit.")
st.write("201-500 units: Billed at ₹4.60 per unit.")
st.write("Above 500 units: Billed at ₹6.60 per unit.")
st.write("Fixed charge: ₹50 for consumption below 500 units, and ₹100 for consumption above 500 units.")
units_consumed = st.number_input("Enter the number of units consumed:", min_value=0)
if units_consumed:
    total_bill = calculate_electricity_bill(units_consumed)
    st.write(f"Your total electricity bill is: ₹{total_bill}")