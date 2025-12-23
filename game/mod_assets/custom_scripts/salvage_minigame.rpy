# Salvage Minigame
# A survival horror-style minigame where you must complete a checklist while avoiding the animatronic

# Python initialization for animatronic system
init python:
    class Animatronic:
        """Represents an animatronic with its threat levels and jumpscare frames"""
        def __init__(self, name):
            self.name = name
            self.threat_images = {
                1: "mod_assets/images/bg/salvage_minigame/{}/{}_threat_1.png".format(name, name),
                2: "mod_assets/images/bg/salvage_minigame/{}/{}_threat_2.png".format(name, name),
                3: "mod_assets/images/bg/salvage_minigame/{}/{}_threat_3.png".format(name, name),
                4: "mod_assets/images/bg/salvage_minigame/{}/{}_threat_4.png".format(name, name)
            }
            # Handle special naming case for glurbox jumpscare frames
            jumpscare_prefix = "glurbux" if name == "glurbox" else name
            self.jumpscare_frames = [
                "mod_assets/images/bg/salvage_minigame/{}/{}_jumpscare_01.png".format(name, jumpscare_prefix),
                "mod_assets/images/bg/salvage_minigame/{}/{}_jumpscare_02.png".format(name, jumpscare_prefix),
                "mod_assets/images/bg/salvage_minigame/{}/{}_jumpscare_03.png".format(name, jumpscare_prefix),
                "mod_assets/images/bg/salvage_minigame/{}/{}_jumpscare_04.png".format(name, jumpscare_prefix),
                "mod_assets/images/bg/salvage_minigame/{}/{}_jumpscare_05.png".format(name, jumpscare_prefix),
                "mod_assets/images/bg/salvage_minigame/{}/{}_jumpscare_06.png".format(name, jumpscare_prefix)
            ]

        def get_threat_image(self, level):
            """Get the image path for a threat level"""
            return self.threat_images.get(level, self.threat_images[1])

        def get_jumpscare_frame(self, frame):
            """Get a jumpscare frame (1-6)"""
            if 1 <= frame <= 6:
                return self.jumpscare_frames[frame - 1]
            return self.jumpscare_frames[0]
    
    # Register all animatronics
    # To add a new animatronic:
    # 1. Create a folder: mod_assets/images/bg/salvage_minigame/[animatronic_name]/
    # 2. Add 4 threat level images: [animatronic_name]_threat_1.png through _threat_4.png
    # 3. Add 6 jumpscare frames: [animatronic_name]_jumpscare_01.png through _jumpscare_06.png
    # 4. Add it to this dictionary: "[animatronic_name]": Animatronic("[animatronic_name]")
    ANIMATRONICS = {
        "el_nig": Animatronic("el_nig"),
        "jax_kob": Animatronic("jax_kob"),
        "glurbox": Animatronic("glurbox"),
        "a1ds": Animatronic("a1ds")
        # Add more animatronics here as needed:
        # "animatronic_4": Animatronic("animatronic_4"),
    }
    
    def get_current_animatronic():
        """Get the current animatronic being used"""
        current = getattr(store, 'current_animatronic_name', 'el_nig')
        return ANIMATRONICS.get(current, ANIMATRONICS['el_nig'])

# Define images for el_nig animatronic (default)
image el_nig_threat_1 = "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_threat_1.png"
image el_nig_threat_2 = "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_threat_2.png"
image el_nig_threat_3 = "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_threat_3.png"
image el_nig_threat_4 = "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_threat_4.png"

# Define images for glurbox animatronic
image glurbox_threat_1 = "mod_assets/images/bg/salvage_minigame/glurbox/glurbox_threat_1.png"
image glurbox_threat_2 = "mod_assets/images/bg/salvage_minigame/glurbox/glurbox_threat_2.png"
image glurbox_threat_3 = "mod_assets/images/bg/salvage_minigame/glurbox/glurbox_threat_3.png"
image glurbox_threat_4 = "mod_assets/images/bg/salvage_minigame/glurbox/glurbox_threat_4.png"

# Define images for a1ds animatronic
image a1ds_threat_1 = "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_threat_1.png"
image a1ds_threat_2 = "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_threat_2.png"
image a1ds_threat_3 = "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_threat_3.png"
image a1ds_threat_4 = "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_threat_4.png"

# Jumpscare animation - frames 1-5 shake, frame 6 is static
image el_nig_jumpscare_shake_part:
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_01.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_02.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_03.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_04.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_05.png"
    0.03

# Last frame of jumpscare (static, no shake)
image el_nig_jumpscare_final = "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_06.png"

# Full jumpscare for backwards compatibility (all 6 frames)
image el_nig_jumpscare:
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_01.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_02.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_03.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_04.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_05.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/el_nig/el_nig_jumpscare_06.png"
    0.03

# Jumpscare animation for glurbox animatronic - frames 1-5 shake, frame 6 is static
image glurbox_jumpscare_shake_part:
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_01.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_02.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_03.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_04.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_05.png"
    0.03

