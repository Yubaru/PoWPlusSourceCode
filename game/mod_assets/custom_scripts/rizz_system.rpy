# Rizz System - Improved and Sanitized Version
# Original code contained harmful and offensive content which has been removed.
# v2 - Corrected syntax errors reported by Ren'Py.

# --- Persistent Variables ---
# Use 'default' for save compatibility. Initialize before other init blocks.
# These lines MUST be outside any 'init python' block.
default persistent.rizz_points = 0
default persistent.rizz_skill = "L Rizz" # Initial skill level (will be updated by init 0)
default persistent.rizz_history = []  # New: Store recent rizz changes
default persistent.max_history_entries = 5  # New: Limit history entries


init -1 python:
    # --- Configuration ---

    # Define skill levels and their minimum point thresholds.
    # Format: (minimum_points, skill_name)
    # This list is used by the update function.
    skill_thresholds = [
        (20, "Unspoken Duke Dennis Rizz"),
        (15, "Rizz God"),
        (10, "Rizzilisious"),
        (7, "Rizzler"),
        (5, "Rizzin' Up"),
        (3, "Rizz Apprentice"),
        (0, "L Rizz"), # Skill at 0 points
        (-3, "Incel Rizz"),
        (-5, "Yazz Rizz"),
        (-8, "It's All Coming Down Rizz"),
        (-12, "Green Aura With Flies Rizz"),
        (-15, "Rapist Rizz"),
        # Add a catch-all for very low scores if needed, e.g.:
        # (-9999, "Utterly Inept")
    ]
    # Sort thresholds descending by point value for easy lookup in the update function
    skill_thresholds.sort(key=lambda item: item[0], reverse=True)

    # Lists of messages
    encouraging_messages = [

        "Is he busy? Nah, he gettin' rizzzyyyyyyyyy!",

        "See? THAT Nigga got some Rizz.",

        "Bruhhhhh, this dude about to take my GIRL.",

        "That is just insanium in my cranium.",

        "Jordan could never.",

        "Jorge could never.",

        "Someone is fucking TONIGHT."

    ] 

    discouraging_messages = [ # Renamed from 'roasts'
        "Damn, bitches be runnin' from yo ass.",

        "I just- just get the fuck out of here.",

        "You dumbass nigger.",

        "No bitches in real life AND in DDLC.",

        "Gotta be a nigger playin' this right now.",

        "Holy fuck, close the game right fucking now." 
    ]

    # --- Constants ---
    # Define constants for easier configuration and readability
    RIZZ_TEXT_COLOR = "#FFA500" # Orange color for Rizz UI elements
    RIZZ_GOOD_SOUND = "mod_assets/sfx/rizz_good.ogg" # Placeholder path
    RIZZ_FAIL_SOUND = "mod_assets/sfx/rizz_fail.ogg" # Placeholder path
    RIZZ_LEVEL_UP_SOUND = "mod_assets/sfx/rizz_point.ogg" # Placeholder path
    RIZZ_LEVEL_DOWN_SOUND = "mod_assets/sfx/rizz_point_down.ogg" # Placeholder path
    RIZZ_MENU_OPEN = "mod_assets/sfx/rizz_status_open.ogg" # Sound for opening rizz menu
    RIZZ_MENU_CLOSE = "mod_assets/sfx/rizz_status_close.ogg" # Sound for closing rizz menu

    # --- Audio Channels ---
    # Define custom audio channels for level-up/down sounds
    renpy.music.register_channel("level_up", mixer="sfx", loop=False)
    renpy.music.register_channel("level_down", mixer="sfx", loop=False)

    # --- Helper Function ---

    # Function to update Rizz Skill based on current points
    def update_persistent_rizz_skill():
        global persistent # Ensure we are modifying the persistent object

        current_points = persistent.rizz_points

        # Iterate through sorted thresholds (highest points first)
        for threshold, name in skill_thresholds:
            if current_points >= threshold:
                persistent.rizz_skill = name
                return # Found the correct skill level

        # Fallback if points are lower than the lowest defined threshold
        # This assigns the name associated with the lowest threshold
        if skill_thresholds: # Check if list is not empty
            persistent.rizz_skill = skill_thresholds[-1][1] # Assign the last skill name (lowest threshold)
        else:
            persistent.rizz_skill = "Unknown" # Should not happen with proper config

    # New: Function to update rizz history
    def update_rizz_history(points_change, reason=""):
        global persistent
        if not hasattr(persistent, 'rizz_history'):
            persistent.rizz_history = []
        
        # Add new entry
        entry = {
            "points": points_change,
            "reason": reason,
            "time": renpy.get_game_runtime()
        }
        persistent.rizz_history.insert(0, entry)
        
        # Trim history if too long
        if len(persistent.rizz_history) > persistent.max_history_entries:
            persistent.rizz_history = persistent.rizz_history[:persistent.max_history_entries]


