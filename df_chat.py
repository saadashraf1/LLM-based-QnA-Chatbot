# Refer to Databutton -> Log in -> Create New App -> Start with Own Chat GPT template
# Thanks to Trygve / Martin
import pandas as pd
import streamlit as st


class user_message:
    def __init__(self, text, user_name="You"):
        self.name = user_name
        self.container = st.empty()
        self.update(text)

    def update(self, text):
        message = f"""<div style='display:flex;align-items:center;justify-content:flex-end;margin-bottom:10px;'>
                     <div style='background-color:{st.get_option("theme.secondaryBackgroundColor")};border-radius:10px;padding:10px;'>
                     <p style='margin:0;font-weight:bold;'>{self.name}</p>
                     <p style='margin:0;color={st.get_option("theme.textColor")}'>{text}</p>
                     </div>
                     <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-i3H7JYv875AbY5HbYauzUq1LM44omXrUNQev6EGcrYC_pqVZ848mjKbwTqre4DCZ0YM&usqp=CAU' style='width:50px;height:50px;border-radius:50%;margin-left:10px;'>
                     </div>
        """
        self.container.write(message, unsafe_allow_html=True)
        return self


class bot_message:
    def __init__(self, text, bot_name="Assistant"):
        self.name = bot_name
        self.container = st.empty()
        self.update(text)

    def update(self, text):
        message = f"""<div style='display:flex;align-items:center;margin-bottom:10px;'>
                    <img src='https://cf.shopee.co.id/file/bbff756b7dddc2a79b578673f9a8b0a6' style='width:50px;height:50px;border-radius:50%;margin-right:10px;'>
                    <div style='background-color:st.get_option("theme.backgroundColor");border: 1px solid {st.get_option("theme.secondaryBackgroundColor")};border-radius:10px;padding:10px;'>
                    <p style='margin:0;font-weight:bold;'>{self.name}</p>
                    <p style='margin:0;color={st.get_option("theme.textColor")}'>{text}</p>
                    </div>
                    </div>
        """
        self.container.write(message, unsafe_allow_html=True)
        return self