# Last frame of glurbox jumpscare (static, no shake)
image glurbox_jumpscare_final = "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_06.png"

# Full glurbox jumpscare for backwards compatibility (all 6 frames)
image glurbox_jumpscare:
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_01.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_02.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_03.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_04.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_05.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/glurbox/glurbux_jumpscare_06.png"
    0.03

# Jumpscare animation for a1ds animatronic - frames 1-5 shake, frame 6 is static
image a1ds_jumpscare_shake_part:
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_01.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_02.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_03.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_04.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_05.png"
    0.03

# Last frame of a1ds jumpscare (static, no shake)
image a1ds_jumpscare_final = "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_06.png"

# Full a1ds jumpscare for backwards compatibility (all 6 frames)
image a1ds_jumpscare:
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_01.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_02.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_03.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_04.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_05.png"
    0.03
    "mod_assets/images/bg/salvage_minigame/a1ds/a1ds_jumpscare_06.png"
    0.03

# Define checklist images
image checklist_base = "mod_assets/images/bg/salvage_minigame/checklist_base.png"
image checklist_words = "mod_assets/images/bg/salvage_minigame/checklist_words.png"
image checklist_box = "mod_assets/images/bg/salvage_minigame/checklist_box.png"
image checklist_box_checked = "mod_assets/images/bg/salvage_minigame/checklist_box_checked.png"
image checklist_button = "mod_assets/images/bg/salvage_minigame/checklist_button.png"

# Transform for screen shake during jumpscare
transform salvage_jumpscare_shake:
    xoffset 0
    yoffset 0
    parallel:
        ease 0.03 xoffset 15
        ease 0.03 xoffset -15
        ease 0.03 xoffset 10
        ease 0.03 xoffset -10
        ease 0.03 xoffset 5
        ease 0.03 xoffset -5
        repeat
    parallel:
        ease 0.04 yoffset 10
        ease 0.04 yoffset -10
        ease 0.04 yoffset 5
        ease 0.04 yoffset -5
        repeat

# Transform for death screen fade (red overlay and jumpscare fade to black)
transform salvage_death_fade:
    alpha 1.0
    linear 2.0 alpha 0.0

# Transform for taser flash effect
transform taser_flash:
    alpha 0.0
    linear 0.05 alpha 1.0
    linear 0.05 alpha 0.0
    linear 0.05 alpha 0.8
    linear 0.05 alpha 0.0
    linear 0.05 alpha 0.6
    linear 0.1 alpha 0.0

# Transform for checklist slide up animation (from bottom)
transform checklist_slide_up:
    yoffset 800
    ease 0.3 yoffset 0

# Transform for checklist slide down animation (to bottom)
transform checklist_slide_down:
    yoffset 0
    ease 0.3 yoffset 800

