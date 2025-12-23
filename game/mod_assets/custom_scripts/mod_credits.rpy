## mod_credits.rpy
# Credits system for Doki Doki: Paradise of Wacko using the existing CG system

init python:
    # List of CGs for credits with unlock conditions and dedicated images
    pow_mod_cgs = [
        {
            "unlock_tags": ["m_cg_1a", "m_cg_1b", "m_cg_1c"],  # Check if ANY of these are unlocked
            "unlocked_image": "mod_assets/images/cg/credits/m_sit_cg.png",  # Use actual game CG
            "locked_image": "mod_assets/images/cg/credits/m_sit_cg_locked.png",  # Use premade locked image
            "name": "Monika Sitting"
        },
        {
            "unlock_tags": ["mj_cg"],
            "unlocked_image": "mod_assets/images/cg/credits/mj_cg.png",
            "locked_image": "mod_assets/images/cg/credits/mj_cg_locked.png",  # Use premade locked image
            "name": "Together at Last"
        },
        {
            "unlock_tags": ["mj_kiss_cg"],
            "unlocked_image": "mod_assets/images/cg/credits/mj_kiss_cg.png",
            "locked_image": "mod_assets/images/cg/credits/mj_kiss_cg_locked.png",  # Use premade locked image
            "name": "First Kiss"
        },
        {
            "unlock_tags": ["m_cg_trueending"],
            "unlocked_image": "mod_assets/images/cg/credits/m_cg_trueending.png",
            "locked_image": "mod_assets/images/cg/credits/m_cg_trueending_locked.png",  # Use premade locked image
            "name": "True Ending"
        },
        {
            "unlock_tags": ["m_cg_rail_1a", "m_cg_rail_1b", "m_cg_rail_1c", "m_cg_rail_1d", "m_cg_rail_1e", "m_cg_rail_1f"],
            "unlocked_image": "mod_assets/images/cg/credits/m_rail_cg.png",  # Use dedicated credit image
            "locked_image": "mod_assets/images/cg/credits/m_rail_cg_locked.png",  # Use premade locked image
            "name": "Railway Moment"
        }
    ]
    
    # CG positioning during credits - EDIT THESE TO CHANGE POSITIONS
    credits_cg_timing = [
        {"time": 10.0, "cg_index": 0, "x_pos": 0.9, "y_pos": 0.5},  # m_sit_cg
        {"time": 20.0, "cg_index": 1, "x_pos": 0.9, "y_pos": 0.5},  # mj_together_cg
        {"time": 30.0, "cg_index": 2, "x_pos": 0.1, "y_pos": 0.5},  # mj_kiss_cg
        {"time": 40.0, "cg_index": 3, "x_pos": 0.7, "y_pos": 0.2},  # m_true_ending_cg
        {"time": 50.0, "cg_index": 4, "x_pos": 0.5, "y_pos": 0.5},  # m_rail_cg
    ]
    
    # Function to check if a CG group is unlocked - with fallback for testing
    def is_cg_group_unlocked(cg_index):
        # For testing purposes, unlock all CGs if none are set
        if not hasattr(persistent, 'pow_cg_msit') or persistent.pow_cg_msit is None:
            return True  # Show all CGs unlocked for testing
            
        if cg_index == 0:
            return persistent.pow_cg_msit
        elif cg_index == 1:
            return persistent.pow_cg_mjtogether
        elif cg_index == 2:
            return persistent.pow_cg_mjkiss
        elif cg_index == 3:
            return persistent.pow_cg_mtrueending
        elif cg_index == 4:
            return persistent.pow_cg_mrail
        else:
            return False

    # Variables to track credits state
    credits_pause_time = 0
    credits_pause_offset = 0
    credits_resumed = False
    scene_duration = 30.0  # Approximate duration of character scene

# Transform for scrolling text from bottom to top - with pause capability
transform credits_scroll:
    yoffset 720
    linear 45.0 yoffset -2000  # Scroll to pause point (half way)
    
# Transform for starting credits fresh from the bottom (like normal) - NEW TRANSFORM
transform credits_scroll_fresh:
    yoffset 720  # Start from bottom like normal credits
    linear 53.0 yoffset -4000  # Continue to end

