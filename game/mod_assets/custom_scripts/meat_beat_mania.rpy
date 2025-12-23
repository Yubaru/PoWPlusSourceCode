init python:
    # Game variables
    slaps = 0
    yazz_slaps = 0
    time_left = 60.0
    game_active = False
    high_score = 0
    slap_sounds = ["mod_assets/sfx/slap{}.ogg".format(i) for i in range(1,6)]
    screen_shake = 0
    time_warning_played = False
    monika_boost = False
    boost_available = False
    boost_end_time = 0
    slaps_since_last_boost = 0
    boost_available_sound_played = False

    # Define audio channels
    renpy.music.register_channel("slap", "sfx", loop=False)
    renpy.music.register_channel("boost", "sfx", loop=False)
    renpy.music.register_channel("timer", "sfx", loop=False)
    renpy.music.register_channel("countdown", "sfx", loop=False)
    renpy.music.register_channel("backmusic", "music", loop=True, stop_on_mute=False, tight=False)
    renpy.music.register_channel("notification", "sfx", loop=False)

    # Define Yazz's slapping function
    def yazz_slap():
        store.yazz_slaps += 1
        renpy.play(renpy.random.choice(store.slap_sounds), channel="slap")
        store.screen_shake = 2
        renpy.restart_interaction()

# Transforms
transform shake:
    xoffset 0
    ease 0.05 xoffset 15
    ease 0.05 xoffset -15
    ease 0.05 xoffset 10
    ease 0.05 xoffset -10
    ease 0.05 xoffset 5
    ease 0.05 xoffset -5
    ease 0.05 xoffset 0

transform pulse:
    zoom 1.0
    ease 0.2 zoom 1.05
    ease 0.2 zoom 1.0
    repeat

transform float_up:
    yoffset 0
    ease 1.0 yoffset -20
    ease 1.0 yoffset 0
    repeat

transform boost_glow:
    alpha 0.0
    linear 0.3 alpha 1.0
    linear 0.3 alpha 0.5
    repeat

transform text_pop:
    zoom 0.8
    alpha 0.0
    ease 0.2 zoom 1.0
    ease 0.2 alpha 1.0

# Main game screen
screen slap_game():
    frame:
        background None
        xfill True
        yfill True
        
        at (shake if screen_shake > 0 else None)
        
        vbox:
            xalign 0.5
            yalign 0.1
            spacing 20
            
            # Title
            text "MEAT BEAT MANIA":
                size 82
                color "#ff3333"
                outlines [(8, "#330000", 0, 0)]
                font "mod_assets/fonts/impact.ttf"
                at transform:
                    zoom 1.0
                    linear 1.0 zoom 1.05
                    linear 1.0 zoom 1.0
                    repeat
            
            # Timer
            if time_left < 10:
                text "TIME: [int(time_left)] SECONDS":
                    size 54
                    color "#ff0000"
                    outlines [(4, "#000", 0, 0)]
                    at transform:
                        linear 0.3 zoom 1.1
                        linear 0.3 zoom 1.0
                        repeat
            else:
                text "TIME: [int(time_left)] SECONDS":
                    size 48
                    color "#ffffff"
                    outlines [(3, "#000", 0, 0)]
                    at float_up
            
            # Scores
            hbox:
                xalign 0.5
                spacing 150
                vbox:
                    text "YOUR BEATS:":
                        size 42
                        color "#ffffff"
                        outlines [(4, "#000", 0, 0)]
                        at pulse
                    text "[slaps]":
                        size 72
                        color "#ffffff"
                        outlines [(5, "#000", 0, 0)]
                        at transform:
                            zoom 1.0 + (0.1 if slaps % 2 == 0 else 0.0)
                
                vbox:
                    text "YAZZ'S BEATS:":
                        size 42
                        color "#ff9999"
                        outlines [(4, "#000", 0, 0)]
                        at pulse
                    text "[yazz_slaps]":
                        size 72
                        color "#ff9999"
                        outlines [(5, "#000", 0, 0)]
                        at transform:
                            zoom 1.0 + (0.1 if yazz_slaps % 2 == 0 else 0.0)
            
            # High score
            text "HIGH SCORE: [high_score]":
                size 38
                color "#ffff00"
                outlines [(4, "#000", 0, 0)]
                at transform:
                    linear 1.0 alpha 0.8
                    linear 1.0 alpha 1.0
                    repeat
            
            # Monika boost indicator
            if monika_boost:
                text "2X BOOST ACTIVE! ([int(boost_end_time - renpy.get_game_runtime())]s)":
                    size 42
                    color "#55ff55"
                    outlines [(4, "#005500", 0, 0)]
                    font "mod_assets/fonts/impact.ttf"
                    at boost_glow
            elif boost_available:
                text "BOOST READY! (Press M)":
                    size 42
                    color "#55ff55"
                    outlines [(4, "#005500", 0, 0)]
                    font "mod_assets/fonts/impact.ttf"
                    at transform:
                        zoom 1.0
                        linear 0.5 zoom 1.05
                        linear 0.5 zoom 1.0
                        repeat
            
            # Instructions
            if game_active:
                if boost_available and not monika_boost:
                    text "Press M for Monika Boost (2x beats for 15s!)":
                        size 32
                        color "#55ff55"
                        outlines [(3, "#005500", 0, 0)]
                        at transform:
                            linear 0.8 alpha 0.6
                            linear 0.8 alpha 1.0
                            repeat
                text "SPAM SPACEBAR TO BEAT YAZZ!":
                    size 42
                    color "#ff9999"
                    outlines [(4, "#000", 0, 0)]
                    at transform:
                        linear 0.5 yoffset -5
                        linear 0.5 yoffset 0
                        repeat

