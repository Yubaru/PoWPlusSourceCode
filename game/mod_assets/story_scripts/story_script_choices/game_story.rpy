# Monika and Jacko's Game Booth Adventure

default ring_toss_played = False
default shooting_gallery_played = False
default whack_a_mole_played = False

default natsuki_scene_done = False

init python:
    if not persistent.has_played_games:
        persistent.has_played_games = False

label game_story:
scene bg school_outside
play music t3
"The sunlight hits the courtyard with a renewed warmth, a sharp contrast to the velvet darkness we just left behind. Monika is still holding my hand, her grip finally relaxing from the 'white-knuckle' tension of the haunted house."
show monika forward happ cm at t11
if haunted_house_done:
    j "You know... after surviving that, I think we deserve something a little more lighthearted. How about we head to the converted gym? The Gaming Club said they’ve turned it into a full-on arcade."
else:
    j "You know... how about we head to the converted gym? The Gaming Club said they’ve turned it into a full on arcade."
show monika forward curi om ldown
m "An arcade? Honestly, Jacko, my experience with games is usually limited to... well, let's just say I'm more of an analyst than a player. I'm not sure I'll be much competition."
show monika forward curi cm ldown
j "Oh, don't give me that. I saw how you handled that ring toss earlier. You’ve got the focus of a pro. I’ll show you the ropes, it’ll be fun."
show monika forward worr om rdown
m "You're sure? I'd hate for you to spend your whole festival afternoon explaining button layouts to a total novice."
show monika forward worr cm rdown
j "I'm positive. Besides, seeing you get competitive over a high score? That’s an experience I wouldn't miss for anything."
show monika forward sedu om lpoint
m "Competitive, huh? You really think you can handle me when I'm actually trying to win?"
show monika forward sedu cm lpoint
j "I'm counting on it. Let's see if those 'nerves of steel' have recovered yet."
show monika forward happ om rdown
m "Challenge accepted. Lead the way, Coach."
show monika forward happ cm rdown
stop music fadeout 2.0

scene bg arcade
with dissolve_scene_full
play music arcade_music
"The gym has been completely transformed. The basketball hoops are obscured by heavy black curtains."
"And the room is lit only by the neon glow of dozens of cabinets and projector screens. The air smells like ozone, popcorn, and the collective excitement of a hundred students."
show monika forward laug om at t11
m "Look at this place! It’s like stepping into a different dimension. I haven't seen this many flashing lights since... well, since the morning assembly."
show monika forward laug cm
j "It’s amazing what a few black-market power strips and a lot of passion can do. I usually just hang back and watch the pros, but today feels like a good day for some glory."
show monika forward sedu om lpoint
m "Glory? Is that what we're after? I thought we were here for the fun of the game."
show monika forward sedu cm lpoint
j "In an arcade, Monika, glory *is* the fun. You think you can take the top spot on that rhythm machine over there?"
show monika forward happ om rdown
m "Is that a dare? Because you know I can’t turn down a well-worded dare, Jacko."
show monika forward happ cm rdown

"The arcade is in full swing. Chiptune melodies overlap into a chaotic symphony of bleeps and bloops. Students dart between rows of machines, clutching plastic cups of tokens and oversized plush prizes. It’s a sensory overload in the best way possible."
show monika forward curi om lpoint
m "Okay, we need a strategy. If we want to win the 'big' prizes—like that giant penguin on the top shelf—we need to optimize our token usage. Should we go for the games that reward precision, or the ones that are just pure endurance?"
show monika forward curi cm ldown
j "My strategy is simpler: we follow the smell of the takoyaki stall at the far end. We play whatever is closest to the snacks. That way, if we lose, we can drown our sorrows in fried batter."
show monika forward laug om rdown
m "Ahaha! Spoken like a true scholar. 'Culinary consolation.' I like your thinking."
show monika forward laug cm rdown
"A group of younger students rushes past us, their laughter echoing off the high gym ceiling. One of them accidentally bumps into Monika, but she just laughs it off, steadying herself with a hand on my arm."
show monika forward happ om lpoint
m "It’s so... vibrant out here. Sometimes I get so wrapped up in being 'The President' and managing everyone else's festival experience that I forget how nice it is to just... exist as a student. To just be a part of the noise."
show monika forward happ cm ldown
j "Well, today, the Literature Club can survive for an hour without its leader. Right now, you're just Monika: the girl who's about to absolutely crush me at air hockey."
show monika forward pout om rdown
m "Air hockey? Oh, Jacko... you have no idea what you’ve just unleashed. I was captain of the air hockey table in middle school."
show monika forward pout cm rdown
j "Wait, really? I thought you were all about the debate team."
show monika forward sedu om lpoint
m "I can be persuasive with a mallet too. Prepare yourself, because I don't plan on going easy on you just because you found me in a haunted house."
show monika forward sedu cm ldown
j "Good. I wouldn't want it any other way."
"As we head toward the tables, the neon light catches the ribbon in her hair, and for a second, she looks completely at peace. The stress of the morning is gone, replaced by a sharp, playful glint in her eyes."
m "Let's go, Jacko. Let's make some memories that aren't written in a book."

