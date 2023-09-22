import streamlit as st
import pandas as pd 

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://th.bing.com/th/id/R.44ec104394406999f29fcbe5150b26f0?rik=jLUbYIwt8dLFtg&riu=http%3a%2f%2fwww.pixelstalk.net%2fwp-content%2fuploads%2f2016%2f08%2fCool-Beautiful-House-Design-HD-Wallpapers.jpg&ehk=oS%2bO5iblYSNkchVMXvcQECT%2bdqR9GQr8redw6qnQ9xM%3d&risl=&pid=ImgRaw&r=0");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_hack_url()

st.title("Rosemary's ADU App")
col1, col2 = st.columns(2)
with col1:
    squarefoothouse = st.number_input("Square footage of house: ",min_value= 1)
with col2:
    squarefootADU = st.number_input("Square footage of ADU: ",min_value= 1)
ratiosquarefootage = squarefootADU / squarefoothouse
st.write("Ratio Square Footage between House and ADU: ",ratiosquarefootage)
if squarefoothouse > 0 and squarefootADU > 0:
    rentincomehouse = st.number_input("Rent Income of House: ",min_value = 1)
rentincomeADU = ratiosquarefootage * rentincomehouse 
st.write("Rent income of ADU: ",rentincomeADU)
growthraterenthouse = st.number_input("Growth rate of the house: ")
growthraterenthouse2 = st.slider("Growth rate of House Rental Income: ",min_value= 1, max_value = 100)
returnoninvestment = rentincomeADU * growthraterenthouse
returninvestment = rentincomeADU * (1 + (growthraterenthouse / 100))**growthraterenthouse2
returnoninvestment = st.number_input("Return on Investment: ",returninvestment)

#Latitude and Longitude
st.write("Exact Location of Land:")
latitude = st.text_input("Latitude: ")
longitude = st.text_input("Longitude: ")
if latitude and longitude: 
    df = pd.DataFrame({'lat': [float(latitude)], 'lon': [float(longitude)]})
    st.map(df)