# Christmas Mode Changes
# Creates falling snowflakes during Christmas mode

# Default persistent variable for Christmas mode
default persistent.christmas_mode = False

# Using the actual snowflake image
# Medium size - most common
image snowflake_particle:
    "mod_assets/images/effect/snowflake.png"
    zoom 0.375  # Adjust zoom based on your image size (for 32x32 image, this gives ~12x12)

# Create smaller snowflakes for variety
image snowflake_particle_small:
    "mod_assets/images/effect/snowflake.png"
    zoom 0.1875  # Adjust zoom based on your image size (for 32x32 image, this gives ~6x6)

# Create larger snowflakes for variety
image snowflake_particle_large:
    "mod_assets/images/effect/snowflake.png"
    zoom 0.5  # Adjust zoom based on your image size (for 32x32 image, this gives ~16x16)

# Snowflake 1 - Fast fall, slight drift to the right (small)
image snowflake1:
    "snowflake_particle_small"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        8.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 200 ypos -20
        linear 8.0 xpos 250 ypos 740
        repeat
    parallel:
        rotate 0
        linear 4.0 rotate 360
        repeat

# Snowflake 2 - Medium speed, drift to the left
image snowflake2:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        12.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 500 ypos -20
        linear 12.0 xpos 420 ypos 740
        repeat
    parallel:
        rotate 45
        linear 5.0 rotate 405
        repeat

# Snowflake 3 - Slow fall, gentle drift to the right (large)
image snowflake3:
    "snowflake_particle_large"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        15.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 800 ypos -20
        linear 15.0 xpos 860 ypos 740
        repeat
    parallel:
        rotate 90
        linear 6.0 rotate 450
        repeat

# Snowflake 4 - Fast fall, minimal drift
image snowflake4:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        7.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 100 ypos -20
        linear 7.0 xpos 115 ypos 740
        repeat
    parallel:
        rotate 180
        linear 3.5 rotate 540
        repeat

# Snowflake 5 - Medium speed, wide drift to the left (large)
image snowflake5:
    "snowflake_particle_large"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        10.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 1100 ypos -20
        linear 10.0 xpos 1000 ypos 740
        repeat
    parallel:
        rotate 225
        linear 5.0 rotate 585
        repeat

# Snowflake 6 - Slow fall, moderate drift to the right
image snowflake6:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        14.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 300 ypos -20
        linear 14.0 xpos 370 ypos 740
        repeat
    parallel:
        rotate 270
        linear 7.0 rotate 630
        repeat

# Snowflake 7 - Fast fall, moderate drift to the left
image snowflake7:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        9.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 900 ypos -20
        linear 9.0 xpos 860 ypos 740
        repeat
    parallel:
        rotate 315
        linear 4.5 rotate 675
        repeat

# Snowflake 8 - Very slow fall, gentle drift to the right (small)
image snowflake8:
    "snowflake_particle_small"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        18.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 600 ypos -20
        linear 18.0 xpos 650 ypos 740
        repeat
    parallel:
        rotate 135
        linear 9.0 rotate 495
        repeat

# Snowflake 9 - Medium speed, slight drift to the left
image snowflake9:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        11.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 1000 ypos -20
        linear 11.0 xpos 965 ypos 740
        repeat
    parallel:
        rotate 20
        linear 5.5 rotate 380
        repeat

# Snowflake 10 - Fast fall, wide drift to the right
image snowflake10:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        6.5
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 400 ypos -20
        linear 6.5 xpos 490 ypos 740
        repeat
    parallel:
        rotate 160
        linear 3.25 rotate 520
        repeat

# Snowflake 11 - Medium speed, drift to the right (small)
image snowflake11:
    "snowflake_particle_small"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        9.5
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 150 ypos -20
        linear 9.5 xpos 200 ypos 740
        repeat
    parallel:
        rotate 60
        linear 4.75 rotate 420
        repeat

# Snowflake 12 - Slow fall, drift to the left (large)
image snowflake12:
    "snowflake_particle_large"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        13.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 700 ypos -20
        linear 13.0 xpos 630 ypos 740
        repeat
    parallel:
        rotate 120
        linear 6.5 rotate 480
        repeat

# Snowflake 13 - Fast fall, minimal drift (small)
image snowflake13:
    "snowflake_particle_small"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        7.5
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 250 ypos -20
        linear 7.5 xpos 270 ypos 740
        repeat
    parallel:
        rotate 200
        linear 3.75 rotate 560
        repeat

# Snowflake 14 - Medium speed, wide drift to the right
image snowflake14:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        10.5
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 550 ypos -20
        linear 10.5 xpos 620 ypos 740
        repeat
    parallel:
        rotate 280
        linear 5.25 rotate 640
        repeat