# Game selection menu
jump game_selection_menu

scene bg arcade
with dissolve
play music arcade_music
"The gym has been completely transformed. The basketball hoops are obscured by heavy black curtains, and the room is lit only by the neon glow of dozens of cabinets and projector screens. The air smells like ozone, popcorn, and the collective excitement of a hundred students."
show monika forward laug om at t11
m "Look at this place! It’s like stepping into a different dimension. I haven't seen this many flashing lights since... well, since the morning assembly."
show monika forward laug cm
j "It’s amazing what a few black-market power strips and a lot of passion can do. I usually just hang back and watch the pros, but today feels like a good day for some glory."
show monika forward sedu om lpoint
m "Glory? Is that what we're after? I thought we were here for the fun of the game."
show monika forward sedu cm lpoint
j "In an arcade, Monika, glory is the fun. You think you can take the top spot on that rhythm machine over there?"
show monika forward happ om rdown
m "Is that a dare? Because you know I can’t turn down a well-worded dare, Jacko."
show monika forward happ cm rdown

"The arcade is in full swing. Chiptune melodies overlap into a chaotic symphony of bleeps and bloops. Students dart between rows of machines, clutching plastic cups of tokens and oversized plush prizes. It’s a sensory overload in the best way possible."
show monika forward curi om lpoint
m "Okay, we need a strategy. If we want to win the 'big' prizes—like that giant penguin on the top shelf—we need to optimize our token usage. Should we go for the games that reward precision, or the ones that are just pure endurance?"
show monika forward curi cm ldown
j "My strategy is simpler: we follow the smell of the takoyaki stall at the far end. We play whatever is closest to the snacks. That way, if we lose, we can drown our sorrows in fried batter."
show monika forward laug om rdown
m "Ahaha! Spoken like a true scholar. 'Culinary consolation.' I like your thinking."
show monika forward laug cm rdown
"A group of younger students rushes past us, their laughter echoing off the high gym ceiling. One of them accidentally bumps into Monika, but she just laughs it off, steadying herself with a hand on my arm."
show monika forward happ om lpoint
m "It’s so... vibrant out here. Sometimes I get so wrapped up in being 'The President' and managing everyone else's festival experience that I forget how nice it is to just... exist as a student. To just be a part of the noise."
show monika forward happ cm ldown
j "Well, today, the Literature Club can survive for an hour without its leader. Right now, you're just Monika: the girl who's about to absolutely crush me at air hockey."
show monika forward pout om rdown
m "Air hockey? Oh, Jacko... you have no idea what you’ve just unleashed. I was captain of the air hockey table in middle school."
show monika forward pout cm rdown
j "Wait, really? I thought you were all about the debate team."
show monika forward sedu om lpoint
m "I can be persuasive with a mallet too. Prepare yourself, because I don't plan on going easy on you just because you found me in a haunted house."
show monika forward sedu cm ldown
j "Good. I wouldn't want it any other way."
"As we head toward the tables, the neon light catches the ribbon in her hair, and for a second, she looks completely at peace. The stress of the morning is gone, replaced by a sharp, playful glint in her eyes."
m "Let's go, Jacko. Let's make some memories that aren't written in a book."

label game_selection_menu:
scene bg arcade
with dissolve
play music arcade_music
$ available_games = []
if not ring_toss_played:
    $ available_games.append(("Ring Toss", "ring_toss"))
if not shooting_gallery_played:
    $ available_games.append(("Shooting Gallery", "shooting_gallery"))
if not whack_a_mole_played:
    $ available_games.append(("Whack-a-Wisp", "whack_a_mole"))

$ available_games.append(("Prize Shop", "show_prize_shop"))
$ available_games.append(("I think I'm finished...", "finish_games"))

if len(available_games) == 2 and available_games[0][0] == "Prize Shop":
    jump after_games_played

show monika forward happ cm rhip ldown at t44
m "Look at all these options! What’s the first target on your list, Jacko? (We have [tickets] tickets to burn!)"
$ result = renpy.display_menu(available_games)

if result == "ring_toss":
    jump play_ring_toss
