################################################################################
# FESTIVAL MIDPOINT CHOICES - Interactive Point & Click Story Selection
################################################################################
# This file handles the festival map interface where players can choose which
# story locations to visit (Takoyaki Stand, Haunted House, Festival Games, 
# Art & Picnic). Players can complete stories in any order and continue once
# all activities are finished.
################################################################################

################################################################################
# MAIN LABEL - MID POINT CHOICES
################################################################################
# Entry point for the festival midpoint choice system. Initializes the scene
# and runs the main loop that handles location selection and story progression.
################################################################################

label mid_point_choices:
    
    # ========================================================================
    # Scene Initialization
    # ========================================================================
    
    # Reset to section 1 when entering/returning to festival map
    $ festival_map_section = 1
    
    # Show festival background and clouds
    scene bg festival zorder 2
    show clouds zorder 1
    with dissolve_scene_full
    
    # Start festival music
    
    
    # Show Monika on screen
    show monika forward happ rhip oe om at t11 zorder 10000
    m "There's alot to do here Jacko, what do you wanna do first?"
    m "Pssstt, you can click on different locations to see what they are!"
    show monika forward happ rhip oe cm at t44 zorder 10000
    window hide
    pause 0.3
    play music festivalmusic
    
    # ========================================================================
    # Main Festival Loop
    # ========================================================================
    # Continuously shows the festival map until all activities are completed
    # and the player chooses to continue.
    # ========================================================================
    
    jump .festival_loop

