default resumed_music = False  # Safe for rollback
default current_music_file = None
default current_music_pos = 0.0

init python:
    import random

    def init_photo_unlocked():
        if not hasattr(persistent, "photo_unlocked") or not isinstance(persistent.photo_unlocked, dict):
            persistent.photo_unlocked = {i: False for i in range(1, 13)}
        else:
            for i in range(1, 13):
                if i not in persistent.photo_unlocked:
                    persistent.photo_unlocked[i] = False

    init_photo_unlocked()

    photo_descriptions = {
        1: "1/23 Jacko's got on his glasses!",
        2: "2/1 Yazz looks... scary..",
        3: "10/31 Jacko has on his Choso fit!",
        4: "5/3 When we all went to the mall together.",
        5: "5/3 Yazz loves his white liquids!",
        6: "6/17 Micheal said his arm looked weird in this photo. What do you think?",
        7: "8/9 A group photo with all of our heads. Can you guess who's who?",
        8: "?/? Who the FUCK IS THIS!?",
        9: "9/14 Yazz seems really distressed...",
        10: "?/? DEUUEAUGH!",
        11: "11/19 That random firework event we all went to together!",
        12: "?/? The final piece of the puzzle."
    }

    def get_photo_description(i):
        return photo_descriptions.get(i, "No description available.")

    def get_random_basil():
        # 20% chance to return alt image, otherwise return original
        if random.random() < 0.01:
            return "mod_assets/images/photos/fb.png"
        return "mod_assets/images/photos/basil.png"

    config.underlay.append(renpy.Keymap(p=ToggleScreen("photo_album")))

    album_music = "mod_assets/music/album.ogg"

    def play_album_music():
        global current_music_file, current_music_pos, resumed_music

        if renpy.music.get_playing(channel="music") == album_music:
            return

        current_music_file = renpy.music.get_playing(channel="music")
        current_music_pos = renpy.music.get_pos(channel="music") or 0.0
        resumed_music = False

        if current_music_file:
            renpy.music.stop(channel="music", fadeout=2.5)

        renpy.music.play(album_music, channel="music", fadein=1.5, loop=True)

    def resume_previous_music():
        global current_music_file, current_music_pos, resumed_music

        if resumed_music:
            return

        if current_music_file:
            renpy.music.stop(channel="music", fadeout=1.5)
            renpy.music.play(current_music_file, fadein=1.5, loop=True)
            resumed_music = True

    def check_all_photos_unlocked():
        return all(persistent.photo_unlocked.get(i, False) for i in range(1, 13))

    def unlock_photo(number):
        if not hasattr(persistent, "photo_unlocked"):
            persistent.photo_unlocked = {}

        if not isinstance(number, int) or number < 1 or number > 12:
            renpy.notify("Invalid photo number!")

        if not persistent.photo_unlocked.get(number, False):
            persistent.photo_unlocked[number] = True
            _full_photo_path = "mod_assets/images/photos/full/photo[{}].png".format(number)
            renpy.call_in_new_context("show_unlocked_photo", _full_photo_path)
            
            # Check if all photos are unlocked
            if check_all_photos_unlocked():
                ach_unlock('photo_album')

        return

init:
    define gui.font = "mod_assets/fonts/omori.ttf"
    define album_text_color = "#ffffff"
    define album_box_color = "#3d3d3d"
    define album_font_size = 24

init python:
    import renpy.exports as renpy_exports

    def typewriter_text(text, sound=None, delay=0.03):
        for i in range(len(text) + 1):
            renpy_exports.window()
            renpy_exports.say(None, text[:i], interact=False)
            if i < len(text) and sound:
                renpy_exports.play(sound, channel="sound")
            renpy.pause(delay, hard=True)
        renpy.exports.interact()

