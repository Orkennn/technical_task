import os
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.getcwd(), '..', '.env')

load_dotenv(dotenv_path)

def get_jwt_token(login, password):
    url = "https://online.omnicomm.ru/auth/login?jwt=1"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }
    data = {
        "login": login,
        "password": password
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()

        token_data = response.json()
        jwt_token = token_data.get("jwt")
        if jwt_token:
            return jwt_token
        else:
            raise ValueError("JWT токен не найден в ответе")

    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP ошибка: {http_err}")

    except ValueError as value_err:
        raise Exception(f"Ошибка значения: {value_err}")

    except Exception as err:
        raise Exception(f"Произошла ошибка: {err}")


if __name__ == "__main__":
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")

    try:
        token = get_jwt_token(login, password)
        print(f"JWT {token}")

    except Exception as e:
        print(f"Не удалось получить данные: {e}")