label .festival_loop:
    # Show the festival map screen
    $ result = renpy.call_screen("festival_map")
    
    # ------------------------------------------------------------------------
    # Handle Section Navigation
    # ------------------------------------------------------------------------
    
    if result == "section2":
        if festival_map_section != 2:
            $ hovered_location = None
            $ festival_map_section = 2
            scene bg festival2 zorder 2
            show clouds zorder 1
            with dissolve
        jump .festival_loop
    
    if result == "section1":
        if festival_map_section != 1:
            $ hovered_location = None
            $ festival_map_section = 1
            scene bg festival zorder 2
            show clouds zorder 1
            with dissolve
        jump .festival_loop
    
    # ------------------------------------------------------------------------
    # Handle Continue (All Activities Completed)
    # ------------------------------------------------------------------------
    
    if result == "continue":
        # Unlock photo and proceed to next story section
        call unlock_photo(10) from _call_unlock_photo_4
        jump after_mid_point_choices
    
    # ------------------------------------------------------------------------
    # Show Confirmation Screen
    # ------------------------------------------------------------------------
    
    # Display confirmation popup for the selected location
    $ confirmation = renpy.call_screen("location_confirmation", location=result)
    
    # If player cancelled, return to map
    if confirmation == "cancel":
        jump .festival_loop
    
    # ------------------------------------------------------------------------
    # Handle Takoyaki Stand Selection
    # ------------------------------------------------------------------------
    
    if confirmation == "takoyaki":
        # Fade out and transition
        stop music fadeout 1.5
        scene black with dissolve_scene_full
        hide monika
        
        # Mark as completed and call story
        $ takoyaki_completed = True
        call takoyaki_story from _call_takoyaki_story
        
        # Play minigame after story only the first time this route is completed
        if not takoyaki_salvage_done:
            $ current_animatronic_name = "el_nig"
            call salvage_minigame from _call_salvage_minigame_takoyaki
            $ takoyaki_salvage_done = True
        
        # Return to festival map
        $ festival_map_section = 1
        scene bg festival zorder 2
        show clouds zorder 1
        with dissolve_scene_full
        jump .festival_loop

    # ------------------------------------------------------------------------
    # Handle Haunted House Selection
    # ------------------------------------------------------------------------
    
    if confirmation == "haunted":
        # Fade out and transition
        stop music fadeout 1.5
        scene black with dissolve_scene_full
        hide monika
        
        # Mark as completed and call story
        $ haunted_house_completed = True
        call haunted_house from _call_haunted_house
        
        # Play minigame after story only the first time this route is completed
        if not haunted_salvage_done:
            $ current_animatronic_name = "jax_kob"
            call salvage_minigame from _call_salvage_minigame_haunted
            $ haunted_salvage_done = True
        
        # Return to festival map
        $ festival_map_section = 1
        scene bg festival zorder 2
        show clouds zorder 1
        with dissolve_scene_full
        jump .festival_loop

    # ------------------------------------------------------------------------
    # Handle Art & Picnic Selection
    # ------------------------------------------------------------------------
    
    if confirmation == "picnic":
        # Fade out and transition
        stop music fadeout 1.5
        scene black with dissolve_scene_full
        hide monika
        
        # Mark as completed and call story
        $ picnic_completed = True
        call picnic from _call_picnic
        
        # Play minigame after story only the first time this route is completed
        if not picnic_salvage_done:
            $ current_animatronic_name = "glurbox"
            call salvage_minigame from _call_salvage_minigame_picnic
            $ picnic_salvage_done = True
        
        # Return to festival map
        $ festival_map_section = 1
        scene bg festival zorder 2
        show clouds zorder 1
        with dissolve_scene_full
        jump .festival_loop

    # ------------------------------------------------------------------------
    # Handle Festival Games Selection
    # ------------------------------------------------------------------------
    
    if confirmation == "game":
        # Fade out and transition
        stop music fadeout 1.5
        scene black with dissolve_scene_full
        hide monika
        
        # Mark as completed and call story
        $ game_completed = True
        call game_story from _call_game_story
        
        # Play minigame after story only the first time this route is completed
        if not game_salvage_done:
            $ current_animatronic_name = "a1ds"
            call salvage_minigame from _call_salvage_minigame_game
            $ game_salvage_done = True
        
        # Return to festival map
        $ festival_map_section = 1
        scene bg festival zorder 2
        show clouds zorder 1
        with dissolve_scene_full
        jump .festival_loop
    
    # ------------------------------------------------------------------------
    # Handle Assorted Minigames Selection (Section 2)
    # ------------------------------------------------------------------------
    
    elif confirmation == "assorted_minigames":
        # Fade out and transition
        stop music fadeout 1.5
        scene black with dissolve_scene_full
        hide monika
        
        # Mark as completed and call test label
        $ assorted_minigames_completed = True
        call test_label from _call_test_label
        
        # Play minigame after story only the first time this route is completed
        if not assorted_salvage_done:
            call salvage_minigame from _call_salvage_minigame_assorted
            $ assorted_salvage_done = True
        
        # Return to festival map (section 2)
        $ festival_map_section = 2
        scene bg festival2 zorder 2
        show clouds zorder 1
        with dissolve_scene_full
        jump .festival_loop
    
    # ------------------------------------------------------------------------
    # Handle Changing Clothes Selection (Section 2)
    # ------------------------------------------------------------------------
    
    elif confirmation == "changing_clothes":
        # Fade out and transition
        stop music fadeout 1.5
        scene black with dissolve_scene_full
        hide monika
        
        # Mark as completed and call test label
        $ changing_clothes_completed = True
        call test_label from _call_test_label_2
        
        # Play minigame after story only the first time this route is completed
        if not changing_salvage_done:
            call salvage_minigame from _call_salvage_minigame_changing
            $ changing_salvage_done = True
        
        # Return to festival map (section 2)
        $ festival_map_section = 2
        scene bg festival2 zorder 2
        show clouds zorder 1
        with dissolve_scene_full
        jump .festival_loop


################################################################################
# CONFIGURATION & TRACKING VARIABLES
################################################################################

# Track completion status for each festival activity
default takoyaki_completed = False
default haunted_house_completed = False
default picnic_completed = False
default game_completed = False

# Track if salvage minigame has already been played for each route
default takoyaki_salvage_done = False
default haunted_salvage_done = False
default picnic_salvage_done = False
default game_salvage_done = False