elif result == "shooting_gallery":
    jump play_shooting_gallery
elif result == "whack_a_mole":
    jump play_whack_a_mole
elif result == "show_prize_shop":
    call screen prize_shop
    jump game_selection_menu
elif result == "finish_games":
    show monika forward curi om at t11
    m "Wait, already? But the night is still young and my mallet hand is just getting warmed up!"
    show monika forward curi cm
    menu:
        "Yes, I'm sure":
            if not ring_toss_played and not shooting_gallery_played and not whack_a_mole_played and not persistent.has_played_games:
                show monika forward sad om at t11
                m "Oh... I see. I thought we were actually going to spend some time together."
                show monika forward sad cm
                "The disappointment in her voice is like a physical weight in your chest. She looks away, her shoulders slumping slightly."
                show monika forward rdown cry cm ce
                m "..."
                m forward dist om oe "I guess I'll just go back to the clubroom then. There’s always... more paperwork to do."
                show monika forward neut e2b b1b
                call rizz_update(points_change=-10) from _call_rizz_update_16
                "You feel like a total failure. Why would you even suggest coming here if you didn't want to play?"
                return
            else:
                $ persistent.has_played_games = True
                return
        "No, let's stay and play some more games":
            j "Actually, you're right. I can't leave until I've at least tried to beat your high score."
            show monika forward happ om
            m "That's the spirit! I promise to make your defeat as graceful as possible."
            show monika forward happ cm rhip
            jump game_selection_menu


label play_ring_toss:
show monika forward happ om lpoint at t11
m "Ring toss! The ultimate test of depth perception and sheer, unadulterated luck. Think you have the 'Presidential' touch, Jacko?"
show monika forward happ cm ldown
j "Luck? Please. This is all about the flick of the wrist. I’ve been practicing my arcs since kindergarten."
show monika forward sedu om rdown
m "Oh? Then let’s make it interesting. If I win, you have to buy the first round of festival snacks later. Savory, not sweet."
show monika forward sedu cm rdown
"We approach the booth. The attendant looks bored, but brightens up when he sees Monika's competitive grin."
attendant "Step right up! Three rings for a token. Aim for the gold bottles for the legendary tier!"
show monika forward laug om lpoint
m "Don't blink, Jacko. You might miss the master at work."
show monika forward laug cm ldown
j "I'll be watching for your 'technical errors.' Just try not to toss the ring into the next booth."
show monika forward sedu om rdown
m "Insolence! Watch and weep!"
show monika forward happ cm ldown at t44
call ring_toss_game from _call_ring_toss_game_1
$ ring_toss_played = True
show monika forward happ om lpoint at t11
m "Phew! My heart is actually racing. Who knew plastic rings could be so stressful?"
show monika forward happ cm ldown
j "I think I need a physical therapist for my pride. Those gold bottles are definitely rigged."
show monika forward laug om rdown
m "Rigged? Or are you just making excuses for the champion? I was aiming for the stars and I hit the bullseye!"
show monika forward laug cm rdown
"We share a laugh as we step away, Monika victoriously clutching a small, glowing trinket."
show monika forward happ om lpoint
m "Look at this! It’s tacky, it’s cheap, and I love it because I earned it."
show monika forward happ cm ldown
j "I’m already planning my comeback. This isn't over."
show monika forward sedu om rdown
m "I look forward to your inevitable defeat in the next round."

if not natsuki_scene_done:
    call natsuki_festival_scene from _call_natsuki_festival_scene
    $ natsuki_scene_done = True

jump game_selection_menu


label play_shooting_gallery:
show monika forward happ om lpoint at t11
m "The shooting gallery! This looks like it requires the kind of focus usually reserved for club elections. Ready to be my sharpshooter?"
show monika forward happ cm ldown
j "If I win this, I’m putting 'Professional Marksman' on my college applications."
show monika forward sedu om rdown
m "Let's raise the stakes. If you hit the moving target, I'll buy you that oversized stuffed bear. But if I win... you have to carry it for the rest of the night."
show monika forward sedu cm rdown
j "A giant bear? Deal. I’ll be the envy of the whole courtyard."
"The booth is crowded with the smell of cheap popcorn and ozone. The attendant hands us two heavy, realistic-looking light rifles."
attendant "Targets reset every ten seconds! Watch out for the ducks—they’re faster than they look!"
show monika forward laug om lpoint
m "Focus, Jacko. Imagine the target is a typo in a very important poem. Breathe... aim... fire."
show monika forward laug cm ldown
j "I'm focusing! I just hope my digital aim is better than my real-world coordination."
call shooting_gallery from _call_shooting_gallery_1
$ shooting_gallery_played = True
show monika forward happ om rdown at t11
m "Incredible! I didn't know you had such steady hands. You were like a machine out there."
show monika forward happ cm rdown
j "All those late-night sessions finally paid off. My eyes are still twitching, though."
show monika forward sedu om lpoint
m "Consider me impressed. I might have to hire you as my personal security detail."
show monika forward sedu cm ldown
"We both grin, the competitive fire between us finally cooling into a warm, shared triumph."
show monika forward laug om rdown
m "Seriously though, that moving duck target was moving at light speed. How did you even see it?"
show monika forward laug cm rdown
j "I didn't. I just felt the vibe and pulled the trigger."
show monika forward happ om lpoint
m "The 'vibe,' huh? I'll have to study that technique. Want to grab a quick soda before the next trial?"
show monika forward happ cm ldown
j "As long as it’s not an 'eating contest' soda. My stomach needs a break."
show monika forward sedu om rdown
m "No promises! I'm feeling quite peckish after all that 'sharpshooting.'"