# Python initialization for minigame variables
init python:
    import random
    
    # Minigame state class
    class SalvageMinigame:
        def __init__(self):
            self.reset()

        def reset(self):
            # Aggression starts randomly at 0 or 100
            self.aggression_meter = renpy.random.choice([0, 100])
            self.audio_prompts_completed = 0  # Number of full cycles completed (audio prompts)
            self.audio_prompts_played = 0  # Number of audio prompts played
            self.total_prompts = 5
            self.taser_uses = 0  # Track total taser uses (4 use limit)
            self.checklist_open = False
            self.checklist_open_time = 0.0
            self.last_page_view_time = 0.0  # Track when page was last viewed
            self.page_view_duration = 0.0  # How long page has been viewed continuously
            self.game_over = False
            self.game_won = False
            self.audio_playing = False
            self.audio_listened = False  # Whether current audio has been listened to
            # Audio prompt durations in seconds (1-indexed in comments for clarity)
            # Prompt 1: 8s, Prompt 2: 10s, Prompt 3: 17s, Prompt 4: 15s, Prompt 5: 16s
            self.audio_durations = [8.0, 10.0, 17.0, 15.0, 16.0]
            self.audio_start_time = 0.0  # When current audio prompt started
            self.fourth_prompt_started = False  # Track if 4th prompt special condition triggered
        
        def can_open_checklist(self):
            """Check if player can open checklist (must have listened to audio first)"""
            return self.audio_listened
        
        def can_play_audio(self):
            """Check if player can play audio - must have viewed page in last 10 seconds"""
            if self.audio_prompts_completed == 0:  # First prompt always available
                return True
            time_since_page_view = renpy.time.time() - self.last_page_view_time
            return time_since_page_view <= 10.0
        
        def get_visual_stage(self):
            """Get current visual stage based on aggression (1-4), increasing by 1 at each threshold"""
            if self.aggression_meter >= 1000:
                return 4
            elif self.aggression_meter >= 750:
                return 3
            elif self.aggression_meter >= 300:
                return 2
            else:
                return 1

        def increase_aggression(self, amount):
            """Increase aggression by specified amount"""
            self.aggression_meter += amount

        def reset_aggression_with_taser(self):
            """Reset aggression to random hundred from 0-300 (0, 100, 200, or 300)"""
            self.aggression_meter = renpy.random.choice([0, 100, 200, 300])

        def update_page_view_time(self):
            """Update the last time the page was viewed"""
            self.last_page_view_time = renpy.time.time()

        def should_move_animatronic(self):
            """Check if animatronic should move (page viewed for at least 0.5s)"""
            return self.page_view_duration >= 0.5
        
        def use_taser(self):
            """Returns tuple: (success, message, aggression_change)"""
            self.taser_uses += 1

            if self.taser_uses <= 4:
                # First 4 uses always work
                old_aggression = self.aggression_meter
                self.reset_aggression_with_taser()
                aggression_change = self.aggression_meter - old_aggression
                return (True, "Taser deployed! Animatronic reset to neutral state!", aggression_change)
            else:
                # After 4 uses, complex failure system
                rand = random.random()
                if rand < 0.80:
                    # 80% chance of not working
                    return (False, "Taser failed! No effect!", 0)
                elif rand < 0.90:
                    # 10% chance of not working and increasing aggression by 300
                    self.increase_aggression(300)
                    return (False, "Taser malfunction! The animatronic got much angrier!", 300)
                else:
                    # 10% chance of working
                    old_aggression = self.aggression_meter
                    self.reset_aggression_with_taser()
                    aggression_change = self.aggression_meter - old_aggression
                    return (True, "Lucky! The taser still worked!", aggression_change)
        
        def check_jumpscare(self):
            """Check if jumpscare should occur"""
            # Jumpscare at 1200 aggression
            return self.aggression_meter >= 1200

        def check_page_close_jumpscare(self):
            """Check if closing page should trigger jumpscare (at 1000+ aggression)"""
            return self.aggression_meter >= 1000

        def update_aggression_during_audio(self):
            """Update aggression during audio playback (called every 10 seconds)"""
            # 50% chance to increase by 150 every 10 seconds during tape playback
            if random.random() < 0.50:
                self.increase_aggression(150)

        def update_aggression_during_page_view(self, delta_time):
            """Update aggression while viewing page (+100 per second)"""
            self.increase_aggression(100 * delta_time)

        def handle_fourth_prompt_start(self):
            """Handle special case when starting 4th prompt"""
            if not self.fourth_prompt_started and self.audio_prompts_played == 3:  # 0-indexed, so 3 is 4th prompt
                self.fourth_prompt_started = True
                if random.random() < 0.50:
                    # 50% chance to bring aggression to 750 (but won't decrease if already above)
                    self.aggression_meter = max(self.aggression_meter, 750)

# Create global instance
default salvage_game = SalvageMinigame()
default persistent.salvage_seen_intro = False
default persistent.animatronics_completed = 0  # Track how many animatronics have been completed (max 5)
default current_animatronic_name = "el_nig"  # Current animatronic being used

# Checklist box positions (set these before calling the minigame or in the screen)
# These are not defaults - set them as needed

