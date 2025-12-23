################################################################################
# BEDROOM POINT & CLICK - Interactive Point & Click Inspection System
################################################################################
# This file handles the bedroom map interface where players can inspect different
# locations/items in the bedroom. Players can inspect locations multiple times.
################################################################################

# ==============================================================================
# IMAGE DEFINITIONS
# ==============================================================================

image jackie1 = "mod_assets/images/misc/jackie1.png"
image jackie2 = "mod_assets/images/misc/jackie2.png"
image jackie3 = "mod_assets/images/misc/jackie3.png"
image jackie4 = "mod_assets/images/misc/jackie4.png"

# Transform to make Jackie smaller
transform jackie_small:
    zoom 0.5  # Adjust this value: 0.5 = 50% size, 0.7 = 70% size, 1.0 = 100% size
    xalign 0.5
    yalign 0.5

################################################################################
# MAIN LABEL - BEDROOM POINT & CLICK
################################################################################
# Entry point for the bedroom point & click system. Initializes the scene
# and runs the main loop that handles location selection and story progression.
################################################################################

label bedroom_point_and_click:
    
    # ========================================================================
    # Scene Initialization
    # ========================================================================
    
    # Show bedroom background
    scene bg bedroom_topdown zorder 2
    with dissolve_scene_full
    
    # Start bedroom music (uncomment when music is available)
    # play music bedroommusic
    
    # ========================================================================
    # Gorp Introduction
    # ========================================================================
    
    window show
    
    "You hear a voice calling out to you."
    
    "???" "Hey! Over here!"
    
    "You turn around and see someone you've never met before."

    
    "???" "Oh, you must be new here! I'm Gorp."
    "Gorp" "Welcome to the mod! I'll be your guide for this little adventure"
    
    "Gorp" "Ill be here to help you out with anything you need by giving you hints and tips."

    "Gorp" "I know this is weird seeing a little version of you but hey!"

    "Gorp" "..."

    pause 2.0

    "Gorp" "Who cares!"
    "Gorp" "Well thats all for now. Maybe you'll see me again later!"
    "Gorp" "Byeeeeeeeeee!!!"
    
    
    window hide
    
    # ========================================================================
    # Main Bedroom Loop
    # ========================================================================
    # Continuously shows the bedroom map where players can inspect locations.
    # ========================================================================
    call show_hint("You can click on the locations to inspect them and get a closer look at them!")

    jump .bedroom_loop

label .bedroom_loop:
    
    # Show the bedroom map screen
    $ result = renpy.call_screen("bedroom_map")
    
    # ------------------------------------------------------------------------
    # Handle Location Selections - Direct to Close-up
    # ------------------------------------------------------------------------
    
    if result == "location1":
        # Fade out and transition to close-up
        scene bg desk_closeup with wipeleft
        
        # Show close-up scene with text
        call bedroom_location1_inspection from _call_bedroom_location1_inspection
        
        # Return to bedroom map
        scene bg bedroom_topdown zorder 2
        with dissolve_scene_full
        jump .bedroom_loop

    if result == "location2":
        # Fade out and transition to close-up
        scene bg bookshelf_closeup with wipeleft
        
        # Show close-up scene with text
        call bedroom_location2_inspection from _call_bedroom_location2_inspection
        
        # Return to bedroom map
        scene bg bedroom_topdown zorder 2
        with dissolve_scene_full
        jump .bedroom_loop

    if result == "location3":
        # Fade out and transition to close-up
        scene bg closet_closeup with wipeleft
        
        # Show close-up scene with text
        call bedroom_location3_inspection from _call_bedroom_location3_inspection
        
        # Return to bedroom map
        scene bg bedroom_topdown zorder 2
        with dissolve_scene_full
        jump .bedroom_loop

    if result == "location4":
        # Fade out and transition to close-up
        scene bg bed_closeup with wipeleft
        
        # Show close-up scene with text
        call bedroom_location4_inspection from _call_bedroom_location4_inspection
        
        # Return to bedroom map
        scene bg bedroom_topdown zorder 2
        with dissolve_scene_full
        jump .bedroom_loop
    
    if result == "location5":
        # Show choice prompt for leaving
        call bedroom_location5_leave_prompt from _call_bedroom_location5_leave_prompt
        
        # If player chose to leave, exit the bedroom system
        if bedroom_leaving:
            return
        
        # If player chose to stay, jump back to loop
        jump .bedroom_loop


################################################################################
# CONFIGURATION & TRACKING VARIABLES
################################################################################