scene bg arcade
with dissolve_scene_full
if not natsuki_scene_done:
    call natsuki_festival_scene from _call_natsuki_festival_scene_1
    $ natsuki_scene_done = True

jump game_selection_menu


label play_whack_a_mole:
show monika forward happ om lpoint at t11
m "Ooh, Whack-a-Wisp! I’ve been looking at this machine since we walked in. It looks so... cathartic."
show monika forward happ cm ldown
j "Cathartic? Monika, are you secretly harboring some repressed mallet-based aggression?"
show monika forward sedu om rdown
m "Only for the sake of the high score, I promise! Besides, look at their little glowing faces. They're practically asking for a friendly bop."
show monika forward sedu cm rdown
j "Friendly? You’re holding that mallet like a Viking warrior."
show monika forward laug om lpoint
m "The Viking President has a certain ring to it! Come on, let's see who can clear the most wisps before the timer runs out."
show monika forward laug cm ldown
j "I'll try to keep my fingers out of the splash zone. I like them attached."
show monika forward happ cm ldown at t44
call whack_a_mole from _call_whack_a_mole
$ whack_a_mole_played = True
show monika forward happ om rdown at t11
m "Haha! That was exhilarating! My arms feel like jelly, but my spirit is soaring."
show monika forward happ cm rdown
j "I think I broke a sweat. Who knew whacking plastic ghosts could be such a workout?"
show monika forward sedu om lpoint
m "At least the tickets are rolling in! We’re practically arcade royalty now."
show monika forward sedu cm ldown
"We both shake out our tired arms, laughing as we watch our ticket total climb on the screen."

if not natsuki_scene_done:
    call natsuki_festival_scene from _call_natsuki_festival_scene_2
    $ natsuki_scene_done = True

jump game_selection_menu


label natsuki_festival_scene:
play music arcade_music
"We’re just heading toward the prize counter when a familiar, sharp voice cuts through the chiptune noise."
show natsuki turned ff happ om at t21
show monika forward at t22
show natsuki turned ff happ cm
n "Well, look what the cat dragged in! You two look like you’ve been through a blender. Having fun without the club’s resident expert, I see?"
show natsuki turned ff happ cm
show monika forward happ om rhip
m "Natsuki! I was wondering when the noise levels would peak. I assume you’ve already conquered the baking stalls?"
show monika forward happ cm rhip
j "Let me guess, you’re only here because you ran out of snacks to judge."
show natsuki cross ff sedu om
n "Excuse you! I am a connoisseur of all festival activities. But yeah, the cupcakes were mediocre at best. I had to come here to see if anyone actually has any skill."
show natsuki cross ff sedu cm
show monika forward laug om rhip
m "Oh, so the 'Master of Games' has arrived to humble us?"
show monika forward laug cm rhip
show natsuki turned ff happ om
n "Please. I could beat your ring toss score while blindfolded and holding a tray of cookies. You guys look like you’re trying way too hard."
show natsuki turned ff happ cm
j "Is that a challenge, Natsuki? Because Monika has been on a bit of a winning streak."
show natsuki cross ff sedu om
n "A challenge? It’s only a challenge if there’s a possibility of me losing. Which, let’s be real, isn't happening."
show natsuki cross ff sedu cm
show monika forward sedu om rhip
m "Careful, Jacko. Natsuki’s competitive drive is basically its own weather system. It’s best to just watch from a distance."
show natsuki turned ff laug om
n "Watch and learn! Watch and weep!"
"Natsuki snatches a ring from a passing student (with a quick 'borrowing' look) and tosses it casually. It lands perfectly over the narrowest bottle neck in the booth."
show natsuki cross ff happ om
n "See? Pure talent. No 'vibe' required."
show natsuki cross ff happ cm
j "Okay, now you're just being a show-off. Do you have a manual for that?"
show monika forward happ om rhip
m "We should definitely team up. With Natsuki’s aim and my... analytical oversight, we’d own this gym."
show monika forward happ cm rhip
show natsuki turned ff sedu om
n "Teaming up, huh? I’ll consider it. But it’s going to cost you a very high-quality crepe from the stall outside. The one with the strawberries."
show natsuki turned ff sedu cm
j "I think we can manage a 'Consultant Fee' like that."
"The three of us spend the next twenty minutes drifting through the aisles, Natsuki critiquing everyone’s form while helping us 'accidentally' win a few extra tickets."
show natsuki cross ff happ om
n "Alright, I’m off. I hear the baking contest is about to announce the finalists, and I need to be there to make sure they didn't pick any losers."
show natsuki cross ff happ cm
show monika forward laug om rhip
m "Go get 'em, Natsuki. Don't be too hard on the judges!"
show monika forward laug cm rhip
j "Good luck! Try not to start a food fight!"
hide natsuki
show monika forward at t11
$ CharacterBio.natsuki.unlock()
call track_character_unlock("natsuki") from _call_track_character_unlock_6
"She gives us a sharp wave and disappears into the colorful crowd, leaving a trail of energy in her wake."
return

