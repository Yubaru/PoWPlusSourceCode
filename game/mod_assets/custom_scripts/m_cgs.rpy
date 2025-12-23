# Adding more cherry blossom petals with the same movement pattern
# Each with different timings and slight variations in path

image cherry_petal1:
    "mod_assets/images/misc/petal1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        10.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xpos 1280 ypos 0
        linear 14.0 xpos 0 ypos 720
        repeat
    parallel:
        rotate 0
        linear 7.0 rotate 360
        repeat

image cherry_petal2:
    "mod_assets/images/misc/petal2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        28.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xpos 1180 ypos 50
        linear 32.0 xpos 100 ypos 670
        repeat
    parallel:
        rotate 90
        linear 9.0 rotate 450
        repeat

image cherry_petal3:
    "mod_assets/images/misc/petal3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        13.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xpos 1230 ypos 120
        linear 17.0 xpos 50 ypos 600
        repeat
    parallel:
        rotate 180
        linear 8.0 rotate 540
        repeat

image cherry_petal4:
    "mod_assets/images/misc/petal4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        15.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xpos 1150 ypos 30
        linear 19.0 xpos 130 ypos 690
        repeat
    parallel:
        rotate 270
        linear 11.0 rotate 630
        repeat

# Additional petals (5-8)
image cherry_petal5:
    "mod_assets/images/misc/petal1.png"
    subpixel True
    parallel:
        alpha 1.00
        5.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        12.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xpos 1200 ypos 80
        linear 16.0 xpos 80 ypos 650
        repeat
    parallel:
        rotate 45
        linear 8.5 rotate 405
        repeat

image cherry_petal6:
    "mod_assets/images/misc/petal2.png"
    subpixel True
    parallel:
        alpha 1.00
        7.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        18.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xpos 1250 ypos 150
        linear 21.0 xpos 30 ypos 680
        repeat
    parallel:
        rotate 135
        linear 10.0 rotate 495
        repeat

image cherry_petal7:
    "mod_assets/images/misc/petal3.png"
    subpixel True
    parallel:
        alpha 1.00
        5.5
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        14.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xpos 1170 ypos 20
        linear 15.0 xpos 110 ypos 700
        repeat
    parallel:
        rotate 225
        linear 7.5 rotate 585
        repeat

image cherry_petal8:
    "mod_assets/images/misc/petal4.png"
    subpixel True
    parallel:
        alpha 1.00
        6.5
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        16.0
        linear 2.0 alpha 0
        repeat
    parallel:
        xpos 1220 ypos 100
        linear 18.0 xpos 60 ypos 620
        repeat
    parallel:
        rotate 315
        linear 9.5 rotate 675
        repeat

# Define images to show in your scene
image cherry_blossoms_falling1:
    "cherry_petal1"

image cherry_blossoms_falling2:
    "cherry_petal2"

image cherry_blossoms_falling3:
    "cherry_petal3"

image cherry_blossoms_falling4:
    "cherry_petal4"

image cherry_blossoms_falling5:
    "cherry_petal5"

image cherry_blossoms_falling6:
    "cherry_petal6"

image cherry_blossoms_falling7:
    "cherry_petal7"

image cherry_blossoms_falling8:
    "cherry_petal8"





image cherry_blossoms_spiraling1:
    "spiral_petal1"

image cherry_blossoms_spiraling2:
    "spiral_petal2"

image cherry_blossoms_spiraling3:
    "spiral_petal3"

image cherry_blossoms_spiraling4:
    "spiral_petal4"

image cherry_blossoms_spiraling5:
    "spiral_petal5"

image cherry_blossoms_spiraling6:
    "spiral_petal6"

image cherry_blossoms_spiraling7:
    "spiral_petal7"

image cherry_blossoms_spiraling8:
    "spiral_petal8"

image cherry_blossoms_spiraling9:
    "spiral_petal9"

image cherry_blossoms_spiraling10:
    "spiral_petal10"



image spiral_petal1:
    "mod_assets/images/misc/petal1.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        6.0
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 0 ypos 0
        linear 10.0 xpos 1280 ypos 720
        delay 0.0
        repeat
    parallel:
        rotate 0
        linear 10.0 rotate 360
        repeat

image spiral_petal2:
    "mod_assets/images/misc/petal2.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        7.0
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 1280 ypos 0
        linear 12.0 xpos 0 ypos 720
        delay 1.0
        repeat
    parallel:
        rotate 45
        linear 12.0 rotate 405
        repeat

image spiral_petal3:
    "mod_assets/images/misc/petal3.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        6.5
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 0 ypos 720
        linear 11.0 xpos 1280 ypos 0
        delay 0.5
        repeat
    parallel:
        rotate 90
        linear 11.0 rotate 450
        repeat

