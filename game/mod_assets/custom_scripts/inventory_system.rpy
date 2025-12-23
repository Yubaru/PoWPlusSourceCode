# Simple Item Inspection System
default inventory_resumed_music = False  # Safe for rollback
default inventory_current_music_file = None
default inventory_current_music_pos = 0.0

init python:
    import os
    import random
    
    # Music handling functions
    def save_current_music():
        global inventory_current_music_file, inventory_current_music_pos, inventory_resumed_music
        
        # Save current music state
        inventory_current_music_file = renpy.music.get_playing(channel="music")
        inventory_current_music_pos = renpy.music.get_pos(channel="music") or 0.0
        inventory_resumed_music = False
        
    def restore_music():
        global inventory_current_music_file, inventory_current_music_pos, inventory_resumed_music
        
        if inventory_resumed_music:
            return
            
        if inventory_current_music_file:
            renpy.music.stop(channel="music", fadeout=1.5)
            renpy.music.play(inventory_current_music_file, fadein=1.5, loop=True, channel="music")
            inventory_resumed_music = True
    
    # Set up music handling - loop music and prevent it from stopping
    renpy.music.register_channel("music_loop", mixer="music", loop=True)
    
    # Define all available items
    available_items = {
        "small_bear": {
            "name": "Small Stuffed Bear",
            "image": "gui/small_bear.png",
            "description": "A small stuffed bear. It's cute, but it's not a good luck charm."
        },
        "literature_poster": {
            "name": "Literature Club Poster",
            "image": "gui/poster_item.png",
            "description": "The Literature Club poster you made."
        },
        "liquid_love": {
            "name": "Yazz's Liquid Love",
            "image": "gui/liquid_love.png",
            "description": "A liquid fabricated by your friend Yazz."
        },
        "ice_cream": {
            "name": "Ice Cream Sundae",
            "image": "gui/ice_cream.png",
            "description": "A delicious ice cream sundae you got at the festival."
        },
        "haunted_ticket": {
            "name": "Haunted House Ticket",
            "image": "gui/haunted_ticket.png",
            "description": "A ticket to the haunted house attraction at the festival."
        },
        "mr_cow": {
            "name": "Mr. Cow",
            "image": "gui/mr_cow.png",
            "description": "A stuffed cow you got at the ring toss game...?"
        },
        "small_bunny": {
            "name": "Small Stuffed Bunny",
            "image": "gui/small_bunny.png",
            "description": "A small stuffed bunny you got at the ring toss game."
        },
        "nubert": {
            "name": "nubert",
            "image": "gui/nubert.png",
            "description": "nubert"
        },
        "beavis": {
            "name": "Beavis",
            "image": "gui/beavis.png",
            "description": "This nigger looks a little bit too happy."
        }
    }

    # Placeholder content
    PLACEHOLDER_IMAGE = "gui/placeholder.png"
    PLACEHOLDER_NAME = "Unknown Item"
    PLACEHOLDER_DESC = "This item's information could not be loaded."
    
    # Function to play rapist theme music
    def play_rapist_theme():
        # Don't save current music if we're already playing the theme
        if renpy.music.get_playing(channel="music") != "mod_assets/music/rapist_theme.ogg":
            # Save current music state for restoration later
            save_current_music()
            
        # Store what we played in a persistent variable for recovery
        persistent._rapist_theme_playing = True
        renpy.music.play("mod_assets/music/rapist_theme.ogg", channel="music", fadein=2.0, loop=True)
    
    # Function to play duke dennis theme music
    def play_dennis_theme():
        # Don't save current music if we're already playing the theme
        if renpy.music.get_playing(channel="music") != "mod_assets/music/duke_dennis_theme.ogg":
            # Save current music state for restoration later
            save_current_music()
            
        # Store what we played in a persistent variable for recovery
        persistent._dennis_theme_playing = True
        renpy.music.play("mod_assets/music/duke_dennis_theme.ogg", channel="music", fadein=2.0, loop=True)
    
    # Function to restore normal music
    def restore_normal_music():
        # Clear flags when we're switching away from theme
        persistent._rapist_theme_playing = False
        persistent._dennis_theme_playing = False
        
        # Restore music that was playing before
        restore_music()
    
    # Color for rapist rizz text - can be edited here to change all text colors
    RAPIST_RIZZ_TEXT_COLOR = "#334e28"  # Default is blood red
    
    # Color for duke dennis rizz text
    DUKE_DENNIS_RIZZ_TEXT_COLOR = "#ffd700"  # Gold color
    
    # Dimming level for Rapist Rizz (0.0 = no dimming, 1.0 = completely black)
    RAPIST_RIZZ_DIM_LEVEL = 0.6
    
    # Dimming level for Duke Dennis Rizz (0.0 = no dimming, 1.0 = completely black)
    DUKE_DENNIS_DIM_LEVEL = 0.0  # Lighter dim for the gold aura effect
    
    # Mapping of rizz skills to their image paths
    rizz_image_mapping = {
        # The paths that work for sure (based on what you said)
        "Unspoken Duke Dennis Rizz": "mod_assets/images/inv/rizzstatus/jackorizz_unspoken_duke_dennis_rizz.png",
        "Rapist Rizz": "mod_assets/images/inv/rizzstatus/jackorizz_rapist_rizz.png",
        "L Rizz": "mod_assets/images/inv/rizzstatus/jackorizz_l_rizz.png",
        
        # Try alternative paths (with PNG capitalized since that might be the issue)
        "Rizz God": "mod_assets/images/inv/rizzstatus/jackorizz_rizz_god.PNG",
        "Rizzilisious": "mod_assets/images/inv/rizzstatus/jackorizz_rizzilisious.PNG",
        "Rizzler": "mod_assets/images/inv/rizzstatus/jackorizz_rizzler.PNG",
        "Rizzin' Up": "mod_assets/images/inv/rizzstatus/jackorizz_rizzin_up.PNG",
        "Rizz Apprentice": "mod_assets/images/inv/rizzstatus/jackorizz_rizz_apprentice.PNG",
        "Incel Rizz": "mod_assets/images/inv/rizzstatus/jackorizz_incel_rizz.PNG",
        "Yazz Rizz": "mod_assets/images/inv/rizzstatus/jackorizz_yazz_rizz.PNG",
        "It's All Coming Down Rizz": "mod_assets/images/inv/rizzstatus/jackorizz_its_all_coming_down_rizz.PNG",
        "Green Aura With Flies Rizz": "mod_assets/images/inv/rizzstatus/jackorizz_green_aura_with_flies_rizz.PNG"
    }
    
    # Default image to use if a rizz skill isn't in the mapping
    DEFAULT_JACKORIZZ_IMAGE = "mod_assets/images/inv/rizzstatus/jackorizz_l_rizz.png"
    
    # Static effect variables
    static_alpha = 0.0  # Current alpha of static
    static_showing = False  # Is static currently showing
    static_timer = 0  # Timer for hiding static
    
    # Noise effect variables
    noise_alpha = 0.0  # Current alpha of noise
    noise_showing = False  # Is noise currently showing
    noise_timer = 0  # Timer for hiding noise
    current_noise = 1  # Current noise image (1-4)
    
    # Animation frame timing (seconds per frame)
    NOISE_FRAME_TIME = 0.03  # Reduced from 0.05 to 0.03 seconds per frame (33% faster)
    noise_frame_timer = 0  # Timer for changing animation frames
    
    # Function to randomly show static
    def show_random_static():
        global static_alpha, static_showing, static_timer
        if not static_showing and random.random() < 0.7:  # Increased from 0.3 to 0.7 - 70% chance to show static
            static_alpha = random.uniform(0.5, 0.9)  # Increased from 0.3-0.8 to 0.5-0.9 for more visibility
            static_showing = True
            # Play static sound
            renpy.sound.play("sfx/s_kill_glitch1.ogg", channel="sound")
            # Set a timer to hide static after a random duration
            static_timer = random.uniform(0.2, 0.4)  # Increased from 0.1-0.3 to 0.2-0.4 for longer duration
            renpy.restart_interaction()
        return
        
    # Function to update static timer and hide static
    def update_static(dt):
        global static_alpha, static_showing, static_timer
        if static_showing:
            static_timer -= dt
            if static_timer <= 0:
                static_alpha = 0.0
                static_showing = False
                renpy.restart_interaction()
        return
        
    # Function to randomly start the noise animation
    def show_random_noise():
        global noise_alpha, noise_showing, noise_timer, current_noise, noise_frame_timer
        if not noise_showing and random.random() < 0.5:  # 50% chance to show noise
            noise_alpha = random.uniform(0.25, 0.4)  # Reduced from 0.4-0.7 to 0.25-0.4 for more transparency
            noise_showing = True
            # Start from the first frame
            current_noise = 1
            noise_frame_timer = NOISE_FRAME_TIME
            # Play noise sound
            renpy.sound.play("mod_assets/sfx/static.ogg", channel="sound")
            # Set a timer for the whole animation duration
            noise_timer = 0.4  # Reduced from 0.5 to 0.4 seconds to match faster frame rate
            renpy.restart_interaction()
        return
        
    # Function to update noise animation
    def update_noise(dt):
        global noise_alpha, noise_showing, noise_timer, current_noise, noise_frame_timer
        if noise_showing:
            # Update main timer for overall animation
            noise_timer -= dt
            
            # Update frame timer
            noise_frame_timer -= dt
            if noise_frame_timer <= 0:
                # Advance to next frame
                current_noise = current_noise % 4 + 1  # Cycle 1->2->3->4->1...
                noise_frame_timer = NOISE_FRAME_TIME
                renpy.restart_interaction()
            
            # End animation when overall timer expires
            if noise_timer <= 0:
                noise_alpha = 0.0
                noise_showing = False
                renpy.restart_interaction()
        return
        
    # Function to show golden particles (for Duke Dennis Rizz)
    def show_golden_particles():
        global gold_particles_showing
        if not gold_particles_showing and random.random() < 0.6:  # 60% chance to show particles
            gold_particles_showing = True
            renpy.restart_interaction()
        return
        
    # Function to update golden particles
    def update_golden_particles(dt):
        global gold_particles_timer
        # The particles themselves never disappear
        # We just reset the timer for the next update
        gold_particles_timer = renpy.random.uniform(0.5, 1.5)
        return
        
    # Function to debug image loading
    def debug_image_loading(skill, path, loadable):
        renpy.log("Rizz Image Debug - Skill: " + skill)
        renpy.log("Trying to load: " + path)
        renpy.log("Is loadable: " + str(loadable))
        
        # Also write to a text file for easier inspection
        with open(renpy.config.savedir + "/image_debug.txt", "a") as f:
            f.write("Skill: " + skill + "\n")
            f.write("Path: " + path + "\n")
            f.write("Loadable: " + str(loadable) + "\n\n")
            
        return loadable
        
    # Function to list directory contents
    def list_directory_contents(path):
        import os
        
        # Get the full path
        full_path = os.path.join(renpy.config.gamedir, path)
        results = []
        
        try:
            # List files in directory
            files = os.listdir(full_path)
            
            # Write to log
            with open(renpy.config.savedir + "/directory_contents.txt", "a") as f:
                f.write("\nListing contents of: " + path + "\n")
                for file in sorted(files):
                    f.write("- " + file + "\n")
                    results.append(file)
                f.write("\n")
            
            return results
        except Exception as e:
            # Log error
            with open(renpy.config.savedir + "/directory_contents.txt", "a") as f:
                f.write("\nError listing contents of: " + path + "\n")
                f.write("Error: " + str(e) + "\n\n")
            return []

