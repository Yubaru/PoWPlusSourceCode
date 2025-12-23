default persistent.debug_mode = False

label debug_menu:
    play music debug
    scene black
    "Welcome to the Debug Menu!"
    menu:
        "Please select a system to test:"
        
        "Page 1 Core Systems":
            jump debug_menu_page1
            
        "Page 2 Game Systems":
            jump debug_menu_page2
            
        "Reset All Persistent Data":
            menu:
                "Are you sure you want to reset ALL persistent data? This cannot be undone!"
                "Yes, reset everything":
                    $ persistent._clear()
                    "All persistent data has been reset. The game will now restart."
                    $ renpy.quit()
                "No, go back":
                    jump debug_menu
                    
        "Return to Main Menu":
            $ persistent.debug_mode = False
            return

label debug_menu_page1:
    menu:
        "Page 1 Core Systems:"
        
        "CG System":
            menu:
                "CG System Debug Options:"
                "Track New CG":
                    call track_cg_msit from _call_track_cg_msit_debug
                    "CG has been tracked."
                "Unlock All CGs":
                    call pow_unlock_all_cgs from _call_pow_unlock_all_cgs
                    "All CGs have been unlocked."
                "Reset CG Count":
                    call pow_reset_all_cgs from _call_pow_reset_all_cgs
                    "CG count has been reset."
                "Return":
                    jump debug_menu_page1
                    
        "Character Bio System":
            menu:
                "Character Bio Debug Options:"
                "Unlock Monika Bio":
                    $ CharacterBio.monika.unlock()
                    "Monika Bio has been unlocked."
                "Unlock All Characters":
                    $ CharacterBio.monika.unlock()
                    $ CharacterBio.natsuki.unlock()
                    $ CharacterBio.sayori.unlock()
                    $ CharacterBio.yuri.unlock()
                    $ CharacterBio.jacko.unlock()
                    $ CharacterBio.jacob.unlock()
                    $ CharacterBio.aiden.unlock()
                    $ CharacterBio.yazz.unlock()
                    "All characters unlocked."
                "Lock All Characters":
                    $ CharacterBio.monika.lock()
                    $ CharacterBio.natsuki.lock()
                    $ CharacterBio.sayori.lock()
                    $ CharacterBio.yuri.lock()
                    $ CharacterBio.jacko.lock()
                    $ CharacterBio.jacob.lock()
                    $ CharacterBio.aiden.lock()
                    $ CharacterBio.yazz.lock()
                    "All characters locked."
                "Return":
                    jump debug_menu_page1
                    
        "Inventory System":
            menu:
                "Inventory Debug Options:"
                "Add All Items":
                    call add_all_items from _call_add_all_items
                    "All items have been added to your inventory."
                "Add 1 Item":
                    call collect_item("literature_poster") from _call_collect_item_3
                    "1 item has been added to your inventory."
                "Remove All Items":
                    call remove_all_items from _call_remove_all_items
                    "All items have been removed from your inventory."
                "Prize Shop":
                    show screen prize_shop
                    "Prize shop has been opened."
                "Return":
                    jump debug_menu_page1
                    
        "Bio Tracking System":
            menu:
                "Bio Tracking Debug Options:"
                "Track New Bio":
                    call pow_track_bio from _call_pow_track_bio
                    "Bio has been tracked."
                "Unlock All Bios":
                    call pow_unlock_all_bios from _call_pow_unlock_all_bios
                    "All bios have been unlocked."
                "Reset Bio Count":
                    call pow_reset_bio_count from _call_pow_reset_bio_count
                    "Bio count has been reset."
                "Return":
                    jump debug_menu_page1
                    
        "Main Menu Art System":
            menu:
                "Main Menu Art Debug Options:"
                "Unlock All Main Menu Art":
                    call update_menu_art("gui/menu_art_mj_6.png") from _call_update_menu_art
                    $ ach_unlock('mj_art_6')
                    $ renpy.restart_interaction()
                    "All menu art has been unlocked."
                "Unlock Specific Menu Art":
                    menu:
                        "Select a menu art to unlock:"
                        "Menu Art 1":
                            call update_menu_art("gui/menu_art_mj_1.png") from _call_update_menu_art_1
                        "Menu Art 2":
                            call update_menu_art("gui/menu_art_mj_2.png") from _call_update_menu_art_2
                        "Menu Art 3":
                            call update_menu_art("gui/menu_art_mj_3.png") from _call_update_menu_art_3
                        "Menu Art 4":
                            call update_menu_art("gui/menu_art_mj_4.png") from _call_update_menu_art_4
                        "Menu Art 5":
                            call update_menu_art("gui/menu_art_mj_5.png") from _call_update_menu_art_5
                        "Menu Art 6":
                            call update_menu_art("gui/menu_art_mj_6.png") from _call_update_menu_art_6
                            $ ach_unlock('mj_art_6')
                            $ renpy.restart_interaction()
                        "Return":
                            jump debug_menu_page1
                "Increment MJ Art":
                    call update_mj_art from _call_update_mj_art_1
                    "MJ art has been updated by 1."
                "Return":
                    jump debug_menu_page1
                    
        "Back to Main Debug Menu":
            jump debug_menu

