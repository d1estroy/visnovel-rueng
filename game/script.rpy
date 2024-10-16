# Declare characters used by this game.
define e = Character(_("Я"), color="#c8ffc8")
define a = Character(_("Юля"), color="#c8c8ff")

define audio.musicst = "music/musicst.mp3"
define audio.msicst = "music/msicst.mp3"
define audio.msst = "music/msst.mp3"

# The game starts here.
label start:

    # Start by playing some music.
    play music musicst

    scene bg airplane
    with fade

    show gg vlad:
        xalign 0.1 yalign 0.2
    e "Смотри, мы, кажется, прилетели!"

    hide gg vlad

    "И верно. Самолет шел на посадку."

    "Из Москвы прямиком в Лондон."

    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "Погоди немного, не вставай со своего места."
    a "Ты же знаешь, что местные жители будут разговаривать на своем родном языке?"

    show gg vlad:
        xalign 0.1 yalign 0.2
    e "Конечно! Не волнуйся, я знаю некоторые фразы, которые мы прошли во втором классе."

    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "Это отлично! А теперь давай перейдем к новой теме."

    a "Я хочу, чтобы ты запомнил несколько фразовых глаголов."

    a "Это такие глаголы-конструкторы, состоящие из глагола и дополнительного «прицепа» в виде наречия или предлога."

    show gg vlad:
        xalign 0.1 yalign 0.2
    e "Сестренка, а зачем они нужны?"

    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "Фразовые глаголы часто используются в речи носителями языка. Ведь ты же хочешь понять, о чем будут разговаривать вокруг тебя?"

    show gg vlad:
        xalign 0.1 yalign 0.2

    e "Конечно, хочу!"

    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "Хорошо, тогда сейчас я расскажу тебе о пяти самых популярных фразовых глаголах."

    show gg vlad:
        xalign 0.1 yalign 0.2
    e "Всего лишь пяти?"

    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "Когда запомнишь эти, мы выучим еще пять других."

    a "Начнем с фразового глагола {b}watch out{/b}. Как думаешь, как он переводится?"

    menu:
        a "Как переводится глагол {b}watch out{/b}?"

        "Смотреть вдаль?":
            jump watchout

        "Берегись!":
            jump watchout


label watchout:
    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "Watch переводится, как смотреть, а out обычно означает движение изнутри наружу."

    a "Несмотря на это, вместе watch out означает 'осторожно!', 'берегись!', 'будь внимательнее!'"

    show gg vlad:
        xalign 0.1 yalign 0.2

    e "То есть если кто-то перебегает дорогу на красный свет, я могу крикнуть 'Watch out!'?"

    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "Да, верно."

    a "Следующий фразовый глагол - {b}be over{/b} - со значением 'завершиться', 'закончиться'."

    show gg vlad:
        xalign 0.1 yalign 0.2

    e "Если я имею в виду, что лето подошло к концу, я скажу..."

    menu:

        "Если я имею в виду, что лето подошло к концу, я скажу..."

        "The summer is over.":
            jump prott

        "The summer be over.":
            jump prott

label prott:

    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "В предложении форма be меняется на am, is, are в зависимости от подлежащего."

    a "Поэтому правильно будет сказать 'The summer is over'."

    a "Следующий фразовый глагол - {b}come on{/b} - в значении 'приходить', 'проходить', 'давай! / брось! /пошли! /кончай!'"

    show gg vlad:
        xalign 0.1 yalign 0.2

    e "Я помню, наша учительница по английскому однажды сказала 'Come on, let's go!', когда мы не хотели идти в столовую."

    e "Так она имела в виду..."

    menu:

        "'Come on, let's go' означало..."

        "Давайте, пойдемте!":
            jump casio

        "Идёмте!":
            jump casio

label casio:

    show gg julia at right:
        xalign 0.8 yalign 0.2

    a "Да, правильно! Учительница хотела, чтобы вы пошли вместе с ней."

    a "Четвертый фразовый глагол - {b}find out{/b} – со значением 'найти', 'обнаружить', 'выяснить', 'разузнать'."

    a "Как будет по-английски 'Полиция не может выяснить, кто преступник'."

    menu:

        "'Полиция не может выяснить, кто преступник...'"

        "Police can't find out who the criminal is.":
            jump prottеs

        "Police can't watch out who the criminal is.":
            jump prottеs

label prottеs:
        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Правильный ответ - Police can't find out who the criminal is."

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Ого! Я теперь могу работать в британской полиции!"

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Вырастешь, станешь! Кстати, 'вырасти' - это еще один фразовый глагол '{b}grow up{/b}'."

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "То есть если я хочу сказать, что этот цветок скоро вырастет, мне нужно использовать фразовый глагол '{b}grow up{/b}...'"

        e "Хмм, grow up..."

        menu:

            "'Этот цветок скоро вырастет...'"

            "This flower will be over soon.":
                jump casion

            "This flower will grow up soon.":
                jump casion

