from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from MODULE_ONAR import TOKEN 
from MODULE_ONAR import table_options
from MODULE_ONAR import getting_memory
import time 

dict_for_ONAR_p1 = ['hello','здарова','привет','бонджорно','здравствуйте']

bot = Bot(token=TOKEN)
system_qui = Dispatcher(bot)

def memory_options(content_types=['text']):
    async def get_memory(msg: types.Message):
        return msg.text 


def start_process():
    @system_qui.message_handler(commands=['start', 'help'])
    async def send_welcome(msg: types.Message):
        await msg.reply_to_message(f'Вы активировали систему. Чтобы продолжить, начните общение, {msg.from_user.firs_name}')

def assessment_of_the_condition(content_types=['text']):
    async def get_assessment_of_the_condition(msg: types.Message):
        if int(msg.text) >= 0 and int(msg.text) <= 3:
            await msg.answer('Не грустите, лучше послушайте трек Denzel Curry - Goodnight, все будет хорошо !')
        elif int(msg.text) > 3  and  int(msg.text) <=5:
            await msg.answer('Отлично, я рад за вас, предлагаю один научный факт:')
            await msg.answer('Эйфелева башня вырастает летом на 15 сантиметров')
        


def communicate_part_1(content_types=['text']):
    async def get_text_messages(msg: types.Message):
        if msg.text.lower() in dict_for_ONAR_p1:
            await msg.answer('Здравствуйте ! Как ваши дела? Оцените ваше состояние от 0 до 5:')

        else:
            await msg.answer('Простите, я не распознал, обновляю лексическое ядро...')
            time.sleep(7)
            dict_for_ONAR_p1.append(msg.text.lower())
def communicate_options(content_types=['text']):
    async def ask_for_something(msg: types.Message):
        await msg.answer('Что бы вы хотели?')
        await msg.answer(table_options)
            
@system_qui.message_handler(commands="choice")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    button_2 = "Без пюрешки"
    keyboard.add(button_2)


if __name__ == "__main__":
    executor.start_polling(system_qui)