# --- Initial Skill Calculation ---
# Ensure the initial skill is correctly set based on the starting points
# Needs to run *after* persistent variables are available (default ran)
# and *after* the skill_thresholds list is defined (init -1 python ran).
init 0 python:
    # Call the function to set the initial skill based on default points (0)
    update_persistent_rizz_skill()

# --- Game Variables ---
# Define non-persistent variables if needed
# define smartsuki_name = "Smartsuki" # Kept from original if needed

# --- Animations ---
# Define Persona 5-style animations (kept from original)
transform persona5_text_popup:
    # Initial state
    zoom 0.5 alpha 0
    # Animation
    parallel:
        easein 0.5 zoom 1.0 alpha 1.0
    parallel:
        easein 0.3 yoffset -50
        easeout 0.2 yoffset 0

transform persona5_level_up:
    # Initial state
    zoom 0.8 alpha 0
    # Animation
    parallel:
        easein 0.5 zoom 1.0 alpha 1.0
    parallel:
        easein 0.3 yoffset -30
        easeout 0.2 yoffset 0

# --- Core Logic Label ---

# Label to handle Rizz Point updates and display feedback
label rizz_update(points_change, reason=""):
    # Store the skill level *before* the change
    $ previous_skill = persistent.rizz_skill

    # Check if already at max level
    $ max_level = skill_thresholds[0][0]  # Get the highest threshold
    if persistent.rizz_points >= max_level and points_change > 0:
        show text "{color=[RIZZ_TEXT_COLOR]}You've reached maximum Rizz!{/color}" at persona5_text_popup zorder 100
        pause 1.0
        hide text with dissolve
        return

    # Update the rizz points
    $ persistent.rizz_points += points_change

    # Update history
    $ update_rizz_history(points_change, reason)

    # Recalculate the rizz skill based on the new points
    $ update_persistent_rizz_skill()

    # --- Visual and Audio Feedback ---

    # Play sound effect based on gaining or losing points
    if points_change > 0:
        play sound RIZZ_GOOD_SOUND
        # Select a random encouraging message
        $ feedback_message = renpy.random.choice(encouraging_messages)
        $ points_display = "+{}".format(points_change) # Ensure '+' sign
    elif points_change < 0:
        play sound RIZZ_FAIL_SOUND
        # Select a random discouraging message
        $ feedback_message = renpy.random.choice(discouraging_messages)
        $ points_display = "{}".format(points_change) # Negative sign is included
    else:
        # Optional: Handle case where points_change is 0 (no points change)
        $ feedback_message = "No change in Rizz."
        $ points_display = "0"
        # Maybe skip the sound or play a neutral one

    # Display the Rizz Point gain/loss with animation (only if points changed)
    if points_change != 0:
        show text "{color=[RIZZ_TEXT_COLOR]}[points_display] Rizz Point(s){/color}" at persona5_text_popup zorder 100 # Using constant
        pause 1.0
        hide text with dissolve # Use a transition like dissolve

    # Display the feedback message (using narrator for simplicity)
    narrator "[feedback_message]"

    # --- Skill Level Change Feedback ---

    # Check if the Rizz Skill level actually changed
    if persistent.rizz_skill != previous_skill:

        # Determine if the skill increased or decreased within a python block
        python:
            # This block executes Python code within the Ren'Py label context
            _skill_increased = False # Use temporary variable name to avoid potential conflicts
            try:
                # Access the globally defined skill_thresholds list
                _skill_names = [name for _, name in skill_thresholds]
                _previous_index = _skill_names.index(previous_skill)
                _current_index = _skill_names.index(persistent.rizz_skill)

                # Lower index means higher skill because list is sorted descending by points
                if _current_index < _previous_index:
                    _skill_increased = True # Set the flag if skill improved
                    
                    # Check if we reached Duke Dennis Rizz level
                    if persistent.rizz_skill == "Unspoken Duke Dennis Rizz":
                        ach_unlock('max_rizz')

            except ValueError:
                # Handle cases where a skill name might not be in the list
                # This might happen if skill_thresholds is modified incorrectly
                renpy.log("Error finding skill index for '{}' or '{}'".format(previous_skill, persistent.rizz_skill))
                # Keep _skill_increased as False or handle as appropriate

            # Assign the result to a Ren'Py variable accessible outside the python block
            skill_increased_flag = _skill_increased

        # Now use the calculated skill_increased_flag variable in Ren'Py script
        if skill_increased_flag:
            # Play the level-up sound effect on the dedicated channel
            play level_up RIZZ_LEVEL_UP_SOUND

            # Show the Rizz Skill level-up animation
            show text "{color=[RIZZ_TEXT_COLOR]}Rizz Skill Increased!{/color}" at persona5_level_up zorder 100
            pause 1.0
            hide text with dissolve

            # Display the new Rizz Skill
            show text "Your Rizz Skill is now {color=[RIZZ_TEXT_COLOR]}[persistent.rizz_skill]{/color}!" at persona5_level_up zorder 100
            pause 1.5
            hide text with dissolve

        else: # Skill decreased (or error occurred in python block)
            # Play the level-down sound effect on the dedicated channel
            play level_down RIZZ_LEVEL_DOWN_SOUND

            # Show the Rizz Skill level-down animation
            show text "{color=[RIZZ_TEXT_COLOR]}Rizz Skill Decreased...{/color}" at persona5_level_up zorder 100
            pause 1.0
            hide text with dissolve

            # Display the new Rizz Skill
            show text "Your Rizz Skill is now {color=[RIZZ_TEXT_COLOR]}[persistent.rizz_skill]{/color}..." at persona5_level_up zorder 100          
            pause 1.5
            hide text with dissolve

    # End of the update process
    return

