init -1 python in CharacterBio:
    from store import persistent

    # Characters dictionary
    charactersList = {}

    class BioCharacter:
        def __init__(self, name, bio, appear, logo=None, chibi=None, chibi_hover=None, images=[], unlocked=True):
            """
            name: The name of the character.
            bio: The description of the character. Use \n to make new lines.
            appear: The mods and/or games the character appears in. Use \n at the end of a game
                    to make a new line.
            logo: The logo displayed on the left.
            chibi: The chibis of the character. No worries if you don't have any!
            images: The images of the character. You can have multiple images for the character.
                    This is a list of paths to your character images.
            unlocked: Defines if the character is available or not in the screen. 
                    Default to True, meaning they will appear in the screen no matter the value
                    of 'persistent.display_all_characters'. You can always lock back a character
                    with '$ CharacterBio.X.lock()' where X is your BioCharacter variable.
            """
            
            if not name:
                raise ValueError("A name must be given to your character in the BioCharacter instance.")
            self.name = name

            if self.name not in persistent.bio_characters:
                persistent.bio_characters[self.name] = {
                    "unlocked": unlocked
                }

            self.bio = bio

            self.appear = appear

            for value in images:
                if not isinstance(value, str):
                    raise TypeError("All images in the images list of the character '{self.name}' must be of type 'str', not '{type(value)}'")
            self.images = images

            self.logo = logo

            self.chibi = chibi if chibi else (None, None) # (idle, hover)
            
            self.unlocked = persistent.bio_characters[self.name]['unlocked']

            # Adds the character to the list of BioCharacters available.
            charactersList[self.name] = self


        # You can unlock a character by doing "CharacterBio.X.unlock()" 
        # where X is the your character instance.
        def unlock(self):
            """
            This function unlocks a character, making it available to be seen in the bio screen.
            If it was already unlocked, does nothing.
            """
            global current_character
            global current_character_image_index
            
            was_already_unlocked = self.unlocked
            
            self.unlocked = True
            persistent.bio_characters[self.name]['unlocked'] = True
            
            if not persistent.display_all_characters and not was_already_unlocked:
                if not current_character.unlocked or all(not char.unlocked for char in charactersList.values() if char.name != self.name):
                    current_character = self
                    current_character_image_index = 0
            
            # Track character unlock for achievement (only if newly unlocked)
            if not was_already_unlocked:
                renpy.call("track_character_unlock", self.name)

        # You can lock back a character by doing "CharacterBio.X.lock()" 
        # where X is the your character instance.
        def lock(self):
            """
            This function locks a character, hiding it from the bio screen (unless 
            persistent.display_all_characters is set to True).
            If it was already locked, does nothing.

            This function is here mostly if you want to lock a character again in 
            your story for some reason.
            """
            global current_character
            global current_character_image_index
            
            is_current = (self.name == current_character.name)
            
            self.unlocked = False
            persistent.bio_characters[self.name]['unlocked'] = False
            
            if is_current and not persistent.display_all_characters:
                unlocked_characters = [char for char in charactersList.values() if char.unlocked]
                 
                if unlocked_characters:
                    current_character = unlocked_characters[0]
                    current_character_image_index = 0


