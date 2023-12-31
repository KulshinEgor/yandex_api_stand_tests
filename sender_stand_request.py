import configuration
import requests
import data


def post_new_user(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=user_body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response = post_new_user(data.user_body);
print(response.status_code)
print(response.json())


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


response = get_users_table()
print(response.status_code)
