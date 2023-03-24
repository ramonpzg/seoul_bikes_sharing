import json
import requests
import streamlit as st

st.image("https://res.heraldm.com/content/image/2017/12/17/20171217000143_0.jpg")
st.title("Seoul Bike Prediction App!")

col1, col2 = st.columns(2)

data = {}

data["hour"] = col1.slider(
    label="Hour", min_value=0, max_value=23, value=10,
    help="Time of the day from 0 to 23."
)

data["temperaturec"] = col2.slider(
    label="Temperature", min_value=-23.0, max_value=40.2, step=0.1, value=-5.2,
    help="Temperature in Celsius."
)

#   "year": 2017,
#   "month": 12,
#   "week": 48,
#   "day": 1,

data["humidity"] = col1.slider(
    label="Humidity",
    min_value=0, max_value=100, value=37,
    help="Humidity percentage."
)

data["wind_speed_ms"] = col2.slider(
    label="Wind Speed (m/s)",
    min_value=0.0, max_value=7.5, value=3.0, step=0.1,
    help="Time of the day from 0 to"
)

data["visibility_10m"] = col1.slider(
    label="Visibility 10m",
    min_value=20, max_value=2100, value=1900, step=10,
    help="Visibility levels. The higher the better one can see."
)

data["dew_point_temperaturec"] = col2.slider(
    label="Dew Point Temperature in Celsius",
    min_value=-30.1, max_value=27.5, value=-17.6, step=0.1,
)

data["solar_radiation_mjm2"] = col1.slider(
    label="Solar Radiation in mjm2",
    min_value=0.5, max_value=3.5, value=0.0, step=0.1,
    # help="Time of the day from 0 to"
)

data["rainfallmm"] = col2.slider(
    label="Rainfall in mm",
    min_value=0, max_value=35, value=10, step=1,
    # help="Time of the day from 0 to"
)

data["snowfall_cm"] = col1.slider(
    label="snowfall_cm",
    min_value=0.0, max_value=8.8, value=0.0, step=0.1
    # help="Time of the day from 0 to"
)

data["year"] = col2.slider(
    label="Year",
    min_value=2018, max_value=2023, value=2019, step=1,
    # help="Time of the day from 0 to"
)

data["month"] = col1.slider(
    label="Month",
    min_value=0, max_value=12, value=10,
    # help="Time of the day from 0 to"
)

data["week"] = col2.slider(
    label="Week (Make sure it matches the Month you chose).",
    min_value=0, value=10, max_value=52,
    # help="Time of the day from 0 to"
)

data["day"] = col1.slider(
    label="Day of the Month.",
    min_value=1, max_value=31, value=15,
    # help="Time of the day from 0 to"
)

data["day_of_week"] = col2.slider(
    label="Day of Week (0=Monday and  6=Sunday).",
    min_value=0, max_value=6, value=4,
    # help="Time of the day from 0 to"
)

data["is_month_start"] = col1.radio(
    label="Is it the start of the Month?",
    options=(True, False)
)

data["holiday"] = col2.radio(
    label="Is the day you chose a public holiday?",
    options=("Yes", "No"))

data["holiday_holiday"] = 1 if data["holiday"] == "Yes" else 0
data["holiday_no_holiday"] = 1 if data["holiday"] == "No" else 0

data["seasons"] = col1.selectbox(
    label="Please select the Season of the year that matches the month you selected.",
    options=('Winter', 'Spring', 'Summer', 'Autum/Fall')
)

if data["seasons"] == "Winter":
    data["seasons_winter"] = 1
else:
    data["seasons_winter"] = 0

if data["seasons"] == "Summer":
    data["seasons_summer"] = 1
else:
    data["seasons_summer"] = 0

if data["seasons"] == "Autumn/Fall":
    data["seasons_autumn"] = 1
else:
    data["seasons_autumn"] = 0

if data["seasons"] == "Spring":
    data["seasons_spring"] = 1
else:
    data["seasons_spring"] = 0

data["functional"] = col2.selectbox(
    label="Please select whether bikes are available on this day or being serviced.",
    options=('Yes', 'No')
)

if data["functional"] == "No":
    data["functioning_day_no"] = 1
else:
    data["functioning_day_no"] = 0

if data["seasons"] == "Yes":
    data["functioning_day_yes"] = 1
else:
    data["functioning_day_yes"] = 0

prompt = f"Find out how many bikes 🚲 are needed on {data['day']}-{data['month']}-{data['year']} to service the city of Seoul 🇰🇷"
if st.button(prompt):
    data_json = json.dumps(data)
    r = requests.post(
        url='https://cy0809ul20.execute-api.ap-southeast-2.amazonaws.com/rf_pred',
        headers={'accept': 'application/json', 'content-type': 'application/json'}, 
        data=data_json
    ).text
    response = int(float(r.split("[")[-1].split("]")[0]))
    st.write(f"{response} is the amount of 🚲🚲 needed on {data['day']}-{data['month']}-{data['year']}! ᕙ(  •̀ ᗜ •́  )ᕗ")