# This is the code that will be used in the script to handle interactions in the bio screen.
init python in CharacterBio:

    current_character = None
    current_character_image_index = 0

    def get_character(name):
        """
        This function returns a BioCharacter instance using the key provided
        in the parameter.
        """
        for char in charactersList.keys():
            if char == name:
                return charactersList[char]
        return None


    def get_characters():
        """
        This function gets all the characters that will be displayed on screen, 
        depending on two things: 
            - If `persistent.display_all_characters` is True, will return every 
            BioCharacter that's been defined.
            - Otherwise, will only return the characters that are unlocked.
        
        Return a dictionary where the keys are the names of the characters and the
        values are their BioCharacter instances.
        """
        if persistent.display_all_characters:
            return charactersList.copy()
        else:
            new_dict = {k: v for k, v in charactersList.items() if v.unlocked}
            return new_dict


    def next_character(back=False):
        """
        This function displays the next (or previous) character in the list.
        If `back` is True, displays the previous one, if it exists, otherwise,
        displays the next one, if it exists.
        """
        global current_character
        global current_character_image_index

        # Create a new list from the keys based on persistent.display_all_characters
        if persistent.display_all_characters:
            all_keys = list(charactersList.keys())
        else:
            all_keys = [k for k, v in charactersList.items() if v.unlocked]
        
        # If no characters match the criteria, do nothing
        if not all_keys:
            return
        
        # If current_character is not in the list of available characters,
        # reset to the first character in the available list
        if current_character.name not in all_keys:
            current_character = charactersList[all_keys[0]]
            current_character_image_index = 0
            return
            
        # Get the index of the current character using its name as the key
        current_index = all_keys.index(current_character.name)

        # Get the next index of the next character
        next_index = current_index - 1 if back else current_index + 1

        #Handle wrapping around the list with cleaner logic
        if next_index < 0:
            next_index = len(all_keys) - 1
        elif next_index >= len(all_keys):
            next_index = 0

        current_character = charactersList[all_keys[next_index]]
        current_character_image_index = 0


    def next_character_image(back=False):
        """
        This function displays the next image (or previous image) of the current character on screen,
        if said image exists; otherwise doesn't do anything. When `back` is True,
        goes to the previous image, otherwise to the next one.
        """
        global current_character
        global current_character_image_index
        
        char = get_character(current_character.name)
        if not char or not char.images:
            return

        # Loops back to the last image in the list if the current index is 0
        # and the left arrow is clicked
        if back:
            current_character_image_index -= 1
            if current_character_image_index < 0:
                current_character_image_index = len(char.images) - 1

        # Loops back to the first image in the list if the current index is the last
        # of the list and the right arrow is clicked
        else:
            current_character_image_index += 1
            if current_character_image_index >= len(char.images):
                current_character_image_index = 0 


    def toggle_display_all_characters():
        """
        Toggle the display of all characters on the bio screen.
        Use it as follows: '$ CharacterBio.toggle_display_all_characters()'
        If persistent.display_all_characters is False, show only unlocked characters.
        If persistent.display_all_characters is True, show all characters, but unlocked
        characters are displayed with a black silhouette and empty information
        """
        global current_character
        persistent.display_all_characters = not persistent.display_all_characters

        # If we're now only showing unlocked characters, make sure current_character is unlocked
        if not persistent.display_all_characters:
            unlocked_characters = [char for char in charactersList.values() if char.unlocked]
            if unlocked_characters and not current_character.unlocked:
                current_character = unlocked_characters[0]
                current_character_image_index = 0


    def initialize_current_character():
        """
        Initialize the current_character based on display settings and unlocked status.
        - If display_all_characters is False, show the first unlocked character
        - If no characters are unlocked but display_all_characters is False, fall back to first character
        - If display_all_characters is True, simply show the first character
        """
        global current_character
        global current_character_image_index

        if not charactersList:
            return
        
        if not persistent.display_all_characters:
            unlocked_characters = [char for char in charactersList.values() if char.unlocked]
            if unlocked_characters:
                current_character = unlocked_characters[0]
            else:
                current_character = list(charactersList.values())[0]
        else:
            current_character = list(charactersList.values())[0]
        
        current_character_image_index = 0

# The animation when hovering a chibi. If you want the chibi to constantly jump
# when you hover them, just remove the # from the #repeat line!
transform chibi_hop:
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    easein_quad 0.12 yoffset -30
    easeout_quad 0.12 yoffset 0
    #repeat