label after_games_played:
show monika forward happ om lpoint at t11
m "That was absolutely fantastic. I can't remember the last time I felt this... unburdened. No quotas, no schedules, just pure, digital chaos."
show monika forward happ cm ldown
j "We actually made a decent team. We might have a future in the professional arcade circuit."
show monika forward sedu om rdown
m "Oh, definitely. Next year, we’re coming back with a custom mallet and a dedicated fan club. No survivors."
show monika forward sedu cm rdown
j "I’ll start training tomorrow. But only if you promise to keep the Viking mallet at home for the first week."
show monika forward laug om lpoint
m "Haha! No promises, Jacko. A President has to keep people on their toes."
show monika forward laug cm ldown
"We both share a quiet laugh as we step back out into the main courtyard, the hanging lanterns casting a soft, amber glow over the stone paths."

show monika forward curi om rdown
m "You know, while we were in there... I realized something."
show monika forward curi cm rdown
j "That arcade games are designed to take all your money?"
show monika forward sedu om lpoint
m "Well, yes, but also... that I really value this. Just being 'Monika' for a few hours. No expectations, no scripts to follow... just me and you, and a few plastic ghosts."
show monika forward sedu cm ldown
j "I like 'just Monika' too. She’s pretty good at air hockey."
show monika forward happ om rdown
m "I’d like to do this more often. Not just the games, but... this. The 'us' without the 'club' attached to it."
show monika forward happ cm rdown
j "I think that can be arranged. We’ll have to find a local arcade that isn't inside a high school gym, though."
show monika forward laug om lpoint
m "We’ll make it happen. I’m very good at project management, remember?"
show monika forward laug cm ldown
j "How could I forget?"

show monika forward neut om lpoint
m "Hey, Jacko?"
show monika forward neut cm ldown
j "Yeah?"
show monika forward sedu om rdown
m "Thanks. For everything today. For dragging me into the haunted house, and for letting me beat you at Whack-a-Wisp."
show monika forward sedu cm rdown
j "Who said I let you win? I was trying my best!"
show monika forward happ om lpoint
m "Sure you were. But I appreciate the sentiment anyway."
show monika forward happ cm ldown
j "Anytime, Monika. Truly."
show monika forward sedu om rdown
m "So... about those snacks? I believe the 'winner' was promised a savory crepe?"
show monika forward sedu cm rdown
j "I thought it was a soda!"
show monika forward laug om lpoint
m "The rules have evolved! Come on, let's go find the most expensive one on the menu."
show monika forward laug cm ldown
"We head toward the main festival area together, our shadows stretching out across the courtyard, the festival lights making the whole world feel like a dream we aren't ready to wake up from."
scene black
with dissolve_scene_full
stop music fadeout 1.0
"The festival is reaching its peak. Would you like to continue toward the main stage, or head back to the arcade for one last round?"
menu:
    "Continue to the main festival area":
        return
    "Go back to the arcade":
        $ ring_toss_played = False
        $ shooting_gallery_played = False
        $ whack_a_mole_played = False
        jump game_selection_menu

    

# (Continue expanding with more festival vignettes, dialogue, and character moments until the file is at least 1000 lines)
# ...