# Default gold particles variables
default gold_particles_showing = False
default gold_particles_timer = 1.0

# Define ItemCollection class
init python:
    class ItemCollection:
        def __init__(self):
            self.items = []
            self.selected_index = 0
            self.previous_index = 0  # Track previous index
            self.close_up_view = False
            self.tutorial_shown = False
            self.waiting_for_inventory = False
            self.right_key_pressed = False
            self.left_key_pressed = False
            self.showing_rizz_status = False
            self.up_key_pressed = False
            self.down_key_pressed = False
            self.exiting_rizz_status = False
            self.cycling_direction = None
            self.showing_previous_item = False  # Flag for showing transition
            self.jackorizz_number = 1  # Initialize jackorizz image number
            self.rapist_music_playing = False  # Flag for tracking music state
            self.dennis_music_playing = False  # Flag for Duke Dennis music
            
        def add_item(self, item_id):
            if item_id in available_items and item_id not in self.items:
                self.items.append(item_id)
                return True
            return False
            
        def get_item(self, index):
            if 0 <= index < len(self.items):
                item_id = self.items[index]
                try:
                    return available_items[item_id]
                except:
                    return {
                        "name": PLACEHOLDER_NAME,
                        "image": PLACEHOLDER_IMAGE,
                        "description": PLACEHOLDER_DESC
                    }
            return None

# Default item collection instance
default items = ItemCollection()

# Transform definitions
transform zoom_in:
    zoom 1.0
    yalign 0.9
    linear 0.3 zoom 1.5 yalign 0.5

transform zoom_out:
    zoom 1.5
    yalign 0.5
    linear 0.3 zoom 1.0 yalign 0.9

transform fade_out:
    alpha 1.0
    linear 0.3 alpha 0.0

transform fade_in:
    alpha 0.0
    linear 0.3 alpha 1.0

transform notify_appear:
    on show:
        xoffset 500
        easein_quad 0.5 xoffset -20
    on hide:
        easeout_quad 0.5 xoffset 500
    on replaced:
        xoffset -20

# Transforms for rizz status view
transform slide_down:
    yoffset 0
    easeout 0.5 yoffset 700

transform slide_up:
    yoffset 700
    easein 0.5 yoffset 0

transform slide_down_pointing:
    parallel:
        yoffset 0
        easeout 0.5 yoffset 700
    parallel:
        linear 0.5

# Arrow key animations
transform arrow_key_up_animation:
    yoffset 0
    easeout 0.1 yoffset -20
    easein 0.1 yoffset 0

transform arrow_key_down_animation:
    yoffset 0
    easeout 0.1 yoffset 20
    easein 0.1 yoffset 0

# Arrow button animations
transform arrow_press_right:
    on idle:
        xoffset 0
        alpha 1.0
    on hover:
        xoffset 0
        alpha 1.0
    on selected:
        parallel:
            xoffset 0
            easeout 0.1 xoffset 20
            easein 0.1 xoffset 0
        parallel:
            alpha 1.0
            linear 0.1 alpha 0.5
            linear 0.1 alpha 1.0

transform arrow_press_left:
    on idle:
        xoffset 0
        alpha 1.0
    on hover:
        xoffset 0
        alpha 1.0
    on selected:
        parallel:
            xoffset 0
            easeout 0.1 xoffset -20
            easein 0.1 xoffset 0
        parallel:
            alpha 1.0
            linear 0.1 alpha 0.5
            linear 0.1 alpha 1.0

transform arrow_key_right_animation:
    xoffset 0
    easeout 0.1 xoffset 20
    easein 0.1 xoffset 0

transform arrow_key_left_animation:
    xoffset 0
    easeout 0.1 xoffset -20
    easein 0.1 xoffset 0

# Tutorial transforms
transform character_normal:
    yalign 1.0
    xalign 0.3
    zoom 0.8
    easein 0.5 yalign 0.7

transform float_up:
    yoffset 20
    alpha 0.0
    easein 0.5 yoffset 0 alpha 1.0
    on hide:
        easeout 0.5 yoffset -20 alpha 0.0

transform dim_screen:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform blur_screen:
    blur 0
    linear 0.5 blur 10
    on hide:
        linear 0.5 blur 0

transform slide_down_inventory:
    parallel:
        yoffset 0
        easeout 0.5 yoffset 700
    parallel:
        alpha 1.0
        linear 0.5 alpha 0.0

transform slide_up_rizz_status:
    yoffset -700
    pause 0.3  # Wait for inventory to slide down first
    parallel:
        easein 0.5 yoffset 0
    parallel:
        linear 0.5

