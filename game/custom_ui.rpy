transform emoji_bounce:
    block:
        linear 0.6 zoom 1.15
        linear 0.6 zoom 1.0
        repeat

transform bp_shake:
    block:
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        repeat

screen reputation_hud():
    zorder 100
    frame:
        align (0.02, 0.02)
        background "#1B4D4DCC"
        padding (20, 20)
        hbox:
            spacing 15
            text "آبرو:" size 40 color "#F5EBD8" font "fonts/Vazirmatn-Regular.ttf" yalign 0.5
            if reputation >= 70:
                text "😎" size 50 at emoji_bounce
            elif reputation >= 30:
                text "😐" size 50 at emoji_bounce
            else:
                text "😰" size 50 at emoji_bounce

screen blood_pressure_hud():
    zorder 100
    frame:
        align (0.98, 0.02)
        background "#3D2B3DCC"
        padding (20, 20)
        vbox:
            spacing 10
            text "فشار خون" size 30 color "#F5EBD8" font "fonts/Vazirmatn-Regular.ttf" xalign 0.5
            fixed:
                xsize 400
                ysize 40
                if blood_pressure >= 70:
                    at bp_shake
                bar:
                    value blood_pressure # This directly links to the variable now
                    range 100
                    xsize 400
                    ysize 40
                    left_bar Solid("#C46B4A")
                    right_bar Solid("#222222")
                    thumb None
                    thumb_shadow None

screen meters_hud():
    use reputation_hud
    use blood_pressure_hud

screen main_menu():
    tag menu
    add Solid("#1B1B1B")
    vbox:
        align (0.5, 0.5)
        spacing 30
        text "مهمان ناخوانده" size 100 color "#D4A843" xalign 0.5 font "fonts/Vazirmatn-Regular.ttf"
        null height 50
        textbutton "شروع بازی":
            action Start()
            xalign 0.5
            text_size 50
            text_color "#F5EBD8"
            text_hover_color "#D4A843"
        textbutton "بارگذاری":
            action ShowMenu("load")
            xalign 0.5
            text_size 50
            text_color "#F5EBD8"
            text_hover_color "#D4A843"
        textbutton "تنظیمات":
            action ShowMenu("preferences")
            xalign 0.5
            text_size 50
            text_color "#F5EBD8"
            text_hover_color "#D4A843"
        textbutton "خروج":
            action Quit(confirm=False)
            xalign 0.5
            text_size 50
            text_color "#F5EBD8"
            text_hover_color "#C46B4A"
