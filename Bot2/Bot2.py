import sqlite3
import telebot
from telebot import types
bot = telebot.TeleBot("5168422705:AAHVU0_vMsT0kGbmSP12b0Oul9_0nNBadMg") 
conn = sqlite3.connect('EF/database211.db', check_same_thread= False)
cursor = conn.cursor()
@bot.message_handler(content_types=['text'])


def start(message):

  

    if message.text == "/start":
        markup_inline = types.InlineKeyboardMarkup()
        item_1 = types.InlineKeyboardButton(text = 'Сериалы', callback_data = 'Сериал')
        item_2 = types.InlineKeyboardButton(text = 'Фильмы', callback_data = 'Фильм')
        markup_inline.add(item_1,item_2)

        bot.send_message(message.chat.id, "Выберите", reply_markup = markup_inline)

    elif message.text == "/group":
          markup_inline_group = types.InlineKeyboardMarkup()
          item_g1 = types.InlineKeyboardButton(text = 'Искать фильмы по подборкам', callback_data = 'list_movie_by_same')
          markup_inline_group.add(item_g1)
          bot.send_message(message.chat.id, "Выберите", reply_markup = markup_inline_group)

    elif message.text =="/help":

        bot.send_message(message.from_user.id, "/search - Поиск фильмов по названию; /start - Для начало выбора между фильмами и сериалами ")





    elif message.text == "Фильм":
        cursor = conn.cursor()
        name_all = cursor.execute("SELECT Name FROM Kino Where Type = 'Фильм'" )
        list_name_same_type = cursor.fetchall()
        bot.send_message(message.chat.id,"Нажмите на /search чтобы искать эти фильмы")
        for list in list_name_same_type:
            bot.send_message(message.from_user.id, list)

    elif message.text == "Сериал":
        cursor = conn.cursor()
        name_all = cursor.execute("SELECT Name FROM Kino Where Type = 'Сериал'" )
        list_name_same_type = cursor.fetchall()
        bot.send_message(message.chat.id,"Нажмите на /search чтобы искать эти сериал")
        for list in list_name_same_type:
            bot.send_message(message.from_user.id, list)

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

    elif message.text == "Фантастика":
         cursor = conn.cursor()
         name_all = cursor.execute("SELECT Name From Kino WHERE Genre = 'Фантастика'" )
         list_name_same_genre = cursor.fetchall()
         bot.send_message(message.chat.id, "Нажмите на /search")
         for list in list_name_same_genre:
             bot.send_message(message.from_user.id, list)

    elif message.text == "Мультфильм":
         cursor = conn.cursor()
         name_all = cursor.execute("SELECT Name From Kino WHERE Genre = 'Мультфильм'" )
         list_name_same_genre = cursor.fetchall()
         bot.send_message(message.chat.id, "Нажмите на /search")
         for list in list_name_same_genre:
             bot.send_message(message.from_user.id, list)
       
      elif message.text == "Аниме":
         cursor = conn.cursor()
         name_all = cursor.execute("SELECT Name From Kino WHERE Genre = 'Аниме'" )
         list_name_same_genre = cursor.fetchall()
         bot.send_message(message.chat.id, "Нажмите на /search")
         for list in list_name_same_genre:
             bot.send_message(message.from_user.id, list)
    elif message.text == "Комедия":
         cursor = conn.cursor()
         name_all = cursor.execute("SELECT Name From Kino WHERE Genre = 'Комедия'" )
         list_name_same_genre = cursor.fetchall()
         bot.send_message(message.chat.id, "Нажмите на /search")
         for list in list_name_same_genre:
             bot.send_message(message.from_user.id, list)
    elif message.text == "Драма":
         cursor = conn.cursor()
         name_all = cursor.execute("SELECT Name From Kino WHERE Genre = 'Драма'" )
         list_name_same_genre = cursor.fetchall()
         bot.send_message(message.chat.id, "Нажмите на /search")
         for list in list_name_same_genre:
             bot.send_message(message.from_user.id, list)

    elif message.text == "Криминал":
         cursor = conn.cursor()
         name_all = cursor.execute("SELECT Name From Kino WHERE Genre = 'Аниме'" )
         list_name_same_genre = cursor.fetchall()
         bot.send_message(message.chat.id, "Нажмите на /search")
         for list in list_name_same_genre:
             bot.send_message(message.from_user.id, list)


    elif message.text == "Детектив":
         cursor = conn.cursor()
         name_all = cursor.execute("SELECT Name From Kino WHERE Genre = 'Детектив'" )
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
         sql_type = "SELECT Type FROM Kino WHERE Name = '"+ (message.text.upper()) + "'"
         

         
         data = cursor.execute(sql_url)
         data = cursor.fetchall()

         i = 0;  
         while i != 1:
             try:
                 bot.send_message(message.from_user.id, cursor.execute(sql_type))
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
        item_back5 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'Фильм')
        markup_inline1.add(item_genre1,item_genre2,item_genre3,item_genre4,item_genre5,item_genre6,item_genre7,item_back5)
        bot.send_message(call.from_user.id, "Выберите по жанрам ", reply_markup = markup_inline1)


    elif call.data == "genre2":
         markup_inline_genre2 = types.InlineKeyboardMarkup()
         item_sngere_1 = types.InlineKeyboardButton(text = 'Фантастика', callback_data = 'Фантастика')
         item_sngere_2 = types.InlineKeyboardButton(text = 'Мультфильм', callback_data = 'Мультфильм')
         item_sngere_3 = types.InlineKeyboardButton(text = 'Комедия', callback_data = 'Комедия')
         item_sngere_4 = types.InlineKeyboardButton(text = 'Аниме', callback_data = 'Аниме')
         item_sngere_5 = types.InlineKeyboardButton(text = 'Драма', callback_data = 'Драма')
         item_sngere_6 = types.InlineKeyboardButton(text = 'Криминал', callback_data = 'Криминал')
         item_sngere_7 = types.InlineKeyboardButton(text ='Детектив', callback_data = 'Детектив')
         item_sngere_8 = types.InlineKeyboardButton(text = 'Военный', callback_data = 'Военный')
         item_back6 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'type')
         markup_inline_genre2.add(item_sngere_1,item_sngere_2,item_sngere_3,item_sngere_4,item_sngere_5,item_sngere_6,item_sngere_7,item_sngere_8,item_back6)
         bot.send_message(call.from_user.id,"Выерите", reply_markup = markup_inline_genre2)
   
    elif call.data == "start":
        markup_inline_start = types.InlineKeyboardMarkup()
        item_call_3 = types.InlineKeyboardButton(text = 'Сериалы', callback_data = 'Сериал')
        item_call_4 = types.InlineKeyboardButton(text = 'Фильмы', callback_data = 'Фильм')
        markup_inline_start.add(item_call_3,item_call_4)

        bot.send_message(call.from_user.id, "Выберите", reply_markup = markup_inline_start)

    elif call.data == "type":
        markup_inline_type = types.InlineKeyboardMarkup()
        item_type1 = types.InlineKeyboardButton(text = 'Сериалы', callback_data = 'Сериал')
        item_type2 = types.InlineKeyboardButton(text = 'Фильмы', callback_data = 'Фильм')
        markup_inline_type.add(item_type1,item_type2)
        bot.send_message(call.from_user.id,"Выберите по типу ", reply_markup = markup_inline_type)

    elif call.data == "Фильм":

         markup_inlinefilm = types.InlineKeyboardMarkup()
         item_f1 = types.InlineKeyboardButton(text = 'Жанры', callback_data = 'genre')
         item_back6 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'type')
         item_g1 = types.InlineKeyboardButton(text = 'Искать фильмы по подборкам', callback_data = 'list_movie_by_same')
         markup_inlinefilm.add(item_f1,item_g1,item_back6)
         bot.send_message(call.from_user.id, "Все фильмы ", reply_markup = markup_inlinefilm)

    elif call.data == "Сериал":
         markup_inlineserial = types.InlineKeyboardMarkup()
         item_s1 = types.InlineKeyboardButton(text = 'Жанры', callback_data = 'genre2')
         item_back6 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'type')
         markup_inlineserial.add(item_s1,item_back6)
         bot.send_message(call.from_user.id, "Все Сериалы", reply_markup = markup_inlineserial)

    elif call.data == 'list_movie_by_same':
        markup_inline_same = types.InlineKeyboardMarkup()
        item_list_same1 = types.InlineKeyboardButton(text = 'Гарри Поттер', callback_data = 'Гарри Поттер')
        item_list_same2 = types.InlineKeyboardButton(text = 'Властелин колец', callback_data = 'Властелин колец')
        item_list_same3 = types.InlineKeyboardButton(text = 'Человек паук', callback_data = 'Человек паук')
        item_back4 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'Фильм')
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

    elif call.data == 'Фантастика':
        markup_inlineFantastika = types.InlineKeyboardMarkup()
        item_cri1 = types.InlineKeyboardButton(text = 'Game Of Thrones', callback_data = 'GOT')
        item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre2')
        markup_inlineFantastika.add(item_cri1,item_back12)
        bot.send_message(call.from_user.id, "Все Сериалы по жанру Фантастика", reply_markup = markup_inlineFantastika)

    elif call.data == 'Мультфильм':
        markup_inlinemult = types.InlineKeyboardMarkup()
        item_m1 = types.InlineKeyboardButton(text = 'Rick and Morty', callback_data = 'Рик и Морти')
        item_m2 = types.InlineKeyboardButton(text = 'Gravity Falls', callback_data = 'Гравити Фолз')
        item_m3 = types.InlineKeyboardButton(text = 'Avatar: The Last Airbende', callback_data = 'Avatar')
        item_m4 = types.InlineKeyboardButton(text = 'Аркейн', callback_data = 'Аркейн')
        item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre2')
        markup_inlinemult.add(item_m1,item_m2,item_m3,item_m4,item_back12)
        bot.send_message(call.from_user.id, "Все Сериалы по жанру Мульфильм", reply_markup =markup_inlinemult)


    elif call.data == 'Комедия':
         markup_inlinekomediya = types.InlineKeyboardMarkup()
         item_k1 = types.InlineKeyboardButton(text = 'Friends', callback_data = 'Friends')
         item_k2 = types.InlineKeyboardButton(text ='Офис', callback_data = 'Офис')
         item_k3 = types.InlineKeyboardButton(text = 'Теория Большого Взрыва', callback_data = 'BigBangT')
         item_k4 = types.InlineKeyboardButton(text = 'Клиника', callback_data = 'Клиника')
         item_k5 = types.InlineKeyboardButton(text = 'Как я встретил вашу маму', callback_data = 'HIMYM')
         item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre2')
         markup_inlinekomediya.add(item_k1,item_k2,item_k3,item_k4,item_k5,item_back12)
         bot.send_message(call.from_user.id, "Все Сериалы по жанру Комедия", reply_markup = markup_inlinekomediya)

    elif call.data == 'Аниме':
         markup_inlineanime = types.InlineKeyboardMarkup()
         item_a1 = types.InlineKeyboardButton(text = 'Attack on Titan', callback_data = 'AOT')
         item_a2 = types.InlineKeyboardButton(text = 'Berserk', callback_data = 'Берсерк')
         item_a3 = types.InlineKeyboardButton(text = 'Cowboy Bebop', callback_data = 'Cowboy Bebop')
         item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre2')
         markup_inlineanime.add(item_a1,item_a2,item_a3,item_back12)
         bot.send_message(call.from_user.id, "Все Сериалы по жанру Аниме", reply_markup =  markup_inlineanime)
    
    
    elif call.data == 'Драма':
         markup_inlineDrama = types.InlineKeyboardMarkup()
         item_d1 = types.InlineKeyboardButton(text = 'Сопрано', callback_data = 'Сопрано')
         item_d2 = types.InlineKeyboardButton(text = 'Доктор Хаус', callback_data = 'Доктор Хаус')
         item_d3 = types.InlineKeyboardButton(text = 'Бестыжие', callback_data = 'Бестыжие')
         item_d4 = types.InlineKeyboardButton(text = 'Гордость и предубеждение', callback_data = 'PaP')
         item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre2')
         markup_inlineDrama.add(item_d1,item_d2,item_d3,item_d4,item_back12)
         bot.send_message(call.from_user.id, "Все Сериалы по жанру Драма", reply_markup =  markup_inlineDrama)
         
    elif call.data == 'Криминал':
         markup_inlineKrim = types.InlineKeyboardMarkup()
         item_kr1 = types.InlineKeyboardButton(text = 'Во все тяжкие', callback_data ='Во все тяжкие')
         item_kr2 = types.InlineKeyboardButton(text = 'Место встречи изменить нельзя', callback_data = 'МВИН')
         item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre2')
         markup_inlineKrim.add(item_kr1,item_kr2,item_back12)
         bot.send_message(call.from_user.id, "Все Сериалы по жанру Криминал", reply_markup = markup_inlineKrim)
         
    elif call.data == 'Детектив':
         markup_inlineDetektiv = types.InlineKeyboardMarkup()
         item_de1 = types.InlineKeyboardButton(text='Шерлок', callback_data = 'Шерлок')
         item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre2')
         markup_inlineDetektiv.add(item_de1,item_back12)
         bot.send_message(call.from_user.id, "Все Сериалы по жанру Детектив", reply_markup = markup_inlineDetektiv)

    elif call.data == 'Военный':
         markup_inlineWar = types.InlineKeyboardMarkup()
         item_w1 = types.InlineKeyboardButton(text='17 Мгновений весны', callback_data = '17spring')
         item_back12 = types.InlineKeyboardButton(text = 'Вернутся назад', callback_data = 'genre2')
         markup_inlineWar.add(item_w1,item_back12)
         bot.send_message(call.from_user.id, "Все Сериалы по жанру Детектив", reply_markup = markup_inlineWar)

    else:
        cursor = conn.cursor()
        sql_url = "SELECT url FROM Kino WHERE Name = '" + call.data + "'"
        sql_country = "SELECT Country FROM Kino WHERE Name = '" + call.data + "'"
        sql_description = "SELECT Description FROM Kino WHERE Name = '" + call.data + "'"
        sql_raiting = "SELECT Raiting FROM Kino WHERE Name = '" + call.data + "'"
        sql_trailer = "SELECT Trailer FROM Kino WHERE Name = '" + call.data + "'"
        sql_type = "SELECT Type FROM Kino WHERE Name = '"+ call.data + "'"
        
        

        data = cursor.execute(sql_url)
        data = cursor.fetchall()

        i = 0;  
        while i != 1:
            try:
                bot.send_message(call.from_user.id, cursor.execute(sql_description))  
                bot.send_message(call.from_user.id, cursor.execute(sql_trailer))  
                bot.send_message(call.from_user.id, cursor.execute(sql_type))

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
