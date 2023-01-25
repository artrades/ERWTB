from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')
button4 = KeyboardButton('4️⃣')



markup = ReplyKeyboardMarkup().add(button1).add(button2).add(button3).add(button4)


