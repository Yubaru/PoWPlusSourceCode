# Define the slow zoom transform for continuous zooming
transform slow_zoom:
    zoom 1.0
    linear 20.0 zoom 1.05
    pause 2.0            # Pause at max zoom
    linear 20.0 zoom 1.0
    pause 2.0            # Pause at normal size
    repeat

# Define left-to-right ghostly movement (complete animation)
transform ghost_left_to_right:
    xpos -0.1  # Start 10% off-screen to the left (reduced from -0.3)
    alpha 0.0  # Start invisible
    parallel:
        ease 2.0 alpha 0.3  # Fade in to higher visibility (30%)
        pause 10.0           # Hold visibility while moving
        ease 2.0 alpha 0.0   # Fade out at the end
    parallel:
        linear 14.0 xpos 1.1  # Move across screen to 10% off-screen right

# Define right-to-left ghostly movement (complete animation)
transform ghost_right_to_left:
    xpos 1.1   # Start 10% off-screen to the right
    alpha 0.0  # Start invisible
    parallel:
        ease 2.0 alpha 0.3  # Fade in to higher visibility (30%)
        pause 10.0           # Hold visibility while moving
        ease 2.0 alpha 0.0   # Fade out at the end
    parallel:
        linear 14.0 xpos -0.1  # Move across screen to 10% off-screen left

# Define the main dissolve transition
define main_dissolve = Dissolve(4)

# SCREEN: background_poetry_mood
screen background_poetry_mood(background_list, sprite_list=None):
    # Use tag to ensure the background system is treated as a single layer
    tag background_system
   
    default index = 0
    default max_index = len(background_list)
    default transition_timer = 15.0
    
    # Variables for sprite management
    default sprite_index = 0
    default max_sprite_index = len(sprite_list) if sprite_list else 0
    default sprite_visible = False  # Start with sprite not visible
    default sprite_direction = "left_to_right"
    default sprite_timer = 15.0  # Changed: Initial wait before first sprite (15 seconds)
    default is_sprite_active = False  # Track if a sprite is currently active
   
    # Current background with zoom
    add background_list[index] at slow_zoom
   
    # Add dust layers on top of the background
    add "y_cg2_dust1"
    add "y_cg2_dust2"
    add "y_cg2_dust3"
    add "y_cg2_dust4"
    add "y_cg2_details"
    
    # Add ghostly sprite if visible and sprites exist
    if sprite_visible and sprite_list and max_sprite_index > 0:
        add sprite_list[sprite_index] at (ghost_left_to_right if sprite_direction == "left_to_right" else ghost_right_to_left)
   
    # Timer for background transitions
    timer transition_timer repeat True action [
        SetScreenVariable("index", (index + 1) % max_index),
        Function(renpy.transition, main_dissolve)
    ]
    
    # Timer for sprite cycling - now showing one every 15 seconds
    timer sprite_timer repeat True action If(
        is_sprite_active,
        # If a sprite is active, this means it just finished its animation
        [
            # Hide the sprite and mark as inactive
            SetScreenVariable("sprite_visible", False),
            SetScreenVariable("is_sprite_active", False),
            # Move to next sprite in sequence
            SetScreenVariable("sprite_index", (sprite_index + 1) % max_sprite_index),
            # Reset timer for next appearance (15 seconds)
            SetScreenVariable("sprite_timer", 15.0),
        ],
        # If no sprite is active, time to show one
        [
            # Special case for nkill sprite (50% chance)
            If(
                sprite_list[sprite_index] == "mod_assets/images/misc/nkill.png",
                # If it's nkill, 50% chance to show
                If(
                    renpy.random.randint(1, 100) <= 75,  # 50% chance
                    [SetScreenVariable("sprite_visible", True)],  # Show it
                    [
                        # Skip it and move to next sprite
                        SetScreenVariable("sprite_index", (sprite_index + 1) % max_sprite_index),
                        SetScreenVariable("sprite_visible", True)
                    ]
                ),
                # For other sprites, always show
                [SetScreenVariable("sprite_visible", True)]
            ),
            # Mark sprite as active
            SetScreenVariable("is_sprite_active", True),
            # Decide direction
            SetScreenVariable("sprite_direction", "left_to_right" if renpy.random.randint(0, 1) == 0 else "right_to_left"),
            # Set timer for sprite animation duration (14 seconds)
            SetScreenVariable("sprite_timer", 14.0),
        ]
    )

# LABEL: yuri_monologue
label yuri_monologue:
    $ background_list = [
        "bg residential_day",
        "bg class_day",
        "bg corridor",
        "bg closet",
        "bg closetin",
        "bg floor",
        "bg floor2",
        "bg house",
        "bg kitchen",
        "bg park",
        "bg park2",
        "bg courtyard",
        "bg corridor_pov",
        "bg corridor_pov2",
        "bg natsuki_room",
        "bg music_room"
    ]
    
    # List of ghostly sprites to cycle through
    $ ghostly_sprites = [
        "mod_assets/images/misc/yuri_mono1.png",
        "mod_assets/images/misc/yuri_mono2.png",
        "mod_assets/images/misc/yuri_mono3.png",
        "mod_assets/images/misc/nkill.png"
    ]
   
    # Initialize with background system
    $ renpy.show_screen("background_poetry_mood", background_list, ghostly_sprites)
    with dissolve_cg
   
    return

# LABEL: stop_yuri_monologue
label stop_yuri_monologue:
    hide screen background_poetry_mood with dissolve
    return