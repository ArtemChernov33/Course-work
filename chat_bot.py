from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
token = 'a4f9550bea4fd476b90d64674f83e4e9b0d30b84c153a43262514a604d698287d249e8140ea4c3d9be6ac'
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'chat_id': user_id, 'message': message,  'random_id': 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            # for i in range(1, 100):
            #     pass
                #print(i)
            if event.from_chat:
                request = event.text
                user_id = event.chat_id
                if request == "привет":
                    write_msg(user_id, 'Приветствую тебя человеков!\n Если ты зашел в беседу и мне написал, значит ты одинок и хочешь найти себе пару, да?')
                    #write_msg(user_id, {i})
                elif request == "да":
                    write_msg(user_id, 'Я тебе помогу!!! Для этого тебе необходимо ввести критерии по которым Я буду искать:'
                                       '\n Возраст (Например: 18)'
                                       '\n Пол (Например: Ж)'
                                       '\n Город (Например: Москва)'
                                       '\n Семейное положение (Например: Не замужем)')
                    write_msg(user_id, 'Введите возраст:')
                elif request == '33':
                    age = request
                    write_msg(user_id, 'Введите пол:')
                    print(age)
                elif request == 'Ж':
                    sex = request
                    write_msg(user_id, 'Введите город:')
                # elif request == 'Ж':
                #     s = 1
                # elif  request == 'М':
                #     s = 2
                # elif request == 'Не важно':
                #     s = 0
                #     write_msg(user_id, 'Введите город:')
                #     print(s)
                elif request == 'М':
                    city = request
                    write_msg(user_id, 'Семейное положение:')
                elif request == 'Н':
                    status = request
                    write_msg(user_id, 'Начинаю искать тебе подружку')
                    print(status)
                #     age = get_age()
                # elif request == "Пол":
                #     gender = get_gender()
                # elif request == "Город":
                #     sity = get_sity()
                # elif request == "Семейное положение":
                #     marital_status = get_marital_status()
                elif request == "пока":
                    write_msg(user_id, "Пока((")
                else:
                    write_msg(user_id, "Не поняла вашего ответа...")
