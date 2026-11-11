define host = Character("میزبان", color="#F5EBD8")
define khaleh = Character("خاله نسرین", color="#D4A843")
define cat_char = Character("گربه", color="#8FB8A8")

image bg livingroom = Transform("images/backgrounds/livingroom.png", xysize=(1920, 1080))

image khaleh neutral = "images/khaleh/neutral.png"
image khaleh happy = "images/khaleh/happy.png"
image khaleh angry = "images/khaleh/angry.png"
image khaleh shocked = "images/khaleh/shocked.png"
image cat neutral = "images/cat/cat.png"

# --- WALKING ANIMATION DEFINITION (Sped up to 0.06s per frame) ---
image khaleh walking:
    "images/khaleh/walk/walk_0.gif"
    pause 0.06
    "images/khaleh/walk/walk_1.gif"
    pause 0.06
    "images/khaleh/walk/walk_2.gif"
    pause 0.06
    "images/khaleh/walk/walk_3.gif"
    pause 0.06
    "images/khaleh/walk/walk_4.gif"
    pause 0.06
    "images/khaleh/walk/walk_5.gif"
    pause 0.06
    "images/khaleh/walk/walk_6.gif"
    pause 0.06
    "images/khaleh/walk/walk_7.gif"
    pause 0.06
    "images/khaleh/walk/walk_8.gif"
    pause 0.06
    repeat

default reputation = 100
default blood_pressure = 0

transform char_right_breathe:
    xalign 0.85
    yalign 1.0
    xanchor 0.5
    yanchor 1.0
    zoom 0.7
    block:
        linear 1.5 zoom 0.72
        linear 1.5 zoom 0.7
        repeat

# NEW: Walk from left to right. Slowed down to 4.5 seconds so it matches the steps.
transform walk_left_to_right:
    xalign -0.4
    yalign 1.0
    xanchor 0.5
    yanchor 1.0
    zoom 3.4
    linear 4.5 xalign 0.85

label start:
    show screen meters_hud
    
    scene bg livingroom
    with fade

    "ساعت ۷ شب است. شام آماده است. زنگ در به صدا درمی‌آید..."

    # 1. She walks in from the left
    show khaleh walking at walk_left_to_right
    
    # 2. Wait for the walk to finish
    pause 4.5
    
    # 3. Instantly snap to neutral without fading out
    show khaleh neutral at char_right_breathe

    # 4. She asks the question
    khaleh "شنیدم کار جدید پیدا کردی! کار واقعیه یا یکی از اون کارهای کامپیوتری؟"

    menu:
        "تعارف کن":
            $ reputation = min(100, reputation + 10)
            $ blood_pressure = min(100, blood_pressure + 20) # Lowered from 40 to 20
            host "کار فوق‌العاده‌ایه خاله. چای بیشتری میل داری؟"
            show khaleh neutral at char_right_breathe
            khaleh "یک ساعت دیگه می‌مونم."
            jump cat_arrives

        "صادق باش":
            $ reputation = max(0, reputation - 50)
            $ blood_pressure = max(0, blood_pressure - 10)
            host "از رضا بیشتر درمیارم خاله. و خونه کار می‌کنم."
            show khaleh angry at char_right_breathe
            khaleh "رسوایی! مادرت می‌فهمه."
            jump cat_arrives

label cat_arrives:
    hide khaleh
    with dissolve
    
    "در همین لحظه، یک گربه خیابانی از در نیمه‌باز وارد می‌شود..."
    
    show cat neutral at char_right_breathe
    with dissolve
    
    cat_char "میو."
    
    "گربه با بی‌خیالی روی مبل می‌پرد و به شما زل می‌زند."
    
    $ blood_pressure = min(100, blood_pressure + 20)
    
    menu:
        "نوازشش کن":
            $ reputation = min(100, reputation + 15)
            $ blood_pressure = max(0, blood_pressure - 10)
            "گربه را نوازش می‌کنی. آرام می‌شود و خرخر می‌کند."
            cat_char "میو میو."
            jump cat_end

        "نادیده بگیر":
            $ reputation = max(0, reputation - 10)
            $ blood_pressure = min(100, blood_pressure + 10)
            "گربه را نادیده می‌گیری. او با عصبانیت به تو زل می‌زند."
            cat_char "میو!"
            jump cat_end

        "بهش غذا بده":
            $ reputation = min(100, reputation + 5)
            $ blood_pressure = max(0, blood_pressure - 5)
            "تکه‌ای غذا به گربه می‌دهی. با خوشحالی می‌خورد."
            cat_char "میو."
            jump cat_end

label cat_end:
    "فشار خونت بالا می‌رود..."
    return
