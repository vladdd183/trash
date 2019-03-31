import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "" #Сюда воткнуть токен
group_id = 123 #Сюда воткнуть айди группы в числовом формате

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

def keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Кнопка 1', color=VkKeyboardColor.DEFAULT, payload= {"button": "button1"}) # Можно поменять название, колличество и цвет
    keyboard.add_line()
    keyboard.add_button('Кнопка 2', color=VkKeyboardColor.DEFAULT, payload= {"button": "button2"})
    keyboard.add_line()
    keyboard.add_button('Кнопка 3', color=VkKeyboardColor.DEFAULT, payload= {"button": "button3"})
    return keyboard.get_keyboard()

longpoll = VkBotLongPoll(vk_session, group_id)



for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW:
		peer_id = int(event.obj.peer_id)
		vk.messages.send(peer_id= peer_id, message= 'TEXT', keyboard=keyboard()) #Можно поменять текст