label casion:

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "The flower will grow up soon! Вот этот вариант правильный!"

        a "А ты отлично справляешься!"

        a "Давай проверим, как хорошо ты запомнил новые слова!"

        a "Помнишь, как переводится be over?"

        menu:

            "Помнишь, как переводится be over?"

            "Закончиться":

                "Правильно! Молодец!"

            "Идёмте":
                "Неверно. Be over - закончиться. Помнишь пример с оконченным летом: The summer is over."

            "Выяснить":
                "Неверно. Be over - закончиться. Помнишь пример с оконченным летом: The summer is over."



        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Следующий вопрос: как перевести на английский словосочетание 'выяснить правду'?"

        menu:

            "'Выяснить правду...'"

            "Be over the truth":

                "Неверно, дружок. Запомни: find out - найти, выяснить. Помнишь пример 'Police can't find out who the criminal is'?"

            "Find out the truth":
                "А у тебя хорошая память!"

            "Grow up the truth":
                "Неверно, дружок. Запомни: find out - найти, выяснить. Помнишь пример 'Police can't find out who the criminal is'?"




        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Теперь к следующему вопросу?"

        a "Как перевести предложение 'I grew up in Russia'?"

        menu:

            "'I grew up in Russia...'"

            "Я выяснил в России.":

                "Grew up - это глагол grow up, но только в прошедшем времени. I grew up переводится как 'Я вырос'."

            "Я вырос в России.":

                "Отлично! Все верно!"

            "Я пошел в Россию.":

                "Grew up - это глагол grow up, но только в прошедшем времени. I grew up переводится как 'Я вырос'."


        show gg julia at right:
            xalign 0.8 yalign 0.2


        a "Теперь можно выучить следующие пять глаголов?"

        a "Не волнуйся, если что-то не до конца запомнил. Мы обязательно попрактикуемся еще!"

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Это было весело!"

        e "Смотри, мы уже приземлились!"

        pause 5

        scene bg proh
        with fade

        pause 3

        'Командир воздушного судна'"Уважаемые пассажиры!"

        'Командир воздушного судна' "Наш самолет готовится совершить посадку в аэропорту города Лондон."

        'Командир воздушного судна' "Пристегните ремни безопасности и не вставайте со своих кресел до специального объявления."

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Ого! Сестренка, ты слышала?"

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Да. Только не отстегивай ремень!"

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Раз у нас есть еще 10 минут, может, выучим следующие 5 фразовых глаголов?"

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Точно! У меня как раз на примете есть несколько интресных конструкций!"

        a "'{b}Calm down{/b}' - это фразовый глагол со значением 'успокоиться'."

        a "К примеру, ты можешь сказать собеседнику 'calm down', когда хочешь помочь ему перестать нервничать."

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Получается, если я говорю с малознакомым мне человеком, мне стоит сказать..."

        menu:

            "Когда говорю с малознакомым мне человеком..."

            "Yo, calm down":

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "Конечно, нет! Чтобы проявить вежливость, используй 'please' или 'excuse me'."


            "Please, try to calm down":

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "Конечно! Чтобы проявить вежливость, всегда используй 'please' или 'excuse me'."

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Да, я понял!"

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Следующий фразовый глагол - '{b}give up{/b}'."

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Give up... Что-то знакомое... Кажется, это значит..."

        menu:

            "Give up означает..."

            "Сдаться!":

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "А у тебя хороший кругозор! Молодец!"

            "Бороться!":

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "Почти угадал! Give up означает 'бороться'."

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "С помощью этого фразового глагола ты так же можешь поддержать своего собеседника."

        a "'Не сдавайся, все будет хорошо!' - 'Don't give up, everything will be fine!'"

        a "Всё понял?"

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Да. Понял! Give up - сдаваться, а calm down - успокаиваться!"


        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Еще один фразовый глагол очень часто используется иностранцами - это '{b}look for{/b}'."

        a "Он означает 'искать'."

        a "Если вдруг ты не найдешь меня рядом, всегда можешь подойти к кому-нибудь и сказать..."

        menu:

            "..."

            "Excuse me, I'm looking for my sister. Can you help me, please?":
                jump sister

            "Sorry, I got lost (потерялся), I'm looking for my sister.":
                jump sister

        label sister:

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Верно! Какой догадливый!"

        a "Но я не позволю тебе попасть в такую ситуацию!"

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Зато теперь я знаю, как вести себя в другой стране, если тебя не окажется рядом."

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Следующий фразовый глагол - '{b}run away{/b}' со значением 'убегать'."

        a "Наверное, ты знаком с этой конструкцией."

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "Да, мы выучили 'run away' еще во втором классе."

        e "Но я только сейчас узнал, что это фразовый глагол."

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Отлично. Тогда сможешь перевести фразу: 'Calm down! Don't run away from me!'?"

        menu:

            "'Calm down! Don't run away from me!' переводится, как..."

            "Не сдавайся! Не убегай от меня!":

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "Помнишь фразовый глагол 'calm down' ('успокоиться')?"

                a "Если 'run away' - 'убегать', то 'don't run away' - 'не убегать'."


            "Успокойся! Не убегай от меня!":

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "Отлично. Хорошая память!"


            "Сдавайся! Убегай от меня!":

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "Помнишь фразовый глагол 'calm down' ('успокоиться')?"

                a "Если 'run away' - 'убегать', то 'don't run away' - 'не убегай'."

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "И последний фразовый глагол - это '{b}shut up{/b}' со значением 'заткнуться', 'замолчать'."

        show gg vlad:
            xalign 0.1 yalign 0.2

        e "То есть если один из пассажиров самолета мешает мне спать громкими разговорами, я могу попросить его замолчать фразой 'Can you, please, shut up?'"

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Нет, это будет грубо! Никогда не используй 'shut up' в диалоге с малознакомыми людьми."

        a "В таком случае лучше попроси своего соседа быть немного потише: 'Could you, please, be more quiet. I'm trying to sleep'."

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Теперь давай проверим, как хорошо ты запомнил пройденные слова."

        '...' "Если возникнут трудности, нажми на кнопку '{b}история{/b}' под диалоговым окном."

        '...' "Там ты сможешь напомнить себе определения каждого фразового глагола, которого мы разобрали."

        label question:
        $ answer = "calm down"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'успокоиться'?")
        $ answer = e.strip()

        if answer.lower() == "calm down":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Calm down - успокоиться."


        $ answer = "shut up"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'заткнуться'?")
        $ answer = e.strip()

        if answer.lower() == "shut up":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Shut up - заткнуться."


        $ answer = "look for"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'искать'?")
        $ answer = e.strip()

        if answer.lower() == "look for":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Look for - искать."


        $ answer = "give up"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'сдаться'?")
        $ answer = e.strip()

        if answer.lower() == "give up":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Give up - сдаться."


        $ answer = "run away"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'убегать'?")
        $ answer = e.strip()

        if answer.lower() == "run away":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Run away - убегать."

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Молодец! А у тебя хорошо получается!"

        show gg vlad:
            xalign 0.1 yalign 0.2

        'Я' "Это ведь так интересно!"

        'Я' "Мне нетерпится погворить с кем-то на английском!"

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Смотри, кажется, та девушка на соседнем сидении - иностранка. Весь полет неврничала и дрожала. Кажется, она боится летать на самолете."

        a "Можешь попробовать ее успокоить!"

        show gg vlad:
            xalign 0.1 yalign 0.2

        'Я' "Ладно, я попробую..."

        show gg stranger:
            xalign 0.1 yalign 0.2
        'Незнакомка' "???"

        show gg vlad:
            xalign 0.8 yalign 0.2

        menu:

            "Какой фразовый глаголый подойдет лучше всего?"

            "Miss, try to calm down... Everything will be fine!":
                    show gg stranger:
                        xalign 0.1 yalign 0.2
                    'Незнакомка' "Oh."
                    'Незнакомка' "Ah. Thank you, dear."
                    'Незнакомка' "I'm just scared of flights."

                    menu:

                        "Как продолжить разговор с незнакомкой с использованием другого фразового глагола?"

                        "It will be over soon, miss.":
                            'Незнакомка' "I know."
                            'Незнакомка' "Thank you for your support!"

                            show gg julia at right:
                                xalign 0.8 yalign 0.2

                            a "А ты молодец! Быстро учишься!"

                        "Shut up, please.":

                            show gg stranger:
                                xalign 0.1 yalign 0.2
                            'Незнакомка' "Such a rude young man!"

                            show gg julia at right:
                                xalign 0.8 yalign 0.2

                            a "Ты что! Никогда не используй 'shut up', когда говоришь с незнакомыми людьми!"


            "Miss, excuse me, I'm looking for my sister.":
                show gg stranger:
                    xalign 0.1 yalign 0.2
                'Незнакомка' "Oh."
                'Незнакомка' "Ah. Sorry, dear."
                'Незнакомка' "Can't help you with it."

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "I'm looking for my sister? Ты сидишь рядом со мной и ищешь свою сестру?"
                show gg vlad:
                    xalign 0.1 yalign 0.2
                'Я' "Точно, прости..."

            "Miss, come on. Try to be more quiet!":
                show gg stranger:
                    xalign 0.1 yalign 0.2
                'Незнакомка' "Oh."
                'Незнакомка' "Ah. Sorry, dear."
                'Незнакомка' "Can't seat still, too nervous about the flight."

                show gg julia at right:
                    xalign 0.8 yalign 0.2

                a "Try to be more quiet? Постарайтесь быть потише?"
                show gg vlad:
                    xalign 0.1 yalign 0.2
                'Я' "Ой, неловко вышло, прости..."

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Какой интересный опыт получился, а?"

        show gg vlad:
            xalign 0.1 yalign 0.2

        'Я' "Да! Мне очень понравилось!"

        show gg julia at right:
            xalign 0.8 yalign 0.2

        a "Всё, мы прилетели! Теперь можно вставать со своего места. Пойдем!"


        scene bg airport
        with fade


        play music msicst

        pause 5

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Не могу представить, что мы в другой стране!"

        show gg julia at right:
            xalign 0.9 yalign 0.2

        a "А я не могу представить, во сколько нам обойдется такси до центра!"

        show gg vlad:
            xalign 0.1 yalign 0.2

        'Я' "Если мы поедем втроем, то такси будет стоить дешевле?"

        show gg julia at right:
            xalign 0.9 yalign 0.2

        a "Да, но к чему ты клонишь?"

        show gg vlad:
            xalign 0.1 yalign 0.2

        'Я' "Сейчас узнаешь!"

        "Вы подбежали к незнакомке из самолета."

        "Юля поняла, что вы хотите сделать, и пошла за вами."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Hello!"

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Незнакомка' "Good afternoon! Young man and his...sister?"

        show gg julia:
            xalign 0.1 yalign 0.2
        a "Nice to meet you! My name is Julia, and my brother is Vlad."

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "I'm Tracey. How're you doing?"

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Что она сказала? Спросила, как у нас дела?"

        show gg julia:
            xalign 0.1 yalign 0.2
        a "Да, что-то вроде того."

        a "Well, we think to take a taxi from the airport to downtown."

        a "Do you mind going with us?"

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Сестричка, ты же предлагаешь ей разделить плату за такси?"

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "Of course, I don't mind going with you!"

        'Tracey' "Probably, it would be less expensive!"

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Ничего себе! Она не против!"


        scene bg taxi
        with fade

        pause 5

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Как удачно получилось!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Точно, сегодня наш счастливый день!"

        a "Но, знаешь, у меня есть нехорошее предчувствие. Эта девушка... Я ей не доверяю."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Она выглядит очень безобидно. Тебе просто кажется."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Раз у нас есть немного времени, может, разучим еще пять фразовых глаголов?"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Какой ты любознательный! Хорошо."

        a "'{b}Point out{/b}' - фразовый глагол со значением 'указывать' или 'обращать внимание'."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "То есть я могу использовать глагол 'point out', когда хочу подчеркнуть какую-то мысль в предложении?"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Верно!"

        a "Следующие два фразовых глаголы - антонимы. Знаешь, что это такое?"

        menu:

            "Что такое антонимы?"

            "Слова, одинаковые по значению!":
                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Нет, это слова, противоположные по значению: white - black, fire - water."

            "Слова, противоположные по значению!":
                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Верно!"

        show gg julia:
            xalign 0.8 yalign 0.2

        a "Это фразовые глаголы '{b}sit down{/b}' и '{b}stand up{/b}'. Слышал когда-нибудь?"

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Да! Учительница постоянно начинает урок с этих фраз."

        show gg julia:
            xalign 0.8 yalign 0.2

        a "Sit down обозначает 'сесть', а stand up - наоборот, 'встать'."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Запомнил! Это легко!"

        show gg julia:
            xalign 0.8 yalign 0.2

        a "Еще один простой фразовый глагол - '{b}get back{/b}' - со значением 'вернуться'."

        a "Сможешь спросить меня на английском, когда мы вернемся домой?"

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Попробую!"

        menu:

            "'Когда мы вернемся домой?'"

            "When will we get back home?":
                show gg julia:
                    xalign 0.8 yalign 0.2

                a "Правильно. А ты молодец!"

            "When will we back home?":
                show gg julia:
                    xalign 0.8 yalign 0.2

                a "When will be GET back home - ты забыл произнести основу фразового глагола."

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Еще один фразовый глагол - '{b}make up{/b}'. У него есть несколько значений."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "И одно из них - это наносить макияж!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Правильно! Также этот глагол значит подготовить или организовать что-то."

        a "К примеру, make up a party - организовать вечеринку."

        a "Еще одно интересное значение фразового глагола 'make up' - сочинить, придумать что-то."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Ага, то есть если кто-то выдумал историю, на английском я опишу это, как..."

        menu:

            "'Он выдумал эту историю...'"

            "He made up the story!":
                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Умница! Отлично."

            "He pointed out the story!":
                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Point out - указать на что-то, а выдумать - make up."

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Давай повторим пройденное!"

        '...' "Если возникнут трудности, нажми на кнопку '{b}история{/b}' под диалоговым окном."

        '...' "Там ты сможешь напомнить себе определения каждого фразового глагола, которого мы разобрали."


        $ answer = "make up"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'выдумать'?")
        $ answer = e.strip()

        if answer.lower() == "make up":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Make up - выдумать, составить, краситься."


        $ answer = "sit down"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'сесть'?")
        $ answer = e.strip()

        if answer.lower() == "sit down":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Sit down - сесть."


        $ answer = "get back"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'вернуться'?")
        $ answer = e.strip()

        if answer.lower() == "get back":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Get back - вернуться."


        $ answer = "stand up"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'встать'?")
        $ answer = e.strip()

        if answer.lower() == "stand up":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Stand up - встать."


        $ answer = "point out"
        $ e = renpy.input("Какой фразовый глагол переводится, как 'подчеркивать'?")
        $ answer = e.strip()

        if answer.lower() == "point out":
            "Твой ответ правильный!"
        else:
            "Твой ответ неправильный. Point out - подчеркивать, делать акцент на чем-то."

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "Are you guys learning new English words?"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Exactly!"

        a "Where are you from, by the way?"

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "From Michigan, the US."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Она из США, представляешь? Она хорошо знает английский!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Да, вот и потренируйся. Скажи ей, откуда ты, используя один из фразовых глаголов, который мы прошли."

        menu:

            "Нужно сказать, откуда я, используя один из пройденных фразовых глаголов."

            "I point out from Moscow, Russia.":
                show gg stranger at right:
                    xalign 0.9 yalign 0.2
                'Tracey' "Oh, sorry, what do you mean?"

                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Нужно было использовать фразовый глагол grow up!"

                a "He meant he grew up in Moscow, Russia."


            "I grew up in Moscow, Russia.":
                show gg stranger at right:
                    xalign 0.9 yalign 0.2
                'Tracey' "In Moscow?"

                'Tracey' "Well, a lovely place for living."



            "I'll be back in Moscow, Russia.":
                show gg stranger at right:
                    xalign 0.9 yalign 0.2
                'Tracey' "Well... nice."

                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Нужно было использовать фразовый глагол grow up!"

                a "He meant he grew up in Moscow, Russia."

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "I love Moscow! Nice people live there!"

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "А я говорил, что она хорошая!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "..."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Такси остановилось! Мы, кажется, приехали!"

        scene bg bigben
        with fade

        pause 5

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Ладно, зато дешевле получилось доехать."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Как можно думать о деньгах, когда ты стоишь напротив Биг-Бена?"

        'Я' "Какая красота!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Да, ты прав! Это чудесное место..."

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "I'm sorry for interrupting you but..."

        'Tracey' "I have no friends here and my {b}check in{/b} at Dorsia only at 7 p.m."

        'Tracey' "I don't know what to do with myself the following 5 hours."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "О чем она говорит? Check in - это еще один фразовый глагол?"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Потом объясню."

        a "I see what you mean."

        a "Okay, you can walk with us if you want."

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "Thanks. You are nice people!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Она будет гулять по городу вместе с нами."

        a "А {b}check in{/b} - это фразовый глагол со значением 'заселиться в гостиницу или отель'."

        a "Есть обратный фразовый глагол - {b}check out{/b} - со значением 'освободить номер в гостинице'."

        menu:

            "Спросить про нашу спустницу..."

            "Она упомянула название отеля, в котором будет жить... Можешь вспомнить?":
                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Хм, зачем тебе?"

                show gg vlad:
                    xalign 0.1 yalign 0.2
                'Я' "Обычное любопытство."

                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Отель под название 'Дорсия' или что-то подобное."

            "А в каком отеле остановимся мы?":
                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Узнаешь, как только дойдем до него."

                a "Здесь недалеко, не волнуйся."


        scene bg street
        with fade

        pause 5

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Раз уж мы начали говорить про фразовые глаголы, давай выучим еще парочку."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Хорошо!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "{b}Come across{/b} - фразовый глагол со значением 'встретить кого-то случайно'."

        a "Как перевести предложение 'I came across your teacher today'?"

        menu:

            "'I came across your teacher today?'"

            "Я встретил твоего учителя сегодня.":
                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Верно!"
            "Я наткунулся на твоего учителя сегодня.":
                show gg julia:
                    xalign 0.8 yalign 0.2
                a "Верно!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "{b}Fall for something{/b} - фразовый глагол со значением 'попасть на удочку','дать себя обмануть'."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Интересное значение!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "И последний фразовый глагол на сегодня - 'get away' - в значении 'выбраться на отдых'."

        a "Все понял?"

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Вроде бы да."

        'Я' "Так жарко сегодня..."

        show gg julia:
            xalign 0.8 yalign 0.2
        a "А у нас кончилась вода."

        a "Слушай, мне нужно отойти ненадолго, подержишь мою сумку?"

        show gg vlad:
            xalign 0.1 yalign 0.2

        menu:

            "..."

            "Конечно!":
                jump pertoy

            "Да.":
                jump pertoy

        label pertoy:

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Спасибо."

        a "Знаешь, не хочу оставлять тебя с этой девушкой. Она кажется ненадежной."

        a "Hey, do you know where we can find here a loo?"

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "Yeah, I guess. It seems to be just over there."

        'Tracey' "Hmm..."

        'Tracey' "I think I can accompany you."

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Would be nice."

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "Little boy..."

        'Tracey' "I have only my wallet. Can you put it in your sister's bag?"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Положи ее кошелек в мою сумку. Так будет надежнее."

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "Thank you. Good boy!"

        show gg julia:
            xalign 0.8 yalign 0.2
        a "Мы скоро вернемся. Никуда не уходи."

        show gg vlad:
            xalign 0.1 yalign 0.2
        'Я' "Возвращайся скорее!"

        "Девушки скрылись за углом здания."

        "Вы остались в одиночестве, держащий сумку вашей сестры."

        "Солнце пекло. В голове один за другим всплывали выученные фразовые глаголы."

        "Скучно."

        "Кто-то положил тяжелую руку на ваше плечо."

        show gg police:
            xalign 0.9 yalign 0.2
        'Полицейский' "Is it he?"

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "Yes, it is."

        scene bg police
        with fade

        play music msst

        show gg vlad:
            xalign 0.1 yalign 0.2
        "Вы не поняли, что случилось."

        "Полицейский что-то говорил, что-то говорила незнакомка из самолета."

        "Затем вы вместе пошли в участок."

        "Вы не проронили ни слова по дороге."

        show gg stranger at right:
            xalign 0.9 yalign 0.2
        'Tracey' "Mister officer, he stole my bag. Look at this!"

        "Она указала на сумку в ваших руках."

        "Постепенно вы стали приходить в себя."

        show gg police:
            xalign 0.9 yalign 0.2
        'Полицейский' "Miss, please, calm down. I need to know if the boy can speak."

        'Полицейский' "Hey, do you have a name?"

        menu:

            "Hey, do you have a name?"

            "Vladislav Kravets.":
                show gg police:
                    xalign 0.9 yalign 0.2
                'Полицейский' "Ahh... Thanks God you're not dumb!"
                show gg vlad:
                    xalign 0.1 yalign 0.2
                "Вы не поняли, что случилось."
                show gg stranger at right:
                    xalign 0.9 yalign 0.2
                'Tracey' "I told you! He stole my bag!"
                show gg police:
                    xalign 0.9 yalign 0.2
                'Полицейский' "Miss, please, keep quiet. I have a terrible headache."
                show gg vlad:
                    xalign 0.1 yalign 0.2
                'Я' "..."
                show gg police:
                    xalign 0.9 yalign 0.2
                'Полицейский' "Vladislav, listen, this girl is sure that you stole her property."
                'Полицейский' "Can you give me your bag?"

                menu:

                    "Can you give me your bag?"

                    "Отдать сумку.":
                        show gg police:
                            xalign 0.9 yalign 0.2
                        'Полицейский' "Thank you."
                        "Полицейский открывает сумку и видит бумажник рыжеволосой девушки, стоящей неподалеку."
                        show gg stranger at right:
                            xalign 0.9 yalign 0.2
                        'Tracey' "I told you!"
                        show gg police:
                            xalign 0.9 yalign 0.2
                        'Полицейский' "Miss, keep quiet."
                        'Полицейский' "Do you know this girl?"

                        menu:

                            "Do you know this girl?"

                            "Yes, I know her.":
                                show gg police:
                                    xalign 0.9 yalign 0.2
                                'Полицейский' "Okay, you know her."
                                'Полицейский' "So, I {b}found out{/b} her wallet..."
                                "Он указал на бумажник рыжеволосой девушки."
                                'Полицейский' "In your bag."
                                'Полицейский' "How did it happen?"

                                menu:

                                    "How did it happen?"

                                    "My sister and me {b}came across{/b} this girl in the airport.":
                                        show gg police:
                                            xalign 0.9 yalign 0.2
                                        'Полицейский' "Please, continue."
                                        show gg vlad:
                                            xalign 0.1 yalign 0.2
                                        'Я' "We took a taxi and came here."
                                        'Я' "My sister gave me her bag and went out with this girl."

                                        menu:

                                            "Как продолжить..."

                                            "This girl promised to {b}get back{/b} with my sister!":
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, continue."
                                                show gg vlad:
                                                    xalign 0.1 yalign 0.2
                                                'Я' "This girl gave me this."
                                                "Вы указываете на бумажник."
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Okay, it seems to be true."
                                                show gg stranger at right:
                                                    xalign 0.9 yalign 0.2
                                                'Tracey' "But!!"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "But where is your sister and how can you prove your words?"

                                                menu:

                                                    "Как мне доказать мои слова?"

                                                    "{b}Check out{/b} the cameras!":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Yes, sure!"
                                                        "Полицейский проверяет свой компьютер, делает несколько звонков."
                                                        "Записи с камер видеонаблюдения оказываются у него на столе."
                                                        'Полицейский' "Oh, sorry for misunderstanding!"
                                                        show gg vlad:
                                                            xalign 0.1 yalign 0.2
                                                        'Я' "Thank you."
                                                        "Полицейский отдает вам сумку и отпускает."
                                                        "Рыжеволосая девушка остается в полицейском участке."
                                                        "В ту же минуту к вам подбегает ваша сестра и крепко обнимает."
                                                        "GOOD ENDING"
                                                        "ХОРОШАЯ КОНЦОВКА"

                                                    "{b}Check out{/b} the bag!":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Why?"
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "You don't have profs. The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                            "This girl promised to {b}get away{/b} with my sister!":
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "I'm sorry? Get away? Probably, you mean {b}get back{/b}?"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, continue."
                                                show gg vlad:
                                                    xalign 0.1 yalign 0.2
                                                'Я' "This girl gave me this."
                                                "Вы указываете на бумажник."
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Okay, I don't even know who {b}made up{/b} the story..."
                                                show gg stranger at right:
                                                    xalign 0.9 yalign 0.2
                                                'Tracey' "But!!"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, answer one question so I'll believe you."
                                                'Полицейский' "Do you know this girl's name?"

                                                menu:

                                                    "Как ее зовут?"

                                                    "Stacey.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                                    "I don't know.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                                    "Tracey.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Right."
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "But where is your sister and how can you prove your words?"
                                                        menu:

                                                            "Как мне доказать мои слова?"

                                                            "{b}Check out{/b} the cameras!":
                                                                show gg police:
                                                                    xalign 0.9 yalign 0.2
                                                                'Полицейский' "Yes, sure!"
                                                                "Полицейский проверяет свой компьютер, делает несколько звонков."
                                                                "Записи с камер видеонаблюдения оказываются у него на столе."
                                                                'Полицейский' "Oh, sorry for misunderstanding!"
                                                                show gg vlad:
                                                                    xalign 0.1 yalign 0.2
                                                                'Я' "Thank you."
                                                                "Полицейский отдает вам сумку и отпускает."
                                                                "Рыжеволосая девушка остается в полицейском участке."
                                                                "В ту же минуту к вам подбегает ваша сестра и крепко обнимает."
                                                                "GOOD ENDING"
                                                                "ХОРОШАЯ КОНЦОВКА"

                                                            "{b}Check out{/b} the bag!":
                                                                show gg police:
                                                                    xalign 0.9 yalign 0.2
                                                                'Полицейский' "Why?"
                                                                'Полицейский' "It doesn't make any sense."
                                                                'Полицейский' "You don't have profs. The bag should be returned."
                                                                "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                                "BAD ENDING"
                                                                "ПЛОХАЯ КОНЦОВКА"




                                    "My sister and me {b}came on{/b} this girl in the airport.":
                                        show gg police:
                                            xalign 0.9 yalign 0.2
                                        'Полицейский' "You mean {b}came across{/b}?"
                                        'Полицейский' "Please, continue."
                                        show gg vlad:
                                            xalign 0.1 yalign 0.2
                                        'Я' "We took a taxi and came here."
                                        'Я' "My sister gave me her bag and went out with this girl."

                                        menu:

                                            "Как продолжить..."

                                            "This girl promised to {b}get back{/b} with my sister!":
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, continue."
                                                show gg vlad:
                                                    xalign 0.1 yalign 0.2
                                                'Я' "This girl gave me this."
                                                "Вы указываете на бумажник."
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Okay, it seems to be true."
                                                show gg stranger at right:
                                                    xalign 0.9 yalign 0.2
                                                'Tracey' "But!!"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "But where is your sister and how can you prove your words?"

                                                menu:

                                                    "Как мне доказать мои слова?"

                                                    "{b}Check out{/b} the cameras!":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Yes, sure!"
                                                        "Полицейский проверяет свой компьютер, делает несколько звонков."
                                                        "Записи с камер видеонаблюдения оказываются у него на столе."
                                                        'Полицейский' "Oh, sorry for misunderstanding!"
                                                        show gg vlad:
                                                            xalign 0.1 yalign 0.2
                                                        'Я' "Thank you."
                                                        "Полицейский отдает вам сумку и отпускает."
                                                        "Рыжеволосая девушка остается в полицейском участке."
                                                        "В ту же минуту к вам подбегает ваша сестра и крепко обнимает."
                                                        "GOOD ENDING"
                                                        "ХОРОШАЯ КОНЦОВКА"

                                                    "{b}Check out{/b} the bag!":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Why?"
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "You don't have profs. The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                            "This girl promised to {b}get away{/b} with my sister!":
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "I'm sorry? Get away? Probably, you mean {b}get back{/b}?"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, continue."
                                                show gg vlad:
                                                    xalign 0.1 yalign 0.2
                                                'Я' "This girl gave me this."
                                                "Вы указываете на бумажник."
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Okay, I don't even know who {b}made up{/b} the story..."
                                                show gg stranger at right:
                                                    xalign 0.9 yalign 0.2
                                                'Tracey' "But!!"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, answer one question so I'll believe you."
                                                'Полицейский' "Do you know this girl's name?"

                                                menu:

                                                    "Как ее зовут?"

                                                    "Stacey.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                                    "I don't know.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                                    "Tracey.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Right."
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "But where is your sister and how can you prove your words?"
                                                        menu:

                                                            "Как мне доказать мои слова?"

                                                            "{b}Check out{/b} the cameras!":
                                                                show gg police:
                                                                    xalign 0.9 yalign 0.2
                                                                'Полицейский' "Yes, sure!"
                                                                "Полицейский проверяет свой компьютер, делает несколько звонков."
                                                                "Записи с камер видеонаблюдения оказываются у него на столе."
                                                                'Полицейский' "Oh, sorry for misunderstanding!"
                                                                show gg vlad:
                                                                    xalign 0.1 yalign 0.2
                                                                'Я' "Thank you."
                                                                "Полицейский отдает вам сумку и отпускает."
                                                                "Рыжеволосая девушка остается в полицейском участке."
                                                                "В ту же минуту к вам подбегает ваша сестра и крепко обнимает."
                                                                "GOOD ENDING"
                                                                "ХОРОШАЯ КОНЦОВКА"

                                                            "{b}Check out{/b} the bag!":
                                                                show gg police:
                                                                    xalign 0.9 yalign 0.2
                                                                'Полицейский' "Why?"
                                                                'Полицейский' "It doesn't make any sense."
                                                                'Полицейский' "You don't have profs. The bag should be returned."
                                                                "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                                "BAD ENDING"
                                                                "ПЛОХАЯ КОНЦОВКА"






                            "No, I don't know her.":
                                show gg police:
                                    xalign 0.9 yalign 0.2
                                'Полицейский' "Okay, you don't know her."
                                'Полицейский' "So, I '{b}found out{/b}' her wallet..."
                                "Он указал на бумажник рыжеволосой девушки."
                                'Полицейский' "In your bag."
                                'Полицейский' "How did it happen?"

                                menu:

                                    "Как это произошло?"

                                    "My sister and me {b}came across{/b} this girl in the airport.":
                                        show gg police:
                                            xalign 0.9 yalign 0.2
                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                        'Полицейский' "You told me a minute ago you don't know her."
                                        'Полицейский' "It doesn't make any sense."
                                        'Полицейский' "The bag should be returned."
                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                        "BAD ENDING"
                                        "ПЛОХАЯ КОНЦОВКА"

                                    "Ahh... we {b}checked in{/b} the same hotel.":
                                        show gg police:
                                            xalign 0.9 yalign 0.2
                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                        'Полицейский' "You told me a minute ago you don't know her."
                                        'Полицейский' "It doesn't make any sense."
                                        'Полицейский' "The bag should be returned."
                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                        "BAD ENDING"
                                        "ПЛОХАЯ КОНЦОВКА"



                    "Не отдавать сумку.":
                        show gg police:
                            xalign 0.9 yalign 0.2
                        'Полицейский' "If you don't want to do this the easy way, then I'll just take the bag from you."
                        'Полицейский' "Thank you."
                        "Полицейский открывает сумку и видит бумажник рыжеволосой девушки, стоящей неподалеку."
                        show gg stranger at right:
                            xalign 0.9 yalign 0.2
                        'Tracey' "I told you!"
                        show gg police:
                            xalign 0.9 yalign 0.2
                        'Полицейский' "Miss, keep quiet."
                        'Полицейский' "Do you know this girl?"

                        menu:

                            "Do you know this girl?"

                            "Yes, I know her.":
                                show gg police:
                                    xalign 0.9 yalign 0.2
                                'Полицейский' "Okay, you know her."
                                'Полицейский' "So, I {b}found out{/b} her wallet..."
                                "Он указал на бумажник рыжеволосой девушки."
                                'Полицейский' "In your bag."
                                'Полицейский' "How did it happen?"

                                menu:

                                    "How did it happen?"

                                    "My sister and me {b}came across{/b} this girl in the airport.":
                                        show gg police:
                                            xalign 0.9 yalign 0.2
                                        'Полицейский' "Please, continue."
                                        show gg vlad:
                                            xalign 0.1 yalign 0.2
                                        'Я' "We took a taxi and came here."
                                        'Я' "My sister gave me her bag and went out with this girl."

                                        menu:

                                            "Как продолжить..."

                                            "This girl promised to {b}get back{/b} with my sister!":
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, continue."
                                                show gg vlad:
                                                    xalign 0.1 yalign 0.2
                                                'Я' "This girl gave me this."
                                                "Вы указываете на бумажник."
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Okay, it seems to be true."
                                                show gg stranger at right:
                                                    xalign 0.9 yalign 0.2
                                                'Tracey' "But!!"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "But where is your sister and how can you prove your words?"

                                                menu:

                                                    "Как мне доказать мои слова?"

                                                    "{b}Check out{/b} the cameras!":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Yes, sure!"
                                                        "Полицейский проверяет свой компьютер, делает несколько звонков."
                                                        "Записи с камер видеонаблюдения оказываются у него на столе."
                                                        'Полицейский' "Oh, sorry for misunderstanding!"
                                                        show gg vlad:
                                                            xalign 0.1 yalign 0.2
                                                        'Я' "Thank you."
                                                        "Полицейский отдает вам сумку и отпускает."
                                                        "Рыжеволосая девушка остается в полицейском участке."
                                                        "В ту же минуту к вам подбегает ваша сестра и крепко обнимает."
                                                        "GOOD ENDING"
                                                        "ХОРОШАЯ КОНЦОВКА"

                                                    "{b}Check out{/b} the bag!":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Why?"
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "You don't have profs. The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                            "This girl promised to {b}get away{/b} with my sister!":
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "I'm sorry? Get away? Probably, you mean {b}get back{/b}?"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, continue."
                                                show gg vlad:
                                                    xalign 0.1 yalign 0.2
                                                'Я' "This girl gave me this."
                                                "Вы указываете на бумажник."
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Okay, I don't even know who {b}made up{/b} the story..."
                                                show gg stranger at right:
                                                    xalign 0.9 yalign 0.2
                                                'Tracey' "But!!"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, answer one question so I'll believe you."
                                                'Полицейский' "Do you know this girl's name?"

                                                menu:

                                                    "Как ее зовут?"

                                                    "Stacey.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                                    "I don't know.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                                    "Tracey.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Right."
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "But where is your sister and how can you prove your words?"
                                                        menu:

                                                            "Как мне доказать мои слова?"

                                                            "{b}Check out{/b} the cameras!":
                                                                show gg police:
                                                                    xalign 0.9 yalign 0.2
                                                                'Полицейский' "Yes, sure!"
                                                                "Полицейский проверяет свой компьютер, делает несколько звонков."
                                                                "Записи с камер видеонаблюдения оказываются у него на столе."
                                                                'Полицейский' "Oh, sorry for misunderstanding!"
                                                                show gg vlad:
                                                                    xalign 0.1 yalign 0.2
                                                                'Я' "Thank you."
                                                                "Полицейский отдает вам сумку и отпускает."
                                                                "Рыжеволосая девушка остается в полицейском участке."
                                                                "В ту же минуту к вам подбегает ваша сестра и крепко обнимает."
                                                                "GOOD ENDING"
                                                                "ХОРОШАЯ КОНЦОВКА"

                                                            "{b}Check out{/b} the bag!":
                                                                show gg police:
                                                                    xalign 0.9 yalign 0.2
                                                                'Полицейский' "Why?"
                                                                'Полицейский' "It doesn't make any sense."
                                                                'Полицейский' "You don't have profs. The bag should be returned."
                                                                "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                                "BAD ENDING"
                                                                "ПЛОХАЯ КОНЦОВКА"




                                    "My sister and me {b}came on{/b} this girl in the airport.":
                                        show gg police:
                                            xalign 0.9 yalign 0.2
                                        'Полицейский' "You mean {b}came across{/b}?"
                                        'Полицейский' "Please, continue."
                                        show gg vlad:
                                            xalign 0.1 yalign 0.2
                                        'Я' "We took a taxi and came here."
                                        'Я' "My sister gave me her bag and went out with this girl."

                                        menu:

                                            "Как продолжить..."

                                            "This girl promised to {b}get back{/b} with my sister!":
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, continue."
                                                show gg vlad:
                                                    xalign 0.1 yalign 0.2
                                                'Я' "This girl gave me this."
                                                "Вы указываете на бумажник."
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Okay, it seems to be true."
                                                show gg stranger at right:
                                                    xalign 0.9 yalign 0.2
                                                'Tracey' "But!!"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "But where is your sister and how can you prove your words?"

                                                menu:

                                                    "Как мне доказать мои слова?"

                                                    "{b}Check out{/b} the cameras!":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Yes, sure!"
                                                        "Полицейский проверяет свой компьютер, делает несколько звонков."
                                                        "Записи с камер видеонаблюдения оказываются у него на столе."
                                                        'Полицейский' "Oh, sorry for misunderstanding!"
                                                        show gg vlad:
                                                            xalign 0.1 yalign 0.2
                                                        'Я' "Thank you."
                                                        "Полицейский отдает вам сумку и отпускает."
                                                        "Рыжеволосая девушка остается в полицейском участке."
                                                        "В ту же минуту к вам подбегает ваша сестра и крепко обнимает."
                                                        "GOOD ENDING"
                                                        "ХОРОШАЯ КОНЦОВКА"

                                                    "{b}Check out{/b} the bag!":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Why?"
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "You don't have profs. The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                            "This girl promised to {b}get away{/b} with my sister!":
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "I'm sorry? Get away? Probably, you mean {b}get back{/b}?"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, continue."
                                                show gg vlad:
                                                    xalign 0.1 yalign 0.2
                                                'Я' "This girl gave me this."
                                                "Вы указываете на бумажник."
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Okay, I don't even know who {b}made up{/b} the story..."
                                                show gg stranger at right:
                                                    xalign 0.9 yalign 0.2
                                                'Tracey' "But!!"
                                                show gg police:
                                                    xalign 0.9 yalign 0.2
                                                'Полицейский' "Please, answer one question so I'll believe you."
                                                'Полицейский' "Do you know this girl's name?"

                                                menu:

                                                    "Как ее зовут?"

                                                    "Stacey.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                                    "I don't know.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "It doesn't make any sense."
                                                        'Полицейский' "The bag should be returned."
                                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                        "BAD ENDING"
                                                        "ПЛОХАЯ КОНЦОВКА"

                                                    "Tracey.":
                                                        show gg police:
                                                            xalign 0.9 yalign 0.2
                                                        'Полицейский' "Right."
                                                        'Полицейский' "You told me a minute ago you know her."
                                                        'Полицейский' "But where is your sister and how can you prove your words?"
                                                        menu:

                                                            "Как мне доказать мои слова?"

                                                            "{b}Check out{/b} the cameras!":
                                                                show gg police:
                                                                    xalign 0.9 yalign 0.2
                                                                'Полицейский' "Yes, sure!"
                                                                "Полицейский проверяет свой компьютер, делает несколько звонков."
                                                                "Записи с камер видеонаблюдения оказываются у него на столе."
                                                                'Полицейский' "Oh, sorry for misunderstanding!"
                                                                show gg vlad:
                                                                    xalign 0.1 yalign 0.2
                                                                'Я' "Thank you."
                                                                "Полицейский отдает вам сумку и отпускает."
                                                                "Рыжеволосая девушка остается в полицейском участке."
                                                                "В ту же минуту к вам подбегает ваша сестра и крепко обнимает."
                                                                "GOOD ENDING"
                                                                "ХОРОШАЯ КОНЦОВКА"

                                                            "{b}Check out{/b} the bag!":
                                                                show gg police:
                                                                    xalign 0.9 yalign 0.2
                                                                'Полицейский' "Why?"
                                                                'Полицейский' "It doesn't make any sense."
                                                                'Полицейский' "You don't have profs. The bag should be returned."
                                                                "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                                                "BAD ENDING"
                                                                "ПЛОХАЯ КОНЦОВКА"






                            "No, I don't know her.":
                                show gg police:
                                    xalign 0.9 yalign 0.2
                                'Полицейский' "Okay, you don't know her."
                                'Полицейский' "So, I '{b}found out{/b}' her wallet..."
                                "Он указал на бумажник рыжеволосой девушки."
                                'Полицейский' "In your bag."
                                'Полицейский' "How did it happen?"

                                menu:

                                    "Как это произошло?"

                                    "My sister and me {b}came across{/b} this girl in the airport.":
                                        show gg police:
                                            xalign 0.9 yalign 0.2
                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                        'Полицейский' "You told me a minute ago you don't know her."
                                        'Полицейский' "It doesn't make any sense."
                                        'Полицейский' "The bag should be returned."
                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                        "BAD ENDING"
                                        "ПЛОХАЯ КОНЦОВКА"

                                    "Ahh... we {b}checked in{/b} the same hotel.":
                                        show gg police:
                                            xalign 0.9 yalign 0.2
                                        'Полицейский' "You think you {b}got away{/b} with this?"
                                        'Полицейский' "You told me a minute ago you don't know her."
                                        'Полицейский' "It doesn't make any sense."
                                        'Полицейский' "The bag should be returned."
                                        "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                                        "BAD ENDING"
                                        "ПЛОХАЯ КОНЦОВКА"



            "Я ничего не сделал. Отпустите меня!":
                show gg police:
                    xalign 0.9 yalign 0.2
                'Полицейский' "Ahh... You're a foreigner. Jeez... Why on my shift?"
                show gg stranger at right:
                    xalign 0.9 yalign 0.2
                'Tracey' "I told you! He stole my bag!"
                'Полицейский' "Please. Give me this bag."

                menu:

                    "Я не понимаю, что вы от меня хотите!":
                        jump here

                    "Пожалуйста, отпустите меня!":
                        jump here

                label here:
                show gg police:
                    xalign 0.9 yalign 0.2
                'Полицейский' "That's insane."
                'Полицейский' "It doesn't make any sense."
                'Полицейский' "The bag should be returned."
                "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                "BAD ENDING"
                "ПЛОХАЯ КОНЦОВКА"




            "...":
                show gg police:
                    xalign 0.9 yalign 0.2
                'Полицейский' "Ahh... He's definitely deaf and dumb. Jeez... Why on my shift?"
                show gg stranger at right:
                    xalign 0.9 yalign 0.2
                'Tracey' "I told you! He stole my bag!"
                show gg police:
                    xalign 0.9 yalign 0.2
                'Полицейский' "Please. Give me this bag."

                menu:

                    "...":
                        jump heres

                    "??!":
                        jump heres

                label heres:
                show gg police:
                    xalign 0.9 yalign 0.2
                'Полицейский' "That's insane."
                'Полицейский' "It doesn't make any sense."
                'Полицейский' "The bag should be returned."
                "Полицейский отдает сумку рыжеволосой девушке, и та благополучно уходит."
                "BAD ENDING"
                "ПЛОХАЯ КОНЦОВКА"


























return
