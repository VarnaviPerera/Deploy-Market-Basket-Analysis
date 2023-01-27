import streamlit as st
from multiapp import MultiApp

from apps import data  # import your app modules here

app = MultiApp()

# Add all your application here
#app.add_app("Classification", home.app)
app.add_app("Association", data.app)
# The main app
app.run()
