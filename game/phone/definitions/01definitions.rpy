# /!\ default
# pc as in phone character :monikk:
default pc_sayori  = phone.character.Character("Sayori", phone.asset("sayori_icon.png"), "s", 21, "#22Abf8")
default pc_jacko      = phone.character.Character("Jacko", phone.asset("jacko_icon.png"), "j", 35, "#484848")
default pc_yuri    = phone.character.Character("Yuri", phone.asset("yuri_icon.png"), "y", 20, "#a327d6")
default pc_monika  = phone.character.Character("Monika", phone.asset("monika_icon.png"), "m", 40, "#0a0")
default pc_natsuki = phone.character.Character("Natsuki", phone.asset("natsuki_icon.png"), "n", 45, "#fbb")

default pov_key = "j"
default walk_with_sayori = False
default natsuki_baking_help = False

define phone_s  = Character("Sayori", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_j = Character("Jacko", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_m = Character("Monika", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_n = Character("Natsuki", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")
define phone_y = Character("Yuri", screen="phone_say", who_style="phone_say_label", what_style="phone_say_dialogue")

init 100 python in phone.application:
    add_app_to_all_characters(message_app)
    add_app_to_all_characters(call_history_app)
    add_app_to_all_characters(calendar_app)

init 100 python in phone.calendar:
    add_calendar_to_all_characters(2023, 6, MONDAY)

init phone register:
    define "Welcome":
        add "s" add "j" add "y" add "m" add "n"
        icon phone.asset("default_icon.png")
        as thanks_for_using_my_framework key "ddu"

init phone register:
    define "Sayori":
        add "s" add "j"
        icon phone.asset("sayori_icon.png")
        as sayori_chat key "sayori_chat"

init phone register:
    define "Natsuki":
        add "n" add "j"
        icon phone.asset("natsuki_icon.png")
        as natsuki_chat key "natsuki_chat"

init phone register:
    define "Monika":
        add "m" add "j"
        icon phone.asset("monika_icon.png")
        as monika_chat key "monika_chat"

init phone register:
    define "Yuri":
        add "y" add "j"
        icon phone.asset("yuri_icon.png")
        as yuri_chat key "yuri_chat"

init phone register:
    define "Jacko":
        add "j"
        icon phone.asset("jacko_icon.png")
        as jacko_chat key "jacko_chat"
label phone_discussion_test:
    phone discussion "ddu":
        time year 2023 month 6 day 5 hour 16 minute 30 delay -1 # exact date and time at which i wrote this. yes i am feeling quite silly and goofy
        label "'Sayori' has been added to the group" delay -1
        label "'MC' has been added to the group" delay -1
        label "'Yuri' has been added to the group" delay -1
        label "'Monika' has been added to the group" delay -1
        label "'Natsuki' has been added to the group" delay 0.2
        "m" "Hey there!"
        "n" "Thank you for using my framework."
        "n" "I mean {i}of course{/i} you're using {b}this{/b} framework."
        "n" "...not like there are any better ones out there~"
        "s" "natsuki!!!!! {emoji=EllenScream}"
        "s" "no being a meanie!!!!!!!{emoji=EllenScream}{emoji=EllenScream}{emoji=EllenScream}"
        "y" "If you are interested in DDLC mods, be sure to check out our mod {a=https://undercurrentsmod.weebly.com}Doki Doki Undercurrents{/a}! {emoji=Melody}"
        "mc" "In case you encounter an issue (or wanna make a suggestion),"
        "mc" "you can:"
        "mc" "DM me at {i}elckarow{/i} on Discord,"
        "mc" "open an issue on {a=https://github.com/Elckarow/Better-EMR-Phone}GitHub{/a},"
        "mc" "make a post on the phone's {a=https://elckarow.itch.io/better-emr-phone}Itch page{/a}."
        "s" "Happy coding!" 
    phone end discussion

    return

label phone_call_test:
    phone call "s"
    phone_s "Ohayouuu!!!!!!!!!!!!!!!!"
    phone_mc "Hey!"
    "Why is she always this energetic?"
    phone end call
    "..."

    return

# Example conversation - triggered when Sayori sends a message
label sayori_conversation_1:
    
    phone discussion "sayori_chat":
        time year 2025 month 12 day 14 hour 12 minute 19 delay -1
        "j" "eh, what's up?"
        "s" "hey jacko do you wanna meet up outside?"
        "s" "we can walk to school together and chat a bit"
        "j" "u sure? we have to get to school early for the festival and set up"
        "s" "im sure monika wont mind if we're a little late"
        "s" "plus i wanna walk with you"
        "s" "what do you say jacko?"
        menu:
            "sure!":
                $ walk_with_sayori = True
                "j" "okay, lets go"
                "j" "where are we meeting?"
                "s" "where we always meet silly!"
                "j" "sounds good! i'll see you there."
                "s" "great ill be there as soon as i can!"
                "j" "seeya chump"
                "s" "see u soon."
            "not today...":
                $ walk_with_sayori = False
                "j" "sorry sayori, i have to get to school early for the festival and set up"
                "s" "oh."
                "s" "ok! thats fine! see you later jacko!"
                "j" "yeah, maybe next time"
    phone end discussion
    return


label natsuki_conversation_1:
    phone discussion "natsuki_chat":
        time year 2025 month 12 day 20 hour 11 minute 17 delay -1
        "j" "eh, what's up?"
        "n" "theres alot of people here and they are in groups and they are all talking and i'm not sure what to do!"
        "n" "i could really use your help jacko."
        "j" "what do you need help with?"
        "j" "im kinda in the middle of something right now."
        "n" "what do you think dummy? BAKING!"
        "n" "listen are you able to or not? i dont have time for this!"
        menu:
            "alright natsuki i'll help you":
                $ natsuki_baking_help = True
                "j" "yeah sure i can help you just tell me where u are"
                "n" "im in the cuilinary room!"
                "n" "i'll be waiting for you there! hurry!"
                "j" "alright natsuki i'll be there as soon as i can"
                "n" "great! see you there!"
            "sorry natsuki i'm busy right now":
                $ natsuki_baking_help = False
                "j" "sorry natsuki i'm busy right now"
                "n" "what? you're always busy! i need your help!"
                "n" "alright fine i'll do it myself then"
                "n" "thanks for nothing"
    phone end discussion
    return


label monika_conversation_call_1:
    phone call "m"
    phone_j "Hello?"
    phone_m "Hey! Good morning!"
    phone_j "Good morning to you too Monika!"
    phone_j "Hows the festival going?"
    phone_m "It's going great! We are still setting up."
    phone_j "That's great to hear! I'm sure it's going to be a lot of fun!"
    phone_m "But thats the reason why I called you, we need your help to finish setting up."
    phone_m "Natsuki is getting a little impatient and Yuri is helping with the cupcakes."
    phone_j "Of course! I have the posters ready to go."
    "Definitely don't want to get on Natsuki's bad side."
    phone_m "Great! I'll be waiting for you at the clubroom."
    phone_j "Bye Monika!"
    phone_m "See you soon Jacko!"
    phone end call