# Track completion status for section 2 activities
default assorted_minigames_completed = False
default changing_clothes_completed = False

# Track if salvage minigame has already been played for section 2 routes
default assorted_salvage_done = False
default changing_salvage_done = False

# Track which location is currently being hovered over
default hovered_location = None

# Track which section of the festival map is being viewed
default festival_map_section = 1  # 1 = main area, 2 = second area


################################################################################
# TRANSFORM ANIMATIONS
################################################################################

# ============================================================================
# Hover & Click Transforms
# ============================================================================

# Hover effect for clickable images
transform hover_glow:
    on idle:
        alpha 0.8
        zoom 1.0
    on hover:
        alpha 1.0
        ease 0.2 zoom 1.05

# Button hover effect
transform button_hover:
    on idle:
        zoom 1.0
    on hover:
        easein 0.15 zoom 1.05


# ============================================================================
# UI Animation Transforms
# ============================================================================

# Smooth tooltip animation - slides in from top
transform tooltip_appear:
    yoffset -30 alpha 0.0
    parallel:
        easein_back 0.4 yoffset 0
    parallel:
        easein 0.3 alpha 1.0

# Zoom and fade in for confirmation screen
transform confirmation_appear:
    alpha 0.0 zoom 0.8
    parallel:
        easein_back 0.5 zoom 1.0
    parallel:
        easein 0.4 alpha 1.0

# Fade out and zoom animation when confirming selection
transform confirm_exit:
    alpha 1.0 zoom 1.0
    parallel:
        easeout 0.4 alpha 0.0
    parallel:
        easeout_back 0.4 zoom 1.15

# Button slide in from bottom
transform button_slide_up:
    yoffset 50 alpha 0.0
    pause 0.3
    parallel:
        easein_back 0.4 yoffset 0
    parallel:
        easein 0.3 alpha 1.0

# Preview image slide in from right
transform preview_slide_in:
    xoffset 600 alpha 0.0
    pause 0.3
    parallel:
        easein_back 0.8 xoffset 0
    parallel:
        easein 0.5 alpha 1.0


# ============================================================================
# Visual Effect Transforms
# ============================================================================

# Glow pulse animation - continuous loop
transform glow_pulse:
    alpha 0.6
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.6
    repeat

# Blur fade in/out transform
transform blur_fade:
    alpha 0.0
    on show:
        linear 0.3 alpha 1.0
    on hide:
        linear 0.25 alpha 0.0


################################################################################
# LOCATION CONFIRMATION SCREEN
################################################################################
# Displays when the player clicks on a location. Shows detailed information
# about the selected activity with a preview image and confirmation buttons.
################################################################################

