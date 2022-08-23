import streamlit as st
from multiapp import MultiApp
from apps import home_page, first_map, second_map  # import your app modules here

app = MultiApp()

st.markdown("""
# Boring Pika.Inc
 ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩ ϞϞ(๑⚈ ․̫ ⚈๑)∩
""")

# Add all your application here
app.add_app("HOME", home_page.app)
app.add_app("FIRST MAP", first_map.app)
app.add_app("SECOND MAP", second_map.app)



# The main app
app.run()