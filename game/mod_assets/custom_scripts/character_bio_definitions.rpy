# Character Bio Definitions
# This file is where you define your characters for the bio system.
# You can define as many characters as you want, following the example below.

# A dictionary containing the name of the character as key and the BioCharacter instance as a value.
default persistent.bio_characters = {}

# Use to show all characters, even locked ones.
# DO NOT CHANGE IT MANUALLY! To activate it, do '$ CharacterBio.toggle_display_all_characters()' in your script.
# If some characters are locked and this is True, they will appear with a black silhouette,
# chibi, will have '???' as name and the bio will be replaced (check the 
# 'character_bio_core.rpy' file for more details).
default persistent.display_all_characters = False

# For your information, CharacterBio is a namespace, so everything defined into it belongs to it,
# and you'll need to use 'CharacterBio' before any method or variable defined in it, e.g
# $ CharacterBio.toggle_display_all_characters() or '$ CharacterBio.yuri.unlock()'
init 1 python in CharacterBio:
    # Define your characters here! (Check the documentation of the BioCharacter 
    # class in character_bio_core.rpy)

    monika  = BioCharacter("Monika", "President of the Literature Club, Monika is best known for her stellar looks, superb athleticism, and being at the top of her class. Much like a book, though, there's a lot more to her than what's on the surface...\n\nHeight: 5'1'' / 160.02cm\nWeight: 125lbs / 56.7kg\nEye Color: Green\nEthnicity: Unknown", "Doki Doki Literature Club! (2017)\nDDLC Plus! (2021)\nParadise of Wacko! (2025)", "mod_assets/images/bio/bio_ddlc.png", ("gui/poemgame/m_sticker_1.png", "gui/poemgame/m_sticker_2.png"), images=["gui/menu_art_m.png", "gui/menu_art_m_casual.png"], unlocked=False)
    
    natsuki = BioCharacter("Natsuki", "An aficionado at all things baking and unhesitant to put you in your place, Natsuki brings equal amounts of sweet and sour to the table...not specifically for you, or anything. No calling her cute!\n\nHeight: 4'11'' / 149.86cm\nWeight: 92.5lbs / 42kg\nEye Color: Magenta\nEthnicity: Japan", "Doki Doki Literature Club! (2017)\nDDLC Plus! (2021)\nParadise of Wacko! (2025)", "mod_assets/images/bio/bio_ddlc.png", ("gui/poemgame/n_sticker_1.png", "gui/poemgame/n_sticker_2.png"), images=["gui/menu_art_n.png", "gui/menu_art_n_casual.png"], unlocked=False)
    
    sayori  = BioCharacter("Sayori", "A best friend to the very end! Sayori's trademark smiles and clumsy attitude never fail to lift the spirits of nearly anyone she meets. Don't be too fooled by it, though, for those who smile the widest tend to cry the hardest...\n\nHeight: 5'2'' / 157.48cm\nWeight: 119lbs / 54kg\nEye Color: Blue\nEthnicity: Japan", "Doki Doki Literature Club! (2017)\nDDLC Plus! (2021)\nParadise of Wacko! (2025)", "mod_assets/images/bio/bio_ddlc.png", ("gui/poemgame/s_sticker_1.png", "gui/poemgame/s_sticker_2.png"), images=["gui/menu_art_s.png", "gui/menu_art_s_casual.png"], unlocked=False)
    
    yuri    = BioCharacter("Yuri", "When she's not buried in the world of books, Yuri shyly brings an air of serenity to wherever she goes, sometimes accompanied by a hot cup of tea. Trust in her eyes goes a long way, so be sure to never break hers.\n\nHeight: 5'5'' / 165.1cm\nWeight: 130lbs / 59kg\nEye Color: Purple\nEthnicity: Japan", "Doki Doki Literature Club! (2017)\nDDLC Plus! (2021)\nParadise of Wacko! (2025)", "mod_assets/images/bio/bio_ddlc.png", ("gui/poemgame/y_sticker_1.png", "gui/poemgame/y_sticker_2.png"), images=["gui/menu_art_y.png", "gui/menu_art_y_casual.png"], unlocked=False)
    
    jacko   = BioCharacter("Jacko", "An avid gamer and a bit of a jokester, Jacko is the main character of the game. He is known for his love of video games and his laid back attitude. He often finds himself in humorous situations, especially when it comes to his interactions with his friends. \n\nHeight: ?'?'' / ???.??cm\nWeight: ???lbs / ???kg\nEye Color: ???\nEthnicity: ???", "Paradise of Wacko! (2025)", "mod_assets/images/bio/bio_pow.png", ("mod_assets/images/bio/j_bio_chibi_1.png", "mod_assets/images/bio/j_bio_chibi_2.png"), images=["mod_assets/images/bio/j_bio.png", "mod_assets/images/bio/j_bio_casual.png"], unlocked=False)  
    
    jacob   = BioCharacter("Jacob", "A friend of Jacko, Jacob loves to joke around and have fun. He is known for his sense of humor and his love for Roblox. One of the original members of the friend group, Jacob is always up for a good time.\n\nHeight: 5'8'' / 172.72cm\nWeight: 130lbs / 58.96kg\nEye Color: Black\nEthnicity: Asian", "Paradise of Wacko! (2025)\nI couldn't find good images for AI :(", "mod_assets/images/bio/bio_pow.png", ("mod_assets/images/bio/ja_bio_chibi_1.png", "mod_assets/images/bio/ja_bio_chibi_2.png"), images=["mod_assets/images/bio/ja_bio.png", "mod_assets/images/bio/ja_bio_casual.png"], unlocked=False)
    
    aiden   = BioCharacter("Aiden", "Ah, Aiden. The friend you'll always need. Aiden loves to game and hang out with his friends. One of the founding members of the Deez SMP and something of a rizz god in the friend group, If I didn't know any better, he could boil my abs. \n\nHeight: 6'0'' / 182.88cm\nWeight: 140lbs / 63.50kg\nEye Color: Brown\nEthnicity: Portuguese", "Paradise of Wacko! (2025)", "mod_assets/images/bio/bio_pow.png", ("mod_assets/images/bio/a_bio_chibi_1.png", "mod_assets/images/bio/a_bio_chibi_2.png"), images=["mod_assets/images/bio/a_bio.png", "mod_assets/images/bio/a_bio_casual.png"], unlocked=False)
    
    yazz    = BioCharacter("Yazz", "The brother of Yami and a kind soul, Yazz is a bit of a quiet one, unless he's talking to his friends then he becomes a true extrovert! He is known for being good at things he likes and is often seen with a emotionless expression...? He usually doesn't smile but when he does, it can make anyone happy. \n\nHeight: 5'7'' / 170.18cm\nWeight: 140lbs / 63.50kg\nEye Color: Dark Brown\nEthnicity: African American", "Paradise of Wacko! (2025)", "mod_assets/images/bio/bio_pow.png", ("mod_assets/images/bio/z_bio_chibi_1.png", "mod_assets/images/bio/z_bio_chibi_2.png"), images=["mod_assets/images/bio/z_bio.png", "mod_assets/images/bio/z_bio_casual.png"], unlocked=False)
    # Add your own characters here! Example below. If you want to make a new line in a string, 
    # use \n.
    # mc = BioCharacter("Character name", "Your custom biography text here...", "Game appearances...", "path/to/logo.png", ("path/to/chibi_idle.png", "path/to/chibi_hover.png"), images=["path/to/character_image.png"], unlocked=True)

    # TO UNLOCK OR LOCK A CHARACTER, USE THE FOLLOWING METHODS:
    # '$ CharacterBio.character_name.unlock()' where 'character_name' is your BioCharacter variable name
    # '$ CharacterBio.character_name.lock()' where 'character_name' is your BioCharacter variable name
    # Example: '$ CharacterBio.yuri.unlock()'

    # Initialize the current character after all characters are defined.
    # DO NOT REMOVE THIS LINE!!!
    initialize_current_character()