# Track which location is currently being hovered over
default bedroom_hovered_location = None

# Track if player chose to leave the bedroom
default bedroom_leaving = False


################################################################################
# TRANSFORM ANIMATIONS
################################################################################

# ============================================================================
# Hover & Click Transforms
# ============================================================================

# Hover effect for clickable images
transform bedroom_hover_glow:
    on idle:
        alpha 0.8
        zoom 1.0
    on hover:
        alpha 1.0
        ease 0.2 zoom 1.05

# Button hover effect
transform bedroom_button_hover:
    on idle:
        zoom 1.0
    on hover:
        easein 0.15 zoom 1.05


# ============================================================================
# UI Animation Transforms
# ============================================================================

# Smooth tooltip animation - slides in from top
transform bedroom_tooltip_appear:
    yoffset -30 alpha 0.0
    parallel:
        easein_back 0.4 yoffset 0
    parallel:
        easein 0.3 alpha 1.0

# Zoom and fade in for confirmation screen
transform bedroom_confirmation_appear:
    alpha 0.0 zoom 0.8
    parallel:
        easein_back 0.5 zoom 1.0
    parallel:
        easein 0.4 alpha 1.0

# Fade out and zoom animation when confirming selection
transform bedroom_confirm_exit:
    alpha 1.0 zoom 1.0
    parallel:
        easeout 0.4 alpha 0.0
    parallel:
        easeout_back 0.4 zoom 1.15

# Button slide in from bottom
transform bedroom_button_slide_up:
    yoffset 50 alpha 0.0
    pause 0.3
    parallel:
        easein_back 0.4 yoffset 0
    parallel:
        easein 0.3 alpha 1.0

# Preview image slide in from right
transform bedroom_preview_slide_in:
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
transform bedroom_glow_pulse:
    alpha 0.6
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.6
    repeat

# Blur fade in/out transform
transform bedroom_blur_fade:
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




################################################################################
# BEDROOM MAP SCREEN
################################################################################
# Interactive point-and-click interface showing all available bedroom locations.
# Players can hover over locations to see tooltips and click to inspect them.
# 
# NOTE: Currently uses placeholder text buttons. Replace imagebutton sections
# with your actual clickable images when ready.
################################################################################

screen bedroom_map():
    modal True

    # ========================================================================
    # Clickable Location Images
    # ========================================================================
    # PLACEHOLDER: Currently using text buttons. Replace with imagebuttons
    # when you have your clickable images ready.
    # 
    # Example imagebutton format (uncomment and customize):
    # imagebutton:
    #     pos (X, Y)  # Position on screen
    #     idle "mod_assets/images/bg/bedroom/location1.png"
    #     hover "mod_assets/images/bg/bedroom/location1_hovered.png"
    #     action Return("location1")
    #     focus_mask True
    #     hovered SetVariable("bedroom_hovered_location", "location1")
    #     unhovered SetVariable("bedroom_hovered_location", None)
    # ========================================================================
    
    # Location 1 - Desk
    imagebutton:
        pos (0, 0)
        idle "mod_assets/images/bg/bedroom/desk_idle.png"
        hover "mod_assets/images/bg/bedroom/desk_hovered.png"
        action Return("location1")
        focus_mask True
        hovered SetVariable("bedroom_hovered_location", "location1")
        unhovered SetVariable("bedroom_hovered_location", None)    
    # Location 2 - Placeholder text button
    imagebutton:
        pos (0, 0)
        idle "mod_assets/images/bg/bedroom/bookshelf_idle.png"
        hover "mod_assets/images/bg/bedroom/bookshelf_hovered.png"
        action Return("location2")
        focus_mask True
        hovered SetVariable("bedroom_hovered_location", "location2")
        unhovered SetVariable("bedroom_hovered_location", None)
    
    # Location 3 - Placeholder text button
    imagebutton:
        pos (0, 0)
        idle "mod_assets/images/bg/bedroom/closet_idle.png"
        hover "mod_assets/images/bg/bedroom/closet_hovered.png"
        action Return("location3")
        focus_mask True
        hovered SetVariable("bedroom_hovered_location", "location3")
        unhovered SetVariable("bedroom_hovered_location", None)

    # Location 4 - Placeholder text button
    imagebutton:
        pos (0, 0)
        idle "mod_assets/images/bg/bedroom/bed_idle.png"
        hover "mod_assets/images/bg/bedroom/bed_hovered.png"
        action Return("location4")
        focus_mask True
        hovered SetVariable("bedroom_hovered_location", "location4")
        unhovered SetVariable("bedroom_hovered_location", None)

    # Location 5 - Door
    imagebutton:
        pos (0, 0)
        idle "mod_assets/images/bg/bedroom/door_idle.png"
        hover "mod_assets/images/bg/bedroom/door_hovered.png"
        action Return("location5")
        focus_mask True
        hovered SetVariable("bedroom_hovered_location", "location5")
        unhovered SetVariable("bedroom_hovered_location", None)

    # ========================================================================
    # Hover Tooltip - Gorp's Commentary
    # ========================================================================
    # Shows Jacko's dialogue when hovering over any location.
    # Appears at the top of the screen with a smooth animation.
    # ========================================================================
    
    if bedroom_hovered_location:
        hbox:
            at bedroom_tooltip_appear
            xalign 0.5
            ypos 30
            spacing 20
            
            # Jacko's name
            text "{color=#FFD700}✦ Jacko ✦{/color}":
                size 28
                bold True
                outlines [(3, "#000000", 0, 0)]
            
            # Location-specific tooltip text
            if bedroom_hovered_location == "location1":
                text "I should probably start with the desk. I have some things on my pc that I need to check.":
                    size 24
                    color "#FFFFFF"
                    outlines [(2, "#000000", 0, 0)]
                    italic True
            
            elif bedroom_hovered_location == "location2":
                text "Theres my mighty bookshelf. I don't read books, only manga.":
                    size 24
                    color "#FFFFFF"
                    outlines [(2, "#000000", 0, 0)]
                    italic True
            
            elif bedroom_hovered_location == "location3":
                text "I should clean out the closet. I have a lot of clothes in here that I don't wear anymore.":
                    size 24
                    color "#FFFFFF"
                    outlines [(2, "#000000", 0, 0)]
                    italic True
            
            elif bedroom_hovered_location == "location4":
                text "There's my bed. I should probably make it.":
                    size 24
                    color "#FFFFFF"
                    outlines [(2, "#000000", 0, 0)]
                    italic True
            
            elif bedroom_hovered_location == "location5":
                text "I think that should do it.":
                    size 24
                    color "#FFFFFF"
                    outlines [(2, "#000000", 0, 0)]
                    italic True


