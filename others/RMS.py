import streamlit as st
from pathlib import Path
import json
from streamlit_lottie import st_lottie

project_file = Path("./Projects/RMS Project.zip")



def load_lottie(filepath: str):
  with open(filepath, 'r') as f:
    return json.load(f)



with open(project_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()

LeftArrow=load_lottie("animations/LeftArrow.json")
LeftArrow2=load_lottie("animations/LeftArrow2.json")


class RentRight:
    def __init__(self):
        st.header("About Project :material/tactic:",divider='red',anchor=False)
        col1,col2=st.columns(2,gap='medium',vertical_alignment='center')
        with col1:
            st.write("""
            A user-friendly rental platform with smart pricing that works well for both renters and property owners. Added a map for easy property search and quick links to improve navigation. Made sure documents are handled securely and kept private, using token confirmations to protect personal info.
            """)
        with col2:
            st.subheader(":green[This project has been developed and is free to use and modify as per your needs.:material/thumb_up:]",anchor=False)
            st.download_button(
            label=":material/download: DOWNLOAD PROJECT FILE", 
            data=PDFbyte,
            file_name=project_file.name,
            mime="application/octet-stream",
            use_container_width=True,
            key='project-file-download-button'
            )
        st.divider()

    def Features(self):
        with st.container(key='features-container',border=True):
            st.header("Features :material/feature_search:",divider='blue',anchor=False)
            c1,c2=st.columns(2,gap='medium',vertical_alignment='center')
            with c1:
                st.write("""
                - :grey[Dynamic Pricing]
                - :grey[Responsive Map]
                - :grey[User Experience]
                - :grey[Data Privacy]
                - :grey[Secure Document Handling]
                - :grey[Confidentiality]
                - :grey[Tokenization]
                - :grey[Bidding]
                - :grey[Advance Search]
                - :grey[Push Notifications]
                - :grey[Availability Alerts]
                """)
            with c2:
                st_lottie(animation_source=LeftArrow, loop=True, quality='high',speed=1)
    def Technology(self):
         with st.container(key='Technology-used-container',border=True):
            st.header("Technologies Used :material/computer:",divider='green',anchor=False)
            c1,c2=st.columns(2,gap='medium',vertical_alignment='center')
            with c1:
                st.write("""
                - :grey[C#]
                - :grey[JavaScript]
                - :grey[SQLSERVER]
                - :grey[HTML]
                - :grey[jQuery]
                - :grey[CSS]
                """)
            with c2:
                st_lottie(animation_source=LeftArrow, loop=True, quality='high',speed=1,height=100)
    def Licensing(self):
        with st.container(key='licensing-container',border=True):
            st.header("Licensing :material/license:",divider='violet',anchor=False)
            st.write("""
            - :grey[This is free and unencumbered software released into the public domain.]

            - :grey[Anyone is free to copy, modify, publish, use, compile, sell, or
            distribute this software, either in source code form or as a compiled
            binary, for any purpose, commercial or non-commercial, and by any
            means.]

            - :grey[In jurisdictions that recognize copyright laws, the author or authors
            of this software dedicate any and all copyright interest in the
            software to the public domain. We make this dedication for the benefit
            of the public at large and to the detriment of our heirs and
            successors. We intend this dedication to be an overt act of
            relinquishment in perpetuity of all present and future rights to this
            software under copyright law.]

            - :grey[THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
            EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
            MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
            IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
            OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
            ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
            OTHER DEALINGS IN THE SOFTWARE.]
            """)




    def OtherProjectMembers(self):
        with st.container(key="team-members-container",border=True):
            st.header("Project Team Members :material/groups:",anchor=False,divider='orange')
            col1,col2=st.columns(2,gap='large',vertical_alignment='center')
            with col1:
                st.title("VANSH GURNANI",anchor=False)
                st.write("""
                A computer engineering student passionate about data science, building a network of astute minds to cultivate teamwork and growth.
                """)
            with col2:
                st.image(image="assets/images/VANSH GURNANI.png",use_container_width=True)
            
            st.subheader(":blue[Technology Proficiency]",divider='blue',anchor=False)
            c1,c2=st.columns(2,gap='medium',vertical_alignment='center')
            with c1:
                st.write("""
                - :blue[Technologies: Frontend Developer, Backend Developer, CRUD Developer.]
                - :blue[Programming: Python, SQL, HTML, CSS,C,C++.]
                - :blue[Frameworks: Pandas, Numpy, Matplotlib, Seaborn, Scikit, Streamlit, Flask.]
                - :blue[Data Visualization: MS Excel, PowerBi, Plotly.]
                - :blue[Video Editing: Adobe Premiere pro, Adobe After Effects, Wondershare Filmora, Sony Vegas Pro, DaVinci Resolve.]
                - :blue[Photo Editing: Adobe Photoshop, Adobe Lightroom, Canva.]
                - :blue[Vector Base Editing: Adobe Illustrator.]
                - :blue[Databases: MySQL.]
                """)
            with c2:
                st_lottie(LeftArrow2,speed=1,loop=True,quality='high')

            st.subheader(":blue[Work Experience]",divider='blue',anchor=False)
            d1,d2=st.columns(2,gap='medium',vertical_alignment='top')
            with d1:
                st.write("""
                - :blue[Graphic Designer: Moksha Foundation(2021)]
                - :blue[Assistant: Future Vision Computers(April 2024-Present)]
                """)
            with d2:
                st_lottie(LeftArrow2,speed=1,loop=True,quality='high',height=125)

            st.subheader(":blue[Educational Qualification]",divider='blue',anchor=False)
            
            e1,e2=st.columns(2,gap='medium',vertical_alignment='top')
            with e1:
                st.write("""
                - :blue[10th: GSEB(65%)[2018]]
                - :blue[Diploma in Computer Engineering(2021-2023): 9.5CGPA]
                - :blue[Bachelors in Computer Engineering (2023-2026): 7.5CGPA]
                """)
            with e2:
                st_lottie(LeftArrow2,speed=1,loop=True,quality='high',height=150)
            
            st.link_button("CONNECT WITH VANSH",url="https://vanshgurnani.streamlit.app/",type='tertiary',use_container_width=True)


RR=RentRight()
RR.Features()
RR.Technology()
RR.Licensing()
RR.OtherProjectMembers()