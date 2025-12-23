## mainmenu.rpy
## Simple main menu with just background and basic buttons

## CONFIGURATION - Customize your main menu here!
################################################################################

# Default variable for tracking if game has been beaten (for showing extras menu)
default persistent.achievement_beat_game = False

# Variable to track if main menu has been seen before
default persistent.first_menu_visit = False

# Variable to track if Christmas mode is enabled
default persistent.christmas_mode = False
# Transform to fade in the main menu from white
transform mainmenu_fadein:
    alpha 0.0
    pause 0.5
    linear 2.0 alpha 1.0

# Transform for logo sliding from top to top right corner
transform logo_slide_in:
    subpixel True
    yoffset -300
    alpha 0.0
    pause 1.925
    easein 1.5 yoffset 0 alpha 1.0

# Transforms for sliding menu buttons from off-screen (FIRST TIME - SLOW)
transform slide_button_1_slow:
    yoffset 800
    pause 1.0
    easein 1.0 yoffset 0

transform slide_button_2_slow:
    yoffset 800
    pause 1.1
    easein 1.2 yoffset 0

transform slide_button_3_slow:
    yoffset 800
    pause 1.2
    easein 1.4 yoffset 0

transform slide_button_4_slow:
    yoffset 800
    pause 1.3
    easein 1.6 yoffset 0

transform slide_button_5_slow:
    yoffset 800
    pause 1.4
    easein 1.8 yoffset 0

transform slide_button_6_slow:
    yoffset 800
    pause 1.5
    easein 2.0 yoffset 0

transform slide_button_0_slow:
    yoffset 800
    pause 0.9
    easein 0.8 yoffset 0

# Transforms for sliding menu buttons from off-screen (RETURNING - FAST)
transform slide_button_1_fast:
    yoffset 800
    pause 0.3
    easein 0.6 yoffset 0

transform slide_button_2_fast:
    yoffset 800
    pause 0.35
    easein 0.6 yoffset 0

transform slide_button_3_fast:
    yoffset 800
    pause 0.4
    easein 0.6 yoffset 0

transform slide_button_4_fast:
    yoffset 800
    pause 0.45
    easein 0.6 yoffset 0

transform slide_button_5_fast:
    yoffset 800
    pause 0.5
    easein 0.6 yoffset 0

transform slide_button_6_fast:
    yoffset 800
    pause 0.55
    easein 0.6 yoffset 0

transform slide_button_0_fast:
    yoffset 800
    pause 0.25
    easein 0.5 yoffset 0

################################################################################

# Background image - change this to use a different background
# For videos, they are automatically scaled to 1280x720
define mainmenu_background = Transform(Movie(play="mod_assets/images/mainmenu/mainmenu.webm"))

# Main menu music - change this to use a different music file
# Set to None to have no music
define mainmenu_music = "mod_assets/music/mainmenuinitial.ogg"
define christmas_music = "mod_assets/music/mainmenu_jolly.ogg" # You can change this to any audio file path

# Main menu logo image definition
image mainmenu_logo:
    Transform("mod_assets/images/mainmenu/logo.png", size=(300,300))
    subpixel True
    xpos 0
    ypos 0
image christmas_mainmenu_logo:
    Transform("mod_assets/images/mainmenu/logo_jolly.png", size=(300,300))
    subpixel True
    xpos 0
    ypos 0

# Button positions - customize X and Y for each button individually
# X position: 0 = left edge, 640 = center, 1280 = right edge
# Y position: 0 = top edge, 360 = center, 720 = bottom edge

# New Game button position
define newgame_button_x = 500
define newgame_button_y = 200

# Load Game button position
define load_button_x = 500
define load_button_y = 250

# Settings button position
define settings_button_x = 500
define settings_button_y = 300

# Character Bios button position (shown before beating game)
define bios_button_x = 500
define bios_button_y = 350

# Debug Mode button position (shown if debug mode is enabled and haven't beaten game)
define debug_button_x = 500
define debug_button_y = 400

# Extras button position (shown after beating game)
define extras_button_x = 500
define extras_button_y = 350

# Quit button position
define quit_button_x = 500
define quit_button_y = 450

# Achievement stars positions (displayed on left side)
# Stars appear at: X=20, Y starts at 20 and increments by 50 for each star
# You can customize these positions in the achievement stars section below

################################################################################

# Function to finish entering name and jump to Christmas story
init python:
    def FinishEnterNameChristmas():
        if not player: return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("jolly_christmas_story")

