import yaml 


def get_token():
    """
    Функция для получения токена бота из файла конфигурации.

    Возвращает:
        str: Токен бота.
    """
    with open('config.yaml') as file:
        token = yaml.safe_load(file)['token']
        return token