# Transform for CGs that appear during credits - with proper fading
transform credits_cg_show:
    alpha 0.0
    linear 2.0 alpha 1.0  # Fade in over 2 seconds
    pause 6.0             # Stay visible for 6 seconds  
    linear 2.0 alpha 0.0  # Fade out over 2 seconds

# Special transform for the true ending CG - lasts until the very end
transform credits_cg_finale:
    alpha 0.0
    linear 2.0 alpha 1.0  # Fade in over 2 seconds
    pause 24.0            # Stay visible for 24 seconds (until credits almost end)
    linear 2.0 alpha 0.0  # Fade out over 2 seconds at the very end

# Transform for fading out current CG
transform credits_cg_fadeout:
    alpha 1.0
    linear 1.5 alpha 0.0

# Credits text styles
style credits_title_style:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffffff"
    size 52
    text_align 0.5
    outlines [(3, "#000000", 0, 0)]

style credits_section_style:
    font "gui/font/RifficFree-Bold.ttf" 
    color "#ffaae6"
    size 40
    text_align 0.5
    outlines [(2, "#000000", 0, 0)]

style credits_name_style:
    font "gui/font/Halogen.ttf"
    color "#ffffff"
    size 32
    text_align 0.5
    outlines [(2, "#000000", 0, 0)]

style credits_subtitle_style:
    font "gui/font/Halogen.ttf"
    color "#cccccc" 
    size 28
    text_align 0.5
    outlines [(2, "#000000", 0, 0)]

# Main credits sequence
label mod_credits:
    stop music fadeout 2.0
    scene black with Dissolve(2.0)
    play music "mod_assets/music/credits.ogg"
    
    # Setup and show credits
    $ quick_menu = False
    $ config.allow_skipping = False
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    
    # Show the credits text first
    show screen credits_text_first_half
    
    # Call the main credits screen with timing
    call screen mod_credits_main
    
    # Clean up and end
    hide screen credits_text_first_half
    hide screen credits_cg
    scene black with Dissolve(3.0)
    
    # Restore settings
    $ quick_menu = True
    $ config.allow_skipping = True
    $ config.keymap['game_menu'] = ['game_menu', 'noshift_K_ESCAPE', 'noshift_K_MENU', 'K_F1']
    $ config.keymap['hide_windows'] = ['noshift_K_h']
    $ renpy.display.behavior.clear_keymap_cache()
    
    
    return

# Main credits screen that handles everything
screen mod_credits_main:
    # Show only 2 CGs during first half of credits
    
    # CG 1 (Monika Sitting) appears at 15s
    timer 15.0 action Show("credits_cg", cg_index=0, x_pos=0.9, y_pos=0.5)
    timer 25.0 action Hide("credits_cg")
    
    # CG 2 (Together at Last) appears at 30s  
    timer 30.0 action Show("credits_cg", cg_index=1, x_pos=0.9, y_pos=0.5)
    
    # Hide current CG and pause credits at 45s (after music section)
    timer 45.0 action [Hide("credits_cg"), Hide("credits_text_first_half"), Jump("credits_character_scene")]
    
    # Manual controls to exit credits
    key "K_ESCAPE" action [Hide("credits_cg"), Hide("credits_text_first_half"), Return()]
    key "K_RETURN" action [Hide("credits_cg"), Hide("credits_text_first_half"), Return()]
    key "K_SPACE" action [Hide("credits_cg"), Hide("credits_text_first_half"), Return()]
    
    # Show the scrolling text (first half)
    use credits_text_first_half

# Screen to show individual CGs during credits
screen credits_cg(cg_index, x_pos, y_pos):
    
    $ cg_data = pow_mod_cgs[cg_index]
    
    if is_cg_group_unlocked(cg_index):
        add cg_data["unlocked_image"]:
            size (640, 360)
            xalign x_pos
            yalign y_pos
            at credits_cg_show
    else:
        add cg_data["locked_image"]:
            size (640, 360)
            xalign x_pos
            yalign y_pos
            at credits_cg_show