screen location_confirmation(location):
    modal True
    
    # Track if player confirmed their choice (triggers exit animation)
    default is_confirming = False
    
    # Timer to return after confirmation animation completes
    if is_confirming:
        timer 0.5 action Return(location)
    
    # Blurred background with fade in/out - changes based on section
    if festival_map_section == 2:
        add "bg festival2_blur" at blur_fade
    else:
        add "bg festival_blur" at blur_fade
    
    
    # ========================================================================
    # Main Confirmation Container
    # ========================================================================
    
    frame:
        at (confirm_exit if is_confirming else confirmation_appear)
        xalign 0.5
        yalign 0.5
        xmaximum 1100
        xpadding 0
        ypadding 0
        background None
        
        hbox:
            spacing 0
            
            # ================================================================
            # LEFT SIDE - Location Information and Action Buttons
            # ================================================================
            
            frame:
                xsize 550
                xpadding 50
                ypadding 50
                background Solid("#00000000")
                
                vbox:
                    spacing 25
                    xalign 0.5
                    
                    # --------------------------------------------------------
                    # Top Decorative Accent
                    # --------------------------------------------------------
                    
                    fixed:
                        xalign 0.5
                        xsize 450
                        ysize 6
                        
                        # Bottom solid gold line
                        frame:
                            xalign 0.5
                            yalign 1.0
                            xsize 450
                            ysize 3
                            background "#FFD700"
                        
                        # Top glowing gold line
                        frame at glow_pulse:
                            xalign 0.5
                            yalign 0.0
                            xsize 450
                            ysize 3
                            background "#FFD700"
                    
                    # --------------------------------------------------------
                    # Location Title
                    # --------------------------------------------------------
                    
                    vbox at glow_pulse:
                        spacing 5
                        xalign 0.5
                        
                        if location == "takoyaki":
                            text "✦ Takoyaki Stand ✦":
                                xalign 0.5
                                size 36
                                bold True
                                color "#FFD700"
                                outlines [(4, "#FF8C00", 0, 0), (6, "#000000", 0, 0)]
                        
                        elif location == "haunted":
                            text "✦ Haunted House ✦":
                                xalign 0.5
                                size 36
                                bold True
                                color "#FFD700"
                                outlines [(4, "#8B008B", 0, 0), (6, "#000000", 0, 0)]
                        
                        elif location == "game":
                            text "✦ Festival Games ✦":
                                xalign 0.5
                                size 36
                                bold True
                                color "#FFD700"
                                outlines [(4, "#FF4500", 0, 0), (6, "#000000", 0, 0)]
                        
                        elif location == "picnic":
                            text "✦ Art & Picnic ✦":
                                xalign 0.5
                                size 36
                                bold True
                                color "#FFD700"
                                outlines [(4, "#32CD32", 0, 0), (6, "#000000", 0, 0)]
                        
                        elif location == "assorted_minigames":
                            text "✦ Assorted Minigames ✦":
                                xalign 0.5
                                size 36
                                bold True
                                color "#FFD700"
                                outlines [(4, "#9370DB", 0, 0), (6, "#000000", 0, 0)]
                        
                        elif location == "changing_clothes":
                            text "✦ Changing Room ✦":
                                xalign 0.5
                                size 36
                                bold True
                                color "#FFD700"
                                outlines [(4, "#FF69B4", 0, 0), (6, "#000000", 0, 0)]
                    
                    # Spacing
                    null height 10
                    
                    # --------------------------------------------------------
                    # Location Description
                    # --------------------------------------------------------
                    
                    if location == "takoyaki":
                        text "Time to grab some delicious takoyaki! You can chat with the girls while enjoying some tasty festival food.":
                            xalign 0.5
                            size 22
                            color "#FFFFFF"
                            text_align 0.5
                            outlines [(2, "#000000", 0, 0)]
                    
                    elif location == "haunted":
                        text "Ready for some spooky fun? Navigate through the haunted house with the girls and see who gets scared first!":
                            xalign 0.5
                            size 22
                            color "#FFFFFF"
                            text_align 0.5
                            outlines [(2, "#000000", 0, 0)]
                    
                    elif location == "game":
                        text "Try your luck at the festival games! Win prizes and compete with the girls to see who has the best aim.":
                            xalign 0.5
                            size 22
                            color "#FFFFFF"
                            text_align 0.5
                            outlines [(2, "#000000", 0, 0)]
                    
                    elif location == "picnic":
                        text "Relax and enjoy some art activities in a peaceful picnic area. Perfect for bonding and creative fun!":
                            xalign 0.5
                            size 22
                            color "#FFFFFF"
                            text_align 0.5
                            outlines [(2, "#000000", 0, 0)]
                    
                    elif location == "assorted_minigames":
                        text "Try out various fun minigames! Challenge yourself and the girls to see who comes out on top!":
                            xalign 0.5
                            size 22
                            color "#FFFFFF"
                            text_align 0.5
                            outlines [(2, "#000000", 0, 0)]
                    
                    elif location == "changing_clothes":
                        text "Head to the changing room to try on some cute festival outfits! See what styles suit you best!":
                            xalign 0.5
                            size 22
                            color "#FFFFFF"
                            text_align 0.5
                            outlines [(2, "#000000", 0, 0)]
                    
                    # Spacing
                    null height 30
                    
                    # --------------------------------------------------------
                    # Action Buttons (Confirm / Cancel)
                    # --------------------------------------------------------
                    
                    if not is_confirming:
                        vbox:
                            spacing 25
                            xalign 0.5
                            
                            # "Let's go!" Confirmation Button
                            frame:
                                at button_slide_up
                                xalign 0.5
                                xsize 400
                                ysize 75
                                background None
                                
                                # Glowing green button with layered effects
                                button:
                                    at button_hover
                                    xfill True
                                    yfill True
                                    background Frame("#1a5c1a", 12, 12)
                                    hover_background Frame("#2d8f2d", 12, 12)
                                    action SetScreenVariable("is_confirming", True)
                                    
                                    # Inner glow layer
                                    frame:
                                        xfill True
                                        yfill True
                                        background Frame("#3db83d88", 16, 16)
                                        xpadding 8
                                        ypadding 8
                                        
                                        frame:
                                            xfill True
                                            yfill True
                                            background Frame("#1a5c1a", 8, 8)
                                            
                                            text "✦ Let's go! ✦":
                                                xalign 0.5
                                                yalign 0.5
                                                size 30
                                                bold True
                                                color "#FFD700"
                                                outlines [(3, "#000000", 0, 0)]
                            
                            # "Maybe not..." Cancel Button
                            frame:
                                at button_slide_up
                                xalign 0.5
                                xsize 400
                                ysize 75
                                background None
                                
                                # Subtle red button
                                button:
                                    at button_hover
                                    xfill True
                                    yfill True
                                    background Frame("#4a1a1a", 12, 12)
                                    hover_background Frame("#6d2828", 12, 12)
                                    action Return("cancel")
                                    
                                    # Inner border effect
                                    frame:
                                        xfill True
                                        yfill True
                                        background Frame("#8f2d2d88", 16, 16)
                                        xpadding 8
                                        ypadding 8
                                        
                                        frame:
                                            xfill True
                                            yfill True
                                            background Frame("#4a1a1a", 8, 8)
                                            
                                            text "Maybe not...":
                                                xalign 0.5
                                                yalign 0.5
                                                size 28
                                                bold True
                                                color "#CCCCCC"
                                                outlines [(2, "#000000", 0, 0)]
                    
                    # --------------------------------------------------------
                    # Bottom Decorative Accent
                    # --------------------------------------------------------
                    
                    fixed:
                        xalign 0.5
                        xsize 450
                        ysize 6
                        
                        # Bottom solid gold line
                        frame:
                            xalign 0.5
                            yalign 0.0
                            xsize 450
                            ysize 3
                            background "#FFD700"
                        
                        # Top glowing gold line
                        frame at glow_pulse:
                            xalign 0.5
                            yalign 1.0
                            xsize 450
                            ysize 3
                            background "#FFD700"
            
            # ================================================================
            # RIGHT SIDE - Location Preview Image
            # ================================================================
            
            frame:
                xsize 550
                xpadding 0
                ypadding 0
                background None
                
                # Display custom preview image for the location
                fixed:
                    xfill True
                    yfill True
                    
                    # Preview image with slide-in animation
                    if location == "takoyaki":
                        add "mod_assets/images/bg/festival/takoyaki_preview.png" at preview_slide_in:
                            xalign 0.5
                            yalign 0.5
                    
                    elif location == "haunted":
                        add "mod_assets/images/bg/festival/haunted_house_preview.png" at preview_slide_in:
                            xalign 0.5
                            yalign 0.5
                    
                    elif location == "game":
                        add "mod_assets/images/bg/festival/game_preview.png" at preview_slide_in:
                            xalign 0.5
                            yalign 0.5
                    
                    elif location == "picnic":
                        add "mod_assets/images/bg/festival/picnic_preview.png" at preview_slide_in:
                            xalign 0.5
                            yalign 0.5
                    
                    elif location == "assorted_minigames":
                        # Use the regular image as preview if no preview exists
                        add "mod_assets/images/bg/festival/assorted_minigames_preview.png" at preview_slide_in:
                            xalign 0.5
                            yalign 0.5
                    
                    elif location == "changing_clothes":
                        # Use the regular image as preview if no preview exists
                        add "mod_assets/images/bg/festival/changing_clothes_preview.png" at preview_slide_in:
                            xalign 0.5
                            yalign 0.5


