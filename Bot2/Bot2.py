import sqlite3
import telebot
from telebot import types
bot = telebot.TeleBot("5168422705:AAHVU0_vMsT0kGbmSP12b0Oul9_0nNBadMg") 
conn = sqlite3.connect('EF/database2.db', check_same_thread= False)
cursor = conn.cursor()
@bot.message_handler(content_types=['text'])


def start(message):

  

    if message.text == "/start":
        markup_inline = types.InlineKeyboardMarkup()
        item_1 = types.InlineKeyboardButton(text = 'Жанры', callback_data = 'genre')
        item_2 = types.InlineKeyboardButton(text = 'Искать фильмы по подборкам', callback_data = 'list_movie_by_same')
       
        markup_inline.add(item_1,item_2)

        bot.send_message(message.chat.id, "Выберите", reply_markup = markup_inline)

    elif message.text =="/help":

        bot.send_message(message.from_user.id, "/search - Поиск фильмов по названию; /start - Для начало поиск по жанрам ")


    elif message.text == "/search":

        bot.send_message(message.from_user.id, "Нашите название фильма. К примеру: Ирландец, Оно 2, Логан и т.д.")
        bot.register_next_step_handler(message, kino_name);

    elif message.text == "УЖАСЫ":
        cursor = conn.cursor()
        name_all = cursor.execute("SELECT Name FROM Kino WHERE Genre = 'УЖАСЫ'" )
        list_name_same_genre = cursor.fetchall()
        bot.send_message(message.chat.id, "Нажмите на /search чтобы искать эти фильмы по имени")
        for list in list_name_same_genre:
            bot.send_message(message.from_user.id, list)
    elif message.text == "ФАНТАСТИКА":
        cursor = conn.cursor() 
        name_all = cursor.execute("SELECT Name FROM Kino WHERE Genre = 'ФАНТАСТИКА'" )
        list_name_same_genre = cursor.fetchall()
        bot.send_message(message.chat.id, "Нажмите на /search")
        for list in list_name_same_genre:
            bot.send_message(message.from_user.id, list)
    elif message.text == "БИОГРАФИЯ":
        cursor = conn.cursor() 
        name_all = cursor.execute("SELECT Name FROM Kino WHERE Genre = 'БИОГРАФИЯ'" )
        list_name_same_genre = cursor.fetchall()
        bot.send_message(message.chat.id, "Нажмите на /search")
        for list in list_name_same_genre:
            bot.send_message(message.from_user.id, list)
    elif message.text == "КРИМИНАЛ":
        cursor = conn.cursor() 
        name_all = cursor.execute("SELECT Name FROM Kino WHERE Genre = 'КРИМИНАЛ'" )
        list_name_same_genre = cursor.fetchall()
        bot.send_message(message.chat.id, "Нажмите на /search")
        for list in list_name_same_genre:
            bot.send_message(message.from_user.id, list)
    elif message.text == "РОМАНТИКА":
        cursor = conn.cursor() 
        name_all = cursor.execute("SELECT Name FROM Kino WHERE Genre = 'РОМАНТИКА'" )
        list_name_same_genre = cursor.fetchall()
        bot.send_message(message.chat.id, "Нажмите на /search")
        for list in list_name_same_genre:
            bot.send_message(message.from_user.id, list)
    elif message.text == "КОМЕДИЯ":
        cursor = conn.cursor() 
        name_all = cursor.execute("SELECT Name FROM Kino WHERE Genre = 'КОМЕДИЯ'" )
        list_name_same_genre = cursor.fetchall()
        bot.send_message(message.chat.id, "Нажмите на /search")
        for list in list_name_same_genre:
            bot.send_message(message.from_user.id, list)
    elif message.text == "ДРАМА":
        cursor = conn.cursor() 
        name_all = cursor.execute("SELECT Name FROM Kino WHERE Genre = 'ДРАМА'" )
        list_name_same_genre = cursor.fetchall()
        bot.send_message(message.chat.id, "Нажмите на /search")
        for list in list_name_same_genre:
            bot.send_message(message.from_user.id, list)


