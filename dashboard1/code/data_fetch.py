import os

import requests

from auth import get_jwt_token


def get_activity_parameters(jwt_token):
    url = "https://online.omnicomm.ru/ls/api/v1/click/log"
    headers = {
        "Authorization": f"JWT {jwt_token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    data = {
        "terminalId": 336040868,
        "dateFrom": 1718277299,
        "dateTo": 1718363699,
        "groups": ["GENERAL"],
        "columns": ["EVENT_DATE", "LATITUDE", "LONGITUDE", "SATELLITES_NMB", "SPEED", "MILEAGE", "U_BOARD", "LLS"]
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()

        parameters_data = response.json()
        return parameters_data

    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP ошибка: {http_err}")

    except Exception as err:
        raise Exception(f"Произошла ошибка: {err}")


if __name__ == "__main__":
    username = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    try:
        jwt_token = get_jwt_token(username, password)
        print(f"JWT {jwt_token}")

        activity_parameters = get_activity_parameters(jwt_token)
        print("Данные о последней активности ТС пользователя:")
        print(activity_parameters)

    except Exception as e:
        print("Не удалось получить данные:", e)

