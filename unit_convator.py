# Project 01: Unit Convertor
# Build a Google Unit Convertor using Python and Streamlit:


import streamlit as st
st.markdown(
    """
    <style>
    body {
        background-color:rgb(17, 37, 77);
        color:white;
    }
    .stApp{
        background: linear-gradient(135deg, #00feba, #5b548a);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1{
        text-align:center;
        font-size:36px;
        color:white;
    }
    .stButton{
        background:linear-gradient(45deg, #0b5384, #351c75);
        color:white;
        font-size:18px;
        padding:10px 20px;
        border-radius:10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg,  #92fe9d, #00c9ff);
        color:black;
    }
    .result-box{
        font-size: 20px
        font-wight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1)
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1> Unit Convertor using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# SideBar
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", min_value=0.0, value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Yard", "Inches", "Foot", "Mile"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Meter", "Kilometer", "Centimeter", "Millimeter", "Micrometer", "Nanometer", "Yard", "Inches", "Foot", "Mile"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit", ["Kilogram", "Gram", "Milligram", "Microgram", "Pound", "Ounce"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Kilogram", "Gram", "Milligram", "Microgram", "Pound", "Ounce"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Logic
def length_convertor(value, from_unit, to_unit):
    length_units = {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Micrometer": 0.000001,
        "Nanometer": 0.000000001,
        "Yard": 0.9144,
        "Inches": 0.0254,
        "Foot": 0.3048,
        "Mile": 1609.34,
    }
    return (value * length_units[from_unit]) / length_units[to_unit]


def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Microgram": 0.000000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit": 
        return (value - 273.15) * 9/5 + 32
    else:
        return value
    
# Conversion
if st.button("👍Convert"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_convertor(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Created with ❤️ Arsalan Maniar</div>", unsafe_allow_html=True)
