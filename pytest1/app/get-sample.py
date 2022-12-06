import requests
import json

def get_api_key(email: str, passwd: str):
   headers = {
       'email': email,
       'password': passwd,
   }
   res = requests.get('https://petfriends.skillfactory.ru/api/key', headers=headers)
   status = res.status_code
   try:
       result = res.json()
   except json.decoder.JSONDecodeError:
       result = res.text
   return status, result


print(get_api_key('vasya@mail.com','12345'))


# мы не можем быть уверены, что сервер вернёт ответ
# в формате json, поэтому сначала пытаемся декодировать
# полученные данные как json-строку. Если с этим возникают проблемы,
# то возвращаем ответ обычным текстом.