image spiral_petal4:
    "mod_assets/images/misc/petal4.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        7.0
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 1280 ypos 720
        linear 11.0 xpos 0 ypos 0
        delay 1.5
        repeat
    parallel:
        rotate 135
        linear 11.0 rotate 495
        repeat

image spiral_petal5:
    "mod_assets/images/misc/petal1.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        7.5
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 640 ypos 720
        linear 12.0 xpos 200 ypos -100
        delay 0.2
        repeat
    parallel:
        rotate 180
        linear 12.0 rotate 540
        repeat

image spiral_petal6:
    "mod_assets/images/misc/petal2.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        6.5
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 640 ypos 0
        linear 11.0 xpos 1080 ypos 900
        delay 0.8
        repeat
    parallel:
        rotate 225
        linear 11.0 rotate 585
        repeat

image spiral_petal7:
    "mod_assets/images/misc/petal3.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        7.0
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 1280 ypos 0
        linear 13.0 xpos 0 ypos 720
        delay 0.3
        repeat
    parallel:
        rotate 270
        linear 13.0 rotate 630
        repeat

image spiral_petal8:
    "mod_assets/images/misc/petal4.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        7.0
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 0 ypos 0
        linear 14.0 xpos 1280 ypos 720
        delay 1.2
        repeat
    parallel:
        rotate 315
        linear 14.0 rotate 675
        repeat

image spiral_petal9:
    "mod_assets/images/misc/petal1.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        6.0
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 640 ypos 360
        linear 12.0 xpos 1000 ypos 1000
        delay 0.4
        repeat
    parallel:
        rotate 45
        linear 12.0 rotate 450
        repeat

image spiral_petal10:
    "mod_assets/images/misc/petal2.png"
    subpixel True
    parallel:
        alpha 0
        linear 1.0 alpha 1.0
        6.5
        linear 1.0 alpha 0
        repeat
    parallel:
        xpos 640 ypos 0
        linear 13.0 xpos 1200 ypos 900
        delay 1.4
        repeat
    parallel:
        rotate 135
        linear 13.0 rotate 495
        repeat


#Monika sitting cg First CG (takoyaki story)
image m_cg_1a:
    subpixel True
    "mod_assets/images/cg/m_cg_1a.png"

image m_cg_1b:
    subpixel True
    "mod_assets/images/cg/m_cg_1b.png"

image m_cg_1c:
    subpixel True
    "mod_assets/images/cg/m_cg_1c.png"

image m_cg_backround:
    subpixel True
    "mod_assets/images/cg/m_cg_backround.png"


#------------------------------------------------------------------------
#Monika and Jacko cg Second CG (takoyaki story)

image mj_cg_backround:
    subpixel True
    "mod_assets/images/cg/mj_cg_backround.png"

image mj_cg:
    subpixel True
    "mod_assets/images/cg/mj_cg.png"

image mj_kiss_cg:
    subpixel True
    "mod_assets/images/cg/mj_kiss_cg.png"

image m_cg_trueending:
    subpixel True
    "mod_assets/images/cg/m_cg_trueending.png"




#Monika and Jacko cg (picnic story)
image m_cg_rail_1a: #Monika mouth closed neutral open eyes
    subpixel True
    "mod_assets/images/cg/m_cg_rail_1a.png"

image m_cg_rail_1b: #Monika mouth closed happy open eyes
    subpixel True
    "mod_assets/images/cg/m_cg_rail_1b.png"

image m_cg_rail_1c: #Monika mouth closed neutral eyes closed
    subpixel True
    "mod_assets/images/cg/m_cg_rail_1c.png"

image m_cg_rail_1d: #Monika mouth closed happy eyes closed
    subpixel True
    "mod_assets/images/cg/m_cg_rail_1d.png"

image m_cg_rail_1e: #Monika mouth open open eyes
    subpixel True
    "mod_assets/images/cg/m_cg_rail_1e.png"

image m_cg_rail_1f: #Monika mouth open closed eyes
    subpixel True
    "mod_assets/images/cg/m_cg_rail_1f.png"

"""
example:
show m_cg_rail_1a zorder 4
m "..."
hide m_cg_rail_1a
show m_cg_rail_1e zorder 4
with dissolve_cg
m "What makes something matter to you?"
play music abyss
hide m_cg_rail_1e
show m_cg_rail_1a zorder 4
with dissolve_cg

just like mpts you should close their mouth when they are done talking
"""





image m_cg_cafeEvent_shaft1:
    "mod_assets/images/cg/m_cg_cafeEvent_sunshaft1.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        9.0
        linear 4.0 alpha 0
        repeat
image m_cg_cafeEvent_shaft2:
    "mod_assets/images/cg/m_cg_cafeEvent_sunshaft2.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        12.0
        linear 4.0 alpha 0
        repeat