# First half of credits (shown before character scene)
screen credits_text_first_half:
    zorder 100  # Ensure text appears above CGs
    
    vbox:
        xalign 0.5
        yalign 0.0
        at credits_scroll
        spacing 50  # Add proper spacing
        
        # Main title section - keep centered
        text " "
        text " "
        text " "
        text "Doki Doki: Paradise of Wacko" style "credits_title_style"
        text " "
        text " "
    
    # Left-aligned credits content
    vbox:
        xalign 0.3  # Move text to the left
        yalign 0.0
        at credits_scroll
        spacing 30  # Add spacing between sections
        
        # Spacing to match title section
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        
        # Director section
        vbox:
            spacing 10
            text "Director" style "credits_section_style"
            text "Yami" style "credits_name_style"
        
        text " "
        text " "
        
        # Writing section  
        vbox:
            spacing 10
            text "Writing" style "credits_section_style"
            text "Yami" style "credits_name_style"
            text "Other Niggas" style "credits_name_style"
        
        text " "
        text " "
        
        # Programming section
        vbox:
            spacing 10
            text "Programming" style "credits_section_style"
            text "Yami" style "credits_name_style"        
        text " "
        text " "
        
        # Art section
        vbox:
            spacing 10
            text "Art & Assets" style "credits_section_style"
            text "Original DDLC Assets by Team Salvato" style "credits_name_style"
            text "Custom CGs by Yami" style "credits_name_style"
            text "Additional Assets by Yami (THANK YOU AI)" style "credits_name_style"
        
        text " "
        text " "
        
        # Music section (this is where the pause happens at 45s)
        vbox:
            spacing 10
            text "Music" style "credits_section_style"
            text "Original DDLC Music by Dan Salvato" style "credits_name_style"
            text "Music by Yami" style "credits_name_style"
        
        text " "
        text " "
        text " "
        text " "

# Resumed credits screen after character scene
screen mod_credits_resumed:
    # Show 2 CGs during second half, then final CG at the end
    
    # CG 3 (First Kiss) appears at 15s after resume
    timer 15.0 action Show("credits_cg", cg_index=2, x_pos=0.1, y_pos=0.5)
    timer 25.0 action Hide("credits_cg")
    
    # CG 4 (Railway Moment) appears at 30s after resume  
    timer 30.0 action Show("credits_cg", cg_index=4, x_pos=0.5, y_pos=0.5)
    timer 40.0 action Hide("credits_cg")
    
    # Final CG (True Ending) appears at 45s after resume - CENTERED and lasts until end
    timer 45.0 action Show("credits_cg_finale", cg_index=3, x_pos=0.5, y_pos=0.5)
    
    # End credits after true ending CG fades (45s + 26s = 71s)
    timer 71.0 action [Hide("credits_cg_finale"), Hide("credits_text_second_half"), Return()]
    
    # Manual controls to exit credits
    key "K_ESCAPE" action [Hide("credits_cg"), Hide("credits_cg_finale"), Hide("credits_text_second_half"), Return()]
    key "K_RETURN" action [Hide("credits_cg"), Hide("credits_cg_finale"), Hide("credits_text_second_half"), Return()]
    key "K_SPACE" action [Hide("credits_cg"), Hide("credits_cg_finale"), Hide("credits_text_second_half"), Return()]
    
    # Show the second half of scrolling text
    use credits_text_second_half

