import streamlit as st
from multipage import MultiPage
import uploads
import entrance
import info



from multipage import MultiPage

app = MultiPage()


# Add all your applications (pages) here
app.add_page('entrance page',entrance.app)
app.add_page("Upload Data", uploads.app)
app.add_page("Info", info.app)


# The main app
app.run()