# Snowflake 15 - Very slow fall, gentle drift to the left (large)
image snowflake15:
    "snowflake_particle_large"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        16.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 950 ypos -20
        linear 16.0 xpos 880 ypos 740
        repeat
    parallel:
        rotate 30
        linear 8.0 rotate 390
        repeat

# Snowflake 16 - Fast fall, moderate drift to the right (small)
image snowflake16:
    "snowflake_particle_small"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        8.5
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 350 ypos -20
        linear 8.5 xpos 410 ypos 740
        repeat
    parallel:
        rotate 340
        linear 4.25 rotate 700
        repeat

# Snowflake 17 - Medium speed, slight drift to the left
image snowflake17:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        11.5
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 750 ypos -20
        linear 11.5 xpos 720 ypos 740
        repeat
    parallel:
        rotate 100
        linear 5.75 rotate 460
        repeat

# Snowflake 18 - Slow fall, wide drift to the right (small)
image snowflake18:
    "snowflake_particle_small"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        14.5
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 450 ypos -20
        linear 14.5 xpos 530 ypos 740
        repeat
    parallel:
        rotate 240
        linear 7.25 rotate 600
        repeat

# Snowflake 19 - Fast fall, drift to the left (large)
image snowflake19:
    "snowflake_particle_large"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        9.0
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 1050 ypos -20
        linear 9.0 xpos 980 ypos 740
        repeat
    parallel:
        rotate 50
        linear 4.5 rotate 410
        repeat

# Snowflake 20 - Medium speed, moderate drift to the right
image snowflake20:
    "snowflake_particle"
    subpixel True
    parallel:
        alpha 0
        linear 0.5 alpha 1.0
        12.5
        linear 0.5 alpha 0
        repeat
    parallel:
        xpos 650 ypos -20
        linear 12.5 xpos 710 ypos 740
        repeat
    parallel:
        rotate 150
        linear 6.25 rotate 510
        repeat

# Define images to show in your scene
image snow_falling1:
    "snowflake1"

image snow_falling2:
    "snowflake2"

image snow_falling3:
    "snowflake3"

image snow_falling4:
    "snowflake4"

image snow_falling5:
    "snowflake5"

image snow_falling6:
    "snowflake6"

image snow_falling7:
    "snowflake7"

image snow_falling8:
    "snowflake8"

image snow_falling9:
    "snowflake9"

image snow_falling10:
    "snowflake10"

image snow_falling11:
    "snowflake11"

image snow_falling12:
    "snowflake12"

image snow_falling13:
    "snowflake13"

image snow_falling14:
    "snowflake14"

image snow_falling15:
    "snowflake15"

image snow_falling16:
    "snowflake16"

image snow_falling17:
    "snowflake17"

image snow_falling18:
    "snowflake18"

image snow_falling19:
    "snowflake19"

image snow_falling20:
    "snowflake20"

# Screen for snow effect - only shows during Christmas mode
screen snow_effect():
    tag snow
    modal False
    zorder 10  # Above background but below UI elements like dialogue windows
    
    if persistent.christmas_mode:
        add "snow_falling1"
        add "snow_falling2"
        add "snow_falling3"
        add "snow_falling4"
        add "snow_falling5"
        add "snow_falling6"
        add "snow_falling7"
        add "snow_falling8"
        add "snow_falling9"
        add "snow_falling10"
        add "snow_falling11"
        add "snow_falling12"
        add "snow_falling13"
        add "snow_falling14"
        add "snow_falling15"
        add "snow_falling16"
        add "snow_falling17"
        add "snow_falling18"
        add "snow_falling19"
        add "snow_falling20"

# Automatically show/hide snow effect based on Christmas mode
init python:
    def update_snow_effect():
        """
        Checks the persistent state and shows/hides the screen only if necessary.
        This prevents restarting the animation loop if the screen is already shown.
        """
        if persistent.christmas_mode:
            # FIX: Only show if NOT already showing. This prevents the reset.
            if not renpy.get_screen("snow_effect"):
                renpy.show_screen("snow_effect", _tag="snow")
        else:
            # Only hide if currently showing
            if renpy.get_screen("snow_effect"):
                renpy.hide_screen("snow_effect", _tag="snow")
    
    # Show snow on startup and after load. 
    # Ren'Py screens persist across interaction, so we REMOVED interact_callbacks.
    config.start_callbacks.append(update_snow_effect)
    config.after_load_callbacks.append(update_snow_effect)
    
    # Function to toggle Christmas mode
    def toggle_christmas_mode():
        """Toggle Christmas mode and show/hide snow"""
        persistent.christmas_mode = not persistent.christmas_mode
        update_snow_effect()
        renpy.restart_interaction()