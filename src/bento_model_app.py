import numpy as np
import bentoml
from bentoml.io import NumpyNdarray, JSON
from pydantic import BaseModel
import pandas as pd

class BikesData(BaseModel):
    hour: int = 0
    temperaturec: float = -5.2
    humidity: int = 37
    wind_speed_ms: float = 2.2
    visibility_10m: int = 2000
    dew_point_temperaturec: float = -17.6
    solar_radiation_mjm2: float = 0.0
    rainfallmm: float = 0.0
    snowfall_cm: float = 0.0
    year: int = 2017
    month: int = 12
    week: int = 48
    day: int = 1
    day_of_week: int = 4
    is_month_start: bool = True
    holiday_holiday: int = 0
    holiday_no_holiday: int = 1
    seasons_autumn: int = 0
    seasons_spring: int = 0
    seasons_summer: int = 0
    seasons_winter: int = 1
    functioning_day_no: int = 0
    functioning_day_yes: int = 1



bikes_runner = bentoml.sklearn.get("bikes_model:latest").to_runner()
svc = bentoml.Service("bikes_predict", runners=[bikes_runner])


@svc.api(input=JSON(pydantic_model=BikesData), output=NumpyNdarray())
def rf_pred(input_series: BikesData) -> np.ndarray:
    data = pd.DataFrame(input_series.dict(), index=[0])
    return bikes_runner.predict.run(data.values)


# hour:0
# temperaturec:-5.2
# humidity:37
# wind_speed_ms:2.2
# visibility_10m:2000
# dew_point_temperaturec:-17.6
# solar_radiation_mjm2:0.0
# rainfallmm:0.0
# snowfall_cm:0.0
# year:2017
# month:12
# week:48
# day:1
# day_of_week:4
# is_month_start:true
# holiday_holiday:0
# holiday_no_holiday:1
# seasons_autumn:0
# seasons_spring:0
# seasons_summer:0
# seasons_winter:1
# functioning_day_no:0
# functioning_day_yes:1

# {
#   "hour": 0,
#   "temperaturec": -5.2,
#   "humidity": 37,
#   "wind_speed_ms": 2.2,
#   "visibility_10m": 2000,
#   "dew_point_temperaturec": -17.6,
#   "solar_radiation_mjm2": 0,
#   "rainfallmm": 0,
#   "snowfall_cm": 0,
#   "year": 2017,
#   "month": 12,
#   "week": 48,
#   "day": 1,
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