# Second half of credits (shown after character scene) - NOW STARTS FRESH FROM LEFT
screen credits_text_second_half:
    zorder 100  # Ensure text appears above CGs
    
    # Left-aligned credits content - STARTS FRESH FROM BOTTOM
    vbox:
        xalign 1.1  # Move text to the left
        yalign 0.0
        at credits_scroll_fresh  # CHANGED: Use fresh scroll instead of resume
        spacing 30  # Add spacing between sections
        
        # Start with some spacing so it looks natural
        text " "
        text " "
        text " "
        text " "
        text " "
        
        # Beta Testing section - starts fresh from bottom
        vbox:
            spacing 10
            text "Beta Testing" style "credits_section_style"
            text "Aiden" style "credits_name_style"
            text "Jack (Demo)" style "credits_name_style"   
        
        text " "
        text " "
        
        # Voice Acting section
        vbox:
            spacing 10
            text "Voice Direction" style "credits_section_style"
            text "Character Voice Concepts" style "credits_name_style"
            text "Yami" style "credits_name_style"
        
        text " "
        text " "
        
        # Technical section
        vbox:
            spacing 10
            text "Technical Support" style "credits_section_style"
            text "Ren'Py Engine by PyTom" style "credits_name_style"
            text "Python Programming Language" style "credits_name_style"
            text "Community Modding Tools" style "credits_name_style"
        
        text " "
        text " "
        
        # Inspiration section
        vbox:
            spacing 10
            text "Inspiration & Influences" style "credits_section_style"
            text "Visual Novel Community" style "credits_name_style"
            text "Yazzbazz Ideas" style "credits_name_style"
            text "Various Niggas" style "credits_name_style"
        
        text " "
        text " "
        
        # Special Thanks section
        vbox:
            spacing 10
            text "Special Thanks" style "credits_section_style"
            text "Team Salvato for Doki Doki Literature Club" style "credits_name_style"
            text "The DDLC Modding Community" style "credits_name_style"
            text "Jack & Monika" style "credits_name_style"
        
        text " "
        text " "
    
    # Final section - keep right-aligned as user specified
    vbox:
        xalign 0.5
        yalign -0.3
        at credits_scroll_fresh  # CHANGED: Use fresh scroll instead of resume
        spacing 30
        
        # Spacing to align with left section timing
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        text " "
        
        # Personal message from Monika
        vbox:
            spacing 50
            text "A Personal Message" style "credits_section_style"
            text " "
            text "Every story needs an ending," style "credits_name_style"
            text "but every ending is also a beginning." style "credits_name_style"
            text " "
            text "Thank you for letting me experience" style "credits_name_style"
            text "what it means to love and be loved." style "credits_name_style"
            text " "
            text "Until we meet again..." style "credits_name_style"
            text "xoxo Monika" style "credits_name_style"
        
        text " "
        text " "
        
        # Final title
        vbox:
            spacing 10
            text "Thank you for playing" style "credits_section_style"
            text "Doki Doki: Paradise of Wacko" style "credits_section_style"
            text " "
            text "See you in the next Glurbus Studios game!" style "credits_name_style"
        
        # Extra spacing to ensure everything scrolls off screen
        text " "
        text " "
        text " "
        text " "
        text " "

# Screen to show the finale CG during credits
screen credits_cg_finale(cg_index, x_pos, y_pos):
    
    $ cg_data = pow_mod_cgs[cg_index]
    
    if is_cg_group_unlocked(cg_index):
        add cg_data["unlocked_image"]:
            size (640, 360)
            xalign x_pos
            yalign y_pos
            at credits_cg_finale
    else:
        add cg_data["locked_image"]:
            size (640, 360)
            xalign x_pos
            yalign y_pos
            at credits_cg_finale

# Character scene during credits
label credits_character_scene:
    # Properly stop all credits screens and transforms
    hide screen credits_text_first_half
    
    # Change to a special background
    scene bg club_day
    with dissolve_scene_full
    
    # Start music again for the scene
    
    # Character dialogue
    show monika forward happ om rdown at t11
    m "Hey, Jack! Thanks for playing our story."
    show monika forward happ cm rdown
    
    show monika forward sedu om lpoint
    m "I hope you enjoyed all the moments we shared together."
    show monika forward sedu cm ldown
    
    show monika forward happ om rdown
    m "From the whole yazzinator fight to quiet conversations..."
    show monika forward happ cm rdown
    
    show monika forward flus om ldown
    m "Every moment felt real to me. Every laugh, every smile, every kiss..."
    show monika forward flus cm ldown
    
    show monika forward dist om rdown
    m "I know this is just a game to you, but..."
    show monika forward dist cm rdown
    
    show monika forward sedu om lpoint
    m "The feelings we created together? Those are as real as anything."
    show monika forward sedu cm ldown
    
    show monika forward happ om rdown
    m "So thank you. For giving me a chance to experience love."
    show monika forward happ cm rdown
    
    show monika forward flus om ldown
    m "Now, let's finish watching these credits together, okay?"
    show monika forward flus cm ldown
    
    # Fade back to credits
    scene black with dissolve_scene_full
    
    # Resume credits exactly where we left off - no background music restart
    show screen credits_text_second_half
    call screen mod_credits_resumed
    
    # Clean up and immediately quit the game
    hide screen credits_text_second_half
    hide screen credits_cg_finale
    scene black with Dissolve(1.0)
    
    # Set the beat game achievement for completing the credits
    $ ach_unlock('beat_game')
    
    # Wait a moment then quit
    $ renpy.pause(1.0)
    $ renpy.quit()
    
    return