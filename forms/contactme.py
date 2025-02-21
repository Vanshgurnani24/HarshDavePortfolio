import streamlit as st
import re
from streamlit_gsheets import GSheetsConnection
import pandas as pd


conn=st.connection(name='gsheets',type=GSheetsConnection)
existing_data=conn.read(worksheet='Contact Sheet',usecols=list(range(5)),ttl=5)


existing_data=existing_data.dropna(how='all')

def is_valid_email(email):
    email_pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern,email) is not None


def Contact_form():
    with st.form("Contact-me-form"):
        name=st.text_input("Name",placeholder="Your name")
        c1,c2=st.columns(2,gap='medium')
        mobile=c1.text_input("Mobile Number",placeholder="Your Mobile No")
        email=c2.text_input("Email",placeholder="Your email")
        message=st.text_input("Message",placeholder="Drop a message")
        if st.form_submit_button("Send",use_container_width=True):
            if not(name):
                st.error("Please enter your name")
                return
            elif not mobile or len(mobile)!=10 or not(mobile.isdigit()):
                st.error("Please enter a valid mobile number")
                return
            elif not email or not(is_valid_email(email)):
                st.error("Please enter a valid email")
                return 
            elif not message:
                st.error("Please enter a message")
                return
            else:
                user_data=pd.DataFrame(
        [
        {
          "Name":name,
          "Email":email,
          "Mobile":mobile,
          "Message":message,
          "Date":pd.Timestamp.now()
        }
        ]
      )
            updated_df=pd.concat([existing_data,user_data],ignore_index=True)
            conn.update(worksheet="Contact Sheet",data=updated_df)
            st.success("Message sent successfully!")