import streamlit as st
from st_pages import add_page_title, get_nav_from_toml
from st_pages import hide_pages


st.set_page_config(layout="wide")

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

# If you want to use the no-sections version, this
# defaults to looking in .streamlit/pages.toml, so you can
# just call `get_nav_from_toml()`
nav = get_nav_from_toml(
    ".streamlit/pages_sections.toml" if sections else ".streamlit/pages.toml"
)

st.logo("logo.png")

pg = st.navigation(nav)

add_page_title(pg)
pg.run()
