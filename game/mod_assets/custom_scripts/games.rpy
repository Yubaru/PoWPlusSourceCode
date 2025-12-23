# Define the ring toss game with animations, sound effects, and variable prizes

# Define transforms for Monika chibi slide
transform next_round_slide:
    # Start off-screen to the left
    xpos -0.5 yalign 0.5
    # Ease in to center (1.5 seconds)
    easein_cubic 1.5 xpos 0.4
    # Ease out to right (1.5 seconds)
    easeout_circ 1.5 xpos 2.0

# Define special transform for NYS
transform next_round_slide_nys:
    # Start off-screen to the left
    xpos -0.5 yalign 0.5
    # Ease in to a different center position (1.5 seconds)
    easein_cubic 1.5 xpos 0.3
    # Ease out to right (1.5 seconds)
    easeout_circ 1.5 xpos 2.0

# Define the next round images
image next_round_sayori = "gui/sayori_next_round.png"
image next_round_natsuki = "gui/natsuki_next_round.png"
image next_round_yuri = "gui/yuri_next_round.png"
image next_round_nys = "gui/nys_next_round.png"

# Define Whack-a-Nigga game assets
image mole_board = Composite(
    (1280, 720),
    (0, 0), Solid("#8B4513"),  # Brown background
    (20, 20), Solid("#654321", xsize=1240, ysize=680)  # Darker brown border
)

image mole_hole = Composite(
    (150, 150),  # Increased hole size
    (0, 0), Solid("#2C1810", xsize=150, ysize=150),  # Dark hole background
    (5, 5), Solid("#1a0f0a", xsize=140, ysize=140)  # Even darker inner hole
)

image mole:
    Composite(
        (120, 120),  # Increased mole size
        (0, 30), Solid("#4a2511", xsize=120, ysize=90),  # Body
        (20, 0), Solid("#4a2511", xsize=80, ysize=80),  # Head
        (40, 20), Solid("#FFF", xsize=15, ysize=15),  # Left eye
        (65, 20), Solid("#FFF", xsize=15, ysize=15),  # Right eye
        (42, 22), Solid("#000", xsize=9, ysize=9),  # Left pupil
        (67, 22), Solid("#000", xsize=9, ysize=9),  # Right pupil
        (52, 40), Solid("#F08080", xsize=15, ysize=8)  # Nose
    )
    on show:
        ypos 80
        easein .2 ypos 0  # Pop up animation
    on hide:
        ypos 0
        easeout .2 ypos 80  # Hide animation

image mole_hit:
    Composite(
        (120, 120),  # Increased mole size
        (0, 30), Solid("#4a2511", xsize=120, ysize=90),  # Body
        (20, 0), Solid("#4a2511", xsize=80, ysize=80),  # Head
        (40, 20), Solid("#FFF", xsize=15, ysize=15),  # Left eye
        (65, 20), Solid("#FFF", xsize=15, ysize=15),  # Right eye
        (40, 22), Text("X", size=12, color="#000"),  # Left eye X
        (65, 22), Text("X", size=12, color="#000"),  # Right eye X
        (52, 40), Solid("#F08080", xsize=15, ysize=8)  # Nose
    )