# Key handling
screen slap_keys():
    key "K_SPACE" action If(game_active,
        [Play("slap", renpy.random.choice(slap_sounds)),
        SetVariable("slaps", slaps + (2 if monika_boost else 1)),
        SetVariable("screen_shake", 3),
        SetVariable("slaps_since_last_boost", slaps_since_last_boost + 1),
        Function(renpy.restart_interaction)])
    
    key "m" action If(game_active and boost_available and not monika_boost,
        [SetVariable("monika_boost", True),
        SetVariable("boost_end_time", renpy.get_game_runtime() + 15),
        SetVariable("boost_available", False),
        SetVariable("slaps_since_last_boost", 0),
        Play("boost", "mod_assets/sfx/mboost.ogg"),
        Notify("You turn your attention toward Monika. Your speed and strength increased for 15 seconds!"),
        Function(renpy.restart_interaction)])
    
    key "9" action If(game_active,
        [SetVariable("slaps", yazz_slaps + 1),
        SetVariable("time_left", 0),
        Function(renpy.restart_interaction)])

label start_slapping:
    $ slaps = 0
    $ yazz_slaps = 0
    $ time_left = 60.0
    $ game_active = False
    $ screen_shake = 0
    $ time_warning_played = False
    $ monika_boost = False
    $ boost_available = False
    $ boost_end_time = 0
    $ slaps_since_last_boost = 0
    $ boost_available_sound_played = False
    
    show screen slap_game
    show screen slap_keys
    
    # Countdown sequence
    show expression Text("3", size=200, color="#ff0000", outlines=[(15, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as countdown:
        align (0.5, 0.5)
        linear 0.8 zoom 1.5
        linear 0.8 alpha 0.0
    play sound "mod_assets/sfx/1.ogg" channel "countdown"
    pause 1.0
    hide countdown
    
    show expression Text("2", size=200, color="#ff0000", outlines=[(15, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as countdown:
        align (0.5, 0.5)
        linear 0.8 zoom 1.5
        linear 0.8 alpha 0.0
    play sound "mod_assets/sfx/2.ogg" channel "countdown"
    pause 1.0
    hide countdown
    
    show expression Text("1", size=200, color="#ff0000", outlines=[(15, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as countdown:
        align (0.5, 0.5)
        linear 0.8 zoom 1.5
        linear 0.8 alpha 0.0
    play sound "mod_assets/sfx/3.ogg" channel "countdown"
    pause 1.0
    hide countdown
    
    show expression Text("BEAT THAT MEAT!", size=180, color="#ff0000", outlines=[(15, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as countdown:
        align (0.5, 0.5)
        linear 1.0 zoom 1.2
        linear 1.0 alpha 0.0
    play sound "mod_assets/sfx/4.ogg" channel "countdown"
    pause 1.0
    hide countdown
    
    $ game_active = True
    play music "mod_assets/music/meat_beat_music.ogg" fadein 1.0
    
    # Game timer
    python:
        start_time = renpy.get_game_runtime()
        last_yazz_slap = start_time
        yazz_slap_delay = 0.05
        
        while time_left > 0:
            renpy.pause(0.01)
            current_time = renpy.get_game_runtime()
            elapsed = current_time - start_time
            time_left = max(0, 60.0 - elapsed)
            
            # Yazz's AI slapping
            if current_time - last_yazz_slap >= yazz_slap_delay * (0.8 + 0.4 * random.random()):
                yazz_slap()
                last_yazz_slap = current_time
            
            # Dynamic music
            if time_left < 20 and not time_warning_played:
                renpy.play("mod_assets/sfx/time_running_out.ogg", channel="timer")
                renpy.music.play("mod_assets/music/meat_beat_music_fast.ogg", channel="music", fadeout=1.0, fadein=1.0)
                time_warning_played = True
            
            # Boost availability
            if slaps_since_last_boost >= 200 and not boost_available and not monika_boost:
                boost_available = True
                if not boost_available_sound_played:
                    renpy.play("mod_assets/sfx/boost_ready.ogg", channel="notification")
                    boost_available_sound_played = True
                renpy.notify("Monika Boost available! Press M to activate!")
            
            if monika_boost and current_time >= boost_end_time:
                monika_boost = False
                renpy.notify("Monika's boost has worn off!")
                
            if screen_shake > 0:
                screen_shake -= 1
    
    # Game over
    $ game_active = False
    $ high_score = max(high_score, slaps)
    play sound "mod_assets/sfx/finish.ogg" channel "countdown"
    
    if slaps > yazz_slaps:
        $ winner_text = "VICTORY!"
        $ winner_color = "#55ff55"
        $ winner_sound = "mod_assets/sfx/victory.ogg"
    elif yazz_slaps > slaps:
        $ winner_text = "DEFEAT!"
        $ winner_color = "#ff5555"
        $ winner_sound = "mod_assets/sfx/defeat.ogg"
    else:
        $ winner_text = "DRAW!"
        $ winner_color = "#ffff00"
        $ winner_sound = "mod_assets/sfx/draw.ogg"
    
    play sound winner_sound channel "notification"
    
    # Results screen
    show expression Text("TIME'S UP!", size=140, color="#ff0000", outlines=[(12, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as result:
        align (0.5, 0.15)
        linear 0.5 zoom 1.1
    
    show expression Text(winner_text, size=120, color=winner_color, outlines=[(10, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as winner:
        align (0.5, 0.3)
        zoom 0.8
        alpha 0.0
        ease 0.3 zoom 1.0
        ease 0.3 alpha 1.0
        ease 0.1 zoom 1.05
        ease 0.1 zoom 1.0
    
    show expression Text("Your Beats: [slaps]", size=70, color="#ffffff", outlines=[(5, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as player_score:
        align (0.5, 0.45)
        zoom 0.9
        alpha 0.0
        ease 0.4 zoom 1.0
        ease 0.4 alpha 1.0
    
    show expression Text("Yazz's Beats: [yazz_slaps]", size=70, color="#ff9999", outlines=[(5, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as yazz_score:
        align (0.5, 0.55)
        zoom 0.9
        alpha 0.0
        ease 0.4 zoom 1.0
        ease 0.4 alpha 1.0
    
    show expression Text("High Score: [high_score]", size=60, color="#ffff00", outlines=[(4, "#000", 0, 0)], font="mod_assets/fonts/impact.ttf") as highscore:
        align (0.5, 0.65)
        zoom 0.9
        alpha 0.0
        ease 0.4 zoom 1.0
        ease 0.4 alpha 1.0
    
    pause 5.0
    
    stop music fadeout 2.0
    hide screen slap_game
    hide screen slap_keys
    return

# Game start
label meat_beat_mania:
    show screen slap_game
    stop music
    
    "Yazz" "Think you can out beat me? Let's see what you got, BITCH ASS NIGGA!"
    
    "Welcome to {b}MEAT BEAT MANIA!{/b} - the ultimate 60-second meat beating challenge against Yazz!"
    "Rules:"
    "1. {color=#ff5555}SPAM SPACEBAR{/color} to beat your meat as fast as possible"
    "2. {color=#ff9999}Yazz will be meat beating too{/color}"
    "3. Reach 200 beats to unlock Monika's 15-second 2x meat boost"
    "4. Most meat beats when time runs out wins!"
    
    call start_slapping from _call_start_slapping
    
    if slaps > yazz_slaps:
        $ yazz_win = True
        "You crushed Yazz with [slaps] meat beats to his [yazz_slaps]! Your current high score is [high_score]."
    elif yazz_slaps > slaps:
        $ yazz_win = False
        "Yazz dominated you [yazz_slaps] to [slaps]! Pathetic. Your high score is [high_score]."
    else:
        "It's a tie! Both you and Yazz got [slaps] meat beats. Your high score is [high_score]."