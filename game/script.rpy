define host = Character("میزبان", color="#F5EBD8")
define khaleh = Character("خاله نسرین", color="#D4A843")

default reputation = 100
default blood_pressure = 0

label start:
    scene bg livingroom
    "ساعت ۷ شب است. شام آماده است. زنگ در به صدا درمی‌آید..."

    show khaleh neutral
    khaleh "شنیدم کار جدید پیدا کردی! کار واقعیه یا یکی از اون کارهای کامپیوتری؟"

    menu:
        "تعارف کن":
            $ reputation += 10
            $ blood_pressure += 15
            host "کار فوق‌العاده‌ایه خاله. چای بیشتری میل داری؟"
            khaleh "یک ساعت دیگه می‌مونم."
            jump the_end

        "صادق باش":
            $ reputation -= 15
            $ blood_pressure -= 10
            host "از رضا بیشتر درمیارم خاله. و خونه کار می‌کنم."
            khaleh "رسوایی! مادرت می‌فهمه."
            jump the_end

label the_end:
    "در ادامه..."
    return
