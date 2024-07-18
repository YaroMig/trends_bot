import openmeteo_requests
from openmeteo_sdk.Variable import Variable


async def get_weather_data(latitude, longitude):
    """
    Функция для получения данных о погоде по заданным координатам.

    Аргументы:
        latitude (float): Широта.
        longitude (float): Долгота.

    Возвращает:
        float: Текущая температура воздуха в градусах Цельсия.
    """
    om = openmeteo_requests.Client()
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m", "precipitation"],
        "current": ["temperature_2m"]
    }

    responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
    response = responses[0]
    current = response.Current()
    current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
    current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))
    current_temperature = round(current_temperature_2m.Value(), 2)
    
    return current_temperature