# Main minigame label
label salvage_minigame:
    stop music
    # Initialize the game
    $ salvage_game.reset()
    $ quick_menu = False
    $ _dismiss_pause = False
    
    # Hide any existing UI
    window hide
    
    # Set up the scene
    scene black
    with dissolve
    pause 2.0
    play music "mod_assets/sfx/salvage_minigame/ambience.ogg" loop fadein 3.0
    
    # Get current animatronic
    $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
    $ threat_1_path = animatronic.get_threat_image(1)
    
    # Check if intro has been seen before
    if persistent.salvage_seen_intro:
        # Play shorter intro
        play sound "mod_assets/sfx/salvage_minigame/cassette_basic_intro.ogg"
        pause 2
        scene expression threat_1_path
        with dissolve_scene_full
        pause 14.5
    else:
        # Play full intro for first time
        play sound "mod_assets/sfx/salvage_minigame/cassette_first_time.ogg"
        pause 4
        scene expression threat_1_path
        with dissolve_scene_full
        pause 84
        # Mark intro as seen
        $ persistent.salvage_seen_intro = True
    
    
    # Introduction dialogue with sound effect

    menu:
        "Yes, start the inspection":
            play sound "mod_assets/sfx/salvage_minigame/cassette_yes.ogg"
            pause 12
            jump .start_game
        "No, I'll pass":
            play sound "mod_assets/sfx/salvage_minigame/cassette_no.ogg"
            pause 2
            stop music fadeout 1.0
            play sound "mod_assets/sfx/salvage_minigame/game_end.ogg"
            scene black
            with dissolve_scene_full
            pause 1.0
            $ quick_menu = True
            play music festivalmusic
            return
    
    label .start_game:
    # Start the game loop - must listen to all 5 audio prompts AND complete all 5 checklists
    $ salvage_game.audio_prompts_completed = 0
    $ salvage_game.audio_prompts_played = 0
    $ salvage_game.audio_listened = False
    $ displayed_threat = 1  # Track what threat level is currently displayed
    $ show_controls = True  # Flag to show controls on first screen call
    
    # Get current animatronic and show initial visual stage
    $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
    $ initial_stage = salvage_game.get_visual_stage()
    $ initial_stage_path = animatronic.get_threat_image(initial_stage)
    scene expression initial_stage_path
    with dissolve_scene_full
    
    # Start ambient sound (loops throughout the minigame)
    play music "mod_assets/sfx/salvage_minigame/ambience.ogg" loop fadein 1.0
    
    label .game_loop:
        # Check if won - must have completed all 5 audio + checklist cycles
        if salvage_game.audio_prompts_completed >= salvage_game.total_prompts:
            jump .win_game
        
        # Show the main game screen
        call screen salvage_main_screen
        
        # Handle the return value
        $ action = _return
        
        # Debug: Instant win/lose
        if action == "instant_win":
            jump .win_game
        elif action == "instant_lose":
            jump .jumpscare

        # Jumpscare from timer (1200 aggression) or other sources
        elif action == "jumpscare":
            jump .jumpscare

        # Update background scene
        elif action == "update_background":
            $ current_stage = salvage_game.get_visual_stage()
            $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
            $ stage_image_path = animatronic.get_threat_image(current_stage)
            scene expression stage_image_path

        # Random jumpscare at threat level 3 (5%) or 4 (10%)
        elif action == "random_jumpscare":
            jump .jumpscare
        
        elif action == "page_closed":
            # Page was viewed and closed - can now progress to next audio prompt
            $ salvage_game.audio_prompts_completed += 1
            $ salvage_game.audio_listened = False  # Reset - must listen to next audio

            # Check for jumpscare when closing page at high aggression
            if salvage_game.check_page_close_jumpscare():
                jump .jumpscare

            # Update visual stage based on current aggression level
            $ current_stage = salvage_game.get_visual_stage()
            $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
            $ stage_image_path = animatronic.get_threat_image(current_stage)
            scene expression stage_image_path
            
        elif action == "taser":
            # Use taser
            $ taser_result = salvage_game.use_taser()
            $ success, message, aggression_change = taser_result

            # Show taser effect (visual only, no text)
            if success:
                play sound ("mod_assets/sfx/salvage_minigame/shock.ogg")
                show expression Solid("#00FFFF") as flash at taser_flash
                pause 0.4
                hide flash

                # Screen goes black after taser
                scene black
                pause 0.5

                # Slowly fade back to the current visual stage background
                $ current_stage = salvage_game.get_visual_stage()
                $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
                $ stage_image_path = animatronic.get_threat_image(current_stage)
                scene expression stage_image_path
                with Dissolve(1.5)
            else:
                play sound "mod_assets/sfx/salvage_minigame/shock_fail.ogg"
                                # Screen goes black after taser
                scene black
                pause 0.5

                # Slowly fade back to the current visual stage background
                $ current_stage = salvage_game.get_visual_stage()
                $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
                $ stage_image_path = animatronic.get_threat_image(current_stage)
                scene expression stage_image_path
                with Dissolve(1.5)

            # Check for jumpscare after taser use
            if salvage_game.check_jumpscare():
                jump .jumpscare
        
        elif action == "wait":
            # Check if we can play audio (page viewed in last 10 seconds for prompts after first)
            if not salvage_game.can_play_audio():
                jump .game_loop

            # Handle fourth prompt special case
            $ salvage_game.handle_fourth_prompt_start()

            # Wait and listen to audio from cassette
            $ salvage_game.audio_playing = True
            $ salvage_game.audio_start_time = renpy.time.time()

            # Play cassette intro sound before audio prompt
            play sound "mod_assets/sfx/salvage_minigame/cassette_audio_prompt_intro.ogg"
            pause 5  # Wait for intro sound to finish

            # Get current prompt number (0-indexed) and play the corresponding audio
            $ current_prompt = salvage_game.audio_prompts_played
            $ audio_file = "mod_assets/sfx/salvage_minigame/audio_prompt_" + str(current_prompt + 1) + ".ogg"
            $ audio_duration = salvage_game.audio_durations[current_prompt]

            # Play the actual audio prompt
            play sound audio_file

            # During audio playback, check for aggression increases every 10 seconds
            $ elapsed_time = 0.0
            while elapsed_time < audio_duration:
                pause 10.0  # Wait 10 seconds
                $ elapsed_time += 10.0
                $ salvage_game.update_aggression_during_audio()

            # Wait remaining time if audio duration wasn't multiple of 10
            $ remaining_time = audio_duration - elapsed_time
            if remaining_time > 0:
                pause remaining_time

            # Wait half a second after audio prompt finishes
            pause 0.5

            # Play cassette results sound
            play sound "mod_assets/sfx/salvage_minigame/cassette_results.ogg"
            pause 0.5  # Wait for results sound to finish

            $ salvage_game.audio_prompts_played += 1
            $ salvage_game.audio_playing = False
            $ salvage_game.audio_listened = True  # Mark audio as listened - can now open page
        
        # Continue game loop
        jump .game_loop
    
    label .jumpscare:
        # JUMPSCARE! Hide everything first
        stop music
        stop sound  # Stop any playing audio prompts
        scene black  # Clear all images including threat level and checklist
        
        # Get current animatronic's jumpscare frames
        $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
        $ jumpscare_frame_1 = animatronic.get_jumpscare_frame(1)
        $ jumpscare_frame_2 = animatronic.get_jumpscare_frame(2)
        $ jumpscare_frame_3 = animatronic.get_jumpscare_frame(3)
        $ jumpscare_frame_4 = animatronic.get_jumpscare_frame(4)
        $ jumpscare_frame_5 = animatronic.get_jumpscare_frame(5)
        $ jumpscare_frame_6 = animatronic.get_jumpscare_frame(6)
        
        play sound "mod_assets/sfx/salvage_minigame/jumpscare.ogg"
        
        # Show shaking part of jumpscare (frames 1-5)
        show expression jumpscare_frame_1 at salvage_jumpscare_shake
        pause 0.02
        show expression jumpscare_frame_2 at salvage_jumpscare_shake
        pause 0.02
        show expression jumpscare_frame_3 at salvage_jumpscare_shake
        pause 0.02
        show expression jumpscare_frame_4 at salvage_jumpscare_shake
        pause 0.02
        show expression jumpscare_frame_5 at salvage_jumpscare_shake
        pause 0.02
        
        # Show final frame static (no shake) with black background
        scene black
        show expression jumpscare_frame_6
        
        # Add red overlay at 50% opacity
        show expression Solid("#FF0000") as red_overlay:
            alpha 0.5
        
        # Show YOU DIED text
        show expression Text("YOU DIED", size=100, color="#FF0000", outlines=[(5, "#000000", 0, 0)]) as death_text at truecenter
        
        pause 1.0
        
        # Fade the red overlay and animatronic to black while keeping text
        scene black
        show expression jumpscare_frame_6 at salvage_death_fade
        show expression Solid("#FF0000") as red_overlay at salvage_death_fade
        
        pause 7.0
        
        # Clean up
        scene black
        hide red_overlay
        hide death_text
        pause 2.0
        $ quick_menu = True
        play music festivalmusic
        return
    
    label .win_game:
        # Victory!
        
        play sound "mod_assets/sfx/salvage_minigame/cassette_completed.ogg"
        
        pause 6.0
        stop music fadeout 2.0
        play sound "mod_assets/sfx/salvage_minigame/game_end.ogg"
        scene black
        with dissolve_scene_full
        if current_animatronic_name == "jax_kob":
            play sound "mod_assets/sfx/salvage_minigame/jax_kob.ogg"
            pause 9.0
        elif current_animatronic_name == "glurbox":
            # Glurbox uses default victory sound for now (can add custom sound later)
            play sound "mod_assets/sfx/salvage_minigame/glurbox.ogg"
            pause 6.0
        elif current_animatronic_name == "a1ds":
            play sound "mod_assets/sfx/salvage_minigame/a1ds.ogg"
            pause 9.0
        else:
            play sound "mod_assets/sfx/salvage_minigame/el_nig.ogg"
            pause 6.0
        # Increment animatronic completion counter (max 5)
        if persistent.animatronics_completed < 5:
            $ persistent.animatronics_completed += 1
        $ rizz_reward = renpy.random.randint(5, 15)
        call rizz_update(points_change=rizz_reward, reason="Salvage completed")
        $ quick_menu = True
        play music festivalmusic
        return