transform slide_down_rizz_status:
    yoffset 700
    alpha 0.0
    pause 0.3  # Wait for inventory to slide down first
    parallel:
        easein 0.5 yoffset 0
    parallel:
        linear 0.5 alpha 1.0

transform slide_up_inventory:
    yoffset 700
    alpha 0.0
    pause 0.3  # Wait for rizz status to slide down first
    parallel:
        easein 0.5 yoffset 0
    parallel:
        linear 0.5 alpha 1.0

transform slide_down_rizz_status_exit:
    parallel:
        yoffset 0
        easeout 0.5 yoffset 700
    parallel:
        alpha 1.0
        linear 0.5 alpha 0.0

transform slide_up_exit:
    parallel:
        yoffset 0
        easeout 0.5 yoffset -700
    parallel:
        alpha 1.0
        linear 0.5 alpha 0.0
    linear 0.1  # Add a small delay at the end to ensure animation completes

# Tutorial screens
screen tutorial_elements():
    zorder 98
    if not renpy.get_screen("item_inspection_screen"):
        add Solid("#000") as dim:
            alpha 0.6
            at dim_screen
        add Solid("#00000000") as blur:
            at blur_screen

screen tutorial_text(speaker, message, xpos=0.7, ypos=0.3, size=36, color="#ffffff"):
    zorder 101
    vbox:
        xalign xpos
        yalign ypos
        spacing 5
        if speaker:
            text speaker:
                size size-8
                color "#fcb5d9"
                outlines [ (3, "#000", 0, 0)]
                bold True
        text message:
            size size
            color color
            outlines [ (3, "#000", 0, 0)]
            at float_up

# Inventory toggle screen
screen toggle_inventory():
    key "i" action If(
        renpy.get_screen("item_inspection_screen"),
        [Play("sound", "mod_assets/sfx/menu_close.ogg"),
        Hide("item_inspection_screen", transition=dissolve)],
        [Play("sound", "mod_assets/sfx/menu_open.ogg"),
        Show("item_inspection_screen", transition=dissolve)]
    )

# Screen for displaying static effect
screen static_effect():
    zorder 150  # Above most elements
    if static_showing:
        add "m_rectstatic" at Transform(alpha=static_alpha)
        timer 0.016 repeat True action Function(update_static, 0.016)  # 60 FPS update

# Screen for displaying noise effect
screen noise_effect():
    zorder 151  # Above static
    if noise_showing:
        add "mod_assets/images/effect/noise[current_noise].png" at Transform(alpha=noise_alpha)
        timer 0.016 repeat True action Function(update_noise, 0.016)  # 60 FPS update

# Define m_rectstatic if it's not already defined
init python:
    if not renpy.has_image("m_rectstatic"):
        renpy.image("m_rectstatic", "mod_assets/images/effects/static.png")
        