image m_cg_cafeEvent_shaft3:
    "mod_assets/images/cg/m_cg_cafeEvent_sunshaft3.png"
    subpixel True
    parallel:
        alpha 1.00
        6.0
        linear 1.0 alpha 0.35
        1.0
        linear 1.0 alpha 1.0
        repeat
    parallel:
        alpha 0
        linear 2.0 alpha 1.0
        24.0
        linear 2.0 alpha 0
        repeat

# CG Tracking System - Reworked for 5 specific CGs
init python:
    # Set up persistent variables for the 5 specific CGs
    if not hasattr(persistent, 'pow_cg_msit') or persistent.pow_cg_msit is None:
        persistent.pow_cg_msit = False
    if not hasattr(persistent, 'pow_cg_mjtogether') or persistent.pow_cg_mjtogether is None:
        persistent.pow_cg_mjtogether = False
    if not hasattr(persistent, 'pow_cg_mjkiss') or persistent.pow_cg_mjkiss is None:
        persistent.pow_cg_mjkiss = False
    if not hasattr(persistent, 'pow_cg_mtrueending') or persistent.pow_cg_mtrueending is None:
        persistent.pow_cg_mtrueending = False
    if not hasattr(persistent, 'pow_cg_mrail') or persistent.pow_cg_mrail is None:
        persistent.pow_cg_mrail = False
    
    # Total CGs available
    persistent.pow_cg_required = 5
    
    # Function to count unlocked CGs
    def count_unlocked_cgs():
        count = 0
        if persistent.pow_cg_msit: count += 1
        if persistent.pow_cg_mjtogether: count += 1
        if persistent.pow_cg_mjkiss: count += 1
        if persistent.pow_cg_mtrueending: count += 1
        if persistent.pow_cg_mrail: count += 1
        return count
    
    # Update the count whenever we check
    def update_cg_count():
        persistent.pow_cg_count = count_unlocked_cgs()
        # Check if achievement should be unlocked
        if persistent.pow_cg_count >= persistent.pow_cg_required and not ach_is('all_cgs'):
            ach_unlock('all_cgs')

# Label to track Monika Sitting CG (m_cg_1a, 1b, 1c group)
label track_cg_msit:
    if not persistent.pow_cg_msit:
        $ persistent.pow_cg_msit = True
        $ update_cg_count()
        $ renpy.notify("CG Unlocked: Monika Sitting")
    return

# Label to track Monika & Jacko Together CG (mj_cg)
label track_cg_mjtogether:
    if not persistent.pow_cg_mjtogether:
        $ persistent.pow_cg_mjtogether = True
        $ update_cg_count()
        $ renpy.notify("CG Unlocked: Together at Last")
    return

# Label to track Monika & Jacko Kiss CG (mj_kiss_cg)
label track_cg_mjkiss:
    if not persistent.pow_cg_mjkiss:
        $ persistent.pow_cg_mjkiss = True
        $ update_cg_count()
        $ renpy.notify("CG Unlocked: First Kiss")
    return

# Label to track Monika True Ending CG (m_cg_trueending)
label track_cg_mtrueending:
    if not persistent.pow_cg_mtrueending:
        $ persistent.pow_cg_mtrueending = True
        $ update_cg_count()
        $ renpy.notify("CG Unlocked: True Ending")
    return

# Label to track Monika Railway CG (m_cg_rail_1a through 1f group)
label track_cg_mrail:
    if not persistent.pow_cg_mrail:
        $ persistent.pow_cg_mrail = True
        $ update_cg_count()
        $ renpy.notify("CG Unlocked: Railway Moment")
    return

# Legacy label for compatibility (redirects to new system)
label pow_track_cg:
    $ renpy.notify("Please use specific CG tracking labels: track_cg_msit, track_cg_mjtogether, track_cg_mjkiss, track_cg_mtrueending, or track_cg_mrail")
    return

# Label to unlock all CGs (for testing)
label pow_unlock_all_cgs:
    $ persistent.pow_cg_msit = True
    $ persistent.pow_cg_mjtogether = True
    $ persistent.pow_cg_mjkiss = True
    $ persistent.pow_cg_mtrueending = True
    $ persistent.pow_cg_mrail = True
    $ update_cg_count()
    $ ach_set('all_cgs', True)
    $ renpy.notify("All CGs have been unlocked!")
    return

# Label to reset all CGs (for testing)
label pow_reset_all_cgs:
    $ persistent.pow_cg_msit = False
    $ persistent.pow_cg_mjtogether = False
    $ persistent.pow_cg_mjkiss = False
    $ persistent.pow_cg_mtrueending = False
    $ persistent.pow_cg_mrail = False
    $ update_cg_count()
    $ ach_set('all_cgs', False)
    $ renpy.notify("All CGs have been reset!")
    return
