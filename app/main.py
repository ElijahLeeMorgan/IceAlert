import streamlit as st
from logging import basicConfig, getLogger, INFO

from UI.home import homePage

# Set up logging
basicConfig(level=INFO)
log = getLogger(__name__)

# Streamlit page configuration
st.set_page_config(
    page_title="IceAlert - Ice Forecasting",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main app logic
log.info("Running IceAlert: Ice Forecasting Application...")
homePage()