################################################################################
# INSPECTION LABELS - Close-up Scenes
################################################################################
# These labels show close-up views of each location with inspection text
################################################################################

label bedroom_location1_inspection:
    # Close-up of desk
    "You take a closer look at the desk."
    j "Alright, let's see what's on my PC."
    j "I've got a few tabs open... mostly gaming stuff and maybe some homework I've been putting off."
    j "Actually, scratch that. It's all gaming stuff."
    j "I should probably check my messages and emails, but that can wait. Right now I'm more interested in what else is in this room."
    return

label bedroom_location2_inspection:
    # Close-up of bookshelf
    "You examine the bookshelf."
    j "Ah, my collection of manga. This is where the real literature is."
    j "I've got some classics here... well, classic manga anyway. None of that boring regular book stuff."
    j "Some of these volumes are pretty worn out from re-reading them so many times."
    j "Maybe I should organize them better, but honestly, I know where everything is, so what's the point?"
    return

label bedroom_location3_inspection:
    # Close-up of closet
    "You look inside the closet."
    j "Wow, this is... a lot of clothes I haven't worn in forever."
    j "I should really do a clean-out one of these days. There's probably stuff in here from like, two years ago."
    j "But cleaning is such a hassle. Maybe I'll do it next week. Or next month. Or... you know what, it can wait."
    j "At least I know where my favorite hoodie is. That's all that matters."
    return

label bedroom_location4_inspection:
    # Close-up of bed
    "You inspect the bed."
    j "My bed. The place where I spend way too much time, but also not enough time."
    j "I really should make it, but honestly? It's just going to get unmade when I sleep in it tonight anyway."
    j "Plus, making beds is overrated. It's not like anyone's coming over to judge my room... right?"
    j "Actually, maybe I should make it. Just in case. But later. Definitely later."
    return

label bedroom_location5_leave_prompt:
    "If you leave now, you won't be able to come back again." 
    "I mean you didnt even clean anything up."
    "You lazy fuck. Just fucking go."
    
    menu:
        "Do you want to leave the room?"
        
        "Yes, leave the room":
            $ bedroom_leaving = True
            "You decide to leave."
            return
        
        "No, stay in the room":
            $ bedroom_leaving = False
            "You decide to stay."
            return


################################################################################
# END OF FILE
################################################################################

