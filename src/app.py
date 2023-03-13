import json
import requests
import streamlit as st


st.title("Seoul Bike Prediction App!")

data = {}

data["hour"] = st.slider(
    label="Hour",
    min_value=0, max_value=23, value=10,
    help="Time of the day from 0 to 23."
)

data["temperaturec"] = st.slider(
    label="Temperature",
    min_value=-23.0, max_value=40.2, step=0.1, value=-5.2,
    help="Temperature in Celsius."
)

#   ,
#   "": 2.2,
#   "visibility_10m": 2000,
#   "dew_point_temperaturec": -17.6,
#   "solar_radiation_mjm2": 0,
#   "rainfallmm": 0,
#   "snowfall_cm": 0,
#   "year": 2017,
#   "month": 12,
#   "week": 48,
#   "day": 1,


data["humidity"] = st.slider(
    label="Humidity",
    min_value=0, max_value=100, value=37,
    help="Humidity percentage."
)

data["wind_speed_ms"] = st.slider(
    label="Wind Speed (m/s)",
    min_value=0.0, max_value=7.5, value=3.0, step=0.1,
    help="Time of the day from 0 to"
)

data["visibility_10m"] = st.slider(
    label="visibility_10m",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["dew_point_temperaturec"] = st.slider(
    label="dew_point_temperaturec",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["solar_radiation_mjm2"] = st.slider(
    label="solar_radiation_mjm2",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["rainfallmm"] = st.slider(
    label="rainfallmm",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["snowfall_cm"] = st.slider(
    label="snowfall_cm",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["year"] = st.slider(
    label="year",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["month"] = st.slider(
    label="month",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["week"] = st.slider(
    label="Week",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["day"] = st.slider(
    label="Day",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)


#   "day_of_week": 4,
#   "is_month_start": true,
#   "holiday_holiday": 0,
#   "holiday_no_holiday": 1,
#   "seasons_autumn": 0,
#   "seasons_spring": 0,
#   "seasons_summer": 0,
#   "seasons_winter": 1,
#   "functioning_day_no": 0,
#   "functioning_day_yes": 1
# }

data["day_of_week"] = st.slider(
    label="day_of_week",
    min_value=0, max_value=6, value=4,
    help="Time of the day from 0 to"
)

data["is_month_start"] = st.select_box(
    label="Is it the start of the Month?",
    options=(True, False), value=True,
    help="Time of the day from 0 to"
)

data["holiday_holiday"] = st.slider(
    label="holiday_holiday",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["holiday_no_holiday"] = st.slider(
    label="holiday_no_holiday",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["seasons_autumn"] = st.slider(
    label="seasons_autumn",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["seasons_spring"] = st.slider(
    label="seasons_spring",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["seasons_summer"] = st.slider(
    label="seasons_summer",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["seasons_winter"] = st.slider(
    label="seasons_winter",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["functioning_day_no"] = st.slider(
    label="functioning_day_no",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)

data["functioning_day_yes"] = st.slider(
    label="functioning_day_yes",
    min_value=0,
    value=10,
    max_value=23,
    help="Time of the day from 0 to"
)