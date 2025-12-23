## stars.rpy
## Star Achievement System
## This file contains all the star achievement functionality

################################################################################
## Default Persistent Variables
################################################################################

# Simple Star Achievement System
default persistent.star_photo_album = False
default persistent.star_all_cgs = False
default persistent.star_all_bios = False
default persistent.star_max_rizz = False
default persistent.star_mj_art_6 = False
default persistent.star_beat_game = False
default persistent.secret_video_unlocked = False
default persistent.secret_video_shown = False
default persistent.star_system_explained = False

################################################################################
## Star System Functions
################################################################################

init python:
    # Achievement registry - list of all achievement keys
    ACH_REGISTRY = {
        "photo_album": "Photo Album Collected",
        "all_cgs": "All CGs Collected",
        "all_bios": "All Character Bios Read",
        "max_rizz": "Maximum Rizz Achieved",
        "mj_art_6": "MJ Art 6",
        "beat_game": "Game Completed"
    }
    
    # Simple star check
    def star_is(key):
        return getattr(persistent, "star_" + key, False)
    
    # Simple star unlock with notification
    def star_unlock(key):
        star_name = "star_" + key
        if not getattr(persistent, star_name, False):
            setattr(persistent, star_name, True)
            
            if key in ACH_REGISTRY:
                renpy.notify("Achievement Unlocked: {}!".format(ACH_REGISTRY[key]))
            
            renpy.save_persistent()
            return True
        return False
    
    # Simple star set (no notification)
    def star_set(key, value):
        setattr(persistent, "star_" + key, bool(value))
        renpy.save_persistent()
    
    # Count unlocked stars
    def star_count():
        count = 0
        for key in ACH_REGISTRY.keys():
            if star_is(key):
                count += 1
        return count
    
    # Check if all stars unlocked
    def star_all_unlocked():
        return star_count() == 6
    
    # Legacy compatibility wrappers
    def ach_is(key):
        return star_is(key)
    
    def ach_unlock(key):
        return star_unlock(key)
    
    def ach_set(key, value, notify=False):
        if notify:
            return star_unlock(key)
        else:
            star_set(key, value)
            return True
    
    def ach_count_stars():
        return star_count()
    
    def ach_all_stars_unlocked():
        return star_all_unlocked()
    
    def ach_check_and_unlock_secret_video():
        if star_all_unlocked() and not persistent.secret_video_unlocked:
            persistent.secret_video_unlocked = True
            renpy.save_persistent()
            renpy.notify("Secret video unlocked!")
            return True
        return False
    
    def ach_check_for_star_explanation():
        stars_earned = star_count()
        if (not persistent.star_system_explained) and (stars_earned >= 1 or persistent.star_beat_game):
            persistent.star_system_explained = True
            renpy.save_persistent()
            return True
        return False
    
    def ach_reset_all():
        for key in ACH_REGISTRY.keys():
            star_set(key, False)
        persistent.secret_video_unlocked = False
        persistent.secret_video_shown = False
        persistent.star_system_explained = False
        renpy.save_persistent()

################################################################################
## Helper/Wrapper Functions
################################################################################

init python:
    def check_all_stars_unlocked():
        # Backward-compatible function name wrapping new system
        return ach_check_and_unlock_secret_video()
    
    def count_stars_earned():
        return ach_count_stars()
    
    def check_for_star_explanation():
        # Wrapper for screens using legacy name
        return ach_check_for_star_explanation()

################################################################################
## Debug Functions
################################################################################

init python:
    def unlock_all_achievements():
        for key in ACH_REGISTRY.keys():
            ach_set(key, True)
        ach_set('secret_video_unlocked', True)
        renpy.notify("All achievements unlocked!")
        renpy.save_persistent()
        
    def reset_all_achievements():
        ach_reset_all()
        renpy.notify("All achievements reset!")
        renpy.save_persistent()
        
    def debug_unlock_all_stars():
        for key in ACH_REGISTRY.keys():
            ach_set(key, True)
        ach_set('secret_video_unlocked', True)
        renpy.notify("All stars unlocked! Secret video available!")
        renpy.save_persistent()
        renpy.restart_interaction()
        
    def force_check_secret_video():
        if ach_check_and_unlock_secret_video():
            return
        elif ach_all_stars_unlocked():
            renpy.notify("Secret video already unlocked!")
        else:
            renpy.notify("Need all 6 stars first!")
        
    def debug_check_stars():
        count = star_count()
        status = "{}/6 stars unlocked".format(count)
        
        if count == 6:
            status += " - Secret video: {}".format('Available' if persistent.secret_video_unlocked else 'Not Available')
        else:
            missing = []
            if not star_is('photo_album'): missing.append("Photo Album")
            if not star_is('all_cgs'): missing.append("All CGs")
            if not star_is('all_bios'): missing.append("All Bios")
            if not star_is('max_rizz'): missing.append("Max Rizz")
            if not star_is('mj_art_6'): missing.append("MJ Art 6")
            if not star_is('beat_game'): missing.append("Beat Game")
            if missing:
                status += ". Missing: " + ', '.join(missing)
        
        renpy.notify(status)

