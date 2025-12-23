# Initialize persistent variables for bio tracking
default persistent.bio_unlock_count = 0
# Achievements now tracked centrally via persistent.ach

init -1 python:
    # Ensure persistent variables are properly initialized
    if persistent.bio_unlock_count is None:
        persistent.bio_unlock_count = 0
    
    # legacy var kept for compatibility but not used by new system
    
    # Required number of bio unlocks for achievement
    BIO_UNLOCK_REQUIREMENT = 8
    
    def track_character_unlock(character_name=""):
        """
        Tracks unique bio unlocks and checks for achievement
        """
        # Ensure persistent variables are initialized
        if persistent.bio_unlock_count is None:
            persistent.bio_unlock_count = 0
        # legacy var kept for compatibility but not used by new system
        if persistent.unlocked_bios is None:
            persistent.unlocked_bios = set()
            
        # Only increment if this is a new bio
        if character_name and character_name not in persistent.unlocked_bios:
            persistent.unlocked_bios.add(character_name)
            persistent.bio_unlock_count = len(persistent.unlocked_bios)
            
            # Debug output
            renpy.notify("Unlocked {} bio ({}/{})".format(character_name, persistent.bio_unlock_count, BIO_UNLOCK_REQUIREMENT))
            
            # Award achievement if requirement met
            if persistent.bio_unlock_count >= BIO_UNLOCK_REQUIREMENT and not ach_is('all_bios'):
                ach_unlock('all_bios')
        elif character_name:
            # Already unlocked
            renpy.notify("{} bio already unlocked".format(character_name))
        else:
            # No character name provided - this is the old deprecated usage
            renpy.notify("Warning: track_character_unlock needs character name!")
    
    def get_bio_unlock_count():
        """
        Returns the current bio unlock count
        """
        return persistent.bio_unlock_count
    
    def reset_bio_tracking():
        """
        Resets all bio tracking progress
        """
        persistent.bio_unlock_count = 0
        ach_set('all_bios', False)
        renpy.notify("Bio tracking reset!")
    
    def debug_show_unlocked():
        """
        Shows current bio unlock progress
        """
        renpy.notify("Bio Progress: {}/{}".format(persistent.bio_unlock_count, BIO_UNLOCK_REQUIREMENT))
        renpy.notify("Achievement: {}".format("Unlocked" if ach_is('all_bios') else "Locked"))

# Labels for game use
label track_character_unlock(character_name=""):
    $ track_character_unlock(character_name)
    return

label reset_bio_tracking:
    $ reset_bio_tracking()
    return

label debug_bio_status:
    $ debug_show_unlocked()
    return

# Legacy labels for compatibility
label pow_track_bio:
    $ track_character_unlock()
    return

label pow_set_bio_requirement(number):
    # This label is now deprecated but kept for compatibility
    return

label pow_unlock_all_bios:
    $ persistent.bio_unlock_count = BIO_UNLOCK_REQUIREMENT
    $ ach_set('all_bios', True)
    $ renpy.notify("All character bios have been unlocked!")
    return

label pow_reset_bio_count:
    call reset_bio_tracking from _call_reset_bio_tracking
    return

# Initialize bio tracking set for unique unlocks
default persistent.unlocked_bios = set()

# Simple label to increment bio counter (DEPRECATED - should use track_character_unlock instead)
label bio_achievement:
    # Ensure persistent variables are initialized
    if persistent.bio_unlock_count is None:
        $ persistent.bio_unlock_count = 0
    # legacy var kept for compatibility but not used by new system
    if persistent.unlocked_bios is None:
        $ persistent.unlocked_bios = set()
        
    # WARNING: This label is deprecated and should not be used for bio tracking
    # It was causing duplicate counting. Use track_character_unlock instead.
    $ renpy.notify("Warning: bio_achievement is deprecated!")
    
    return

# Reset function for testing
label reset_bio_count:
    $ persistent.bio_unlock_count = 0
    $ ach_set('all_bios', False)
    $ renpy.notify("Bio count reset to 0")
    return

# Debug function to check progress
label check_bio_count:
    $ renpy.notify("Bio count: [persistent.bio_unlock_count]/8")
    return 