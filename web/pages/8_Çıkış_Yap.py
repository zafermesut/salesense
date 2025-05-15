import streamlit as st
import pandas as pd
import analysis as an
from authenticate import logout
from streamlit_extras.switch_page_button import switch_page




logout()
switch_page("login")