# Main game screen - page viewing for jumpscares and progression
screen salvage_main_screen():
    modal True

    # Track if page is shown
    default page_visible = False
    default page_time_opened = 0.0
    default page_closing = False
    default page_return_value = None
    default last_update_time = 0.0
    default answer_given = False
    default aggression_meter_visible = False
    default last_displayed_stage = 1

    # Page checkbox states (4 groups of 5 boxes = 20 boxes total)
    # Boxes1
    default boxes1_1_checked = False
    default boxes1_2_checked = False
    default boxes1_3_checked = False
    default boxes1_4_checked = False
    default boxes1_5_checked = False
    # Boxes2
    default boxes2_1_checked = False
    default boxes2_2_checked = False
    default boxes2_3_checked = False
    default boxes2_4_checked = False
    default boxes2_5_checked = False
    # Boxes3
    default boxes3_1_checked = False
    default boxes3_2_checked = False
    default boxes3_3_checked = False
    default boxes3_4_checked = False
    default boxes3_5_checked = False
    # Boxes4
    default boxes4_1_checked = False
    default boxes4_2_checked = False
    default boxes4_3_checked = False
    default boxes4_4_checked = False
    default boxes4_5_checked = False
    
    default controls_alpha = 1.0
    default controls_timer = 0.0
    default controls_shown = False

            # Continuous aggression increase while page is visible (+100 per second)
    if page_visible:
        timer 1.0 repeat True action [
            Function(lambda: salvage_game.update_aggression_during_page_view(1.0)),
            SetVariable("salvage_game.page_view_duration", salvage_game.page_view_duration + 1.0)
        ]

    # Check for jumpscare every 0.5 seconds (at 1200 aggression)
    timer 0.5 repeat True action If(
        salvage_game.check_jumpscare(),
        Return("jumpscare"),
        NullAction()
    )
    
    # Initialize controls display on first screen call
    if globals().get('show_controls', False) and not controls_shown:
        timer 0.01 action [
            SetScreenVariable("controls_shown", True),
            SetVariable("show_controls", False)
        ]
    
    # Controls display timer - show for 10 seconds then fade out over 1 second
    if controls_shown:
        timer 0.1 repeat True action If(
            controls_timer < 10.0,
            SetScreenVariable("controls_timer", controls_timer + 0.1),
            If(
                controls_timer < 11.0,
                [
                    SetScreenVariable("controls_timer", controls_timer + 0.1),
                    SetScreenVariable("controls_alpha", 1.0 - ((controls_timer - 10.0) / 1.0))
                ],
                NullAction()
            )
        )
    
    # Show controls in top right
    if controls_shown and controls_alpha > 0.0:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -20
            yoffset 20
            background "#00000099"
            padding (15, 10)
            at Transform(alpha=controls_alpha)
            vbox:
                spacing 5
                text "SPACE - Play cassette" size 20 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Click bottom - Checklist" size 20 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "ALT - Taser" size 20 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
    
    # Alt key for taser
    key "alt_K_LALT" action Return("taser")
    key "alt_K_RALT" action Return("taser")
    key "K_LALT" action Return("taser")
    key "K_RALT" action Return("taser")
    
    # Space key to play audio (when audio is needed)
    if salvage_game.can_play_audio() and not page_visible:
        key "K_SPACE" action Return("wait")
    
    # Debug keybinds for instant win/lose
    key "shift_K_LEFTBRACKET" action Return("instant_win")  # { key
    key "shift_K_RIGHTBRACKET" action Return("instant_lose")  # } key

    # Aggression meter toggle
    key ";" action ToggleScreenVariable("aggression_meter_visible")

    # Debug: Increase aggression by 50 (for testing stage changes)
    key "shift_K_EQUALS" action Function(lambda: salvage_game.increase_aggression(50))

    # Debug: Increase aggression by 200 (for testing jumpscares)
    key "shift_K_MINUS" action Function(lambda: salvage_game.increase_aggression(200))  # + key
    
    # Page button image to open page
    if salvage_game.can_open_checklist() and not page_visible:
        imagebutton:
            idle "checklist_button"
            hover "checklist_button"
            xalign 0.5
            yalign 1.0
            action [
                Play("sound", "mod_assets/sfx/salvage_minigame/page_open.ogg"),
                SetScreenVariable("page_visible", True),
                SetScreenVariable("page_time_opened", renpy.time.time()),
                Function(lambda: salvage_game.update_page_view_time()),
                SetVariable("salvage_game.page_view_duration", 0.0),
                # Reset all boxes
                SetScreenVariable("boxes1_1_checked", False),
                SetScreenVariable("boxes1_2_checked", False),
                SetScreenVariable("boxes1_3_checked", False),
                SetScreenVariable("boxes1_4_checked", False),
                SetScreenVariable("boxes1_5_checked", False),
                SetScreenVariable("boxes2_1_checked", False),
                SetScreenVariable("boxes2_2_checked", False),
                SetScreenVariable("boxes2_3_checked", False),
                SetScreenVariable("boxes2_4_checked", False),
                SetScreenVariable("boxes2_5_checked", False),
                SetScreenVariable("boxes3_1_checked", False),
                SetScreenVariable("boxes3_2_checked", False),
                SetScreenVariable("boxes3_3_checked", False),
                SetScreenVariable("boxes3_4_checked", False),
                SetScreenVariable("boxes3_5_checked", False),
                SetScreenVariable("boxes4_1_checked", False),
                SetScreenVariable("boxes4_2_checked", False),
                SetScreenVariable("boxes4_3_checked", False),
                SetScreenVariable("boxes4_4_checked", False),
                SetScreenVariable("boxes4_5_checked", False),
                SetScreenVariable("answer_given", False)
            ]
    
    # Page overlay (shown when clicking bottom middle)
    if page_visible and salvage_game.can_open_checklist():
        # Dark overlay
        add Solid("#000000EE")

            # Page content frame with slide animation
        python:
            page_transform = checklist_slide_down if page_closing else checklist_slide_up

        frame:
            xfill True
            yfill True
            background None
            at page_transform

            # Page base image (background)
            add "checklist_base" xalign 0.5 yalign 0.5

            # Page words image (overlay text)
            add "checklist_words" xalign 0.5 yalign 0.5

            # Page button image (shown in page, clickable to close)
            if answer_given:
                imagebutton:
                    idle "checklist_button"
                    hover "checklist_button"
                    xalign 0.5
                    yalign 1.0
                    action [
                        Play("sound", "mod_assets/sfx/salvage_minigame/page_close.ogg"),
                        SetScreenVariable("page_closing", True),
                        SetScreenVariable("page_return_value", "page_closed")
                    ]
            else:
                # Can still close without answering but it won't count
                imagebutton:
                    idle "checklist_button"
                    hover "checklist_button"
                    xalign 0.5
                    yalign 1.0
                    action [
                        Play("sound", "mod_assets/sfx/salvage_minigame/page_close.ogg"),
                        SetScreenVariable("page_closing", True),
                        SetScreenVariable("page_return_value", None)
                    ]

            # Boxes1 - 5 boxes (580, 208), (580, 475), (745, 410), (900, 345), (900, 475)
            # Boxes1_1
            if boxes1_1_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (580, 208)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (580, 208)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes1_1_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes1_2
            if boxes1_2_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (580, 475)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (580, 475)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes1_2_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes1_3
            if boxes1_3_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (745, 410)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (745, 410)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes1_3_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes1_4
            if boxes1_4_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (900, 345)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (900, 345)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes1_4_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes1_5
            if boxes1_5_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (900, 475)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (900, 475)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes1_5_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes2 - 5 boxes (580, 275), (745, 208), (745, 475), (900, 410), (580, 208)
            # Boxes2_1
            if boxes2_1_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (580, 275)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (580, 275)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes2_1_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes2_2
            if boxes2_2_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (745, 208)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (745, 208)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes2_2_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes2_3
            if boxes2_3_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (745, 475)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (745, 475)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes2_3_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes2_4
            if boxes2_4_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (900, 410)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (900, 410)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes2_4_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes2_5
            if boxes2_5_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (580, 208)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (580, 208)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes2_5_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes3 - 5 boxes (580, 345), (745, 275), (900, 208), (900, 345), (580, 208)
            # Boxes3_1
            if boxes3_1_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (580, 345)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (580, 345)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes3_1_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes3_2
            if boxes3_2_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (745, 275)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (745, 275)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes3_2_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes3_3
            if boxes3_3_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (900, 208)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (900, 208)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes3_3_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes3_4
            if boxes3_4_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (900, 345)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (900, 345)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes3_4_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes3_5
            if boxes3_5_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (580, 208)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (580, 208)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes3_5_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes4 - 5 boxes (580, 410), (745, 345), (900, 275), (900, 410), (580, 208)
            # Boxes4_1
            if boxes4_1_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (580, 410)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (580, 410)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes4_1_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes4_2
            if boxes4_2_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (745, 345)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (745, 345)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes4_2_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes4_3
            if boxes4_3_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (900, 275)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (900, 275)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes4_3_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes4_4
            if boxes4_4_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (900, 410)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (900, 410)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes4_4_checked", True), Function(lambda: renpy.restart_interaction())]

            # Boxes4_5
            if boxes4_5_checked:
                imagebutton:
                    idle "checklist_box_checked"
                    hover "checklist_box_checked"
                    pos (580, 208)
                    action NullAction()  # Cannot uncheck once checked
            else:
                imagebutton:
                    idle "checklist_box"
                    hover "checklist_box"
                    pos (580, 208)
                    action [Play("sound", "mod_assets/sfx/salvage_minigame/checklist_tick.ogg"), SetScreenVariable("boxes4_5_checked", True), Function(lambda: renpy.restart_interaction())]

    # Update answer_given based on checkbox states (any of the 20 boxes checked)
    if page_visible:
        timer 0.1 repeat True action If(
            boxes1_1_checked or boxes1_2_checked or boxes1_3_checked or boxes1_4_checked or boxes1_5_checked or
            boxes2_1_checked or boxes2_2_checked or boxes2_3_checked or boxes2_4_checked or boxes2_5_checked or
            boxes3_1_checked or boxes3_2_checked or boxes3_3_checked or boxes3_4_checked or boxes3_5_checked or
            boxes4_1_checked or boxes4_2_checked or boxes4_3_checked or boxes4_4_checked or boxes4_5_checked,
            SetScreenVariable("answer_given", True),
            SetScreenVariable("answer_given", False)
        )

        # Timer to handle closing animation - wait 0.3s then close and return
        if page_closing:
            timer 0.3 repeat False action If(
                page_return_value is not None,
                [
                    SetScreenVariable("page_visible", False),
                    SetScreenVariable("page_closing", False),
                    SetScreenVariable("page_return_value", None),
                    Return(page_return_value)
                ],
                [
                    SetScreenVariable("page_visible", False),
                    SetScreenVariable("page_closing", False)
                ]
            )

        # Timer to update elapsed time display
        timer 0.5 repeat True action NullAction()

    # Aggression meter display (toggled with ";" key)
    if aggression_meter_visible:
        frame:
            xalign 1.0
            yalign 0.5
            xoffset -50
            yoffset 0
            background "#000000CC"
            padding (20, 15)

            vbox:
                spacing 10

                # Title
                text "AGGRESSION METER" size 16 color "#FF0000" outlines [(2, "#000000", 0, 0)]

                # Current aggression value
                text "[salvage_game.aggression_meter]/1200" size 24 color "#FFFFFF" outlines [(2, "#000000", 0, 0)] xalign 0.5

                # Debug info
                text "Page viewed: [salvage_game.page_view_duration:.1f]s" size 12 color "#FFFF00" outlines [(1, "#000000", 0, 0)] xalign 0.5
                text "Current Stage: [salvage_game.get_visual_stage()]" size 12 color "#00FF00" outlines [(1, "#000000", 0, 0)] xalign 0.5

                # Visual bar
                bar:
                    value salvage_game.aggression_meter
                    range 1200
                    xmaximum 200
                    ymaximum 20
                    left_bar "#00FF00"  # Green for low
                    right_bar "#FF0000"  # Red for high
                    thumb None
                    thumb_shadow None

                # Danger level indicators
                hbox:
                    spacing 5
                    xalign 0.5
                    text "SAFE" size 12 color "#00FF00" outlines [(1, "#000000", 0, 0)]
                    text "CAUTION" size 12 color "#FFFF00" outlines [(1, "#000000", 0, 0)]
                    text "DANGER" size 12 color "#FF8800" outlines [(1, "#000000", 0, 0)]
                    text "CRITICAL" size 12 color "#FF0000" outlines [(1, "#000000", 0, 0)]

                # Stage indicator
                text "Visual Stage: [salvage_game.get_visual_stage()]" size 14 color "#00FF00" outlines [(2, "#000000", 0, 0)] xalign 0.5
    