def kino_name(message):
        
         cursor = conn.cursor()

         sql_url ="SELECT url FROM Kino WHERE Name = '"+ (message.text.upper()) + "'"
         sql_country ="SELECT Country FROM Kino WHERE Name = '"+ (message.text.upper()) + "'"
         sql_description ="SELECT Description FROM Kino WHERE Name = '"+ (message.text.upper()) + "'"
         sql_raiting = "SELECT Raiting FROM Kino WHERE Name = '"+ (message.text.upper()) + "'"
         sql_trailer ="SELECT Trailer FROM Kino WHERE Name = '"+ (message.text.upper()) + "'"
         data = cursor.execute(sql_url)
         data = cursor.fetchall()

         i = 0;  
         while i != 1:
             try:
                 bot.send_message(message.from_user.id,  cursor.execute(sql_description))
                 bot.send_message(message.from_user.id,  cursor.execute(sql_trailer)) 
                 bot.send_message(message.chat.id, "Страна:")
                 bot.send_message(message.from_user.id,  cursor.execute(sql_country)) 
                 bot.send_message(message.chat.id, "Кинопоиск рейтинг:")
                 bot.send_message(message.from_user.id,  cursor.execute(sql_raiting))
                 bot.send_message(message.from_user.id,  cursor.execute(sql_url))  
                 i = 1;
             except :
                 bot.send_message(message.from_user.id, "В базе данных не найдена или же вы неправильно ввели, проверьте что лишные пробелы не поставил. Чтобы начать искать /search")
                 i = 1;
                 
                

@bot.callback_query_handler( func = lambda call: True)



