import streamlit as st
from forms.contactme import Contact_form
from pathlib import Path
import pandas as pd
from streamlit_lottie import st_lottie
import requests
import json

my_resume=Path('./assets/resume/CV.pdf')

def load_lottie(filepath: str):
  with open(filepath, 'r') as f:
    return json.load(f)


with open(my_resume,"rb") as pdf_file:
    PDFbyte=pdf_file.read()

right_arrow=load_lottie("animations/RightArrow.json")



class MainPanel:
  def __init__(self):
    st.html("<H1 class='prompt'>ABOUT ME</H1>")
    col1,col2,col3=st.columns(3,gap='medium',vertical_alignment='top')
    with col1:
      st.header("Professional Overview",anchor=False)
      st.write("""Motivated and detail-oriented third year student at C.K.Pithawala College with a
               strong foundation in Python Programming. Passionate about problem-solving, data structures,
               and software development. Currently honing skills through hands-on projects and continuous learning.
               Enthusiastic about applying knowledge to real-world applications and eager to contribute to dynamic teams in the tech industry.
               """)
    with col2:
      st.header("Personal Information",anchor=False)
      st.image(image="assets/images/harsh dave.png",width=280)
      st.write(":grey[:material/badge: Name: Harsh Dave]")
      st.write(":grey[:material/calendar_month: Date Of Birth: 5/11/2004]")
      st.write(":grey[:material/flag: Nationality: Indian]")
      st.write(":grey[:material/male: Gender: Male]")

    with col3: 
      st.header("Resume and Contact Information",anchor=False)
      st.write(":grey[:material/location_on: Surat, Gujarat]")
      st.write(":grey[:material/mail: harshdave0511@gmail.com]")
      st.write(":grey[:material/phone: +91 8160408834]")
      if st.button("Get In Touch",use_container_width=True,key='get-in-touch'):
        st.balloons()
        self.contact_form()
      st.html("<H4 style='text-align: center;'>OR</H4>")
      st.download_button(label=":material/download: DOWNLOAD CV",
                               data=PDFbyte,
                               file_name=my_resume.name,
                               mime="application/octet-stream",use_container_width=True,
                               key='resume-download-button')
      
  def Education(self):
    st.header(":grey[Education]",anchor=False,divider='grey')
    with st.container(border=True):
      st.write("- :blue[10th, J.H.AMBANI SCHOOL(2021)]")
      st.write("- :blue[12th, RIVER DALE SCHOOL(2023)]")
      st.write("- :blue[B.E in Computer Engineering, C.K. Pithawala(Ongoing)]")
    
  def ExtraCurricular(self):
    st.header(":grey[EXTRA-CURRICULAR ACTIVITIES]",anchor=False,divider='grey')
    with st.container(border=True):
      st.subheader(":orange[Sports Secretary, C.K. Pithawala College]",anchor=False,divider='orange')
      c1,c2=st.columns(2,gap='medium',vertical_alignment ='center')
      with c2:
        st.write("- :orange[Organized and managed college sports events and tournaments.]")
        st.write("- :orange[Led a team to promote student participation in athletics.]")
        st.write("- :orange[Coordinated with faculty and external organizations for event planning.]")
      with c1:
        st_lottie(right_arrow,loop=True,speed=1)


  def skills(self):
    st.header(":grey[SKILLS]",anchor=False,divider='grey')
    with st.container(border=True):
      st.subheader(":orange[Technical Skills]",anchor=False,divider='orange')
      c1,c2=st.columns(2,gap='medium',vertical_alignment='center')
      with c2:
        st.write("- :orange[Programming Languages: Python,C,.NET]")
        st.write("- :orange[Frameworks: Pandas,NumPy,Matplotlib,scikit-learn,seaborn]")
        st.write("- :orange[Microsoft Applications: Microsoft PowerPoint, Microsoft Excel, Microsoft Word]")
      with c1:
        st_lottie(right_arrow,loop=True,speed=1)
    with st.container(border=True):
      st.subheader(":orange[Soft Skills]",anchor=False,divider='orange')
      c1,c2=st.columns(2,gap='medium',vertical_alignment='center')
      with c2:
        st.write("- :orange[Communication Skills]")
        st.write("- :orange[Teamwork and Collaboration]")
        st.write("- :orange[Adaptability and Problem-Solving Skills]")
        st.write("- :orange[Creativity and Innovation]")
        st.write("- :orange[Patience and Perseverance]")
      with c1:
        st_lottie(right_arrow,loop=True,speed=1)


  def languages(self):
    st.header(":grey[languages]",anchor=False,divider='grey')
    with st.container(border=True):
      c1,c2=st.columns(2,gap='medium',vertical_alignment='center')
      with c2:
        st.write("- :orange[English]")
        st.write("- :orange[Hindi]")
        st.write("- :orange[Gujarati]")
      with c1:
        st_lottie(right_arrow,loop=True,speed=1)
  
  def SocialHandles(self):
    st.html("<H1 style='text-align: center;'>STAY IN TOUCH<H1>")
    c1,c2=st.columns(2,gap='medium',vertical_alignment='center')
    with c1:
      st.link_button("LINKEDIN",url="https://www.linkedin.com/in/harsh0511/",type='secondary',use_container_width=True)
    with c2:
      st.link_button("INSTAGRAM",url="https://www.instagram.com/harshhdavee/",type='secondary',use_container_width=True)

  @st.dialog(title='contact me')
  def contact_form(self):
    Contact_form()

MP=MainPanel()
MP.Education()
MP.ExtraCurricular()
MP.skills()
MP.languages()
MP.SocialHandles()