################################################################################
# FESTIVAL MAP SCREEN
################################################################################
# Interactive point-and-click interface showing all available festival locations.
# Players can hover over locations to see tooltips and click to visit them.
# Shows completion status with checkmarks and completed images.
################################################################################

screen festival_map():
    modal True
    
    # ========================================================================
    # Navigation & Debug Hotkeys
    # ========================================================================
    # Press "3" - Mark all stories as completed
    # Press "Down Arrow" - Move to festival section 2
    # Press "Up Arrow" - Return to festival section 1
    # ========================================================================
    
    key "3" action [
        SetVariable("takoyaki_completed", True),
        SetVariable("haunted_house_completed", True),
        SetVariable("picnic_completed", True),
        SetVariable("game_completed", True)
    ]
    
    if festival_map_section == 1:
        key "K_DOWN" action Return("section2")
    elif festival_map_section == 2:
        key "K_UP" action Return("section1")

    # Clickable Location Images - Only shown in section 1
    # ========================================================================
    # Each imagebutton shows the normal image by default, but switches to
    # the completed version once the story is finished. All images use
    # Clickable location images.
    # ========================================================================
    
    if festival_map_section == 1:
        # Haunted House
        imagebutton:
            pos (0, 0)
            idle ("mod_assets/images/bg/festival/haunted_house_completed.png" if haunted_house_completed else "mod_assets/images/bg/festival/haunted_house.png")
            hover "mod_assets/images/bg/festival/haunted_house_hovered.png"
            action Return("haunted")
            focus_mask True
            hovered SetVariable("hovered_location", "haunted")
            unhovered SetVariable("hovered_location", None)
        
        # Takoyaki Stand
        imagebutton:
            pos (0, 0)
            idle ("mod_assets/images/bg/festival/takoyaki_completed.png" if takoyaki_completed else "mod_assets/images/bg/festival/takoyaki.png")
            hover "mod_assets/images/bg/festival/takoyaki_hovered.png"
            action Return("takoyaki")
            focus_mask True
            hovered SetVariable("hovered_location", "takoyaki")
            unhovered SetVariable("hovered_location", None)
        
        # Festival Games
        imagebutton:
            pos (0, 0)
            idle ("mod_assets/images/bg/festival/game_completed.png" if game_completed else "mod_assets/images/bg/festival/game.png")
            hover "mod_assets/images/bg/festival/game_hovered.png"
            action Return("game")
            focus_mask True
            hovered SetVariable("hovered_location", "game")
            unhovered SetVariable("hovered_location", None)
        
        # Art & Picnic Area
        imagebutton:
            pos (0, 0)
            idle ("mod_assets/images/bg/festival/picnic_completed.png" if picnic_completed else "mod_assets/images/bg/festival/picnic.png")
            hover "mod_assets/images/bg/festival/picnic_hovered.png"
            action Return("picnic")
            focus_mask True
            hovered SetVariable("hovered_location", "picnic")
            unhovered SetVariable("hovered_location", None)
    
    # ========================================================================
    # Clickable Location Images - Section 2
    # ========================================================================
    # Imagebuttons for section 2 activities.
    # ========================================================================
    
    elif festival_map_section == 2:
        # Assorted Minigames
        imagebutton:
            pos (0, 0)
            idle ("mod_assets/images/bg/festival/assorted_minigames_completed.png" if assorted_minigames_completed else "mod_assets/images/bg/festival/assorted_minigames.png")
            hover "mod_assets/images/bg/festival/assorted_minigames_hovered.png"
            action Return("assorted_minigames")
            focus_mask True
            hovered SetVariable("hovered_location", "assorted_minigames")
            unhovered SetVariable("hovered_location", None)
        
        # Changing Clothes
        imagebutton:
            pos (0, 0)
            idle ("mod_assets/images/bg/festival/changing_clothes_completed.png" if changing_clothes_completed else "mod_assets/images/bg/festival/changing_clothes.png")
            hover "mod_assets/images/bg/festival/changing_clothes_hovered.png"
            action Return("changing_clothes")
            focus_mask True
            hovered SetVariable("hovered_location", "changing_clothes")
            unhovered SetVariable("hovered_location", None)
    
    # ========================================================================
    # Monika Sprite Display - stays on top, moves per section
    # ========================================================================
    
    if festival_map_section == 1:
        add "monika forward happ rhip oe cm" at t44
    elif festival_map_section == 2:
        add "monika forward happ rdown ce cm" at t41

    if festival_map_section == 1:
        # ====================================================================
        # Hover Tooltip - Jacko's Commentary (Section 1 only)
        # ====================================================================
        # Shows Jacko's dialogue when hovering over any location.
        # Appears at the top of the screen with a smooth animation.
        # ====================================================================
        
        if hovered_location:
            hbox:
                at tooltip_appear
                xalign 0.5
                ypos 30
                spacing 20
                
                # Jacko's name
                text "{color=#FFD700}✦ Jacko ✦{/color}":
                    size 28
                    bold True
                    outlines [(3, "#000000", 0, 0)]
                
                # Location-specific tooltip text
                if hovered_location == "takoyaki":
                    text "There's a takoyaki stand over there, what do you say we head there?":
                        size 24
                        color "#FFFFFF"
                        outlines [(2, "#000000", 0, 0)]
                        italic True
                
                elif hovered_location == "haunted":
                    text "Ooh, a haunted house! That could be fun... if you're brave enough!":
                        size 24
                        color "#FFFFFF"
                        outlines [(2, "#000000", 0, 0)]
                        italic True
                
                elif hovered_location == "game":
                    text "Check out those festival games! Want to try your luck and win a prize?":
                        size 24
                        color "#FFFFFF"
                        outlines [(2, "#000000", 0, 0)]
                        italic True
                
                elif hovered_location == "picnic":
                    text "There's a nice spot for art and relaxation. How about we check it out?":
                        size 24
                        color "#FFFFFF"
                        outlines [(2, "#000000", 0, 0)]
                        italic True
    
    elif festival_map_section == 2:
        # ====================================================================
        # Hover Tooltip - Jacko's Commentary (Section 2)
        # ====================================================================
        # Shows Jacko's dialogue when hovering over section 2 locations.
        # Appears at the top of the screen with a smooth animation.
        # ====================================================================
        
        if hovered_location:
            hbox:
                at tooltip_appear
                xalign 0.5
                ypos 30
                spacing 20
                
                # Jacko's name
                text "{color=#FFD700}✦ Jacko ✦{/color}":
                    size 28
                    bold True
                    outlines [(3, "#000000", 0, 0)]
                
                # Location-specific tooltip text
                if hovered_location == "assorted_minigames":
                    text "Ooh, look at all those minigames! Want to try your hand at some fun challenges?":
                        size 24
                        color "#FFFFFF"
                        outlines [(2, "#000000", 0, 0)]
                        italic True
                
                elif hovered_location == "changing_clothes":
                    text "There's a changing room over there! Want to try on some different outfits?":
                        size 24
                        color "#FFFFFF"
                        outlines [(2, "#000000", 0, 0)]
                        italic True
    
    # ========================================================================
    # Continue Button (Section 1 only)
    # ========================================================================
    # Only appears when all four activities have been completed.
    # Allows the player to proceed with the festival story.
    # ========================================================================
    
    if festival_map_section == 1:
        if takoyaki_completed and haunted_house_completed and picnic_completed and game_completed and assorted_minigames_completed and changing_clothes_completed:
            textbutton "Continue with the Festival":
                action Return("continue")
                xalign 0.5
                yalign 0.85
                xsize 450
                ysize 100
                text_size 30
    
    # ========================================================================
    # Navigation Hint
    # ========================================================================
    # Shows which section the player is in and how to navigate
    
    vbox:
        xalign 0.98
        yalign 0.98
        spacing 5
        
        if festival_map_section == 1:
            text "↓ Press Down Arrow to explore more":
                size 18
                color "#FFD700"
                outlines [(2, "#000000", 0, 0)]
        elif festival_map_section == 2:
            text "↑ Press Up Arrow to go back":
                size 18
                color "#FFD700"
                outlines [(2, "#000000", 0, 0)]
        
        text "Section [festival_map_section]/2":
            size 16
            color "#FFFFFF"
            outlines [(2, "#000000", 0, 0)]
    
    # ========================================================================
    # Easter Egg - Click on Monika
    # ========================================================================
    # Clickable area over Monika's sprite (position changes per section)
    # Placed last in screen to render on top
    
    if festival_map_section == 1:
        imagebutton:
            xpos 1200
            ypos 0
            xysize (300, 900)
            idle Solid("#00000000")  # Transparent
            hover Solid("#FFFFFF22")  # Slight white tint on hover
            action Jump("monika_christmas_mode_change")