# Higher init priority to override the default main menu
init 1:

    # This screen overrides the default main menu
    screen main_menu():

        # This ensures that any other menu screen is replaced.
        tag menu

        style_prefix "main_menu"
        
        # Set flag to False after first menu visit
        on "show" action SetField(persistent, "first_menu_visit", False)
        
        # White background (will show through as menu fades in)
        add "white"
        
        # Fixed container to hold everything with fade-in effect
        fixed at mainmenu_fadein:

            # Background - uses the configurable background variable
            if persistent.christmas_mode:
                add "mod_assets/images/mainmenu/christmas_main_menu.png"
                add "y_cg2_dust1"
                add "y_cg2_dust2"
                add "y_cg2_dust3"
                add "y_cg2_dust4"

            else:
                add mainmenu_background
                add "y_cg2_dust1"
                add "y_cg2_dust2"
                add "y_cg2_dust3"
                add "y_cg2_dust4"
                add "y_cg2_details"
                add "cherry_blossoms_falling1"
                add "cherry_blossoms_falling2"
                add "cherry_blossoms_falling3"
                add "cherry_blossoms_falling4"
                add "cherry_blossoms_falling5"
                add "cherry_blossoms_falling6"
                add "cherry_blossoms_falling7"
                add "cherry_blossoms_falling8"
                add "m_cg_cafeEvent_shaft1"
            
            # Centered vbox container for menu buttons
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 20

                # A Jolly Christmas Story button - only shown when Christmas mode is enabled
                if persistent.christmas_mode:
                    textbutton _("A Jolly Christmas Story"):
                        style "navigation_button"
                        at (slide_button_0_slow if persistent.first_menu_visit else slide_button_0_fast)
                        action If(persistent.playername, true=Jump("jolly_christmas_story"), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterNameChristmas)))

                # New Game button
                if persistent.playthrough == 1:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«"):
                        style "navigation_button"
                        at (slide_button_1_slow if persistent.first_menu_visit else slide_button_1_fast)
                        action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("New Game"):
                        style "navigation_button"
                        at (slide_button_1_slow if persistent.first_menu_visit else slide_button_1_fast)
                        action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

                # Load Game button
                textbutton _("Load Game"):
                    style "navigation_button"
                    at (slide_button_2_slow if persistent.first_menu_visit else slide_button_2_fast)
                    action ShowMenu("load")

                # Settings button
                textbutton _("Settings"):
                    style "navigation_button"
                    at (slide_button_3_slow if persistent.first_menu_visit else slide_button_3_fast)
                    action ShowMenu("preferences")

                # Character Bios button - only shown before beating game
                if not persistent.achievement_beat_game:
                    textbutton _("Character Bios"):
                        style "navigation_button"
                        at (slide_button_4_slow if persistent.first_menu_visit else slide_button_4_fast)
                        action [ShowMenu("bio_screen"), SensitiveIf(renpy.get_screen("bio_screen") == None)]

                # Debug Mode button - only shown if debug mode is enabled and haven't beaten game
                if not persistent.achievement_beat_game and persistent.debug_mode:
                    textbutton _("Debug Mode"):
                        style "navigation_button"
                        at (slide_button_5_slow if persistent.first_menu_visit else slide_button_5_fast)
                        action If(persistent.playername, true=Function(renpy.jump_out_of_context, "debug_menu"), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))

                # Extras button - only shown after beating game
                if persistent.achievement_beat_game:
                    textbutton _("Extras"):
                        style "navigation_button"
                        at (slide_button_4_slow if persistent.first_menu_visit else slide_button_4_fast)
                        action [ShowMenu("extras_menu"), SensitiveIf(renpy.get_screen("extras_menu") == None)]

                # Quit button
                if renpy.variant("pc"):
                    textbutton _("Quit"):
                        style "navigation_button"
                        at (slide_button_6_slow if persistent.first_menu_visit else slide_button_6_fast)
                        action Quit(confirm=not main_menu)

            # Version number
            if gui.show_name:
                vbox:
                    text "[config.name!t]":
                        style "main_menu_title"

                    text "[config.version]":
                        style "main_menu_version"
        
        # Snow effect - only shows during Christmas mode
        use snow_effect
        
        # Logo - slides in from top to top right corner
        if persistent.christmas_mode:
            add "christmas_mainmenu_logo" at logo_slide_in
        else:
            add "mainmenu_logo" at logo_slide_in
        
        # Achievement stars (clickable) - displayed on top layer
        fixed:
            if ach_is('photo_album'):
                imagebutton:
                    idle "gui/star.png"
                    hover "gui/star.png"
                    pos (0, 650)
                    at achievement_star
                    action Function(renpy.notify, "Achievement Star: Photo Album Collected!")
            if ach_is('mj_art_6'):
                imagebutton:
                    idle "gui/star.png"
                    hover "gui/star.png"
                    pos (60, 650)
                    at achievement_star
                    action Function(renpy.notify, "Achievement Star: MJ Art 6 Unlocked!")
            if ach_is('all_cgs'):
                imagebutton:
                    idle "gui/star.png"
                    hover "gui/star.png"
                    pos (120, 650)
                    at achievement_star
                    action Function(renpy.notify, "Achievement Star: All CGs Collected!")
            if ach_is('all_bios'):
                imagebutton:
                    idle "gui/star.png"
                    hover "gui/star.png"
                    pos (180, 650)
                    at achievement_star
                    action Function(renpy.notify, "Achievement Star: All Character Bios Read!")
            if ach_is('max_rizz'):
                imagebutton:
                    idle "gui/star.png"
                    hover "gui/star.png"
                    pos (240, 650)
                    at achievement_star
                    action Function(renpy.notify, "Achievement Star: Maximum Rizz Achieved!")
            if ach_is('beat_game'):
                imagebutton:
                    idle "gui/star.png"
                    hover "gui/star.png"
                    pos (300, 650)
                    at achievement_star
                    action Function(renpy.notify, "Achievement Star: Game Completed!")

        # Keyboard shortcuts
        key "K_ESCAPE" action Quit(confirm=False)
        key "K_7" action If(persistent.playername, true=Function(renpy.jump_out_of_context, "debug_menu"), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
        key "K_8" action [SetField(persistent, "achievement_beat_game", True), Function(renpy.notify, "Extras Menu Unlocked!")]