# Item inspection screen
screen item_inspection_screen():
    python:
        # Ensure new attributes exist for compatibility with old saves
        if not hasattr(items, "right_key_pressed"):
            items.right_key_pressed = False
        if not hasattr(items, "left_key_pressed"):
            items.left_key_pressed = False
        if not hasattr(items, "showing_rizz_status"):
            items.showing_rizz_status = False
        if not hasattr(items, "up_key_pressed"):
            items.up_key_pressed = False
        if not hasattr(items, "down_key_pressed"):
            items.down_key_pressed = False
        if not hasattr(items, "cycling_direction"):
            items.cycling_direction = None
        if not hasattr(items, "exiting_rizz_status"):
            items.exiting_rizz_status = False
        if not hasattr(items, "previous_index"):
            items.previous_index = 0
        if not hasattr(items, "showing_previous_item"):
            items.showing_previous_item = False
        if not hasattr(items, "jackorizz_number"):
            items.jackorizz_number = 1
        if not hasattr(items, "rapist_music_playing"):
            items.rapist_music_playing = False
            
        # Special handling for music during screen transitions
        current_music = renpy.music.get_playing(channel="music")
        music_pos = renpy.music.get_pos(channel="music")
        
        # If music stopped and we were playing the theme, restart it
        if items.rapist_music_playing and persistent.rizz_skill == "Rapist Rizz" and not current_music:
            play_rapist_theme()
            
        # Add Duke Dennis music handling
        dennis_music_playing = getattr(items, "dennis_music_playing", False)
        if dennis_music_playing and persistent.rizz_skill == "Unspoken Duke Dennis Rizz" and not current_music:
            play_dennis_theme()
        
        # Set up current and previous items
        current_item = items.get_item(items.selected_index) if items.items else None
        previous_item = items.get_item(items.previous_index) if items.items and items.showing_previous_item else None
    
    modal True
    predict False # Don't predict this screen to avoid issues with music
    
    # Save current music when first showing the screen
    on "show" action Function(save_current_music)
    
    add "menu_bg"
    add "menu_fade"

    # Show vertical line animation when transitioning
    if items.up_key_pressed:
        $ line_anim.start("up")
        for i in range(1, 15):  # Changed to 14 frames (1-14)
            add "mod_assets/images/inv/wind{:04d}.png".format(i):
                alpha 0.7
                at vertical_lines_up
                
    if items.down_key_pressed:
        $ line_anim.start("down")
        for i in range(1, 15):  # Changed to 14 frames (1-14)
            add "mod_assets/images/inv/wind{:04d}.png".format(i):
                alpha 0.7
                at vertical_lines_down

    # Reset arrow key flags after a short delay
    if items.right_key_pressed:
        timer 0.2 action [SetField(items, "right_key_pressed", False), Function(renpy.restart_interaction)]
    
    if items.left_key_pressed:
        timer 0.2 action [SetField(items, "left_key_pressed", False), Function(renpy.restart_interaction)]
    
    if items.up_key_pressed:
        timer 0.5 action [SetField(items, "up_key_pressed", False), Function(renpy.restart_interaction)]
    
    if items.down_key_pressed:
        timer 0.5 action [SetField(items, "down_key_pressed", False), Function(renpy.restart_interaction)]

    # Main inventory container that will animate everything together
    frame:
        xalign 0.5
        yalign 0.4
        xsize 800
        ysize 600
        background None
        at (slide_down_inventory if items.showing_rizz_status else slide_up_inventory)

        if not items.close_up_view:
            text "Inventory" size 50 color "#FFFFFF" xalign 0.5 yalign 0.07
        else:
            text "Inventory" size 50 color "#FFFFFF" xalign 0.5 yalign 0.07 at fade_out

        # Pointing image with proper fade handling
        if not items.close_up_view:
            add "mod_assets/images/inv/pointing.png":
                xalign 0.5
                yalign 0.4
        else:
            add "mod_assets/images/inv/pointing.png":
                xalign 0.5
                yalign 0.4
                at pointing_fade

        # Inventory content
        fixed:
            xalign 0.5
            yalign 0.5
            xsize 800
            ysize 500

            if items.items:
                if current_item:
                    # Show the previous item with exit animation if cycling
                    if previous_item and items.showing_previous_item and items.cycling_direction:
                        fixed:
                            xsize 500
                            ysize 500
                            xalign 0.5
                            yalign 0.9
                            if items.close_up_view:
                                if items.cycling_direction == "right":
                                    add previous_item["image"] at inspection_slide_out_left xalign 0.5 yalign 0.5
                                else:
                                    add previous_item["image"] at inspection_slide_out_right xalign 0.5 yalign 0.5
                            else:
                                if items.cycling_direction == "right":
                                    add previous_item["image"] at item_slide_out_left xalign 0.5 yalign 0.9
                                else:
                                    add previous_item["image"] at item_slide_out_right xalign 0.5 yalign 0.9
                    
                    # Show the current item - with sliding but no bounce
                    fixed:
                        xsize 500
                        ysize 500
                        xalign 0.5
                        yalign 0.9

                        # For close-up view, just show the zoomed image
                        if items.close_up_view:
                            if items.cycling_direction == "right":
                                add current_item["image"]:
                                    zoom 1.5
                                    xalign 0.5 
                                    yalign 0.5
                                    at inspection_slide_in_right
                            elif items.cycling_direction == "left":
                                add current_item["image"]:
                                    zoom 1.5
                                    xalign 0.5 
                                    yalign 0.5
                                    at inspection_slide_in_left
                            else:
                                add current_item["image"]:
                                    zoom 1.5
                                    xalign 0.5 
                                    yalign 0.5
                                    at inspection_zoom_in
                        # For normal view, add back sliding animations
                        else:
                            if items.cycling_direction == "right":
                                add current_item["image"] at item_slide_in_right xalign 0.5 yalign 0.9
                            elif items.cycling_direction == "left":
                                add current_item["image"] at item_slide_in_left xalign 0.5 yalign 0.9
                            else:
                                add current_item["image"]:
                                    zoom 1.0
                                    xalign 0.5 
                                    yalign 0.9

                        # Reset cycling state after a short delay
                        if items.cycling_direction:
                            timer 0.3 action [
                                SetField(items, "cycling_direction", None),
                                SetField(items, "showing_previous_item", False),
                                Function(renpy.restart_interaction)
                            ]

                    if not items.close_up_view:
                        vbox:
                            xsize 700
                            spacing 20
                            xalign 0.5
                            yalign 0.2
                            
                            text current_item["name"]:
                                size 40
                                color "#fcb5d9"
                                xalign 0.5
                                text_align 0.5
                                at item_name_glow
                            
                            frame:
                                xsize 650
                                ysize 100
                                xalign 0.5
                                background None
                                
                                text current_item["description"]:
                                    size 30
                                    color "#FFFFFF"
                                    xalign 0.5
                                    text_align 0.5
                                    layout "subtitle"
                                    at fade_in
                else:
                    text "Empty" size 50 color "#FFFFFF" xalign 0.5 yalign 0.5

        # Arrow navigation for inventory items (inside the main container)
        if len(items.items) > 1 and not items.close_up_view and not items.showing_rizz_status:
            textbutton "<":
                text_size 60
                text_color "#FFFFFF"
                text_outlines [(2, "#E17AAF", 0, 0)]
                xalign 0.1
                yalign 0.22
                at (arrow_press_left if not items.left_key_pressed else arrow_key_left_animation)
                action [
                    SetField(items, "previous_index", items.selected_index),
                    SetField(items, "selected_index", (items.selected_index - 1) % len(items.items)),
                    SetField(items, "left_key_pressed", True),
                    SetField(items, "cycling_direction", "left"),
                    SetField(items, "showing_previous_item", True),
                    Play("sound", "mod_assets/sfx/menu_move.ogg"),
                    Function(renpy.restart_interaction)
                ]

            textbutton ">":
                text_size 60
                text_color "#FFFFFF"
                text_outlines [(2, "#E17AAF", 0, 0)]
                xalign 0.9
                yalign 0.22
                at (arrow_press_right if not items.right_key_pressed else arrow_key_right_animation)
                action [
                    SetField(items, "previous_index", items.selected_index),
                    SetField(items, "selected_index", (items.selected_index + 1) % len(items.items)),
                    SetField(items, "right_key_pressed", True),
                    SetField(items, "cycling_direction", "right"),
                    SetField(items, "showing_previous_item", True),
                    Play("sound", "mod_assets/sfx/menu_move.ogg"),
                    Function(renpy.restart_interaction)
                ]

            # Up arrow (inside main container)
            textbutton "^":
                text_size 40
                text_color "#FFFFFF"
                text_outlines [(2, "#E17AAF", 0, 0)]
                xalign 0.5
                yalign 0.0
                at (arrow_key_up_animation if items.up_key_pressed else None)
                action [
                    SetField(items, "showing_rizz_status", True),
                    SetField(items, "up_key_pressed", True),
                    Play("sound", "mod_assets/sfx/menu_up.ogg"),
                    Function(renpy.restart_interaction)
                ]

    # Rizz Status Section (main, entry animation)
    if items.showing_rizz_status:
        # Check if player has Rapist Rizz or Duke Dennis Rizz
        $ is_rapist_rizz = (persistent.rizz_skill == "Rapist Rizz")
        $ is_duke_dennis_rizz = (persistent.rizz_skill == "Unspoken Duke Dennis Rizz")
        
        # Silently check directory exists without notifications
        python:
            import os
            # Check if directory exists
            dir_path = os.path.join(renpy.config.gamedir, "mod_assets/images/inv/rizzstatus")
            if not os.path.exists(dir_path):
                try:
                    os.makedirs(dir_path, exist_ok=True)
                except:
                    pass
        
        # Play creepy music if Rapist Rizz (only once when the screen appears)
        if is_rapist_rizz and (not hasattr(items, "rapist_music_playing") or not items.rapist_music_playing):
            $ play_rapist_theme()
            $ items.rapist_music_playing = True
            
        # Play duke dennis music if Duke Dennis Rizz
        if is_duke_dennis_rizz and (not hasattr(items, "dennis_music_playing") or not items.dennis_music_playing):
            $ play_dennis_theme()
            $ items.dennis_music_playing = True
        
        # Add a dim overlay for Rapist Rizz
        if is_rapist_rizz:
            add "black" at dim_pulse(RAPIST_RIZZ_DIM_LEVEL)
            
            # TEST: Force static to show immediately when entering rizz status
            $ static_alpha = 0.8
            $ static_showing = True
            $ static_timer = 0.5
            
            # TEST: Force noise animation to show immediately when entering rizz status
            $ noise_alpha = 0.35  # More transparent (was 0.6)
            $ noise_showing = True
            $ noise_timer = 0.8  # Longer duration to see multiple animation cycles
            $ current_noise = 1  # Start with first frame
            $ noise_frame_timer = NOISE_FRAME_TIME  # Initialize frame timer
            
            # Add timer to trigger static effects
            timer 0.7 repeat True action If(items.showing_rizz_status and is_rapist_rizz, Function(show_random_static))
            
            # Add timer to trigger noise effects
            timer 1.2 repeat True action If(items.showing_rizz_status and is_rapist_rizz, Function(show_random_noise))
            
            # Explicitly show the static and noise effect screens
            $ renpy.show_screen("static_effect")
            $ renpy.show_screen("noise_effect")
            
        # Add golden aura for Duke Dennis Rizz
        elif is_duke_dennis_rizz:
            add "black" at dim_pulse(DUKE_DENNIS_DIM_LEVEL)
            
            # Add gold particles
            $ gold_particles_showing = True
            $ gold_particles_timer = 1.0
            
            # Add golden border vignette effect
            add "mod_assets/images/effect/gold_vignette.png" at golden_border_pulse
            
            # Add timer to trigger gold particle effects
            timer 1.0 repeat True action If(items.showing_rizz_status and is_duke_dennis_rizz, Function(show_golden_particles))
            
            # Show the gold particle effect screen
            $ renpy.show_screen("gold_particle_effect")
        
        frame:
            xalign rizz_frame_xalign
            yalign rizz_frame_yalign
            xsize rizz_frame_xsize
            ysize rizz_frame_ysize
            background None
            at (rapist_slide_shake if is_rapist_rizz else duke_dennis_slide if is_duke_dennis_rizz else slide_up_rizz_status)

            # Add the jackorizz image based on mapping - SIMPLIFIED APPROACH
            python:
                # Get the image path from mapping without any checks
                try:
                    # Simply use the path from the mapping without checking if it exists
                    # This will let Ren'Py's image loader handle missing files
                    rizz_image_path = rizz_image_mapping.get(persistent.rizz_skill, DEFAULT_JACKORIZZ_IMAGE)
                    
                    # Force the path to be lowercase just in case
                    rizz_image_path = rizz_image_path.lower()
                    
                    # Hardcode proven working paths for certain rizz levels
                    if persistent.rizz_skill == "Rapist Rizz":
                        rizz_image_path = "mod_assets/images/inv/rizzstatus/jackorizz_rapist_rizz.png"
                    elif persistent.rizz_skill == "Unspoken Duke Dennis Rizz":
                        rizz_image_path = "mod_assets/images/inv/rizzstatus/jackorizz_unspoken_duke_dennis_rizz.png"
                    elif persistent.rizz_skill == "L Rizz":
                        rizz_image_path = "mod_assets/images/inv/rizzstatus/jackorizz_l_rizz.png"
                    
                    # Log what we're using
                    renpy.log("Using image: " + rizz_image_path)
                except:
                    # If anything fails, use L Rizz image
                    rizz_image_path = "mod_assets/images/inv/rizzstatus/jackorizz_l_rizz.png"

            add rizz_image_path:
                at (jackorizz_slide_in if not is_duke_dennis_rizz else jackorizz_golden_slide_in)

            text "Rizz Status":
                style "rizz_status_title"
                xalign rizz_title_xalign
                yalign rizz_title_yalign
                color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#FFA500")  # Orange is default
                at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
            
            # Random quote at bottom left - custom version for each rizz level
            $ random_quote = renpy.random.choice(rizz_quotes)
            if is_rapist_rizz:
                $ random_quote = "You're a monster. Look at what you've become."
            elif is_duke_dennis_rizz:
                $ random_quote = "The King of Rizz has arrived. RIZZ CHIGGAS ALL AROUND."
            
            text random_quote:
                style "rizz_quote_text"
                xpos rizz_quote_xpos
                ypos rizz_quote_ypos
                color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#ffffff")
                at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
            
            # Down arrow for returning to inventory
            textbutton "v":
                text_size 40
                text_color "#FFFFFF"
                text_outlines [(2, "#E17AAF", 0, 0)]
                xalign rizz_arrow_xalign
                yalign rizz_arrow_yalign
                at (arrow_key_down_animation if items.down_key_pressed else None)
                action [
                    SetField(items, "showing_rizz_status", False),
                    SetField(items, "exiting_rizz_status", True),
                    Function(lambda: globals().update(static_showing=False, static_alpha=0.0, noise_showing=False, noise_alpha=0.0, gold_particles_showing=False)),  # Hide effects
                    Play("sound", "mod_assets/sfx/menu_move.ogg")
                ]

            # Main rizz status content
            vbox:
                xalign rizz_content_xalign
                yalign rizz_content_yalign
                spacing rizz_content_spacing
                
                # Current level and points
                frame:
                    background None
                    xsize rizz_stats_xsize
                    padding rizz_stats_padding
                    
                    vbox:
                        spacing rizz_stats_spacing
                        xalign rizz_stats_xalign
                        
                        text "Current Level: [persistent.rizz_skill]":
                            style "rizz_status_text"
                            color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#FFFFFF")
                            at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
                            
                        text "Points: [persistent.rizz_points]":
                            style "rizz_status_text"
                            color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#FFFFFF")
                            at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
                
                # Recent changes history
                frame:
                    background None
                    xsize rizz_stats_xsize
                    padding rizz_stats_padding
                    
                    vbox:
                        spacing rizz_history_spacing
                        
                        text "Recent Changes:":
                            style "rizz_status_text"
                            color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#FFFFFF")
                            at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
                        
                        for entry in persistent.rizz_history:
                            # For Rapist Rizz, all text is the same creepy color
                            if is_rapist_rizz:
                                $ color = RAPIST_RIZZ_TEXT_COLOR
                                $ sign = "+" if entry["points"] > 0 else ""
                                hbox:
                                    xalign rizz_history_xalign
                                    spacing 10
                                    text "{color=[color]}[sign][entry['points']] points{/color}" style "rizz_status_history" at creepy_text_flicker
                                    if entry["reason"]:
                                        text "[entry['reason']]" style "rizz_status_history" color RAPIST_RIZZ_TEXT_COLOR at creepy_text_flicker
                            # For Duke Dennis Rizz, all text is golden
                            elif is_duke_dennis_rizz:
                                $ color = DUKE_DENNIS_RIZZ_TEXT_COLOR
                                $ sign = "+" if entry["points"] > 0 else ""
                                hbox:
                                    xalign rizz_history_xalign
                                    spacing 10
                                    text "{color=[color]}[sign][entry['points']] points{/color}" style "rizz_status_history" at golden_text_glow
                                    if entry["reason"]:
                                        text "[entry['reason']]" style "rizz_status_history" color DUKE_DENNIS_RIZZ_TEXT_COLOR at golden_text_glow
                            # Normal coloring for other ranks
                            else:
                                $ color = "#00FF00" if entry["points"] > 0 else "#FF0000"
                                $ sign = "+" if entry["points"] > 0 else ""
                                hbox:
                                    xalign rizz_history_xalign
                                    spacing 10
                                    text "{color=[color]}[sign][entry['points']] points{/color}" style "rizz_status_history"
                                    if entry["reason"]:
                                        text "[entry['reason']]" style "rizz_status_history"

    # Separate copy of Rizz Status for exit animation - with same positioning variables
    if items.exiting_rizz_status:
        # Check if player has Rapist Rizz or Duke Dennis Rizz
        $ is_rapist_rizz = (persistent.rizz_skill == "Rapist Rizz")
        $ is_duke_dennis_rizz = (persistent.rizz_skill == "Unspoken Duke Dennis Rizz")
        
        # Stop the creepy music if it was playing
        if is_rapist_rizz and items.rapist_music_playing:
            $ restore_normal_music()
            $ items.rapist_music_playing = False
            
        # Stop the duke dennis music if it was playing
        if is_duke_dennis_rizz and getattr(items, "dennis_music_playing", False):
            $ restore_normal_music()
            $ items.dennis_music_playing = False
        
        # Add a dim overlay for Rapist Rizz
        if is_rapist_rizz:
            add "black" at dim_pulse(RAPIST_RIZZ_DIM_LEVEL)
            
            # Add timer to trigger static effects during exit
            timer 0.7 repeat True action If(items.exiting_rizz_status and is_rapist_rizz, Function(show_random_static))
            
            # Add timer to trigger noise effects during exit
            timer 1.2 repeat True action If(items.exiting_rizz_status and is_rapist_rizz, Function(show_random_noise))
            
        # Add golden aura for Duke Dennis Rizz during exit
        elif is_duke_dennis_rizz:
            add "black" at dim_pulse(DUKE_DENNIS_DIM_LEVEL)
            
            # Add golden border vignette effect for exit animation
            add "mod_assets/images/effect/gold_vignette.png" at golden_border_pulse
            
            # Continue gold particles during exit
            timer 1.0 repeat True action If(items.exiting_rizz_status and is_duke_dennis_rizz, Function(show_golden_particles))
        
        frame:
            xalign rizz_frame_xalign
            yalign rizz_frame_yalign
            xsize rizz_frame_xsize
            ysize rizz_frame_ysize
            background None
            at (rapist_exit_shake if is_rapist_rizz else duke_dennis_exit if is_duke_dennis_rizz else slide_up_exit)

            # Use the rizz rank for the jackorizz image - SIMPLIFIED
            python:
                # Get the image path from mapping without any checks
                try:
                    # Simply use the path from the mapping without checking if it exists
                    rizz_image_path = rizz_image_mapping.get(persistent.rizz_skill, DEFAULT_JACKORIZZ_IMAGE)
                    
                    # Force the path to be lowercase just in case
                    rizz_image_path = rizz_image_path.lower()
                    
                    # Hardcode proven working paths for certain rizz levels
                    if persistent.rizz_skill == "Rapist Rizz":
                        rizz_image_path = "mod_assets/images/inv/rizzstatus/jackorizz_rapist_rizz.png"
                    elif persistent.rizz_skill == "Unspoken Duke Dennis Rizz":
                        rizz_image_path = "mod_assets/images/inv/rizzstatus/jackorizz_unspoken_duke_dennis_rizz.png"
                    elif persistent.rizz_skill == "L Rizz":
                        rizz_image_path = "mod_assets/images/inv/rizzstatus/jackorizz_l_rizz.png"
                except:
                    # If anything fails, use L Rizz image
                    rizz_image_path = "mod_assets/images/inv/rizzstatus/jackorizz_l_rizz.png"

            add rizz_image_path:
                at (jackorizz_exit if not is_duke_dennis_rizz else jackorizz_golden_exit)

            text "Rizz Status":
                style "rizz_status_title"
                xalign rizz_title_xalign
                yalign rizz_title_yalign
                color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#FFA500")
                at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
            
            # Same random quote for consistency during transition
            if is_rapist_rizz:
                $ random_quote = "You're a monster. Look at what you've become."
            elif is_duke_dennis_rizz:
                $ random_quote = "The King of Rizz has arrived. RIZZ CHIGGAS ALL AROUND."
                
            text random_quote:
                style "rizz_quote_text"
                xpos rizz_quote_xpos
                ypos rizz_quote_ypos
                color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#ffffff")
                at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
            
            # Main rizz status content (duplicate)
            vbox:
                xalign rizz_content_xalign
                yalign rizz_content_yalign
                spacing rizz_content_spacing
                
                # Current level and points
                frame:
                    background None
                    xsize rizz_stats_xsize
                    padding rizz_stats_padding
                    
                    vbox:
                        spacing rizz_stats_spacing
                        xalign rizz_stats_xalign
                        
                        text "Current Level: [persistent.rizz_skill]":
                            style "rizz_status_text"
                            color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#FFFFFF")
                            at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
                            
                        text "Points: [persistent.rizz_points]":
                            style "rizz_status_text"
                            color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#FFFFFF")
                            at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
                
                # Recent changes history
                frame:
                    background None
                    xsize rizz_stats_xsize
                    padding rizz_stats_padding
                    
                    vbox:
                        spacing rizz_history_spacing
                        
                        text "Recent Changes:":
                            style "rizz_status_text"
                            color (RAPIST_RIZZ_TEXT_COLOR if is_rapist_rizz else DUKE_DENNIS_RIZZ_TEXT_COLOR if is_duke_dennis_rizz else "#FFFFFF")
                            at (creepy_text_flicker if is_rapist_rizz else golden_text_glow if is_duke_dennis_rizz else None)
                        
                        for entry in persistent.rizz_history:
                            # For Rapist Rizz, all text is the same creepy color
                            if is_rapist_rizz:
                                $ color = RAPIST_RIZZ_TEXT_COLOR
                                $ sign = "+" if entry["points"] > 0 else ""
                                hbox:
                                    xalign rizz_history_xalign
                                    spacing 10
                                    text "{color=[color]}[sign][entry['points']] points{/color}" style "rizz_status_history" at creepy_text_flicker
                                    if entry["reason"]:
                                        text "[entry['reason']]" style "rizz_status_history" color RAPIST_RIZZ_TEXT_COLOR at creepy_text_flicker
                            # For Duke Dennis Rizz, all text is golden
                            elif is_duke_dennis_rizz:
                                $ color = DUKE_DENNIS_RIZZ_TEXT_COLOR
                                $ sign = "+" if entry["points"] > 0 else ""
                                hbox:
                                    xalign rizz_history_xalign
                                    spacing 10
                                    text "{color=[color]}[sign][entry['points']] points{/color}" style "rizz_status_history" at golden_text_glow
                                    if entry["reason"]:
                                        text "[entry['reason']]" style "rizz_status_history" color DUKE_DENNIS_RIZZ_TEXT_COLOR at golden_text_glow
                            # Normal coloring for other ranks
                            else:
                                $ color = "#00FF00" if entry["points"] > 0 else "#FF0000"
                                $ sign = "+" if entry["points"] > 0 else ""
                                hbox:
                                    xalign rizz_history_xalign
                                    spacing 10
                                    text "{color=[color]}[sign][entry['points']] points{/color}" style "rizz_status_history"
                                    if entry["reason"]:
                                        text "[entry['reason']]" style "rizz_status_history"

            # Timer to end the exit animation
            timer 0.7 action [
                SetField(items, "exiting_rizz_status", False),
                Function(renpy.restart_interaction)
            ]

    # Key handlers
    if len(items.items) > 0:
        key "K_RIGHT" action [
            SetField(items, "previous_index", items.selected_index),
            SetField(items, "selected_index", (items.selected_index + 1) % len(items.items)),
            SetField(items, "right_key_pressed", True),
            SetField(items, "cycling_direction", "right"),
            SetField(items, "showing_previous_item", True),
            Play("sound", "mod_assets/sfx/menu_move.ogg"),
            Function(renpy.restart_interaction)
        ]
        key "K_LEFT" action [
            SetField(items, "previous_index", items.selected_index),
            SetField(items, "selected_index", (items.selected_index - 1) % len(items.items)),
            SetField(items, "left_key_pressed", True),
            SetField(items, "cycling_direction", "left"),
            SetField(items, "showing_previous_item", True),
            Play("sound", "mod_assets/sfx/menu_move.ogg"),
            Function(renpy.restart_interaction)
        ]
        key "K_RETURN" action If(not items.showing_rizz_status, [
            ToggleField(items, "close_up_view"),
            If(items.close_up_view, Play("sound", "mod_assets/sfx/zoom_in.ogg"), Play("sound", "mod_assets/sfx/zoom_out.ogg"))
        ])
    
    # Up/down arrow keys for rizz status toggle
    key "K_UP" action [
        If(not items.showing_rizz_status, [
            SetField(items, "showing_rizz_status", True),
            SetField(items, "up_key_pressed", True),
            Play("sound", "mod_assets/sfx/menu_up.ogg"),
            Function(renpy.restart_interaction)
        ])
    ]
    key "K_DOWN" action [
        If(items.showing_rizz_status, [
            SetField(items, "showing_rizz_status", False),
            SetField(items, "exiting_rizz_status", True),
            Function(lambda: globals().update(static_showing=False, static_alpha=0.0, noise_showing=False, noise_alpha=0.0, gold_particles_showing=False)),  # Hide effects
            Play("sound", "mod_assets/sfx/menu_down.ogg"),
            Function(renpy.restart_interaction)
        ])
    ]
    
    key "i" action [
        Play("sound", "mod_assets/sfx/menu_close.ogg"),
        If(hasattr(items, "rapist_music_playing") and items.rapist_music_playing, Function(restore_normal_music)),  # Reset music if needed
        If(hasattr(items, "dennis_music_playing") and items.dennis_music_playing, Function(restore_normal_music)),  # Reset duke dennis music
        SetField(items, "rapist_music_playing", False),  # Reset music flag
        SetField(items, "dennis_music_playing", False),  # Reset dennis music flag
        Function(lambda: globals().update(static_showing=False, static_alpha=0.0, noise_showing=False, noise_alpha=0.0, gold_particles_showing=False)),  # Hide effects
        Hide("item_inspection_screen", transition=dissolve),
        Hide("static_effect"),  # Hide the static effect screen
        Hide("noise_effect"),  # Hide the noise effect screen
        Hide("gold_particle_effect") if renpy.has_screen("gold_particle_effect") else NullAction(),  # Hide the gold particles screen
        Function(restore_music),  # Restore previous music
        If(items.waiting_for_inventory, SetField(items, "waiting_for_inventory", False))
    ]

