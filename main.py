import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("weather_api_key")

st.set_page_config(page_title="Weather App",page_icon="☀️",)
st.title("Weather App")
st.write("Enter the city name and click on the button to get the current  weather information")
city =st.text_input("Enter City Name:")

API_URL=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
if st.button("Fetch Weather Data"):
    response=requests.get(API_URL)

    if(response.status_code == 200):
        st.success("Weather data fetched successfully!")
        
        data = response.json()
        
        #fetch the weather data in variables 
        temperature=data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed=data["wind"]["speed"]
        weather =data["weather"][0]["main"]
        
        st.write("🌡️ Temperature:", temperature, "°C")
        st.write("💧 Humidity:", humidity, "%")
        st.write("💨 Wind Speed:", wind_speed, "m/s")
        st.write("🌤️ Weather:", weather)

    else:
        st.error("invalid city name")    