import streamlit as st
import plotly.express as px
from APIs import apod_generator
from APIs import apod_generator_list
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

# Important note: APOD = Astronomy Picture of the Day

# Asks user to input their API key.
unique_key = st.text_input("Enter your API key: ")

if unique_key:
    # Initial title and text prompting user to input the date:
    st.title("Picture of the Date")
    st.divider()
    st.text("Input the date of the APOD you wish to see:")

    # Pieces of the final url:
    url = "https://api.nasa.gov/planetary/apod?api_key="

    # User clicks on date and selects the date related to the picture of the day they wish to see:
    chosen_date = st.date_input("Select a date", datetime.date.today())

    apod = apod_generator(url, unique_key, str(chosen_date))

    tab1, tab2, tab3 = st.tabs(["Picture of the Date",
                                "Basic Data values",
                                "APOD Title Length (From the past 30 days)"])

    # Contains a basic page that moreso replicates what one would see on NASA's picture of the day website.
    with tab1:
        st.subheader(apod["title"])
        st.image(apod["hdurl"])
        st.divider()
        st.text(apod["explanation"])

    # Data table of values associated with the picture of the day (like its title, url, etc.)
    with tab2:
        st.dataframe(apod)

    # Bar graph with the title lengths of the last 30 APODs.
    with tab3:
        start_date = str(datetime.date.today() - datetime.timedelta(days=30))
        end_date = str(datetime.date.today())
        data = apod_generator_list(url, unique_key, start_date, end_date)

        title_data = {
            "Date": [],
            "Title Length": []
        }

        # For loop for inputting data from data to title_data:
        for object in data:
            title_data["Date"].append(object["date"])
            title_data["Title Length"].append(len(object["title"]))

        fig1 = px.bar(title_data, x="Date", y="Title Length")
        st.plotly_chart(fig1)

else:
    st.error("Please enter a valid API key")
    exit(0)