# Item notification screen
screen item_notification():
    zorder 100
    if show_item_notification:
        frame:
            at notify_appear
            xalign 1.5
            yalign 0.0
            xoffset -20
            yoffset 20
            background None
            
            add "mod_assets/images/inv/nbar.png":
                xalign 1.0
                yalign 0.0
                xoffset -20
                yoffset 20
                
            hbox:
                xalign 0.84
                yalign 0.1
                spacing 15
                
                vbox:
                    spacing 5
                    text "You found an item!":
                        size 22
                        color "#FFFFFF"
                        xalign 0.0
                        yalign 0.0
                    text notification_item:
                        size 20
                        color "#f7d053"
                        xalign 0.0
                        yalign 0.0
        
        timer 3.5 action Hide("item_notification")

# Labels for item management
label collect_item(*args):
    if len(args) == 1:
        # New format: single item_id parameter
        $ item_id = args[0]
    else:
        # Old format: name, image_path, description
        $ item_id = "custom_" + str(len(items.items))
        $ available_items[item_id] = {
            "name": args[0] if len(args) > 0 else PLACEHOLDER_NAME,
            "image": args[1] if len(args) > 1 else PLACEHOLDER_IMAGE,
            "description": args[2] if len(args) > 2 else PLACEHOLDER_DESC
        }
    
    if items.add_item(item_id):
        $ current_item = available_items.get(item_id, {
            "name": PLACEHOLDER_NAME,
            "image": PLACEHOLDER_IMAGE,
            "description": PLACEHOLDER_DESC
        })
        $ notification_item = current_item["name"]
        $ show_item_notification = True
        show screen item_notification
        play sound "mod_assets/sfx/item_collect.ogg"

        if not items.tutorial_shown and len(items.items) == 1:
            $ items.tutorial_shown = True
            call item_tutorial from _call_item_tutorial

    return

