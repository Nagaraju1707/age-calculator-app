import streamlit as st
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

# Page config
st.set_page_config(
    page_title="Smart Age Calculator",
    page_icon="🎂",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #667eea, #764ba2);
    }
    .stApp {
        background-color: #f4f6f9;
    }
    .title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #4A4A4A;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🎉 Smart Age Calculator</p>', unsafe_allow_html=True)
st.write("Enter your birth date and discover your exact age!")

dob = st.date_input(
    "Select your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if dob:
    now = datetime.now()
    birth = datetime.combine(dob, datetime.min.time())

    diff = relativedelta(now, birth)

    total_seconds = int((now - birth).total_seconds())
    total_minutes = total_seconds // 60
    total_hours = total_seconds // 3600

    st.success("Here is your Age:")

    st.markdown(f"""
    ### 📅 {diff.years} Years, {diff.months} Months, {diff.days} Days
    ### ⏰ {total_hours:,} Hours
    ### ⏱ {total_minutes:,} Minutes
    ### ⌛ {total_seconds:,} Seconds
    """)