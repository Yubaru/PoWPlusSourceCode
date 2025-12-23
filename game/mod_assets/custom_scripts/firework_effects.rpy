# Firework Light Effects
# Custom visual effects for firework scenes

# Transform for subtle screen flash effect
transform firework_flash:
    alpha 0.0
    linear 0.05 alpha 0.3
    linear 0.4 alpha 0.0

# Transform for gentle light glow
transform firework_glow:
    alpha 0.0
    linear 0.15 alpha 0.15
    linear 1.0 alpha 0.0

# Transform for dramatic burst effect
transform firework_burst:
    alpha 0.0
    linear 0.03 alpha 0.4
    linear 0.08 alpha 0.2
    linear 0.6 alpha 0.0

# Transform for finale multi-flash
transform firework_finale_flash:
    alpha 0.0
    linear 0.02 alpha 0.3
    linear 0.05 alpha 0.1
    linear 0.02 alpha 0.25
    linear 0.05 alpha 0.05
    linear 0.02 alpha 0.35
    linear 0.4 alpha 0.0

# Transform for distant ambient glow
transform firework_distant:
    alpha 0.0
    linear 0.2 alpha 0.08
    linear 0.8 alpha 0.0

# Improved color overlay images with more realistic firework colors
image firework_red_flash = "#ff6644"
image firework_gold_flash = "#ffcc33"
image firework_blue_flash = "#4499ff"
image firework_green_flash = "#66ff99"
image firework_purple_flash = "#aa66ff"
image firework_white_flash = "#ffffff"
image firework_orange_flash = "#ff8844"
image firework_pink_flash = "#ff6699"

# Gradient overlays for more realistic lighting
image firework_warm_glow = "#ffaa66"
image firework_cool_glow = "#66aaff"

# Main firework effect function
label firework_light_effect(color="red", intensity="normal"):
    $ firework_sound = renpy.random.choice(["mod_assets/sfx/firework1.ogg", "mod_assets/sfx/firework2.ogg", "mod_assets/sfx/firework3.ogg"])
    play sound firework_sound
    if color == "red":
        if intensity == "strong":
            show firework_red_flash at firework_burst
            with None
        elif intensity == "finale":
            show firework_red_flash at firework_finale_flash
            with None
        else:
            show firework_red_flash at firework_flash
            with None
    elif color == "gold":
        if intensity == "strong":
            show firework_gold_flash at firework_burst
            with None
        elif intensity == "finale":
            show firework_gold_flash at firework_finale_flash
            with None
        else:
            show firework_gold_flash at firework_flash
            with None
    elif color == "blue":
        if intensity == "strong":
            show firework_blue_flash at firework_burst
            with None
        elif intensity == "finale":
            show firework_blue_flash at firework_finale_flash
            with None
        else:
            show firework_blue_flash at firework_flash
            with None
    elif color == "green":
        if intensity == "strong":
            show firework_green_flash at firework_burst
            with None
        elif intensity == "finale":
            show firework_green_flash at firework_finale_flash
            with None
        else:
            show firework_green_flash at firework_flash
            with None
    elif color == "purple":
        if intensity == "strong":
            show firework_purple_flash at firework_burst
            with None
        elif intensity == "finale":
            show firework_purple_flash at firework_finale_flash
            with None
        else:
            show firework_purple_flash at firework_flash
            with None
    elif color == "white":
        if intensity == "strong":
            show firework_white_flash at firework_burst
            with None
        elif intensity == "finale":
            show firework_white_flash at firework_finale_flash
            with None
        else:
            show firework_white_flash at firework_flash
            with None
    elif color == "orange":
        if intensity == "strong":
            show firework_orange_flash at firework_burst
            with None
        elif intensity == "finale":
            show firework_orange_flash at firework_finale_flash
            with None
        else:
            show firework_orange_flash at firework_flash
            with None
    elif color == "pink":
        if intensity == "strong":
            show firework_pink_flash at firework_burst
            with None
        elif intensity == "finale":
            show firework_pink_flash at firework_finale_flash
            with None
        else:
            show firework_pink_flash at firework_flash
            with None
    
    return

# Quick call functions for common effects
label firework_red():
    call firework_light_effect("red", "normal") from _call_firework_light_effect_30
    return

label firework_gold():
    call firework_light_effect("gold", "normal") from _call_firework_light_effect_31
    return

label firework_blue():
    call firework_light_effect("blue", "normal") from _call_firework_light_effect_32
    return

label firework_green():
    call firework_light_effect("green", "normal") from _call_firework_light_effect_33
    return

label firework_orange():
    call firework_light_effect("orange", "normal") from _call_firework_light_effect_34
    return

label firework_finale():
    call firework_light_effect("white", "finale") from _call_firework_light_effect_35
    return

# Gentle ambient firework glow (for distant fireworks)
label firework_ambient_glow(color="gold"):
    if color == "gold":
        show firework_gold_flash at firework_distant
        with None
    elif color == "red":
        show firework_red_flash at firework_distant
        with None
    elif color == "blue":
        show firework_blue_flash at firework_distant
        with None
    elif color == "white":
        show firework_white_flash at firework_distant
        with None
    elif color == "warm":
        show firework_warm_glow at firework_distant
        with None
    elif color == "cool":
        show firework_cool_glow at firework_distant
        with None
    
    return

# Special combination effects
label firework_spectacular():
    call firework_light_effect("gold", "strong") from _call_firework_light_effect_36
    pause 0.3
    call firework_light_effect("blue", "normal") from _call_firework_light_effect_37
    pause 0.2
    call firework_light_effect("red", "normal") from _call_firework_light_effect_38
    return

label firework_romantic_moment():
    call firework_ambient_glow("warm") from _call_firework_ambient_glow
    return 