# Tutorial label
label item_tutorial:
    window hide(None)
    window auto
    hide monika
    show smartsuki at character_normal
    stop music fadeout 4.0
    play music bloopin fadein 4.5
    
    show screen tutorial_elements
    
    show screen tutorial_text("Smartsuki", "You found an item! It has been added to your collection.", 0.7, 0.3, 42, "#ffffff")
    $ renpy.pause()
    hide screen tutorial_text
    
    show screen tutorial_text("Smartsuki", "Press {i}'i'{/i} to view your items.", 0.7, 0.4, 42, "#ffffff")
    $ renpy.pause()
    hide screen tutorial_text
    
    show screen tutorial_text("Smartsuki", "Use Left & Right Arrow Keys to navigate between items.", 0.7, 0.5, 42, "#ffffff")
    $ renpy.pause()
    hide screen tutorial_text
    
    show screen tutorial_text("Smartsuki", "Press Enter to zoom in and get a closer look at an item.", 0.7, 0.6, 42, "#ffffff")
    $ renpy.pause()
    hide screen tutorial_text
    
    show screen tutorial_text("Smartsuki", "Press {i}'i'{/i} again to close the item viewer.", 0.7, 0.7, 42, "#ffffff")
    $ renpy.pause()
    hide screen tutorial_text
    
    show screen tutorial_text("Smartsuki", "Try it now! Press {i}'i'{/i}", 0.7, 0.8, 48, "#a6e3ff")
    $ items.waiting_for_inventory = True
    while items.waiting_for_inventory:
        $ renpy.pause()
    hide screen tutorial_text
    
    show screen tutorial_text("Smartsuki", "Great! Now you can view your items anytime!", 0.7, 0.5, 48, "#a6ffb8")
    $ renpy.pause()
    hide screen tutorial_text
    
    stop music fadeout 4.0
    play music t3 fadein 4.5
    hide screen tutorial_elements
    hide smartsuki
    return

