# ==============================================================================
# ANIMATION EXAMPLES USING RENPY'S NATIVE IMAGE SYNTAX
# ==============================================================================
# These examples show how to define animations using Renpy's built-in image
# system instead of custom wrappers.
# ==============================================================================

# Example: Crimson Transition Animation
# 24 frames at 24fps = ~0.0417 seconds per frame




# ==============================================================================
# ADDITIONAL EXAMPLES
# ==============================================================================

# Example: Simple looping animation
image example_loop:
    "mod_assets/images/example/frame1.png"
    pause 0.1
    "mod_assets/images/example/frame2.png"
    pause 0.1
    "mod_assets/images/example/frame3.png"
    pause 0.1
    repeat  # Loop forever


# Example: Animation with custom transform
image example_with_transform:
    "mod_assets/images/example/frame1.png"
    pause 0.05
    "mod_assets/images/example/frame2.png"
    pause 0.05
    
    # You can also apply transforms directly in the image definition
    block:
        zoom 1.0
        linear 0.5 zoom 1.5
        "mod_assets/images/example/frame3.png"
        pause 0.5


# Example: Using Renpy's Animation() for more complex sequences
image example_animation = Animation(
    "mod_assets/images/frame1.png", 0.1,
    "mod_assets/images/frame2.png", 0.1,
    "mod_assets/images/frame3.png", 0.1,
    "mod_assets/images/frame4.png", 0.1,
)

