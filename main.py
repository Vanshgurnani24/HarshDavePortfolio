import streamlit as st
import pathlib


def load_css(css_file: str):
  with open(css_file, 'r') as f:
    st.html(f'<style>{f.read()}</style>')

# Load custom CSS
css_file=pathlib.Path("assets/style.css")
load_css(css_file)


AboutMe=st.Page(
  page="others/about.py",
  title='About Me',
  icon=":material/account_circle:",
  default=True
)
RentRight=st.Page(
  page="others/RMS.py",
  title="Rent Right",
  icon=":material/home:",
)


pg=st.navigation(
  {
    "About Me":[AboutMe],
    "Projects":[RentRight],
  }
)
st.sidebar.text("Programmed with ♥ by Vansh")
pg.run()