# --- Example Usage ---

# New: Label to reset rizz points and skill
label reset_rizz():
    $ persistent.rizz_points = 0
    $ persistent.rizz_skill = "L Rizz"
    $ persistent.rizz_history = []
    return

# New: Label to manually set rizz skill level
label set_rizz_skill(skill_name=""):
    python:
        # If no skill name is provided, show a selection menu
        if not skill_name:
            # Extract all skill names from skill_thresholds
            available_skills = [name for _, name in skill_thresholds]
            # Split the skills into two pages
            skill_count = len(available_skills)
            page1_skills = available_skills[:skill_count//2]  # First half
            page2_skills = available_skills[skill_count//2:]  # Second half
            
            # Start with page 1
            current_page = 1
            menu_choice = None
            
            while menu_choice != "Return":
                # Create menu options based on current page
                menu_options = []
                
                if current_page == 1:
                    # Add page 1 skills
                    for skill in page1_skills:
                        menu_options.append((skill, skill))
                    # Add navigation options
                    menu_options.append(("Next Page >>", "next_page"))
                    menu_options.append(("Return", "Return"))
                else:  # Page 2
                    # Add page 2 skills
                    for skill in page2_skills:
                        menu_options.append((skill, skill))
                    # Add navigation options
                    menu_options.append(("<< Previous Page", "prev_page"))
                    menu_options.append(("Return", "Return"))
                
                # Display the menu without restart loops
                try:
                    menu_choice = renpy.display_menu(menu_options)
                except Exception as e:
                    renpy.log("Menu error: " + str(e))
                    menu_choice = "Return"  # Default to return if error
                
                # Handle navigation choices
                if menu_choice == "next_page":
                    current_page = 2
                    continue
                elif menu_choice == "prev_page":
                    current_page = 1
                    continue
                elif menu_choice == "Return":
                    skill_name = ""  # Set empty to skip skill setting
                    break
                else:
                    # A skill was selected
                    skill_name = menu_choice
                    break
        
        # Find the skill in the thresholds
        skill_found = False
        if skill_name:  # Only proceed if a skill was actually selected
            for threshold, name in skill_thresholds:
                if name == skill_name:
                    # Set the skill level
                    persistent.rizz_skill = skill_name
                    # Set points to the minimum threshold for this skill
                    persistent.rizz_points = threshold
                    # Add to history
                    update_rizz_history(0, "Manually set to " + skill_name)
                    skill_found = True
                    break
            
            if not skill_found:
                renpy.notify("Skill '" + skill_name + "' not found!")

    # Display confirmation if skill was found
    if skill_found:
        show text "{color=[RIZZ_TEXT_COLOR]}Rizz Skill set to [persistent.rizz_skill]!{/color}" at persona5_level_up zorder 100
        pause 1.5
        hide text with dissolve
    
    return

# Initialize the rizz status toggle
# init python:
#     config.underlay.append(renpy.Keymap(
#         r=lambda: renpy.run([Play("sound", RIZZ_MENU_OPEN), Show("rizz_status")])
#     ))

