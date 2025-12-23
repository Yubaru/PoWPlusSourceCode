# Image Popup System
# Usage: call image_popup("path/to/image")

# Transform for the popup effect
transform popup_fade:
    on show:
        alpha 1.0
        pause 0.1
        linear 1.0 alpha 0.0
    on hide:
        linear 1.0 alpha 0.0

# Label for displaying image popup
label image_popup(image_path):
    # Play sound effect automatically
    play sound "mod_assets/sfx/boom.ogg"
    
    # Show the image on master layer (appears on top)
    show expression image_path as popup_img at popup_fade
    
    # Wait for the full animation (0.2 + 2.0 + 1.0 = 3.2 seconds)
    pause 1.5
    
    # Hide the image
    hide popup_img
    
    return 