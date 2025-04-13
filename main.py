# импорт
import os
import telebot

# определяем рабочую директорию
if not os.path.isdir("memory"):
     os.mkdir("memory")
os.chdir("memory")

# чистим память!!!!!!!!!!!!!!!!!!!!!
#if os.path.isfile("memory.txt"):
#     os.remove("memory.txt")

# функция для записи в файл памяти
def rw(str):
     if os.path.isfile("memory.txt"):
          text_file = open("memory.txt", "r")
          result = text_file.read()
          result += "\n"
     else:
          result = ""

     result += str
     text_file = open("memory.txt", "w")
     text_file.write(result)

     result = result.split("\n")
     for i in range(len(result)):
          result[i] = result[i].split("/~/")

     return result

# функция для ответа
def remes(str):
     if os.path.isfile("memory.txt"):
          text_file = open("memory.txt", "r")
          basmem = text_file.read()
     else:
          basmem = ""

     result = "ответа нет"
     basmem = basmem.split("\n")
     for i in range(len(basmem)):
          basmem[i] = basmem[i].split("/~/")
          if basmem[i][0] == str:
               result = basmem[i][1]


     return result


# загружаем бота Телеграмм @DataScientistRoBot
bot = telebot.TeleBot("5056295653:AAGMm5MdWs_W9xqDw7yurJA7Hc2penLBuGs")




# читаем сообщение от пользователя
@bot.message_handler(content_types=['text'])
# отвечаем на сообщение пользователю
def send_echo(message):
     if message.reply_to_message:
          strrep = message.reply_to_message.text
          str = message.text
          rw(strrep + "/~/" + str)
     else:
          str = message.text
          answer = remes(str)
          bot.send_message(message.chat.id, answer)




# работа бота без остановки
bot.polling( none_stop = True )