# Optional: Test label to jump directly to minigame
label test_salvage_minigame:
    "Starting Salvage Minigame test..."
    call salvage_minigame from _call_salvage_minigame
    "Minigame complete!"
    return

# Test label for jumpscare only
label test_salvage_jumpscare:
    $ quick_menu = False
    window hide
    scene black
    "..."
    stop music
    
    # Get current animatronic's jumpscare frames
    $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
    $ jumpscare_frame_1 = animatronic.get_jumpscare_frame(1)
    $ jumpscare_frame_2 = animatronic.get_jumpscare_frame(2)
    $ jumpscare_frame_3 = animatronic.get_jumpscare_frame(3)
    $ jumpscare_frame_4 = animatronic.get_jumpscare_frame(4)
    $ jumpscare_frame_5 = animatronic.get_jumpscare_frame(5)
    $ jumpscare_frame_6 = animatronic.get_jumpscare_frame(6)
    
    play sound "mod_assets/sfx/salvage_minigame/jumpscare.ogg"
    
    # Show shaking part of jumpscare (frames 1-5)
    show expression jumpscare_frame_1 at salvage_jumpscare_shake
    pause 0.03
    show expression jumpscare_frame_2 at salvage_jumpscare_shake
    pause 0.03
    show expression jumpscare_frame_3 at salvage_jumpscare_shake
    pause 0.03
    show expression jumpscare_frame_4 at salvage_jumpscare_shake
    pause 0.03
    show expression jumpscare_frame_5 at salvage_jumpscare_shake
    pause 0.03
    
    # Show final frame static (no shake) with black background
    scene black
    show expression jumpscare_frame_6
    
    # Add red overlay at 50% opacity
    show expression Solid("#FF0000") as red_overlay:
        alpha 0.5
    
    # Show YOU DIED text
    show expression Text("YOU DIED", size=100, color="#FF0000", outlines=[(5, "#000000", 0, 0)]) as death_text at truecenter
    
    pause 1.0
    
    # Fade the red overlay and animatronic to black while keeping text
    scene black
    show expression jumpscare_frame_6 at salvage_death_fade
    show expression Solid("#FF0000") as red_overlay at salvage_death_fade
    
    pause 10.0
    
    # Clean up
    scene black
    hide red_overlay
    
    "..."
    $ quick_menu = True
    return

# Test label for page only - simple test of bottom click area
label test_salvage_checklist:
    $ quick_menu = False
    window hide

    # Initialize game state for testing
    $ salvage_game.reset()
    $ salvage_game.audio_listened = True  # Allow page to be opened
    $ salvage_game.audio_prompts_completed = 0  # Start at first item
    $ show_controls = False  # Don't show controls in test

    # Show visual stage background
    $ animatronic = ANIMATRONICS.get(current_animatronic_name, ANIMATRONICS['el_nig'])
    $ stage_1_path = animatronic.get_threat_image(1)
    scene expression stage_1_path
    with dissolve

    label .test_loop:
        "Click the bottom of the screen to open/close page. Check some boxes to enable closing."
        # Show the main game screen (page should be available)
        call screen salvage_main_screen

        # Handle return
        $ action = _return

        if action == "page_closed":
            "Page viewed and closed! Can now progress to next audio."
            "Testing again..."
            jump .test_loop
        else:
            "Test ended. Restart?"
            menu:
                "Yes":
                    jump test_salvage_checklist
                "No":
                    pass

    $ quick_menu = True
    return