################################################################################
## Transform for Achievement Stars
################################################################################

# Transform for achievement stars
transform achievement_star:
    zoom 0.5
    alpha 0.0
    easein 1.0 alpha 1.0

################################################################################
## Dialogue Screens for Achievements and Stars
################################################################################

screen star_system_explanation():
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    
    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            
            python:
                stars_earned = count_stars_earned()
                if ach_is('beat_game') and stars_earned == 1:
                    message = "Congratulations on beating the game!\nYou've also earned your first star!"
                elif ach_is('beat_game'):
                    message = "Congratulations on beating the game!\nBut you still have some stars to find."
                else:
                    message = "Congratulations!\nYou've unlocked your first star!"
            
            label "[message]":
                style "confirm_prompt"
                xalign 0.5
                
            label "There are a total of 6 stars to collect.\nClick on any stars you've earned to see what they're for.\n\nBut I won't help you find what or where\nthe other stars are!\n\nHappy hunting!":
                style "confirm_prompt"
                xalign 0.5
            
            hbox:
                xalign 0.5
                spacing 100
                textbutton "OK" action Hide("star_system_explanation")

screen all_stars_unlocked_dialog():
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    
    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            label "You have unlocked all of the stars!":
                style "confirm_prompt"
                xalign 0.5
            
            hbox:
                xalign 0.5
                spacing 100
                textbutton "OK" action [Hide("all_stars_unlocked_dialog"), Show("secret_video_dialog")]

screen secret_video_dialog():
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    
    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30
            
            label "You have unlocked the secret video!\nWould you like to see it?":
                style "confirm_prompt"
                xalign 0.5
            
            hbox:
                xalign 0.5
                spacing 100
                textbutton "Yes" action [Hide("secret_video_dialog"), Function(ach_set, 'secret_video_shown', True), Jump("secret_video")]
                textbutton "No" action [Hide("secret_video_dialog"), Function(ach_set, 'secret_video_shown', True)]

################################################################################
## Labels for Achievement Unlocking
################################################################################

# Labels for achievement unlocking
label unlock_achievement_photo_album:
    $ ach_unlock('photo_album')
    call check_star_explanation from _call_check_star_explanation_1
    return

label unlock_achievement_all_cgs:
    $ ach_unlock('all_cgs')
    call check_star_explanation from _call_check_star_explanation_2
    return

label unlock_achievement_all_bios:
    $ ach_unlock('all_bios')
    call check_star_explanation from _call_check_star_explanation_3
    return

label unlock_achievement_max_rizz:
    $ ach_unlock('max_rizz')
    call check_star_explanation from _call_check_star_explanation_4
    return

label unlock_achievement_mj_art_6:
    $ ach_unlock('mj_art_6')
    call check_star_explanation from _call_check_star_explanation_5
    return

label unlock_achievement_beat_game:
    $ ach_unlock('beat_game')
    call check_star_explanation from _call_check_star_explanation_6
    return

label check_star_explanation:
    python:
        if check_for_star_explanation():
            renpy.call_screen("star_system_explanation")
    return

# Placeholder label for secret video
label secret_video:
    #: Add secret video here roadmap
    scene black
    with Dissolve(1.0)
    stop music fadeout 1.0
    $ renpy.movie_cutscene("mod_assets/images/misc/RoadmapP1.webm")
    scene black
    with Dissolve(1.0)

    return

################################################################################
## Legacy Labels (for backward compatibility)
################################################################################

label unlock_all_stars():
    python:
        for key in ACH_REGISTRY.keys():
            ach_set(key, True)
        renpy.notify("All achievement stars unlocked!")
    return

label lock_all_stars():
    python:
        for key in ACH_REGISTRY.keys():
            ach_set(key, False)
        renpy.notify("All achievement stars locked...")
    return