################################################################################
# TEST LABEL - Temporary label for section 2 activities
################################################################################
# Placeholder label for testing section 2 minigames
################################################################################

label test_label:
    
    scene black with dissolve_scene_full
    
    "This is a test label for the assorted minigames!"
    "You can replace this with your actual minigame content later."
    
    return


################################################################################
# MONIKA SKIP SCHOOL TALK - Easter Egg Dialogue
################################################################################
# Triggered when player clicks on Monika's sprite during the festival map
################################################################################

label monika_christmas_mode_change:
    
    # Hide the festival map screen
    hide screen festival_map
    
    # Monika's first question
    show monika forward happ rhip oe om at t11 zorder 10000
    m "Huh? You don't wanna do any of these?"
    
    # Player choice
    menu:
        "I'm just not sure yet":
            m "Oh, I see. Take your time deciding!"
            jump mid_point_choices
        
        "Maybe we could do something else?":
            m "Something else? Like what?"
            j "I don't know, I'm not sure what to do."
            m "Oh, I see..."
            m "You must want something new to happen dont you?"
            m "I bet you've already played through most of this mod by now havent you?"
            m "Well, I've got just the thing for you then!"
            m "I've been working on a new mode for the game that's been a long time coming."
            m "It's a new mode that adds a lot of new content to the game, and it's a lot of fun."
            m "Would you like to try it?"
            menu:
                "Yes, I'd love to try it!":
                    m "Great! I'll let you know when it's ready."
                    m "..."
                    m "Uhm, this might take a moment so.."
                    m "Please bare with me here!"
                    "..."
                    jump christmas_mode_change
                "No, I'm not interested.":
                    m "Oh, I see. Take your time deciding then!"
                    jump mid_point_choices
    
    
label christmas_mode_change:
$ persistent.christmas_mode = True
stop music
scene black
play sound building
"..."
"....."
"......"
"......."
"........"
"........."
"..........."
"............."
"..............."
"................."
"..................."
m "Sorry! just a moment here!"
$ run_input("renpy.file(\"images/christmasPack\")", "Replacing old assets.")
"...................."
"...................."
"...................."
"...................."
m "Almost done!"
$ run_input("renpy.file(\"story_scripts/christmas.rpy\")", "Loading Christmas Mode...")
"...................."
"...................."
m "There! Now let me restart the game for you!"
$ run_input("renpy.function(\"$ renpy.full_restart\")", "Restarting!")
stop sound
play sound g1
pause 3.0
$ renpy.full_restart(transition=None, label="splashscreen")
################################################################################
# END OF FILE
################################################################################
