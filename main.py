from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN
from glossary import algo_list, algo_book, algo_video_links, algo_tasks, traning_list
import random

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start_message(message):
    text = "Привет, дорогой пользователь. Я очень рад, что ты решил изучить алгоритмы! Используй команду /help, чтобы узнать мой функционал!"
    await bot.send_message(chat_id=message.chat.id, text=text)


@dp.message_handler(commands=['help'])
async def start_message(message):
    text = "1: /algo - вывести все достпуные для изучения темы.\n" \
            "2: algo.<b>число</b> - получить ссылку на лекцию по заданной теме, число от 1 до 16\n" \
            "3: /rand_task  - выдает рандомную задачку с <b>codeforces</b>.\n" \
            "4: task.<b>число</b> - выдает задачку по заданной теме, число от 1 до 16\n" \
            "5: training.<b>число</b> - выдает контест. Число указывает сложность контеста, принимает значения от 1 до 5."
    await bot.send_message(chat_id=message.chat.id, text=text, parse_mode="html")


@dp.message_handler(commands=['algo'])
async def algo_message(message):
    await bot.send_message(chat_id=message.chat.id, text=algo_list)
    await bot.send_message(chat_id=message.chat.id, text="Пришли мне сообщение <b>algo.число</b>, и я тебе отправлю лекцию и конспект по выбранной теме!", parse_mode="html")

@dp.message_handler(commands=['rand_task'])
async def task_message(message):
    i = random.randint(1, 16)
    j = random.randint(1, 3)
    await bot.send_message(chat_id=message.chat.id, text=algo_tasks[i][j])


@dp.message_handler()
async def get_message(message : types.Message):
    if (len(message.text) > 9 and message.text[0:9] == 'training.'):
        number = message.text[9:]
        if (number.isnumeric()):
            number = int(number)
            if (number > 5 or number <= 0):
                await bot.send_message(chat_id=message.chat.id,
                                       text="Всего 5 уровней сложности(от 1 до 5).")
            else:
                i = random.randint(1, 4)
                await bot.send_message(chat_id=message.chat.id, text="<b>Уровень сложности контеста: " + str(number) + "</b>",
                                       parse_mode="html")
                await bot.send_message(chat_id=message.chat.id, text=traning_list[number][i])
        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text=message.text[9:] + " - это не число или число меньше 0")



    elif (len(message.text) > 5 and message.text[0:5] == 'task.'):
        number = message.text[5:]
        if (number.isnumeric()):
            number = int(number)
            if (number > 16):
                await bot.send_message(chat_id=message.chat.id,
                                       text="Я не знаю так много алгоритмов, но скоро точно узнаю, обещаю!")
                await bot.send_message(chat_id=message.chat.id, text="Число должно быть от 1 до 16")
            elif (number == 0):
                await bot.send_message(chat_id=message.chat.id, text="Число должно быть от 1 до 16")
            else:
                i = random.randint(1, 3)
                await bot.send_message(chat_id=message.chat.id, text="<b>Задачка на тему:</b> " + algo_book[number], parse_mode="html")
                await bot.send_message(chat_id=message.chat.id, text=algo_tasks[number][i])
        else:
            await bot.send_message(chat_id=message.chat.id,
                                   text=message.text[5:] + " - это не число или число меньше 0")
    elif (len(message.text) > 5 and message.text[0:5] == 'algo.'):
        number = message.text[5:]
        if (number.isnumeric()):
            number = int(number)
            if (number > 16):
                await bot.send_message(chat_id=message.chat.id, text="Я не знаю так много алгоритмов, но скоро точно узнаю, обещаю!")
                await bot.send_message(chat_id=message.chat.id, text="Число должно быть от 1 до 16")
            elif (number == 0):
                await bot.send_message(chat_id=message.chat.id, text="Число должно быть от 1 до 16")
            else:
                await bot.send_message(chat_id=message.chat.id, text="<b>" + algo_book[number] + "</b>", parse_mode="html")
                await bot.send_message(chat_id=message.chat.id, text=algo_video_links[number])

        else:
            await bot.send_message(chat_id=message.chat.id, text=message.text[5:] + " - это не число или число меньше 0")

    else:
        await bot.send_message(chat_id=message.chat.id, text="Твоя моя не понимать")

executor.start_polling(dp)