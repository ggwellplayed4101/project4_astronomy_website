import streamlit
from backend import astronomy_info_provider

heading, description = astronomy_info_provider()

streamlit.title(heading)

streamlit.image("image.jpg")

streamlit.write(description)