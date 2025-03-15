import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"meters": 1, "kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084},
        "Weight": {"grams": 1, "kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
        "Temperature": {"celsius": "C", "fahrenheit": "F", "kelvin": "K"},
        "Speed": {"meters/sec": 1, "km/hour": 3.6, "miles/hour": 2.23694}
    }
    
    if category in ["Length", "Weight", "Speed"]:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])
    elif category == "Temperature":
        if from_unit == "celsius" and to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "celsius" and to_unit == "kelvin":
            return value + 273.15
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            return (value - 32) * 5/9
        elif from_unit == "fahrenheit" and to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin" and to_unit == "celsius":
            return value - 273.15
        elif from_unit == "kelvin" and to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # No conversion needed
    return None

# Streamlit UI
st.set_page_config(page_title="Google Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Google Unit Converter")
st.write("Convert between different units easily and accurately.")

categories = ["Length", "Weight", "Temperature", "Speed"]
category = st.selectbox("Select Conversion Category", categories)

unit_options = {
    "Length": ["meters", "kilometers", "miles", "feet"],
    "Weight": ["grams", "kilograms", "pounds", "ounces"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Speed": ["meters/sec", "km/hour", "miles/hour"]
}

from_unit = st.selectbox("From Unit", unit_options[category])
to_unit = st.selectbox("To Unit", unit_options[category])
value = st.number_input("Enter Value", min_value=0.0, format="%.6f")

if st.button("Convert"):
    if from_unit != to_unit:
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"{value} {from_unit} = {result:.6f} {to_unit}")
    else:
        st.warning("Please select different units for conversion.")
