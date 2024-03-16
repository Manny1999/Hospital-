import streamlit as st
from streamlit_option_menu import option_menu
import about, account, home, paitents, your_appointments

st.set_page_config(
        page_title="Hosptial",
)

class MultiApp:


    def __init__(self):
          self.apps = []
    def add_app(self, title, function):
        
        self.apps.append({
            "title": title,
            "function": function
          
          })
          
          
    def run():
          
        with st.sidebar:
              app = option_menu(
                  menu_title='Hospital ',
                  options=['Home', 'Account', 'Paitents', 'about', 'Your Appointments'],
                  icons=['house-fill', 'person-circle', 'people-fill','chat-fill', 'pen-fill'],
                  menu_icon='chat-text-fill',
                  default_index=1,
                  styles={
                    "container": {"padding": "5!important","background-color":'white'},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"color":"black","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
        
                    )
        
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()
        if app == "Paitents":
            paitents.app()
        if app == "about":
            about.app()
        if app == "Your Appointments":
            your_appointments.app()
                
                
    run()
                
              
              
              
              
              
              
              
              
              
              
              
              
              
              
