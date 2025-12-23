# ==============================================================================
# HINT SYSTEM WITH GORP ANIMATION
# ==============================================================================
# This system displays hints in the game with a gorp animation.
#
# USAGE EXAMPLES:
#   # Using the label (recommended for Ren'Py scripts):
#   call show_hint("Try talking to Sayori to progress the story!")
#   call show_hint("You can skip dialogue you've already read.")
#
#   # Using the Python function (for Python blocks):
#   $ show_hint_popup("Check your phone for new messages!")
#
# The hint screen will display with:
#   - The hint box positioned at the top right of the screen
#   - The gorp animation playing inside the box on the left
#   - Your custom hint message next to gorp
#   - Automatically disappears after 5 seconds
# ==============================================================================

init python:
    # Store for hint text
    hint_text = ""

# ==============================================================================
# GORP ANIMATION DEFINITION
# ==============================================================================
# Define the gorp talk animation (4 frames)
image gorp_hint_animation:
    "mod_assets/animations/gorp/gorp_hint_talk0001.png"
    pause 0.07
    "mod_assets/animations/gorp/gorp_hint_talk0002.png"
    pause 0.07
    "mod_assets/animations/gorp/gorp_hint_talk0003.png"
    pause 0.07
    "mod_assets/animations/gorp/gorp_hint_talk0004.png"
    pause 0.13
    repeat  # Loop the animation

# ==============================================================================
# TRANSFORMS FOR HINT SCREEN
# ==============================================================================

# Transform for the hint box appearance and disappearance
transform hint_box_appear:
    # Initial state
    alpha 0.0
    xoffset 50
    yoffset -30
    
    # On show: slide in and fade in
    on show:
        parallel:
            easein_back 0.4 alpha 1.0
        parallel:
            easein_back 0.4 xoffset 0
        parallel:
            easein_back 0.4 yoffset 0
    
    # On hide: slide out and fade out
    on hide:
        parallel:
            easeout 0.3 alpha 0.0
        parallel:
            easeout 0.3 xoffset 50
        parallel:
            easeout 0.3 yoffset -30

# Transform for the gorp animation (inside the box)
transform gorp_hint_transform:
    zoom 0.4
    xalign 0.0
    yalign 0.5
    yoffset -6

# Transform for hint text
transform hint_text_appear:
    alpha 0.0
    pause 0.2
    linear 0.3 alpha 1.0

# ==============================================================================
# HINT SCREEN
# ==============================================================================

screen hint_popup(hint_message=""):
    zorder 200
    modal False
    
    style_prefix "confirm"
    
    # Auto-dismiss after 5 seconds
    timer 7.0 action Hide("hint_popup")
    
    # Main hint container - positioned at top right
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        xsize 450
        ysize 180
        padding (15, 15)
        at hint_box_appear
        
        hbox:
            spacing 10
            xfill True
            
            # Gorp animation inside the box (left side)
            add "gorp_hint_animation" at gorp_hint_transform
            
            # Text content (right side)
            vbox:
                xfill True
                spacing 8
                yalign 0.1
                
                # Title
                text "A Gorpulous Hint!":
                    size 32
                    color "#fffb00"
                    font gui.interface_font
                    outlines [(2, "#000000", 0, 0)]
                
                # Hint message
                text "[hint_message]":
                    size 15
                    color "#ffffff"
                    font gui.interface_font
                    text_align 0.0
                    layout "subtitle"
                    outlines [(2, "#000000", 0, 0)]
                    at hint_text_appear

# ==============================================================================
# LABEL TO SHOW HINTS
# ==============================================================================

label show_hint(hint_message):
    python:
        global hint_text
        hint_text = hint_message
    
    # Show the hint screen (non-blocking)
    show screen hint_popup(hint_message)
    play sound "mod_assets/sfx/menu_open.ogg"
    
    return

# ==============================================================================
# ALTERNATIVE: FUNCTION-BASED APPROACH
# ==============================================================================

init python:
    def show_hint_popup(hint_message):
        """
        Python function to show a hint popup.
        
        Args:
            hint_message: The text to display as a hint
        """
        renpy.call_screen("hint_popup", hint_message=hint_message)