def answer(call):

    if call.data == 'genre':
        markup_inline1 = types.InlineKeyboardMarkup()
        item_genre1 = types.InlineKeyboardButton(text = 'УЖАСЫ', callback_data = 'УЖАСЫ')
        item_genre2 = types.InlineKeyboardButton(text = 'ФАНТАСТИКА', callback_data = 'ФАНТАСТИКА')
        item_genre3 = types.InlineKeyboardButton(text = 'БИОГРАФИЯ', callback_data = 'БИОГРАФИЯ')
        item_genre4 = types.InlineKeyboardButton(text = 'РОМАНТИКА', callback_data = 'РОМАНТИКА')
        item_genre5 = types.InlineKeyboardButton(text = 'КОМЕДИЯ', callback_data = 'КОМЕДИЯ')
        item_genre6 = types.InlineKeyboardButton(text = 'ДРАМА' , callback_data =  'ДРАМА')
        item_genre7 = types.InlineKeyboardButton(text = 'КРИМИНАЛ', callback_data = 'КРИМИНАЛ')
        item_back5 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'start')
        markup_inline1.add(item_genre1,item_genre2,item_genre3,item_genre4,item_genre5,item_genre6,item_genre7,item_back5)
        bot.send_message(call.from_user.id, "Выберите по жанрам ", reply_markup = markup_inline1)

    elif call.data == "start":
        markup_inline_start = types.InlineKeyboardMarkup()
      
        item_call_1 = types.InlineKeyboardButton(text = 'Жанры', callback_data = 'genre')
        item_call_2 = types.InlineKeyboardButton(text = 'Искать фильмы по подборкам', callback_data = 'list_movie_by_same')
        markup_inline_start.add(item_call_1,item_call_2)

        bot.send_message(call.from_user.id, "Choose", reply_markup = markup_inline_start)

    elif call.data == 'list_movie_by_same':
        markup_inline_same = types.InlineKeyboardMarkup()
        item_list_same1 = types.InlineKeyboardButton(text = 'Гарри Поттер', callback_data = 'Гарри Поттер')
        item_list_same2 = types.InlineKeyboardButton(text = 'Властелин колец', callback_data = 'Властелин колец')
        item_list_same3 = types.InlineKeyboardButton(text = 'Человек паук', callback_data = 'Человек паук')
        item_back4 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'start')
        markup_inline_same.add(item_list_same1,item_list_same2,item_list_same3,item_back4)
        bot.send_message(call.from_user.id, "Подборка фильмов", reply_markup = markup_inline_same)


  
    elif call.data == 'Гарри Поттер':
        markup_inline_same_harry = types.InlineKeyboardMarkup()
        item_list_harry1 = types.InlineKeyboardButton(text = 'Дары Смерти 2', callback_data = 'ГПИДС2')
        item_list_harry2 = types.InlineKeyboardButton(text = 'Дары Смерти 1', callback_data = 'ГПИДС1')
        item_list_harry3 = types.InlineKeyboardButton(text = 'Тайная Комната', callback_data = 'ГПИТК')
        item_list_harry4 = types.InlineKeyboardButton(text = 'Узник Азкабана', callback_data = 'ГПИУА')
        item_list_harry5 = types.InlineKeyboardButton(text = 'Кубок Огня', callback_data = 'ГПИКО')
        item_list_harry6 = types.InlineKeyboardButton(text = 'Принц Полукровка', callback_data = 'ГПИПП')
        item_list_harry7 = types.InlineKeyboardButton(text = 'Орден Феникса', callback_data = 'ГПИОФ')
        item_list_harry8 = types.InlineKeyboardButton(text = 'Философский Камень', callback_data = 'ГПИФК')
        item_back1 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'list_movie_by_same')
        markup_inline_same_harry.add(item_list_harry1,item_list_harry2,item_list_harry3,item_list_harry4,item_list_harry5,item_list_harry6,item_list_harry7,item_list_harry8,item_back1)
        bot.send_message(call.from_user.id, "Все фильмы по Гарри Поттеру", reply_markup = markup_inline_same_harry)
    elif call.data == 'Властелин колец':
        markup_inline_same_kolec = types.InlineKeyboardMarkup()
        item_list_kolec1 = types.InlineKeyboardButton(text = 'Братство кольца', callback_data = 'ВС:БК')
        item_list_kolec2 = types.InlineKeyboardButton(text = 'Две крепости', callback_data = 'ВС:ДК')
        item_list_kolec3 = types.InlineKeyboardButton(text = 'Возвращение короля', callback_data = 'ВС:ВК')
        item_back2 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'list_movie_by_same')
        markup_inline_same_kolec.add(item_list_kolec1,item_list_kolec2,item_list_kolec3,item_back2)
        bot.send_message(call.from_user.id, "Все фильмы по Властелину колец", reply_markup = markup_inline_same_kolec)
    elif call.data == 'Человек паук':
        markup_inline_same_spider = types.InlineKeyboardMarkup()
        item_list_spider1 = types.InlineKeyboardButton(text = 'Вдали от Дома', callback_data = 'ЧЕЛОВЕК ПАУК ВДАЛИ ОТ ДОМА')
        item_list_spider2 = types.InlineKeyboardButton(text = 'Человек паук ', callback_data = 'ЧЕЛОВЕК ПАУК')
        item_list_spider3 = types.InlineKeyboardButton(text = 'Человек паук 2', callback_data = 'ЧЕЛОВЕК ПАУК 2')
        item_list_spider4 = types.InlineKeyboardButton(text = 'Человек Паук 3', callback_data = 'ЧЕЛОВЕК ПАУК 3')
        item_list_spider5 = types.InlineKeyboardButton(text = 'Новый Человек Паук', callback_data = 'НОВЫЙ ЧЕЛОВЕК ПАУК')
        item_list_spider6 = types.InlineKeyboardButton(text = 'Новый Человек Паук : Высокое напряжение', callback_data = 'НЧП:ВН')
        item_back3 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'list_movie_by_same')
        markup_inline_same_spider.add(item_list_spider1,item_list_spider2,item_list_spider3,item_list_spider4,item_list_spider5,item_list_spider6,item_back3)
        bot.send_message(call.from_user.id, "Все фильмы по Властелину колец", reply_markup = markup_inline_same_spider)


    
    elif call.data == 'УЖАСЫ':
        
        markup_inlinehorror = types.InlineKeyboardMarkup()
        item_h1 = types.InlineKeyboardButton(text = 'Оно 2', callback_data = 'ОНО 2')
        item_back6 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre')
        markup_inlinehorror.add(item_h1,item_back6)
        bot.send_message(call.from_user.id, "Все фильмы по жанру ужас", reply_markup = markup_inlinehorror)
        
        
    
    elif call.data == 'ФАНТАСТИКА':
     
        markup_inlinefanta = types.InlineKeyboardMarkup()
        item_f1 = types.InlineKeyboardButton(text = 'Логан', callback_data = 'ЛОГАН')
        item_f2 = types.InlineKeyboardButton(text = 'Призрачный патруль', callback_data = 'ПРИЗРАЧНЫЙ ПАТРУЛЬ')
        item_f3 = types.InlineKeyboardButton(text = 'Гарри Поттер и Дары Смерти часть 2', callback_data = 'ГПИДС2')
        item_f4 = types.InlineKeyboardButton(text = 'Аквамен', callback_data = 'АКВАМЕН')
        item_f5 = types.InlineKeyboardButton(text = 'Гарри Поттер и Тайная Комната', callback_data = 'ГПИТК') 
        item_f6 = types.InlineKeyboardButton(text = 'Варкрафт', callback_data = 'ВАРКРАФТ')
        item_f7 = types.InlineKeyboardButton(text = 'Гарри Поттер и Узник Азкабана', callback_data = 'ГПИУА')
        item_f8 = types.InlineKeyboardButton(text = 'Гарри Поттер и Кубок Огня', callback_data = 'ГПИКО')
        item_f9 = types.InlineKeyboardButton(text = 'Гарри Поттер и Орден Феникса', callback_data = 'ГПИОФ')
        item_f10 = types.InlineKeyboardButton(text = 'Гарри Поттер и Принц Полукровка', callback_data = 'ГПИПП')
        item_f11 = types.InlineKeyboardButton(text = 'Гарри Поттер и Дары Смерти часть 1', callback_data = 'ГПИДС1')
        item_f12 = types.InlineKeyboardButton(text = 'Властелин колец : Братство кольца', callback_data = 'ВС:БК')
        item_f13 = types.InlineKeyboardButton(text = 'Властелин колец : Две крепости', callback_data = 'ВС:ДК')
        item_f14 = types.InlineKeyboardButton(text = 'Властелин колец : Возвращение короля', callback_data = 'ВС:ВК')
        item_f15 = types.InlineKeyboardButton(text = 'Человек Паук Вдали от Дома', callback_data = 'ЧЕЛОВЕК ПАУК ВДАЛИ ОТ ДОМА')
        item_f16 = types.InlineKeyboardButton(text = 'Человек Паук', callback_data = 'ЧЕЛОВЕК ПАУК')
        item_f17 = types.InlineKeyboardButton(text = 'Человек Паук 2', callback_data = 'ЧЕЛОВЕК ПАУК 2')
        item_f18 = types.InlineKeyboardButton(text = 'Гарри Поттер и Философский Камень', callback_data = 'ГПИФК')
        item_f19 = types.InlineKeyboardButton(text = 'Человек Паук 3', callback_data = 'ЧЕЛОВЕК ПАУК 3')
        item_f20 = types.InlineKeyboardButton(text = 'Новый Человек Паук', callback_data = 'НОВЫЙ ЧЕЛОВЕК ПАУК')
        item_f21 = types.InlineKeyboardButton(text = 'Новый Человек Паук : Высокое напряжение', callback_data = 'НЧП:ВН')
        item_back7 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre')
        markup_inlinefanta.add(item_f1,item_f2,item_f3,item_f4,item_f5,item_f6,item_f7,item_f8,item_f9,item_f10,item_f11,item_f12,item_f13,item_f14,item_f15,item_f16,item_f17,item_f18,item_f19,item_f20,item_f21,item_back7)
        bot.send_message(call.from_user.id, "Все фильмы по жанру фантастика", reply_markup = markup_inlinefanta)

    elif call.data == 'БИОГРАФИЯ':
     
        markup_inlinebio = types.InlineKeyboardMarkup()
        item_b1 = types.InlineKeyboardButton(text = 'Ford против Ferrari', callback_data = 'FORD ПРОТИВ FERRARI')
        item_back8 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre')
        markup_inlinebio.add(item_b1,item_back8)
        bot.send_message(call.from_user.id, "Все фильмы по жанру биография", reply_markup = markup_inlinebio)

    elif call.data == 'РОМАНТИКА':
        markup_inlineromantic = types.InlineKeyboardMarkup()
        item_roma1 =  types.InlineKeyboardButton(text = 'Аладдин', callback_data = 'АЛАДДИН')
        item_roma2 = types.InlineKeyboardButton(text = 'Загадочная история Бенджамина Баттона', callback_data = 'БАТТОНА')
        item_back9 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre')
        markup_inlineromantic.add(item_roma1,item_roma2,item_back9)
        bot.send_message(call.from_user.id, "Все фильмы по жанру романтика", reply_markup = markup_inlineromantic)

    elif call.data == 'КОМЕДИЯ':
        
        markup_inlinecomedy = types.InlineKeyboardMarkup()
        item_c1 = types.InlineKeyboardButton(text = 'Один дома', callback_data = 'ОДИН ДОМА')
        item_c2 = types.InlineKeyboardButton(text = 'Каникулы off-line ', callback_data = 'КАНИКУЛЫ OFF-LINE ')
        item_c3 = types.InlineKeyboardButton(text = 'Superнянь', callback_data = 'SUPERНЯНЬ')
        item_c4 = types.InlineKeyboardButton(text = 'Типа копы', callback_data = 'ТИПА КОПЫ')
        item_c5 = types.InlineKeyboardButton(text = 'Тысяча слов', callback_data = 'ТЫСЯЧА СЛОВ')
        item_c6 = types.InlineKeyboardButton(text = 'Почему он?', callback_data = 'ПОЧЕМУ ОН?')
        item_back10 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre')
        markup_inlinecomedy.add(item_c1,item_c2,item_c3,item_c4,item_c5,item_c6,item_back10)
        bot.send_message(call.from_user.id, "Все фильмы по жанру комедия", reply_markup = markup_inlinecomedy)

    elif call.data == 'ДРАМА':
      
        markup_inlinedrama = types.InlineKeyboardMarkup()
        item_d1 = types.InlineKeyboardButton(text = 'Двадцать одно', callback_data = 'ДВАДЦАТЬ ОДНО')
        item_back11 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre')
        markup_inlinedrama.add(item_d1,item_back11)
        bot.send_message(call.from_user.id, "Все фильмы по жанру драма", reply_markup = markup_inlinedrama)

    elif call.data == 'КРИМИНАЛ':
        
        markup_inlinecriminal = types.InlineKeyboardMarkup()
        item_cri1 = types.InlineKeyboardButton(text = 'Ирландец', callback_data = 'ИРЛАНДЕЦ')
        item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre')
        markup_inlinecriminal.add(item_cri1,item_back12)
        bot.send_message(call.from_user.id, "Все фильмы по жанру криминал", reply_markup = markup_inlinecriminal)




   

    else:
        cursor = conn.cursor()
        sql_url = "SELECT url FROM Kino WHERE Name = '" + call.data + "'"
        sql_country = "SELECT Country FROM Kino WHERE Name = '" + call.data + "'"
        sql_description = "SELECT Description FROM Kino WHERE Name = '" + call.data + "'"
        sql_raiting = "SELECT Raiting FROM Kino WHERE Name = '" + call.data + "'"
        sql_trailer = "SELECT Trailer FROM Kino WHERE Name = '" + call.data + "'"
        data = cursor.execute(sql_url)
        data = cursor.fetchall()

        i = 0;  
        while i != 1:
            try:
                bot.send_message(call.from_user.id, cursor.execute(sql_description))  
                bot.send_message(call.from_user.id, cursor.execute(sql_trailer))  

                bot.send_message(call.from_user.id, "Страна:")
                bot.send_message(call.from_user.id, cursor.execute(sql_country))  
                bot.send_message(call.from_user.id, "Кинопоиск рейтинг:")
                bot.send_message(call.from_user.id, cursor.execute(sql_raiting))  

                bot.send_message(call.from_user.id, cursor.execute(sql_url))  
                i = 1;
            except:
                bot.send_message(call.from_user.id,
                                 "В базе данных не найдена или же вы неправильно ввели, проверьте что лишние пробелы не поставили. Чтобы начать искать по названию /search")
                i = 1;

conn.commit()

bot.polling( none_stop = True, interval = 1 )
