import streamlit as st

def homePage() -> bool:
    st.title("Welcome to IceAlert: Ice Forecasting Application")
    st.write("This application helps you monitor and forecast ice conditions using advanced machine learning techniques.")
    st.write("Use the sidebar to navigate through different features of the application.")
    # Additional UI components can be added here
    ...
    return True