screen bio_screen:
    tag menu
    add "menu_bg"

    if not CharacterBio.get_characters() and config.developer:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 15
            xcenter 0.5
            text "No Characters" style "character_name_title" 
            null height 5
            text "No characters have been defined yet." style "no_characters_defined_style"
            text "Go to 'character_bio_definitions.rpy' to add one!" style "no_characters_defined_style"
            null height 10
            text "This screen only displays when config.developer is set to True." size 20 style "no_characters_defined_style"

    elif not persistent.display_all_characters:
        if all(not char.unlocked for char in CharacterBio.get_characters().values()):
            vbox: # No characters unlocked yet
                xalign 0.5
                yalign 0.5
                spacing 15
                text "Character Biographies" style "character_name_title"
                null height 5
                text "Characters can't be seen at the moment and none have been unlocked yet." style "character_name_style"

        else:   

            vbox: # Character name, logo, and chibi
                xalign 0.1
                yalign 0.1
                spacing 15
                null height 5
                text CharacterBio.current_character.name style "character_name_title" xalign 0.5
                null height 5
                if CharacterBio.current_character.logo:
                    add CharacterBio.current_character.logo xalign 0.5 size(300, 300)

                null height 25
                if CharacterBio.current_character.chibi[0]:
                    imagebutton:
                        xalign 0.5
                        action NullAction()
                        idle CharacterBio.current_character.chibi[0]
                        if CharacterBio.current_character.chibi[1]:
                            hover CharacterBio.current_character.chibi[1]
                            at transform:
                                xalign 0.5
                                on hover:
                                    chibi_hop
                                on idle:
                                    easeout_quad .1 yoffset 0

            vbox:
                #Character sprite
                xalign 0.45 yalign 0.5
                add CharacterBio.current_character.images[CharacterBio.current_character_image_index] xalign 0.0 yalign 0.6 zoom 0.5

                hbox:
                    style_prefix "arrows"
                    xalign 0.5
                    yalign 0.97
                    spacing 20
                    vbox:     
                        hbox:
                            textbutton "<" action Function(CharacterBio.next_character, True)
                            text CharacterBio.current_character.name style "character_name_style"
                            textbutton ">" action Function(CharacterBio.next_character)
                        if len(CharacterBio.current_character.images) > 1:
                            hbox:
                                textbutton "<" action Function(CharacterBio.next_character_image, True)
                                text "Outfit" style "character_name_style"
                                textbutton ">" action Function(CharacterBio.next_character_image)

            null width 30

            frame:
                background "mod_assets/images/bio/bio_box.png"
                xalign 1
                yalign 0.4
                padding (790, 130, 160, 220)
                vbox:
                    xfill True
                    box_wrap True
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        text CharacterBio.current_character.bio size 22 justify True

            frame:
                background None
                xalign 1
                yalign 0.4
                padding (790, 455, 160, 10)
                vbox:
                    xfill True
                    box_wrap True
                    text CharacterBio.current_character.appear size 20 justify True

    else:
        python:
            logo_img = Transform(CharacterBio.current_character.logo, matrixcolor=BrightnessMatrix(-1)) \
                        if not CharacterBio.current_character.unlocked and CharacterBio.current_character.logo \
                        else CharacterBio.current_character.logo

            chibi_idle = Transform(CharacterBio.current_character.chibi[0], matrixcolor=BrightnessMatrix(-1)) \
                        if not CharacterBio.current_character.unlocked \
                        else CharacterBio.current_character.chibi[0]
            chibi_hover = Transform(CharacterBio.current_character.chibi[1], matrixcolor=BrightnessMatrix(-1)) \
                        if not CharacterBio.current_character.unlocked \
                        else CharacterBio.current_character.chibi[1]


        vbox: # Character name, logo, and chibi
            xalign 0.1
            yalign 0.1
            spacing 15
            null height 5
            text "[CharacterBio.current_character.name if CharacterBio.current_character.unlocked else '???']" style "character_name_title" xalign 0.5
            null height 5
            if logo_img:
                add logo_img xalign 0.5 size(300, 300)

            null height 25
            if chibi_idle:
                imagebutton:
                    xalign 0.5
                    action NullAction()
                    idle chibi_idle
                    if chibi_hover and CharacterBio.current_character.unlocked:
                        hover chibi_hover
                        at transform:
                            xalign 0.5
                            on hover:
                                chibi_hop
                            on idle:
                                easeout_quad .1 yoffset 0

        vbox:
            #Character sprite
            xalign 0.45 yalign 0.5
            if CharacterBio.current_character.unlocked:
                add CharacterBio.current_character.images[CharacterBio.current_character_image_index] xalign 0.0 yalign 0.6 zoom 0.5
            else: 
                add Transform(CharacterBio.current_character.images[CharacterBio.current_character_image_index], matrixcolor=BrightnessMatrix(-1)) xalign 0.0 yalign 0.6 zoom 0.5 


            hbox:
                style_prefix "arrows"
                xalign 0.5
                yalign 0.97
                spacing 20
                vbox:     
                    hbox:
                        textbutton "<" action Function(CharacterBio.next_character, True)
                        text "[CharacterBio.current_character.name if CharacterBio.current_character.unlocked else '???']" style "character_name_style"
                        textbutton ">" action Function(CharacterBio.next_character)
                    if len(CharacterBio.current_character.images) > 1 and CharacterBio.current_character.unlocked:
                        hbox:
                            textbutton "<" action Function(CharacterBio.next_character_image, True)
                            text "Outfit" style "character_name_style"
                            textbutton ">" action Function(CharacterBio.next_character_image)

        null width 30

        frame:
            background "mod_assets/bio_box.png"
            xalign 1
            yalign 0.4
            padding (790, 130, 160, 220)
            vbox:
                xfill True
                box_wrap True
                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    text [CharacterBio.current_character.bio if CharacterBio.current_character.unlocked else "This character hasn't been met yet. Keep playing to discover them!"] size 22 justify True

        frame:
            background None
            xalign 1
            yalign 0.4
            padding (790, 455, 160, 10)
            vbox:
                xfill True
                box_wrap True
                text "[CharacterBio.current_character.appear if CharacterBio.current_character.unlocked else '???']" size 20 justify True

            
    textbutton _("Return"):
        style "return_button"
        action [Return(), SetField(CharacterBio, "current_character_image_index", 0)]


style no_characters_defined_style:
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    xalign 0.5
    justify True

style character_name_style:
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    anchor(0, 0)

style character_name_title is character_name_style:
    size 45 
    xalign 0.5

style arrows_button is gui_button
style arrows_button_text is gui_button_text

style arrows_button:
    size_group "arrows"
    properties gui.button_properties("arrows_button")

style arrows_button_text:
    properties gui.button_text_properties("arrows_button")
    font "gui/font/RifficFree-Bold.ttf"
    color "#fff"
    outlines [(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)]
    hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]