init python:
    # Persistent variables for high scores and game data
    if not persistent.ring_toss_high_score:
        persistent.ring_toss_high_score = 0
    if not persistent.shooting_gallery_high_score:
        persistent.shooting_gallery_high_score = 0
    if not persistent.whack_a_mole_high_score:
        persistent.whack_a_mole_high_score = 0
    if not persistent.owned_items:
        persistent.owned_items = set()
    
    # Ticket system
    tickets = 0
    owned_items = persistent.owned_items.copy() if persistent.owned_items else set()  # Create a copy to avoid reference issues
    
    # Shop items with their costs (limited to 3 items)
    shop_items = {
        "mr_cow": {"name": "Mr. Cow", "cost": 50, "description": "A cute plush cow. Perfect for cuddling!"},
        "small_bunny": {"name": "Small Stuffed Bunny", "cost": 30, "description": "A soft, huggable bunny plush."},
        "nubert": {"name": "nubert", "cost": 1, "description": "nubert"},
        "beavis": {"name": "Beavis", "cost": 75, "description": "This nigger looks a little bit too happy."}
    }
    
    def add_tickets(amount):
        global tickets
        # Check if we're in extras mode
        if not globals().get('extras_mode', False):
            tickets += amount
            renpy.show_screen("ticket_notification", amount)
            renpy.play("mod_assets/sfx/coin.ogg", channel="sound")
        else:
            # Show extras mode message instead
            renpy.show_screen("extras_notification", "Playing for Fun!")
        
    def spend_tickets(amount):
        global tickets
        # Don't allow spending tickets in extras mode
        if globals().get('extras_mode', False):
            return False
            
        if tickets >= amount:
            tickets -= amount
            return True
        return False
        
    def add_owned_item(item_id):
        global owned_items
        # Don't add items in extras mode
        if globals().get('extras_mode', False):
            renpy.show_screen("extras_notification", "No items in Extras Mode!")
            return
            
        # Add to the inventory system (primary storage)
        if hasattr(renpy.store, 'items'):
            success = renpy.store.items.add_item(item_id)
            if success:
                # Also add to persistent storage as backup
                owned_items.add(item_id)
                persistent.owned_items.add(item_id)
                # Show purchase notification
                if item_id in shop_items:
                    item_name = shop_items[item_id]["name"]
                    renpy.show_screen("purchase_notification", item_name)
        renpy.restart_interaction()
    
    def get_random_next_round():
        import random
        characters = ["sayori", "natsuki", "yuri", "nys"]
        return "next_round_" + random.choice(characters)
    
    # Register audio channels
    renpy.music.register_channel("sound2", "sfx", loop=False)
    
    def update_mole_states(old_states, hit_index=None):
        """Update mole states, either hiding a hit mole or spawning a new one"""
        new_states = list(old_states)
        if hit_index is not None:
            # Hide the hit mole
            new_states[hit_index] = False
        else:
            # Try to spawn a new mole
            empty_holes = [i for i in range(9) if not old_states[i]]
            if empty_holes:
                # Spawn 1-3 moles at a time based on difficulty
                spawn_count = min(len(empty_holes), renpy.random.randint(1, 3))
                spawn_indices = renpy.random.sample(empty_holes, spawn_count)
                for idx in spawn_indices:
                    new_states[idx] = True
        return new_states

    import random
    
    def generate_mole_pattern(difficulty):
        """Generate a random pattern of moles based on difficulty"""
        pattern = [False] * 9
        # Number of moles increases with difficulty
        num_moles = min(random.randint(1, 2) + (difficulty // 3), 4)  # Reduced max moles
        positions = random.sample(range(9), num_moles)
        for pos in positions:
            pattern[pos] = True
        return pattern

    def get_pattern_duration(difficulty, hits_in_pattern):
        """Get how long a pattern should stay visible based on difficulty and hits"""
        # Base durations for each difficulty (in seconds)
        if difficulty == 2:  # Easy
            base_duration = 3.0
            hit_reduction = 0.15
            min_duration = 1.0
        elif difficulty == 5:  # Medium
            base_duration = 2.5
            hit_reduction = 0.2
            min_duration = 0.75
        elif difficulty == 7:  # Hard
            base_duration = 2.0
            hit_reduction = 0.25
            min_duration = 0.5
        else:  # Expert
            base_duration = 1.5
            hit_reduction = 0.3
            min_duration = 0.25
        
        # Calculate duration with hit penalties
        duration = base_duration - (hits_in_pattern * hit_reduction)
        return max(duration, min_duration)

    def calculate_score_bonus(combo):
        """Calculate score bonus based on combo"""
        return min(combo // 3, 3)  # Cap bonus at 3x

    def calculate_ticket_reward(difficulty, combo):
        """Calculate ticket reward based on difficulty and combo"""
        # Base tickets based on difficulty
        base_tickets = difficulty // 3  # 0 for easy, 1 for medium, 2 for hard, 3 for expert
        
        # Combo bonus (smaller than before)
        combo_bonus = min(combo // 4, 2)  # Max +2 tickets from combo
        
        return max(1, base_tickets + combo_bonus)  # Minimum 1 ticket

label ring_toss_game:
    # Initialize variables
    $ rings_thrown = 0
    $ max_attempts = 3
    $ total_points = 0
    $ combo = 0
    $ max_combo = 0
    $ difficulty = 1  # 1 = Easy, 2 = Medium, 3 = Hard, 4 = Expert
    $ sweet_spot_start = 40  # Start of the sweet spot (percentage)
    $ sweet_spot_end = 60    # End of the sweet spot (percentage)
    $ line_speed = 2.5       # Speed of the bouncing line
    $ practice_mode = False  # Practice mode toggle
    $ points_to_win = 5      # Points needed to win
    $ out_of_bounces = False # Track if player ran out of bounces
    $ high_score = persistent.ring_toss_high_score  # Load persistent high score

label difficulty_select:
    # Set difficulty (can be adjusted before calling the game)
    menu:
        "Choose your game mode:"
        "Practice Mode (Unlimited Rings)":
            $ practice_mode = True
            $ max_attempts = 999
            $ difficulty = 1
            $ sweet_spot_start = 40
            $ sweet_spot_end = 60
            $ line_speed = 2.0
            $ points_to_win = 999
        "Easy Mode":
            $ practice_mode = False
            $ max_attempts = 3
            $ difficulty = 1
            $ sweet_spot_start = 40
            $ sweet_spot_end = 60
            $ points_to_win = 5
            $ line_speed = 2.0
        "Medium Mode":
            $ practice_mode = False
            $ max_attempts = 3
            $ difficulty = 2
            $ sweet_spot_start = 45
            $ sweet_spot_end = 55
            $ points_to_win = 8
            $ line_speed = 3.0
        "Hard Mode":
            $ practice_mode = False
            $ max_attempts = 3
            $ difficulty = 3
            $ sweet_spot_start = 47
            $ sweet_spot_end = 53
            $ points_to_win = 12
            $ line_speed = 4.0
        "NIGGA MODE":
            $ practice_mode = False
            $ max_attempts = 3
            $ difficulty = 4
            $ sweet_spot_start = 48
            $ sweet_spot_end = 52
            $ points_to_win = 15
            $ line_speed = 5.0

    # Reset game variables when selecting new difficulty
    $ rings_thrown = 0
    $ total_points = 0
    $ combo = 0
    $ max_combo = 0
    $ out_of_bounces = False

    # Introduction to the game
    play music "mod_assets/music/circus_music.ogg" fadein 2.0

    if not practice_mode:
        "You step up to the ring toss booth. The attendant hands you three colorful rings."
        attendant "Welcome to the ring toss game! You have [max_attempts] tries to land rings on the bottles."
        attendant "Hit the sweet spot for bonus points, and try to build up combos for even more points!"
        attendant "Earn tickets based on your performance:"
        attendant "Perfect throws: 5 tickets + combo bonus"
        attendant "Close throws: 3 tickets + combo bonus"
        attendant "Miss: No tickets"
        attendant "Good luck!"
    else:
        "Welcome to Practice Mode! Take your time to perfect your throws."
        "You can throw as many rings as you want. Press ESC when you're done practicing."

    # Start the game loop
    while rings_thrown < max_attempts:
        if not practice_mode:
            "You have [max_attempts - rings_thrown] rings left."
        else:
            "Practice throw #[rings_thrown + 1]"

        # Show combo counter if active
        if combo > 0:
            show expression Text("Combo x[combo]!", size=40, color="#FFD700") as combo_text at truecenter with dissolve
            pause 0.5
            hide combo_text with dissolve

        $ rings_thrown += 1

        # Simulate the ring toss with a progress bar and visual guides
        call screen ring_toss_bar(sweet_spot_start, sweet_spot_end, line_speed)
        $ toss_result = _return

        # Check if player ran out of bounces
        if toss_result == 0:
            $ out_of_bounces = True
            play sound "mod_assets/sfx/miss.ogg"
            show expression Text("Out of Bounces!", size=50, color="#FF0000", outlines=[(2, "#000000", 0, 0)]) as text at truecenter with dissolve
            pause 1.0
            hide text with dissolve
            hide ring_miss with dissolve
            "You took too long to throw! The ring slipped from your hand."
            $ combo = 0

        # Calculate points and show feedback based on the result
        if toss_result >= sweet_spot_start and toss_result <= sweet_spot_end:
            $ points = 5  # Perfect toss
            $ combo += 1
            $ max_combo = max(combo, max_combo)
            $ bonus_points = min(combo // 2, 3)  # Bonus points from combo
            $ points += bonus_points
            play sound "mod_assets/sfx/perfect.ogg"
            show expression Text("PERFECT! +[points] Tickets\nCombo x[combo]!", size=50, color="#00FF00", outlines=[(2, "#000000", 0, 0)]) as text at truecenter with dissolve
            pause 1.0
            hide text with dissolve
            hide ring_perfect with dissolve
            "Perfect throw! You earned [points] tickets ([bonus_points] bonus from combo)!"
            $ add_tickets(points)
        elif toss_result >= sweet_spot_start - 10 and toss_result <= sweet_spot_end + 10:
            $ points = 3  # Close to sweet spot
            $ combo += 1
            $ max_combo = max(combo, max_combo)
            $ bonus_points = min(combo // 3, 2)  # Smaller bonus for close throws
            $ points += bonus_points
            play sound "mod_assets/sfx/close.ogg"
            show expression Text("CLOSE! +[points] Tickets\nCombo x[combo]!", size=50, color="#FFFF00", outlines=[(2, "#000000", 0, 0)]) as text at truecenter with dissolve
            pause 1.0
            hide text with dissolve
            hide ring_close with dissolve
            "Nice throw! You earned [points] tickets ([bonus_points] bonus from combo)!"
            $ add_tickets(points)
        else:
            $ points = 0  # Miss
            $ combo = 0  # Reset combo
            play sound "mod_assets/sfx/miss.ogg"
            show expression Text("Miss!", size=50, color="#FF0000", outlines=[(2, "#000000", 0, 0)]) as text at truecenter with dissolve
            pause 1.0
            hide text with dissolve
            hide ring_miss with dissolve
            "The ring bounced off. No tickets earned."

        # Add points to the total
        $ total_points += points

        # Show random character next round transition before next throw
        if rings_thrown < max_attempts:
            $ next_round_char = get_random_next_round()
            # Use special transform for NYS
            if next_round_char == "next_round_nys":
                show expression next_round_char at next_round_slide_nys
            else:
                show expression next_round_char at next_round_slide
            pause 3.0  # Wait for full animation
            hide expression next_round_char

        # Check if player wants to continue in practice mode
        if practice_mode:
            menu:
                "Continue practicing?"
                "Yes":
                    pass
                "Exit Practice Mode":
                    "Practice session ended! You scored [total_points] points with a max combo of [max_combo]."
                    "Come back to play for real and win tickets!"
                    jump difficulty_select

    # Game over handling
    if not practice_mode:
        if out_of_bounces:
            play sound "mod_assets/sfx/lose.ogg"
            attendant "Oh no! Better luck next time!"
        else:
            play sound "mod_assets/sfx/win.ogg"
            show expression Text("Game Complete!", size=60, color="#00FF00", outlines=[(3, "#000000", 0, 0)]) as win_text at truecenter with dissolve
            pause 1.0
            hide win_text with dissolve
            attendant "Great job! You scored [total_points] points with a max combo of [max_combo]!"
            
            # Show final results
            show expression Text("Final Score: [total_points]\nMax Combo: [max_combo]", size=50, color="#FFD700", outlines=[(2, "#000000", 0, 0)]) as result_text at truecenter
            pause 2.0
            hide result_text with dissolve

        menu:
            "Would you like to play again?"
            "Yes":
                jump difficulty_select
            "No":
                pass

    # End the game
    stop music fadeout 2.0
    return

# Define the enhanced ring toss bar screen
screen ring_toss_bar(sweet_spot_start, sweet_spot_end, line_speed):
    # Add carnival background elements    
    # Progress bar setup with visual guides
    default bar_value = 0
    default direction = 1  # 1 for right, -1 for left
    default bounce_count = 0
    default max_bounces = 6
    default last_bounce_pos = None  # Track last bounce position
    default bounce_threshold = 5  # Minimum distance needed between bounces
    
    frame:
        background "#00000080"
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        vbox:
            spacing 10
            
            # Bounce counter
            text "Bounces: [bounce_count]/[max_bounces]" size 25 xalign 0.5 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
            
            # Sweet spot indicator (using fixed instead of nested bars)
            fixed:
                xmaximum 400
                ymaximum 20
                
                # Background bar
                bar:
                    value 100
                    xmaximum 400
                    ymaximum 20
                    left_bar "#33333380"
                    right_bar "#33333380"
                
                # Sweet spot zone
                fixed:
                    xpos (sweet_spot_start * 4)
                    xsize ((sweet_spot_end - sweet_spot_start) * 4)
                    ysize 20
                    add Solid("#00FF0080")
                
                # Close zones
                fixed:
                    xpos ((sweet_spot_start - 10) * 4)
                    xsize (10 * 4)
                    ysize 20
                    add Solid("#FFFF0040")
                
                fixed:
                    xpos (sweet_spot_end * 4)
                    xsize (10 * 4)
                    ysize 20
                    add Solid("#FFFF0040")

            # Main progress bar
            bar:
                value AnimatedValue(value=bar_value, range=100, delay=1.0 / line_speed)
                xmaximum 400
                ymaximum 30
                left_bar "#3498db"
                right_bar "#2c3e50"

            # Power meter text
            text "Power: [bar_value]%" size 30 xalign 0.5 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]

    # Player input to stop the bar
    key "K_SPACE" action Return(bar_value)

    # Update the bar value over time and handle bouncing
    timer 0.01 repeat True action If(
        bounce_count >= max_bounces,
        Return(0),  # Auto miss after max bounces
        If(
            bar_value >= 100,  # Right edge bounce
            [
                SetScreenVariable("direction", -1),
                If(
                    last_bounce_pos is None or last_bounce_pos == "left",
                    [
                        SetScreenVariable("bounce_count", bounce_count + 1),
                        SetScreenVariable("last_bounce_pos", "right"),
                        Play("sound", "mod_assets/sfx/bounce.ogg")
                    ]
                ),
                SetScreenVariable("bar_value", 99)  # Prevent overshooting
            ],
            If(
                bar_value <= 0,  # Left edge bounce
                [
                    SetScreenVariable("direction", 1),
                    If(
                        last_bounce_pos is None or last_bounce_pos == "right",
                        [
                            SetScreenVariable("bounce_count", bounce_count + 1),
                            SetScreenVariable("last_bounce_pos", "left"),
                            Play("sound", "mod_assets/sfx/bounce.ogg")
                        ]
                    ),
                    SetScreenVariable("bar_value", 1)  # Prevent overshooting
                ],
                SetScreenVariable("bar_value", bar_value + (direction * line_speed))
            )
        )
    )

    # Show instructions and bounce warning if close to max
    vbox:
        xalign 0.5
        yalign 0.7
        spacing 10
        text "Press SPACE to throw!" size 40 xalign 0.5 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
        if bounce_count >= max_bounces - 2:
            text "Warning: Running out of bounces!" size 30 xalign 0.5 color "#FF0000" outlines [(2, "#000000", 0, 0)]

# Shooting gallery game
label shooting_gallery:
    # Initialize variables
    $ score = 0
    $ time_remaining = 30  # Time limit in seconds
    $ difficulty = 1  # 1 = Easy, 2 = Medium, 3 = Hard, 4 = Expert
    $ target_speed = 1.0  # Base speed of targets
    $ combo = 0  # Combo counter
    $ max_combo = 0  # Highest combo achieved
    $ shots_fired = 0
    $ shots_hit = 0
    $ high_score = persistent.shooting_gallery_high_score  # Load persistent high score
    $ screen_shake = 0  # Screen shake effect duration
    $ game_active = False

    # Set difficulty (can be adjusted before calling the game)
    menu:
        "Choose your difficulty level:"
        
        "Easy (30 seconds)":
            $ difficulty = 2
            $ time_remaining = 30
            $ target_speed = 1.5
        
        "Medium (25 seconds)":
            $ difficulty = 5
            $ time_remaining = 25
            $ target_speed = 2.0
        
        "Hard (20 seconds)":
            $ difficulty = 7
            $ time_remaining = 20
            $ target_speed = 2.5
        
        "NIGGA MODE (15 seconds)":
            $ difficulty = 10
            $ time_remaining = 15
            $ target_speed = 4.5

    # Introduction to the game
    "You step up to the shooting gallery. The attendant hands you a toy gun."
    attendant "Welcome to the shooting gallery! You have [time_remaining] seconds to break as many targets as you can."
    attendant "Hit consecutive targets to build up your combo multiplier!"
    
    # Show ticket rewards based on difficulty
    if difficulty == 1:
        attendant "Rewards on Easy:"
        attendant "1 ticket per target hit"
        attendant "Bonus tickets based on accuracy"
    elif difficulty == 2:
        attendant "Rewards on Medium:"
        attendant "2 tickets per target hit"
        attendant "Combo bonus: +1 ticket per 3 combo"
        attendant "Bonus tickets based on accuracy"
    elif difficulty == 3:
        attendant "Rewards on Hard:"
        attendant "3 tickets per target hit"
        attendant "Combo bonus: +1 ticket per 2 combo"
        attendant "Extra bonus tickets based on accuracy"
    else:
        attendant "Rewards on NIGGA MODE:"
        attendant "4 tickets per target hit"
        attendant "Combo bonus: +1 ticket every combo"
        attendant "Maximum bonus tickets for accuracy"
    
    attendant "Good luck!"

    # Start the game
    $ game_active = True
    play music "mod_assets/music/circus_music.ogg" fadein 1.0
    
    # Show countdown
    show expression Text("3", size=120, color="#FF0000", outlines=[(4, "#000000", 0, 0)]) as countdown at truecenter
    play sound "mod_assets/sfx/count.ogg"
    pause 1.0
    hide countdown
    
    show expression Text("2", size=120, color="#FF0000", outlines=[(4, "#000000", 0, 0)]) as countdown at truecenter
    play sound "mod_assets/sfx/count.ogg"
    pause 1.0
    hide countdown
    
    show expression Text("1", size=120, color="#FF0000", outlines=[(4, "#000000", 0, 0)]) as countdown at truecenter
    play sound "mod_assets/sfx/count.ogg"
    pause 1.0
    hide countdown
    
    show expression Text("START!", size=140, color="#00FF00", outlines=[(4, "#000000", 0, 0)]) as countdown at truecenter
    play sound "mod_assets/sfx/start.ogg"
    pause 1.0
    hide countdown

    # Main game screen
    hide window
    call screen shooting_gallery_screen

    # Game over handling
    $ game_active = False
    stop music fadeout 1.0

    # Calculate tickets and bonuses
    if shots_hit > 0:
        $ accuracy = (shots_hit / float(shots_fired)) * 100 if shots_fired > 0 else 0
        
        # Base tickets (1 per hit)
        $ base_tickets = shots_hit
        
        # Combo bonus tickets (scales with difficulty)
        if difficulty == 1:
            $ combo_bonus = max_combo // 4  # +1 ticket per 4 combo
        elif difficulty == 2:
            $ combo_bonus = max_combo // 3  # +1 ticket per 3 combo
        elif difficulty == 3:
            $ combo_bonus = max_combo // 2  # +1 ticket per 2 combo
        else:
            $ combo_bonus = max_combo  # +1 ticket per combo on Expert
        
        # Accuracy bonus (scales with difficulty and accuracy)
        $ accuracy_bonus = int((accuracy / 100.0) * (10 * difficulty))  # Up to 10/20/30/40 bonus tickets for perfect accuracy
    else:
        $ accuracy = 0
        $ base_tickets = 0
        $ combo_bonus = 0
        $ accuracy_bonus = 0

    # Update high score
    if score > high_score:
        $ high_score = score
        $ persistent.shooting_gallery_high_score = score  # Save to persistent
        play sound "mod_assets/sfx/perfect.ogg"
        "New High Score: [score] points!"

    # Show results
    $ accuracy_display = str(int(accuracy)) if accuracy == int(accuracy) else "%.1f" % accuracy
    attendant "Great shooting! You hit [shots_hit] targets with [accuracy_display] percent accuracy!"
    attendant "Your highest combo was [max_combo]x!"
    
    # Award base tickets
    if base_tickets > 0:
        play sound "mod_assets/sfx/coin.ogg"
        show expression Text("Base Tickets: +[base_tickets]!", size=50, color="#00FF00") as text at truecenter with dissolve
        pause 1.0
        hide text with dissolve
        $ add_tickets(base_tickets)
    
    # Award combo bonus tickets
    if combo_bonus > 0:
        play sound "mod_assets/sfx/coin.ogg"
        show expression Text("Combo Bonus: +[combo_bonus] Tickets!", size=50, color="#FFD700") as text at truecenter with dissolve
        pause 1.0
        hide text with dissolve
        $ add_tickets(combo_bonus)
    
    # Award accuracy bonus tickets
    if accuracy_bonus > 0:
        play sound "mod_assets/sfx/perfect.ogg"
        show expression Text("Accuracy Bonus: +[accuracy_bonus] Tickets!", size=50, color="#00FF00") as text at truecenter with dissolve
        pause 1.0
        hide text with dissolve
        $ add_tickets(accuracy_bonus)

    # Ask to play again
    menu:
        "Would you like to play again?"
        "Yes":
            jump shooting_gallery
        "No":
            pass

    return

# Shooting gallery screen
screen shooting_gallery_screen():
    modal True
    zorder 1000
    on "show" action [Hide("say"), Hide("choice")]  # Hide textbox and choice menu
    on "hide" action [Show("say", who=None, what="")]  # Show empty textbox when hiding
    
    # Initialize variables
    default target_x = renpy.random.randint(100, 1180)
    default target_y = renpy.random.randint(100, 620)
    default target_visible = True
    default target_broken = False
    default target_fade_timer = 0.5
    default target_move_timer = 0.0
    default target_lifetime = 0.0
    default target_max_lifetime = 3.0 / difficulty
    default target_direction = 1

    # Background
    add Solid("#FFC0CB")

    # Main game container with shake effect
    $ current_transform = shake_transform if screen_shake > 0 else null_transform
    frame:
        background None
        xfill True
        yfill True
        at current_transform

        # Score and time display
        frame:
            style_prefix "game_hud"
            vbox:
                text "Score: [score]" size 40 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Time: [time_remaining]" size 40 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                if combo > 1:
                    text "Combo: x[combo]" size 40 color "#FFD700" outlines [(2, "#000000", 0, 0)] at pulse
                text "High Score: [high_score]" size 30 color "#FFD700" outlines [(2, "#000000", 0, 0)]

        # Display the target
        if target_visible and game_active:
            fixed:
                pos (target_x, target_y)
                if not target_broken:
                    # Target lifetime indicator
                    bar:
                        value (target_max_lifetime - target_lifetime)
                        range target_max_lifetime
                        xsize 100
                        ysize 5
                        ypos -10
                        xalign 0.5
                        left_bar "#00FF00"
                        right_bar "#FF0000"
                    imagebutton:
                        idle "mod_assets/images/games/target.png"
                        hover "mod_assets/images/games/target.png"
                        action [
                            SetScreenVariable("target_broken", True),
                            SetVariable("score", score + (1 * combo)),
                            SetVariable("shots_hit", shots_hit + 1),
                            SetVariable("combo", combo + 1),
                            SetVariable("max_combo", max(combo + 1, max_combo)),
                            SetVariable("screen_shake", 3),
                            Function(add_tickets, 2 + min(combo // 2, 3)),
                            Play("sound", "mod_assets/sfx/target_break.ogg")
                        ]
                else:
                    add "mod_assets/images/games/target_broken.png"
                    timer 0.3 action [
                        SetScreenVariable("target_broken", False),
                        SetScreenVariable("target_visible", False),
                        SetScreenVariable("target_lifetime", 0)
                    ]

        # Click anywhere to shoot (and miss) if game is active
        if game_active:
            button:
                background None
                xfill True
                yfill True
                action [
                    SetVariable("shots_fired", shots_fired + 1),
                    SetVariable("combo", 1),
                    Play("sound", "mod_assets/sfx/miss.ogg")
                ]

    # Timer for target movement, spawning, and lifetime
    timer 0.016 repeat True action If(
        game_active,
        [
            SetScreenVariable("target_move_timer", target_move_timer + 0.016),
            If(
                target_visible and not target_broken,
                [
                    SetScreenVariable("target_lifetime", target_lifetime + 0.016),
                    If(
                        target_lifetime >= target_max_lifetime,
                        [
                            SetScreenVariable("target_visible", False),
                            SetScreenVariable("target_lifetime", 0),
                            SetVariable("combo", 1),
                            Play("sound", "mod_assets/sfx/miss.ogg")
                        ]
                    )
                ]
            ),
            If(
                target_move_timer >= (1.0 / target_speed),
                [
                    SetScreenVariable("target_move_timer", 0),
                    If(
                        not target_visible,
                        [
                            SetScreenVariable("target_x", renpy.random.randint(100, 1180)),
                            SetScreenVariable("target_y", renpy.random.randint(100, 620)),
                            SetScreenVariable("target_visible", True),
                            SetScreenVariable("target_broken", False),
                            SetScreenVariable("target_lifetime", 0),
                            Play("sound", "mod_assets/sfx/target_spawn.ogg")
                        ]
                    )
                ]
            )
        ]
    )

    # Game timer
    timer 1.0 repeat True action If(
        game_active,
        [
            SetVariable("time_remaining", time_remaining - 1),
            If(
                time_remaining <= 0,
                Return()
            )
        ]
    )

style game_hud_frame:
    background "#0008"
    xalign 0.0
    yalign 0.0
    padding (20, 20)

transform shake_transform:
    xoffset 0
    ease 0.05 xoffset 10
    ease 0.05 xoffset -10
    ease 0.05 xoffset 5
    ease 0.05 xoffset -5
    ease 0.05 xoffset 0

transform null_transform:
    xoffset 0

transform pulse:
    zoom 1.0
    ease 0.2 zoom 1.1
    ease 0.2 zoom 1.0
    repeat

transform notify_appear:
    alpha 0.0
    ease .25 alpha 1.0
    pause .5
    ease .25 alpha 0.0

# Whack-a-Nigga game
label whack_a_mole:
    # Initialize variables
    $ score = 0
    $ time_remaining = 30  # Time limit in seconds
    $ difficulty = 1  # 1 = Easy, 2 = Medium, 3 = Hard, 4 = Expert
    $ mole_speed = 1.0  # Base speed of moles
    $ combo = 0  # Combo counter
    $ max_combo = 0  # Highest combo achieved
    $ hits = 0
    $ misses = 0
    $ high_score = persistent.whack_a_mole_high_score  # Load persistent high score
    $ screen_shake = 0  # Screen shake effect duration
    $ game_active = False

    # Set difficulty (can be adjusted before calling the game)
    menu:
        "Choose your difficulty level:"
        
        "Easy (30 seconds)":
            $ difficulty = 2
            $ time_remaining = 30
            $ mole_speed = 1.5
        
        "Medium (25 seconds)":
            $ difficulty = 5
            $ time_remaining = 25
            $ mole_speed = 2.0
        
        "Hard (20 seconds)":
            $ difficulty = 7
            $ time_remaining = 20
            $ mole_speed = 2.5
        
        "NIGGA MODE (15 seconds)":
            $ difficulty = 10
            $ time_remaining = 15
            $ mole_speed = 3.0

    # Introduction to the game
    "You step up to the Whack-a-Nigga booth. The attendant hands you a soft mallet."
    attendant "Welcome to Whack-a-Nigga! You have [time_remaining] seconds to hit as many niggas as you can."
    attendant "Each nigger you hit is worth one ticket. Simple as that!"
    attendant "Good luck!"

    # Start the game
    $ game_active = True
    play music "mod_assets/music/circus_music.ogg" fadein 1.0
    
    # Show countdown
    show expression Text("3", size=120, color="#FF0000", outlines=[(4, "#000000", 0, 0)]) as countdown at truecenter
    play sound "mod_assets/sfx/count.ogg"
    pause 1.0
    hide countdown
    
    show expression Text("2", size=120, color="#FF0000", outlines=[(4, "#000000", 0, 0)]) as countdown at truecenter
    play sound "mod_assets/sfx/count.ogg"
    pause 1.0
    hide countdown
    
    show expression Text("1", size=120, color="#FF0000", outlines=[(4, "#000000", 0, 0)]) as countdown at truecenter
    play sound "mod_assets/sfx/count.ogg"
    pause 1.0
    hide countdown
    
    show expression Text("START!", size=140, color="#00FF00", outlines=[(4, "#000000", 0, 0)]) as countdown at truecenter
    play sound "mod_assets/sfx/start.ogg"
    pause 1.0
    hide countdown
    
    # Main game screen
    call screen whack_a_mole_screen

    # Game over handling
    $ game_active = False
    stop music fadeout 1.0
    
    # Update high score
    if score > high_score:
        $ high_score = score
        $ persistent.whack_a_mole_high_score = score  # Save to persistent
        play sound "mod_assets/sfx/perfect.ogg"
        "New High Score: [score] points!"

    # Show results
    attendant "Great job! You hit [hits] niggas!"
    
    # Award tickets (1:1 ratio)
    if hits > 0:
        play sound "mod_assets/sfx/coin.ogg"
        show expression Text("You earned [hits] tickets!", size=50, color="#00FF00") as text at truecenter with dissolve
        pause 1.0
        hide text with dissolve
        $ add_tickets(hits)
            
    # Ask to play again
    menu:
        "Would you like to play again?"
        "Yes":
            jump whack_a_mole
        "No":
            pass

    return

# Whack-a-Nigga game screen
screen whack_a_mole_screen():
    # Initialize variables for 9 mole holes
    default mole_states = [False] * 9  # Whether each mole is visible
    default pattern_timer = 0.0  # Time until current pattern changes
    default pattern_duration = get_pattern_duration(difficulty, 0)  # Initial pattern duration
    default holes_pos = [  # Grid positions for the 9 holes
        (320, 180), (640, 180), (960, 180),  # Top row
        (320, 360), (640, 360), (960, 360),  # Middle row
        (320, 540), (640, 540), (960, 540)   # Bottom row
    ]
    default hit_states = [False] * 9  # Track which moles are in hit state
    default hits_in_pattern = 0  # Track hits in current pattern
    default total_moles_in_pattern = 0  # Track total moles in current pattern
    default best_score = 0  # Track best score achieved
    
    # Background
    add "mole_board"
    
    # Main game container
    frame:
        background None
        xfill True
        yfill True
        at (shake_transform if screen_shake > 0 else null_transform)

        # Score and time display
        frame:
            style_prefix "game_hud"
            vbox:
                text "Score: [score]" size 40 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Time: [time_remaining]" size 40 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                text "Hits: [hits]" size 40 color "#00FF00" outlines [(2, "#000000", 0, 0)]
                text "Best Score: [best_score]" size 30 color "#FFD700" outlines [(2, "#000000", 0, 0)]
                text "Niggas Left: [max(0, total_moles_in_pattern - hits_in_pattern)]" size 30 color "#FF0000" outlines [(2, "#000000", 0, 0)]

        # Display mole holes and moles
        for i in range(9):
            fixed:
                pos holes_pos[i]
                
                # Always show the hole
                add "mole_hole":
                    xanchor 0.5
                    yanchor 0.5
                
                # Show mole if it's up
                if mole_states[i]:
                    if hit_states[i]:
                        add "mole_hit":
                            xanchor 0.5
                            yanchor 0.5
                    else:
                        imagebutton:
                            idle "mole"
                            hover "mole"
                            xanchor 0.5
                            yanchor 0.5
                            action [
                                SetScreenVariable("mole_states", 
                                    [False if j == i else mole_states[j] for j in range(9)]),
                                SetScreenVariable("hit_states", [j == i for j in range(9)]),
                                SetScreenVariable("hits_in_pattern", hits_in_pattern + 1),
                                SetScreenVariable("pattern_timer", 
                                    get_pattern_duration(difficulty, hits_in_pattern + 1)),
                                SetVariable("score", score + 1),
                                SetVariable("hits", hits + 1),
                                SetVariable("screen_shake", 3),
                                Play("sound", "mod_assets/sfx/hit.ogg")
                            ]

        # Click anywhere to miss if game is active
        if game_active:
            button:
                background None
                xfill True
                yfill True
                action [
                    SetVariable("score", 0),
                    SetVariable("hits", 0),
                    SetVariable("misses", misses + 1),
                    SetScreenVariable("mole_states", generate_mole_pattern(difficulty)),
                    SetScreenVariable("pattern_timer", get_pattern_duration(difficulty, 0)),
                    SetScreenVariable("hits_in_pattern", 0),
                    SetScreenVariable("total_moles_in_pattern", sum(generate_mole_pattern(difficulty))),
                    Play("sound", "mod_assets/sfx/miss.ogg")
                ]

    # Force spawn initial pattern
    on "show" action [
        SetScreenVariable("mole_states", generate_mole_pattern(difficulty)),
        SetScreenVariable("pattern_timer", get_pattern_duration(difficulty, 0)),
        SetScreenVariable("hits_in_pattern", 0),
        SetScreenVariable("total_moles_in_pattern", sum(generate_mole_pattern(difficulty)))
    ]

    # Update pattern and timers
    timer 0.016 repeat True action If(
        game_active,
        [
            # Update pattern timer
            SetScreenVariable("pattern_timer", pattern_timer - 0.016),
            
            # Reset hit states quickly
            If(
                any(hit_states),
                [
                    SetScreenVariable("hit_states", [False] * 9)
                ]
            ),
            
            # Generate new pattern when timer expires
            If(
                pattern_timer <= 0,
                [
                    # Check if all moles in pattern were hit
                    If(
                        hits_in_pattern < total_moles_in_pattern,
                        [
                            # Reset combo if pattern wasn't cleared
                            SetVariable("combo", 1),
                            Play("sound", "mod_assets/sfx/miss.ogg"),
                            Show("pattern_failed", dissolve),
                        ]
                    ),
                    # Generate new pattern
                    SetScreenVariable("mole_states", generate_mole_pattern(difficulty)),
                    SetScreenVariable("pattern_timer", get_pattern_duration(difficulty, hits)),
                    SetScreenVariable("hits_in_pattern", 0),
                    SetScreenVariable("total_moles_in_pattern", sum(generate_mole_pattern(difficulty))),
                    Play("sound", "mod_assets/sfx/target_spawn.ogg")
                ]
            ),
            
            # Update best score
            SetScreenVariable("best_score", max(score, best_score))
        ]
    )

    # Game timer
    timer 1.0 repeat True action If(
        game_active,
        [
            SetVariable("time_remaining", time_remaining - 1),
            If(
                time_remaining <= 0,
                Return()
            )
        ]
    )

# Pattern failed notification screen
screen pattern_failed():
    zorder 100
    frame:
        at notify_appear
        xalign 0.5
        yalign 0.3
        background None
        text "Pattern Failed!" size 60 color "#FF0000" outlines [(3, "#000000", 0, 0)]
    timer 1.0 action Hide("pattern_failed")

# Ticket notification screen
screen ticket_notification(amount):
    zorder 100
    frame:
        at notify_appear
        xalign 1.0
        yalign 0.0
        xoffset -20
        yoffset 20
        background None
        hbox:
            spacing 10
            text "+ [amount]" size 40 color "#FFD700" outlines [(2, "#000000", 0, 0)]
            text "Tickets!" size 40 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
    timer 3.0 action Hide("ticket_notification")

# Prize shop screen
screen prize_shop():
    modal True
    zorder 1000  # Ensure it's on top of everything
    on "show" action [Hide("say"), Hide("choice")]  # Hide textbox and choice menu
    on "hide" action [Show("say", who=None, what="")]  # Show empty textbox when hiding prize shop
    
    # Debug key binding for adding tickets
    key "t" action [Function(add_tickets, 200), Play("sound", "mod_assets/sfx/coin.ogg")]
    frame:
        background "#0008"
        xfill True
        yfill True
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20
            frame:
                background "#2228"
                xsize 800
                ysize 500
                padding (20, 20)
                vbox:
                    spacing 10
                    text "Festival Prize Shop" size 50 xalign 0.5 color "#FFD700" outlines [(3, "#000000", 0, 0)]
                    text "Your Tickets: [tickets]" size 30 xalign 0.5 color "#FFFFFF" outlines [(2, "#000000", 0, 0)]
                    null height 20
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        ysize 300
                        vbox:
                            spacing 10
                            for item_id, item in shop_items.items():
                                frame:
                                    background "#4448"
                                    padding (10, 10)
                                    xfill True
                                    hbox:
                                        spacing 20
                                        xfill True
                                        vbox:
                                            spacing 5
                                            text item["name"] size 24 color "#FFFFFF"
                                            text "[item['cost']] Tickets" size 20 color "#FFD700"
                                            text item["description"] size 16 color "#AAAAAA"
                                        if item_id in items.items:  # Check actual inventory
                                            frame:
                                                background None
                                                yalign 0.5
                                                text "Owned" size 20 color "#00FF00" xalign 1.0
                                        else:
                                            frame:
                                                background None
                                                yalign 0.5
                                                textbutton "Buy":
                                                    text_size 20
                                                    action If(tickets >= item["cost"],
                                                        [Function(spend_tickets, item["cost"]),
                                                        Function(add_owned_item, item_id),
                                                        Play("sound", "mod_assets/sfx/buy.ogg")],
                                                        [Show("insufficient_tickets"),
                                                        Play("sound", "mod_assets/sfx/error.ogg")]
                                                    )
                                                    text_color "#FFFFFF"
                                                    text_hover_color "#FFD700"
                                                    xalign 1.0
            textbutton "Back" action Return("back") text_size 30 text_color "#FFFFFF" text_hover_color "#FFD700"

# Insufficient tickets notification
screen insufficient_tickets():
    modal True
    zorder 1001
    frame:
        background "#0008"
        xfill True
        yfill True
        frame:
            background "#2228"
            xalign 0.5
            yalign 0.5
            padding (40, 20)
            vbox:
                spacing 10
                text "Not Enough Tickets!" size 30 xalign 0.5 color "#FF0000" outlines [(2, "#000000", 0, 0)]
                text "You need more tickets to buy this item." size 20 xalign 0.5 color "#FFFFFF"
                null height 10
                textbutton "OK" action Hide("insufficient_tickets") xalign 0.5 text_size 20 text_color "#FFFFFF" text_hover_color "#FFD700"

# Purchase success notification
screen purchase_notification(item_name):
    zorder 1002
    frame:
        at notify_appear
        xalign 0.5
        yalign 0.1
        background "#2228"
        padding (30, 15)
        vbox:
            spacing 5
            text "Purchase Successful!" size 24 xalign 0.5 color "#00FF00" outlines [(2, "#000000", 0, 0)]
            text "You bought: [item_name]" size 20 xalign 0.5 color "#FFFFFF" outlines [(1, "#000000", 0, 0)]
            text "Check your inventory (Press 'i')" size 16 xalign 0.5 color "#FFD700" outlines [(1, "#000000", 0, 0)]
    
    timer 3.0 action Hide("purchase_notification")

# ================================================================================================
# EXTRAS MENU VERSIONS - NO REWARDS/TICKETS
# ================================================================================================

# These are reward-free versions of the games for the extras menu
# Players can enjoy the games without affecting their progress or economy

init python:
    extras_mode = False  # Flag to track if we're in extras mode
    
    def set_extras_mode(enabled):
        global extras_mode
        extras_mode = enabled
    
    def add_tickets_extras_safe(amount):
        # Don't add tickets in extras mode
        if not extras_mode:
            add_tickets(amount)
        else:
            # Show a different message for extras mode
            renpy.show_screen("extras_notification", "Playing for Fun!")

# Extras notification screen
screen extras_notification(message):
    zorder 100
    frame:
        at notify_appear
        xalign 0.5
        yalign 0.1
        background "#2228"
        padding (20, 10)
        text message size 24 color "#FFD700" outlines [(2, "#000000", 0, 0)] xalign 0.5
    timer 2.0 action Hide("extras_notification")

# Ring Toss Game - Extras Version (No Rewards)
label ring_toss_game_extras:
    $ set_extras_mode(True)
    scene bg festival_day
    with dissolve_scene_full
    play music t6
    
    "Welcome to Ring Toss! (Extras Mode - No Rewards)"
    "Try to get the highest score just for fun!"
    
    call difficulty_select from _call_difficulty_select_extras
    call ring_toss_game from _call_ring_toss_game_extras
    
    $ set_extras_mode(False)
    return

# Shooting Gallery - Extras Version (No Rewards)  
label shooting_gallery_extras:
    $ set_extras_mode(True)
    scene bg festival_day
    with dissolve_scene_full
    play music t6
    
    "Welcome to Shooting Gallery! (Extras Mode - No Rewards)"
    "See how many targets you can hit!"
    
    call difficulty_select from _call_difficulty_select_extras_2
    call shooting_gallery from _call_shooting_gallery_extras
    
    $ set_extras_mode(False)
    return

# Whack-a-Mole - Extras Version (No Rewards)
label whack_a_mole_extras:
    $ set_extras_mode(True)
    scene bg festival_day  
    with dissolve_scene_full
    play music t6
    
    "Welcome to Whack-a-Mole! (Extras Mode - No Rewards)"
    "Test your reflexes and see how high you can score!"
    
    call difficulty_select from _call_difficulty_select_extras_3
    call whack_a_mole from _call_whack_a_mole_extras
    
    $ set_extras_mode(False)
    return

# Yazzinator Battle - Extras Version (No Rewards)
label battle_start_extras:
    $ set_extras_mode(True)
    
    "Yazzinator Battle! (Extras Mode - No Rewards)"
    "Fight the Yazzinator again just for the fun of it!"
    
    call battle_start from _call_battle_start_extras
    
    $ set_extras_mode(False)
    return

# Meat Beat Mania - Extras Version (No Rewards)
label meat_beat_mania_extras:
    $ set_extras_mode(True)
    
    "Meat Beat Mania! (Extras Mode - No Rewards)"
    "Beat the meat... for fun!"
    
    call meat_beat_mania from _call_meat_beat_mania_extras
    
    $ set_extras_mode(False)
    return






