# Label to remove all items
label remove_all_items:
    $ items.items = []
    $ items.selected_index = 0
    $ items.close_up_view = False
    return

# Label to add all available items
label add_all_items:
    python:
        items_added = 0
        for item_id in available_items:
            if item_id not in items.items:
                items.add_item(item_id)
                items_added += 1
    if items_added > 0:
        $ notification_item = "Added " + str(items_added) + " items to your inventory."
        $ show_item_notification = True
        show screen item_notification
        play sound "mod_assets/sfx/item_collect.ogg"
    return

# Initialize the inventory toggle screen
init python:
    config.underlay.append(renpy.Keymap(
        i=lambda: renpy.run(Show("toggle_inventory"))
    ))
# Arrow key animations
transform arrow_key_press_right:
    on show:
        xoffset 0
        easeout 0.1 xoffset 20
        easein 0.1 xoffset 0

transform arrow_key_press_left:
    on show:
        xoffset 0
        easeout 0.1 xoffset -20
        easein 0.1 xoffset 0

# Add these new transforms for item cycling
transform item_slide_in_right:
    zoom 1.0
    xoffset 300
    alpha 0.0
    linear 0.3 xoffset 0 alpha 1.0

transform item_slide_in_left:
    zoom 1.0
    xoffset -300
    alpha 0.0
    linear 0.3 xoffset 0 alpha 1.0

transform item_slide_out_right:
    zoom 1.0
    xoffset 0
    alpha 1.0
    linear 0.3 xoffset 300 alpha 0.0

transform item_slide_out_left:
    zoom 1.0
    xoffset 0
    alpha 1.0
    linear 0.3 xoffset -300 alpha 0.0

transform item_name_glow:
    on show:
        alpha 0.0
        linear 0.3 alpha 1.0
    on replace:
        alpha 0.0
        linear 0.3 alpha 1.0

# Add a new transform for the pointing image
transform pointing_fade:
    alpha 1.0
    linear 0.3 alpha 0.0

# Remove the additional item slide in/out animations during cycling
# and simplify to a basic fade
transform item_transition:
    alpha 0.0
    linear 0.2 alpha 1.0

# Updated transforms with consistent zoom levels
transform inspection_zoom_in:
    zoom 1.0
    linear 0.3 zoom 1.5

transform inspection_zoom_out:
    zoom 1.5
    linear 0.3 zoom 1.0

transform inspection_slide_in_right:
    zoom 1.5  # Set consistent zoom level
    xoffset 500
    linear 0.3 xoffset 0
    
transform inspection_slide_in_left:
    zoom 1.5  # Set consistent zoom level
    xoffset -500
    linear 0.3 xoffset 0

# Add transforms for showing previous item in inspection mode
transform inspection_slide_out_right:
    zoom 1.5  # Set consistent zoom level
    xoffset 0
    linear 0.3 xoffset 500 alpha 0.0
    
transform inspection_slide_out_left:
    zoom 1.5  # Set consistent zoom level
    xoffset 0
    linear 0.3 xoffset -500 alpha 0.0

# Add custom styles for rizz status text
style rizz_status_title:
    font "mod_assets/fonts/p5.ttf"
    size 50
    color "#FFA500"
    outlines [(3, "#000000", 0, 0)]
    xalign 0.0
    yalign 0.07

style rizz_status_text:
    font "mod_assets/fonts/p5.ttf"
    size 36
    color "#FFFFFF"
    outlines [(2, "#000000", 0, 0)]
    xalign 0.0

style rizz_status_value:
    font "mod_assets/fonts/p5.ttf"
    size 36
    color "#FFA500"
    outlines [(2, "#000000", 0, 0)]

style rizz_status_history:
    font "mod_assets/fonts/p5.ttf"
    size 24
    color "#FFFFFF"
    outlines [(1, "#000000", 0, 0)]
    xalign 0.0

# Add a style for rizz quotes
style rizz_quote_text:
    font "mod_assets/fonts/p5.ttf"
    size 30
    color "#ffffff"
    outlines [(1, "#e17aaf", 0, 0)]
    xalign 0.0
    text_align 0.5

# Rizz status positioning variables
init python:
    # Rizz quotes list
    rizz_quotes = [
        "A lion molests everything that moves",
        "The rizzler never sleeps",
        "You reep what you sow",
        "Rizz is a mindset, not a skill",
        "Confidence is temporary, rizz is forever",
        "The secret to rizz is to not care",
        "Rizz or die trying",
        "Sigma grindset: acquire rizz",
        "They don't know about my rizz levels"
    ]
    
    # Main frame position
    rizz_frame_xalign = 0.1
    rizz_frame_yalign = 0.4
    rizz_frame_xsize = 800
    rizz_frame_ysize = 600
    
    # Quote position
    rizz_quote_xpos = 10
    rizz_quote_ypos = 550
    
    # Title position
    rizz_title_xalign = 0.0
    rizz_title_yalign = 0.07
    
    # Down arrow position
    rizz_arrow_xalign = 0.75
    rizz_arrow_yalign = 1.1
    
    # Main content position
    rizz_content_xalign = 0.0
    rizz_content_yalign = 0.4
    rizz_content_spacing = 20
    
    # Stats frame size
    rizz_stats_xsize = 600
    rizz_stats_padding = (10, 10)
    
    # Stats content position
    rizz_stats_xalign = 0.0
    rizz_stats_spacing = 10
    
    # History entries position
    rizz_history_xalign = 0.0
    rizz_history_spacing = 10

# Add transforms for the vertical line animations
transform vertical_lines_up:
    alpha 0
    linear 0.05 alpha 1.0
    linear 0.5 yoffset -720
    alpha 0

transform vertical_lines_down:
    alpha 0
    linear 0.05 alpha 1.0
    linear 0.5 yoffset 720
    alpha 0

