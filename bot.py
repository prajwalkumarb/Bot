import telebot

Token ="6602489930:AAHxDtODMEW-3b6WSzZSouoxN6x2bdvQqZE"

bot= telebot.TeleBot(Token)

#start
@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Welcome to PKB CREATION🧑‍💻 a study Platform📚"
                 """want to learn the course click the below command\n/course 👇\n/help 💁
                """)

#help
@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message,"""
                 \n/course -> 📚want to know about Courses\n \n/free_platform_to_study ->👨🏻‍🏫 free to study\n\n/Udemy_platform_unlocker - 🔓 you can get free Enroll\n\n/contact -> 📞 Contact me
    """)
#menu
@bot.message_handler(['menu'])
def menu(message):
    bot.reply_to(message,"""/start 🙋🏻\n/course 📚\n/help 💁""")


#contact
@bot.message_handler(['contact'])
def contact(message):
    bot.reply_to(message," email 📧: prajwalkumarb9105@gmail.com")
    bot.reply_to(message,"""/menu 👀""")

#chanels
@bot.message_handler(['Udemy_platform_unlocker'])
def platform_unlocker(message):
    bot.reply_to(message,"✒️ NOTE\n\n1). Join the below channel\n2). Search the required course\n3). click the respected link and get free Enroll\n\n channel : https://t.me/Udacity_Skillshare_Coursera_Edx ")
    bot.reply_to(message,"✒️ NOTE\n\n1). Join the below channel\n2). Search the required course\n3). click the respected link and get free Enroll\n\n channel : https://t.me/UdemyKing1")
    bot.reply_to(message,"""/menu 👀""")

#free platforms
@bot.message_handler(['free_platform_to_study'])
def free_platform_to_study(message):
    bot.reply_to(message, "👇🏻==================simplilearn==================\n\nsimplilearn website : https://www.simplilearn.com/skillup-free-online-courses")
    bot.reply_to(message, "👇🏻==================w3school==================\n\nw3school website : https://www.w3schools.com/")
    bot.reply_to(message, "👇🏻==================programiz==================\n\nprogramize website : https://www.programiz.com/")
    bot.reply_to(message,"""/menu 👀""")

# courses
@bot.message_handler(['course'])
def course(message):
    bot.reply_to(message,"""
    This which course do you want to learn
    ----------------------------------------------------
    /Python ->👉🏻 Python is an interpreted, object-oriented, high-level programming language.\n
    /sql -> 👉🏻 SQL is a standard language for storing, manipulating and retrieving data in databases.\n
    /java -> 👉🏻 Java is a programming language and computing platform first released by Sun Microsystems in 1995.\n         
    /api  -> 👉🏻APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols.\n
    Want to Enroll for free Udemy Course click Shelp 👇🏻\n/help 💁
    """)
    bot.reply_to(message,"""/menu 👀""")

@bot.message_handler(['Python'])
def python(message):
    bot.reply_to(message," tutorual link : https://www.w3schools.com/python/")
    bot.reply_to(message,"""/menu 👀""")

@bot.message_handler(['sql'])
def sql(message):
    bot.reply_to(message,"tutorial link : https://www.w3schools.com/sql/")
    bot.reply_to(message,"""/menu 👀""")

@bot.message_handler(['java'])
def java(message):
    bot.reply_to(message,"tutorial link : https://www.w3schools.com/java/")
    bot.reply_to(message,"""/menu 👀""")

@bot.message_handler(['api'])
def api(message):
    bot.reply_to(message," tutorual link : https://www.w3schools.com/js/js_api_intro.asp")
    bot.reply_to(message,"""/menu 👀""")


bot.polling()
