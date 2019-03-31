import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "6deb20fb6651911d89e9df532424501b9f1fa1256054638ec07729934f5f928b9e7da32ed41c1e1c53d38"
group_id = 175626312

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

def keyboard():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Кнопка 1', color=VkKeyboardColor.DEFAULT, payload= {"button": "button1"})
    keyboard.add_line()
    keyboard.add_button('Кнопка 2', color=VkKeyboardColor.DEFAULT, payload= {"button": "button2"})
    keyboard.add_line()
    keyboard.add_button('Кнопка 3', color=VkKeyboardColor.DEFAULT, payload= {"button": "button3"})
    return keyboard.get_keyboard()

longpoll = VkBotLongPoll(vk_session, group_id)



for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW:
		peer_id = int(event.obj.peer_id)
		vk.messages.send(peer_id= peer_id, message= 'TEXT', keyboard=keyboard())