# New transform for jackorizz slide-in animation
transform jackorizz_slide_in:
    xalign -2.0  # Start off-screen to the left
    yalign 0.4   # Keep vertical position consistent
    pause 0.6
    easein_quint 1.5 xalign 0.1  # Slide in with a slight bounce effect

# New transform for jackorizz exit animation
transform jackorizz_exit:
    xalign 0.1
    yalign 0.4
    parallel:
        easeout 0.5 yoffset -700  # Slide up like the parent frame
    parallel:
        linear 0.5 alpha 0.0      # Fade out

# Creepy transforms for Rapist Rizz
transform creepy_shake:
    # Remove xalign and yalign to preserve original positioning
    parallel:
        ease 0.05 xoffset 3
        ease 0.05 xoffset -3
        ease 0.05 xoffset 2
        ease 0.05 xoffset -2
        ease 0.05 xoffset 1
        ease 0.05 xoffset -1
        ease 0.05 xoffset 0
        repeat
    parallel:
        ease 0.1 yoffset 2
        ease 0.1 yoffset -2
        repeat

transform creepy_overlay:
    alpha 0.6
    block:
        ease 2.0 alpha 0.4
        ease 2.0 alpha 0.6
        repeat

transform creepy_text_flicker:
    alpha 1.0
    block:
        linear 0.1 alpha 0.7
        linear 0.1 alpha 1.0
        linear 0.2 alpha 1.0
        linear 0.1 alpha 0.8
        linear 0.1 alpha 1.0
        pause 2.0
        repeat

# Animation class for sequential line animation
init python:
    class LineAnimation:
        def __init__(self):
            self.showing = False
            self.direction = None  # "up" or "down"
            self.current_frame = 1
            self.total_frames = 14  # Updated to 14 frames
            self.animation_time = 0.0
            
        def start(self, direction):
            self.showing = True
            self.direction = direction
            self.current_frame = 1
            self.animation_time = 0.0
            
        def stop(self):
            self.showing = False
            
        def update(self, dt):
            if not self.showing:
                return
                
            self.animation_time += dt
            if self.animation_time >= 1:  # Change frame every 0.05 seconds
                self.current_frame += 1
                self.animation_time = 0.0
                
                if self.current_frame > self.total_frames:
                    self.current_frame = 1
                    
        def get_image(self):
            return "mod_assets/images/inv/wind{:04d}.png".format(self.current_frame)

# Default line animation instance
default line_anim = LineAnimation()

# Add a combined transform for rapist rizz entry
transform rapist_slide_shake:
    # First do the slide_up_rizz_status animation
    yoffset -700
    parallel:
        easein 0.5 yoffset 0
    parallel:
        linear 0.5
    # Then add the shaking effect
    parallel:
        pause 0.5  # Wait for slide to complete
        block:
            ease 0.05 xoffset 3
            ease 0.05 xoffset -3
            ease 0.05 xoffset 2
            ease 0.05 xoffset -2
            ease 0.05 xoffset 1
            ease 0.05 xoffset -1
            ease 0.05 xoffset 0
            repeat
    parallel:
        pause 0.5  # Wait for slide to complete
        block:
            ease 0.1 yoffset 2
            ease 0.1 yoffset -2
            repeat

# Add a combined transform for rapist rizz exit
transform rapist_exit_shake:
    parallel:
        easeout 0.5 yoffset -700
    parallel:
        linear 0.5 alpha 0.0
    # Add shaking during exit
    parallel:
        block:
            ease 0.05 xoffset 3
            ease 0.05 xoffset -3
            ease 0.05 xoffset 2
            ease 0.05 xoffset -2
            ease 0.05 xoffset 1
            ease 0.05 xoffset -1
            ease 0.05 xoffset 0
            repeat

# Add a pulsing dim overlay animation
transform dim_pulse(level=0.6):
    alpha level
    block:
        ease 3.0 alpha (level - 0.1)
        ease 3.0 alpha (level + 0.1)
        repeat

# Gold particle effect transforms
transform golden_text_glow:
    alpha 1.0
    block:
        ease 1.0 alpha 0.8
        ease 1.0 alpha 1.0
        repeat

# Gold particle animation - REMOVED (redundant)

# Duke Dennis transforms
transform duke_dennis_slide:
    # First do the slide_up_rizz_status animation
    yoffset -700
    parallel:
        easein 0.5 yoffset 0
    parallel:
        linear 0.5
    # Then add golden pulsing effect
    parallel:
        pause 0.5  # Wait for slide to complete
        block:
            ease 1.0 zoom 1.02
            ease 1.0 zoom 1.0
            repeat
            
transform duke_dennis_exit:
    parallel:
        easeout 0.5 yoffset -700
    parallel:
        linear 0.5 alpha 0.0
    # Add golden effect during exit
    parallel:
        block:
            ease 0.2 zoom 1.05
            ease 0.2 zoom 1.0
            repeat 2

transform jackorizz_golden_slide_in:
    xalign -2.0  # Start off-screen to the left
    yalign 0.4   # Keep vertical position consistent
    pause 0.6
    easein_quint 1.5 xalign 0.1  # Slide in with a slight bounce effect
    parallel:
        block:
            ease 2.0 zoom 1.05
            ease 2.0 zoom 1.0
            repeat

transform jackorizz_golden_exit:
    xalign 0.1
    yalign 0.4
    parallel:
        easeout 0.5 yoffset -700  # Slide up like the parent frame
    parallel:
        linear 0.5 alpha 0.0      # Fade out
    parallel:
        ease 0.2 zoom 1.05
        ease 0.2 zoom 1.0
        repeat 2

# Screen for gold particles effect - much simpler
screen gold_particle_effect():
    zorder 152  # Above other effects
    if gold_particles_showing:
        # Just 10 particles with different delays, speeds and sizes for a smooth effect
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=0.0, speed=35, size=0.6)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=3.5, speed=40, size=0.4)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=7.0, speed=30, size=0.7)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=10.5, speed=45, size=0.5)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=14.0, speed=38, size=0.6)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=17.5, speed=42, size=0.5)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=21.0, speed=36, size=0.7)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=24.5, speed=43, size=0.4)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=28.0, speed=39, size=0.6)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(delay=31.5, speed=37, size=0.5)

# Screen for static gold particles - REMOVED (redundant)

# Gold particle using m_cgs animation - REMOVED (redundant)
        

# Screen for gold particles with fade effect - this is the ONLY gold_particle_effect screen
screen gold_particle_effect():
    zorder 152  # Above other effects
    if gold_particles_showing:
        # Add a reasonable number of particles with varied sizes and delays
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.7, 0.0)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.6, 0.5)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.8, 1.0)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.6, 1.5)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.9, 2.0)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.5, 2.5)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.7, 3.0)
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.8, 3.5)
        # Extra large and small particles for variety
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 1.0, 0.3)  # Extra large
        add "mod_assets/images/effect/gold_particle.png" at simple_gold_particle(renpy.random.randint(100, 1820), renpy.random.randint(100, 980), 0.4, 1.7)  # Extra small

# Gold particle effect that randomly appears and fades out
transform simple_gold_particle(x_pos, y_pos, size=0.7, delay=0):
    # Position randomly on screen
    xpos x_pos
    ypos y_pos
    # Size
    zoom size
    # Initial state - invisible
    alpha 0
    # Wait random delay before appearing for staggered effect
    pause delay
    # Simple fade in
    linear 0.5 alpha 1.0
    # Gentle rotation while visible
    parallel:
        rotate 0
        linear 7.0 rotate 360
    # Stay visible for slightly shorter time (2.5 seconds instead of 3.0)
    pause 2.5
    # Fade out more quickly
    linear 0.7 alpha 0
    # Wait shorter time before reappearing for more particles on screen
    pause 0.5
    repeat

# Screen for gold particles that appear and fade - REMOVED (redundant)

# Add gold border vignette transform after other transforms
transform golden_border_pulse:
    alpha 0.0
    ease 1.5 alpha 0.7
    ease 2.5 alpha 0.3
    ease 1.0 alpha 0.1
    ease 1.5 alpha 0.0
    repeat


