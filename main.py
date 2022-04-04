import time
import requests
# импортируем pprint для более комфортного вывода информации
from pprint import pprint
token = ''
#from chat_bot import age, status, city, sex
class VK:

    def __init__(self):
        # self.age = age
        # self.status = status
        # self.city = city
        # self.sex = sex
        self.city_id = []
        self.profile = []

    def get_para(self):
        URL = 'https://api.vk.com/method/users.search'
        params = {
            'sex': '1',
            'status': '1',
            'count': '3',
            'city' : self.city_id,
            'age_from': '18',
            'age_to': '80',
            'access_token': token,
             'is_closed' : False,
            'v':'5.131'
        }
        res = requests.get(URL, params=params)
        pprint(res.json())
        profiles = res.json()['response']['items']
        # for profile in profiles:
        #     self.profile.append('https://vk.com/id' + str(profile['id']))
        # print(self.profile)
            #return profile['id']

    def get_city(self, city):
        URL = 'https://api.vk.com/method/database.getCities'
        params = {
            'country_id' : '1',
            'count': '1',
            'q' : city,
            'access_token': token,
            'v': '5.131'
        }
        res = requests.get(URL, params=params)
        citys = res.json()['response']['items']
        for city in citys:
            self.city_id.append(city['id'])
            return self.city_id

    def get_photo(self):
        user_ids = vk.get_para()
        URL_photo = 'https://api.vk.com/method/photos.get'
        URL_user = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids': user_ids,
            'access_token': token,
            'v': '5.131',
        }
        res = requests.get(URL_user, params=params)
        items = res.json()['response']
        for id in items:
            id_user = id['id']
            params = {
                'owner_id': id_user,
                'access_token': token,
                'album_id': 'profile',
                'extended': 'likes',
                'photo_sizes': '1',
                'v': '5.131',
                'count': '5'
            }
            res = requests.get(URL_photo, params=params)
            res_photo = res.json()['response']['items']



if __name__ == '__main__':
    vk = VK()
    city = input('Город:')
    vk.get_city(city)
    vk.get_para()
    vk.get_photo()