screen photo_album():
    tag menu
    modal True
    zorder 200
    on "show" action [Play("sound", "mod_assets/sfx/album_open.ogg"), Function(play_album_music)]
    on "hide" action [Play("sound", "mod_assets/sfx/album_close.ogg"), Function(resume_previous_music)]

    add "mod_assets/images/photos/album_backround.png"

    frame:
        style_prefix "album"
        xfill True
        yfill True
        background None

        vbox:
            spacing 20
            xalign 0.5
            yalign 0.0

            text _("Photo Album"):
                xalign 0.5
                size 40
                color album_text_color
                font gui.font

            hbox:
                spacing 40
                xalign 0.5
                yalign 0.0

                # 🌼 Basil sprite on the LEFT (with randomness)
                add get_random_basil():
                    xsize 178
                    ysize 625
                    yalign 0.5

                # 📸 Scrollable photo grid stays CENTERED with scrollbar
                viewport:
                    draggable True
                    scrollbars "vertical"
                    mousewheel True
                    ymaximum 600

                    grid 3 4:
                        xalign 0.5
                        xspacing 40
                        yspacing 40

                        for i in range(1, 13):
                            fixed:
                                xsize 250
                                ysize 300

                                if persistent.photo_unlocked.get(i, False):
                                    add "mod_assets/images/photos/empty_photo.png":
                                        xysize (250, 300)
                                        align (0.5, 0.5)

                                    add "mod_assets/images/photos/photo[{}].png".format(i):
                                        align (0.5, 0.5)
                                        xysize (245, 295)

                                    button:
                                        background None
                                        hover_background "mod_assets/images/photos/hover.png"
                                        hover_sound "mod_assets/sfx/photo_hover.ogg"
                                        xysize (250, 300)
                                        action [Play("sound", "mod_assets/sfx/photo_click.ogg"), Show("inspect_photo", photo="mod_assets/images/photos/photo[{}].png".format(i), desc=get_photo_description(i))]
                                else:
                                    add "mod_assets/images/photos/locked.png":
                                        xysize (250, 300)
                                        align (0.5, 0.5)

screen inspect_photo(photo, desc):
    tag menu
    modal True
    zorder 210

    add "mod_assets/images//photos/album_backround.png"
    add Solid("#00000080")

    frame:
        style_prefix "album"
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 700
        background None

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5

            fixed:
                xsize 500
                ysize 300
                xalign 0.5

                add "mod_assets/images/photos/empty_photo.png":
                    xysize (250, 300)
                    align (0.5, 0.5)

                add photo:
                    align (0.5, 0.5)
                    xysize (245, 295)

            window:
                xalign 0.5
                xsize 816
                ysize 146
                background Frame("mod_assets/images/photos/omori_textbox.png", 20, 20)
                padding (25, 20)

                text "[desc]":
                    font "mod_assets/fonts/omori.ttf"
                    color "#ffffff"
                    size 32
                    slow_cps 25
                    xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5
                    text_align 0.5

            textbutton _("Back") style "my_button_text":
                xalign 0.5
                action [Play("sound", "mod_assets/sfx/inspect_exit.ogg"), Hide("inspect_photo"), Show("photo_album")]

init -1:
    style album_frame:
        padding (30, 30)

    style album_button:
        background Solid("#4d4d4d")
        hover_background Solid("#5d5d5d")
        insensitive_background Solid("#3d3d3d")
        xminimum 200
        yminimum 50

label remove_photo(number):
    python:
        if not hasattr(persistent, "photo_unlocked"):
            persistent.photo_unlocked = {}

        if not isinstance(number, int) or number < 1 or number > 12:
            renpy.notify("Invalid photo number!")

        persistent.photo_unlocked[number] = False
        renpy.notify("Photo {} removed.".format(number))
    return

label unlock_all_photos():
    python:
        for i in range(1, 13):
            persistent.photo_unlocked[i] = True
        renpy.notify("All photos unlocked!")
    return

label remove_all_photos():
    python:
        for i in range(1, 13):
            persistent.photo_unlocked[i] = False
    return

label unlock_photo(number):
    python:
        unlock_photo(number)
    return

label show_unlocked_photo(photo_path):
    window hide(None)
    window auto
    play sound "mod_assets/sfx/photo_unlock.ogg"

    transform zoom_reveal:
        alpha 0.0 zoom 0.9
        linear 0.5 alpha 1.0 zoom 1.0

    show expression photo_path as unlocked_photo at truecenter, zoom_reveal zorder 10000

    show expression Text("You unlocked a new photo! Press '{i}P{/i}' to view it in your Photo Album!", style="unlock_text") as unlock_msg at truecenter zorder 10000

    pause 4.0

    hide unlocked_photo with dissolve
    hide unlock_msg
    return

init:
    style my_button_text is default
    style my_button_text font "mod_assets/fonts/omori.ttf"
    style unlock_text is default
    style unlock_text font "mod_assets/fonts/omori.ttf"
    style unlock_text size 40
    style unlock_text color "#FFFFFF"
    style unlock_text outlines [(2, "#000000")]
    style unlock_text xpos 0.5
    style unlock_text ypos 0.85
    style unlock_text xanchor 0.5
    style unlock_text yanchor 0.5
