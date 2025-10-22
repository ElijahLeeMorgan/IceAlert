import streamlit as st
import pandas as pd
import numpy as np
import pytorch as torch
from logging import basicConfig, getLogger, INFO

from UI.home import homePage

# Set up logging
basicConfig(level=INFO)
log = getLogger(__name__)

if __name__ == "__main__":
    log.info("Initializing IceAlert: Ice Forecasting Application...")
    # Launch streamlit app
    if homePage():
        log.error("Home page failed to load, exiting application...")
        exit(1)
    log.info("Closing IceAlert...")
    exit(0)
