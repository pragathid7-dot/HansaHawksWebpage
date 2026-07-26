import streamlit as st

st.set_page_config(
    page_title="SALT CITY CHAMPIONSHIP",
    page_icon=":cricket_game:",
    layout="wide"
)

# Centered Header
st.markdown(
    """
    <h1 style='text-align: center;'>
    SALT CITY CHAMPIONSHIP
    </h1>
    """,
    unsafe_allow_html=True
)

# Subtitle
st.markdown(
    """
    <h3 style='text-align: center;'>
    Match Verification Platform
    </h3>
    """,
    unsafe_allow_html=True
)

# Text
st.write("Hello! This website is created to verify matches.")
