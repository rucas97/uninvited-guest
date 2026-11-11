define host = Character("میزبان", color="#F5EBD8")
define khaleh = Character("خاله نسرین", color="#D4A843")

image khaleh neutral = "images/khaleh/neutral.png"
image khaleh happy = "images/khaleh/happy.png"
image khaleh angry = "images/khaleh/angry.png"
image khaleh shocked = "images/khaleh/shocked.png"

default reputation = 100
default blood_pressure = 0

# This tells Ren'Py how to size and place the character
transform char_right:
    xalign 0.8
    yalign 1.0
    zoom 0.6

label start:
    "ساعت ۷ شب است. شام آماده است. زنگ در به صدا درمی‌آید..."

    show khaleh neutral at char_right
    with dissolve

    khaleh "شنیدم کار جدید پیدا کردی! کار واقعیه یا یکی از اون کارهای کامپیوتری؟"

    menu:
        "تعارف کن":
            $ reputation += 10
            $ blood_pressure += 15
            host "کار فوق‌العاده‌ایه خاله. چای بیشتری میل داری؟"
            show khaleh happy at char_right
            khaleh "یک ساعت دیگه می‌مونم."
            jump the_end

        "صادق باش":
            $ reputation -= 15
            $ blood_pressure -= 10
            host "از رضا بیشتر درمیارم خاله. و خونه کار می‌کنم."
            show khaleh angry at char_right
            khaleh "رسوایی! مادرت می‌فهمه."
            jump the_end

label the_end:
    "در ادامه..."
    return