label debug_menu_page2:
    menu:
        "Page 2 Game Systems:"
        
        "Main Menu Star System":
            menu:
                "Star System Debug Options:"
                "Unlock All Stars":
                    python:
                        for _k in ("photo_album","all_cgs","all_bios","max_rizz","mj_art_6","beat_game"):
                            star_set(_k, True)
                        renpy.notify("All stars unlocked!")
                        renpy.restart_interaction()
                    "All stars have been unlocked."
                "Lock All Stars":
                    python:
                        for _k in ("photo_album","all_cgs","all_bios","max_rizz","mj_art_6","beat_game"):
                            star_set(_k, False)
                        renpy.notify("All stars locked.")
                        renpy.restart_interaction()
                    "All stars have been locked."
                "Check Stars Status":
                    $ debug_check_stars()
                    "Status notification shown."
                "Force Check Secret Video":
                    $ force_check_secret_video()
                    "Secret video status checked."
                "Return":
                    jump debug_menu_page2
                    
        "Photo Album System":
            menu:
                "Photo Album Debug Options:"
                "Unlock All Photos":
                    call unlock_all_photos from _call_unlock_all_photos
                    "All photos have been unlocked."
                "Remove All Photos":
                    call remove_all_photos from _call_remove_all_photos
                    "All photos have been removed."
                "Unlock Specific Photo":
                    $ number = renpy.input("Enter photo number:", length=3, allow="0123456789")
                    call unlock_photo(int(number)) from _call_unlock_photo_5
                    "Photo [number] has been unlocked."
                "Remove Specific Photo":
                    $ number = renpy.input("Enter photo number:", length=3, allow="0123456789")
                    call remove_photo(int(number)) from _call_remove_photo
                    "Photo [number] has been removed."
                "Return":
                    jump debug_menu_page2
                    
        "Games System":
            menu:
                "Games Debug Options:"
                "Ring Toss Game":
                    call ring_toss_game from _call_ring_toss_game
                "Shooting Gallery":
                    call shooting_gallery from _call_shooting_gallery
                "Meat Beat Mania":
                    call meat_beat_mania from _call_meat_beat_mania_1
                "Yazzinator Battle":
                    call battle_start from _call_battle_start
                "Return":
                    jump debug_menu_page2
                    
        "Rizz System":
            menu:
                "Rizz System Debug Options:"
                "Update Rizz Points":
                    $ points = renpy.input("Enter points change:", length=5, allow="-0123456789")
                    $ reason = renpy.input("Enter reason:", length=50)
                    call rizz_update(int(points), reason) from _call_rizz_update_3
                    "Rizz points updated by [points] for reason: [reason]"
                "Set Rizz Skill Directly":
                    call set_rizz_skill from _call_set_rizz_skill
                    "Rizz skill has been manually set."
                "Reset Rizz":
                    call reset_rizz from _call_reset_rizz
                    "Rizz points have been reset."
                "Return":
                    jump debug_menu_page2
                    
        "Back to Main Debug Menu":
            jump debug_menu
