# Set the mood
label natsuki_baking_help:
stop music fadeout 2.0
play music tt2 fadein 2.0

scene bg corridor_reverse
with dissolve_scene_full

"I check my watch for the fifth time in ten seconds."
"2:15 PM."
"I'm dead. I am actually, physically, metaphysically dead."

"The hallway stretches out before me, empty and echoing with the sound of my frantic footsteps."
"The faint scent of vanilla and sugar usually brings a sense of comfort, but today? Today it smells like judgment."

"I was supposed to be here twenty minutes ago."
"Twenty. Minutes."
"In Natsuki time, that's equivalent to three lifetimes and a prison sentence."

"I skid around the corner, nearly colliding with a janitor, and barrel toward the culinary room doors."
"I can already hear the noise from the hallway."
"It sounds less like a baking club and more like a construction site."

scene bg baking_comp
with wipeleft


"I burst through the doors and the wall of heat hits me instantly."
"The culinary room is unrecognizable."

"What is usually a quiet space for home ec classes has been transformed into a battlefield."
"Stoves are roaring, industrial mixers are whirring at maximum speed, and the air is a chaotic blend of cinnamon, yeast, melting chocolate, and burning sugar."

"Over twenty teams are packed into the long rows of stations for the 'Winter Festival Bake-Off.'"
"Banners hang from the ceiling: 'PRECISION', 'PASSION', 'PERFECTION'."
"The pressure is palpable. It feels heavy in my lungs."

"I start weaving through the crowd, dodging a student carrying a tray of boiling caramel."

"Student A" "Coming through! Hot sugar! Move it!"
"Student B" "Where is the whisk?! Who took the whisk?!"

"I duck under a tray of croissants and spot a familiar pink pigtail bobbing near the back of the room, station 14."
"Natsuki is standing there. She's not moving. She's staring at the empty counter space where I should have been."
"She looks like she's about to go to war."

"I approach slowly, like one approaches a sleeping tiger."
stop music fadeout 1.0
j "N-Natsuki?"

show natsuki 4b at t11 zorder 2
"She spins around. If looks could kill, there would be a crime scene outline on the floor right now."
play music natsuki_baking
n 4b "Where."
n 4b "Have."
n 4b "You."
n 4e "Been?!"

menu:
    "Tell the truth.":
        j "I was with Monika and I got lost on the way here."
        j "We we're in the music room before you texted me and I had to run all the way here."
        j "I'm sorry I'm late, I promise I'll make it up to you."
        n 1g "..."
        "Natsuki scans me up and down like i'm some kind of criminal."
        "She looks at me for a few seconds before she speaks again."
        n 1g "Fine. I'll let you off the hook this time."
        n 1g "But don't do it again."
        n 1g "We've got a lot of work to do and I'm not going to let you ruin it for me."
        n 1g "Now get to work."
        j "Yes, Natsuki."
    "Make a heroic excuse.":
        j "I... I was saving a cat! From a tree! It looked just like the one on your apron!"
        n 4e "..."
        n 4c "Do you think I'm stupid, Jacko?"
        j "Okay, fine. I was with Monika and I got lost on the way here."
        n "Jacko, why do you gotta lie? I obviously know you're not with Monika right now."
        n "Nevermind, just get to work."

scene black
with wipeleft_scene
scene bg baking_comp
with wipeleft_scene
show natsuki 4d at t11 zorder 2
n 4d "Ten minutes! We've lost ten minutes of prep time, Jacko!"
n 4b "Do you see that clock? It doesn't stop for paperwork errors!"
n 4e "The judges are already circling the room like sharks, and we haven't even started the base!"

"She points aggressively toward the front of the room."
"Three stern-looking teachers—the judges—are scribbling on clipboards, walking past a station where a soufflé has already collapsed."

j "I know, I'm sorry. Really. I ran all the way here."
j "But look, I came prepared."

"I reach into my bag and pull out a small, heavy package."

j "I got the extra-fine caster sugar you wanted. The imported stuff."

n 4c "..."
"Natsuki pauses. She looks at the sugar, then at me. Her expression softens by exactly 5 percent."

n 4c "The... the brand I texted you right?"
j "The exact one. Had to beat an old lady with a stick to get it."

n 1c "Fine. That buys you survival. But not forgiveness."
n 4b "If we lose to the 'Bread Bros' at station five because you were late, I'm never letting you live it down."

"I glance over at Station Five. Two guys who look like linebackers are kneading dough with terrifying aggression."
z "COME ON NIGGA WE GOTTA WIN THIS THING."
aiden "BEAT THAT FUCKING BREAD."
"The two of them are wearing matching black and white chef's hats and aprons."
"They look like they're ready to take on the world."

j "We aren't going to lose to them. They're making sourdough. We're making art."
j "We've got the best baker in school right here."

n 5c "D-Don't try to flatter your way out of this! Apron on! Hands scrubbed! Now!"

# ==================================================================================
# ACT 2: THE SCIENCE OF SIFTING
# ==================================================================================

"I scramble to the sink, scrubbing my hands until they're red."
"I run back to the station. Natsuki tosses an apron at me—it hits me square in the face."

j "Oof. Nice aim."
n 4a "Less talking, more tying."

"I struggle with the knot behind my back."
"Natsuki groans, grabs my shoulder, spins me around, and ties it in one sharp tug."

n 4c "Useless."

"She steps back, surveying our station. It's laid out with surgical precision."
"Bowls of varying sizes. Spatulas aligned by length. Ingredients measured in glass ramekins."

n 1g "Okay, Jacko. Listen closely because I am not repeating myself."
n 1g "We are making the 'Cat-tastic' Chocolate Specials."
n 1g "This is a sponge cake base, not a muffin base. Do you know the difference?"

menu:
    "Is it the amount of sugar?":
        n 2d "No! Well, yes, but mostly it's the air!"
        n 2c "Muffins are dense. Sponge cake is aerated."
    "Is it the mixing method?":
        n 1d "Exactly. You've actually been listening."
        n 1a "We need to incorporate air."
    "They taste the same?":
        n 4m "Get out. Get out of my kitchen right now."
        j "I'm kidding! It's the texture!"

n 1g "We need maximum aeration. That starts with the flour."
n 1g "I need you to sift this flour. Three times."

j "Three times? Natsuki, isn't that overkill? The bag says pre-sifted."

n 4e "The bag lies, Jacko. The bag sits on a shelf getting compressed for months."
n 4b "Judge Miller is the head judge today. He's a texture freak."
n 4b "If he finds a single dense crumb, a single pocket of unmixed flour, we're done. Disqualified. Exiled."
n 2y "Do you want to be exiled?"

j "Not particularly."

n 2y "Then sift! And keep it high! Let the flour fall through the air!"

"I grab the sieve and the bowl. I start tapping the side, letting the white powder rain down."

"Tap. Tap. Tap."

n 2b "Higher! You're not gardening, you're baking!"

"I raise the sieve higher. A cloud of flour dust drifts up."

j "Is it just me, or is it getting hot in here?"
n 4a "It's a kitchen, Jacko. If you can't stand the heat, go join the literature club."

"Despite her bite, I see a bead of sweat on her forehead. She's nervous."
"She's vibrating with nervous energy. She wants this trophy. Badly."

j "Hey."
n 1g "What?"
j "You're doing great. The setup is perfect."

"She doesn't look up from the butter she's cutting."

n 1u "Just... just keep sifting. Don't stop until I say so."

# ==================================================================================
# ACT 3: THE EGG CRACKING INCIDENT
# ==================================================================================

"After what feels like an eternity of sifting, Natsuki inspects the bowl."
"She runs a finger through the mountain of soft, white powder."

n 1d "Acceptable. Now, the wet ingredients."
n 1g "I'm creaming the butter and sugar. I need you to prep the eggs."
n 1g "Crack them into the separate glass bowl first. One at a time."

j "Why not just throw them in the mixer?"

n 1f "Because if you get a bad egg, or a shell, and you crack it directly into the batter, you ruin the whole batch."
n 1f "We don't have enough ingredients for a second batch. We have one shot."
hide natsuki

"No pressure. Just one shot at glory."

"I reach for the eggs. Natsuki has chosen the organic, free-range ones. They look expensive."
"I pick up the first one. My hands are shaking slightly from the adrenaline and the caffeine I had earlier."

"Okay, Jacko. Be the egg. You are one with the egg."



"I hit it against the rim of the glass bowl."
"The yolk plops in perfectly."
stop music fadeout 2.0
"But... a tiny, jagged shard of white shell falls in with it."

"I freeze."
"I stare at the shell."
"The shell stares at me."

"I look at Natsuki. She's busy whisking."
"Maybe I can get it out before she sees."

"I reach a finger toward the bowl."
"Suddenly, a hand grabs my wrist."
scene black
with dissolve_scene_full
scene bg natsuki_grab
with dissolve_scene_full
play sound crimson
pause 3.0
n 2f "Don't."

"I freeze again.."

j "H-how did you...?"
n 2f "I heard it. The crack was too crunchy. You shattered the shell, didn't you?"
scene bg baking_comp
with dissolve_scene_full

"She turns around slowly, setting down her whisk."
"She walks over, peers into the bowl, and sighs. A long, suffering sigh."

show natsuki 4c at t11 zorder 2
n 4c "Jacko. What am I going to do with you?"
j "I can get it! Just let me—"
n 2e "Move. You're going to chase it around with your clumsy fingers and break the yolk."

"She steps in front of me. She smells like strawberries and sugar."
"She takes one half of the eggshell I'm holding."
"With a surgical dip, she uses the shell to scoop out the fragment. It attracts the piece like a magnet."

n 4a "Surface tension. Use the shell to catch the shell."
play music natsuki_baking fadein 2.0
n 4a "Basic chemistry. Did you sleep through science class too?"

j "I might have napped a little."
n 1c "Breathe, Jacko. You're shaking. You're making me more nervous."
j "Right. Sorry. Deep breaths."
scene bg baking_comp
with dissolve_scene_full

# ==================================================================================
# ACT 4: THE RIVAL
# ==================================================================================

"We get back into a rhythm. Whisking, mixing, folding."
"The batter is coming together. It's a pale, creamy yellow."

"Suddenly, a shadow falls over our station."
"I look up to see a tall student leaning over from the neighboring station."
"It's Brad. The self proclaimed 'King of Mousse'."
"He's wearing a chef's hat that is frankly too tall for a high school competition."
play music brad

show brad at t22 zorder 2
show natsuki 4f at t21 zorder 2
"Brad" "Well, well, well. If it isn't the Cupcake Queen."
"Brad" "I see you finally got your assistant to show up."

"Natsuki doesn't even look up. She's aggressively folding vanilla extract into the mix."

n 1e "Focus on your own station, Brad. Your gelatin is setting too fast."

"Brad's smile falters for a second, glancing back at his bowl before recovering."

"Brad" "It's perfectly calculated, actually."
"Brad" "But really, Natsuki... Cupcakes? For the Winter Festival?"
"Brad" "Isn't that a bit... childish? Simple? For a grand prize competition?"
"Brad" "The judges are looking for sophistication. Layers. Complexity."

"Natsuki's knuckles turn white on the spatula handle."

n 4w "Complexity doesn't mean quality, Brad."
n 4w "You can hide a bad cake under seven layers of mousse, but a cupcake has nowhere to hide."
n 4w "It has to be perfect. Every bite."
n 1r "Besides, your 'Seven-Layer Tower' looks like it's leaning to the left. Hope you brought a spirit level."

"Brad" "We'll see who's leaning when the results come out. Enjoy your... snacks."

hide brad
show natsuki 4f at t11 zorder 2
"He struts away, bumping the edge of our table as he goes."

j "What a jerk."

"Natsuki lets out a sharp breath, her shoulders sagging slightly."

stop music fadeout 2.0
n 1u "He's right though. The judges usually go for the big, fancy cakes."
n 1u "Cupcakes are seen as... easy."

j "Hey."
"I nudge her arm."
j "These aren't just cupcakes. They're Natsuki Specials."
j "Remember what you told me? It's about putting personality into the food."
j "Brad has no personality. He's just mousse in a human suit."

n 3a "Mousse in a human suit... that's dumb."
n 3a "But... thanks."
n 2b "Okay! Enough pity party! Give me the cocoa powder! We need to make the chocolate swirl!"

# ==================================================================================
# ACT 5: THE COCOA DISASTER
# ==================================================================================
scene bg baking_comp
with dissolve_scene_full
play music natsuki_baking
"I grab the container of cocoa powder."
"I'm feeling pumped now. We're going to crush Brad. We're going to win this."

j "One high-grade Dutch cocoa, coming right up!"

"In my haste to be efficient, I pry the lid off a little too enthusiastically."
"The lid pops free."
"And with it, a pressurized puff of dark brown powder explodes into the air."



"Time seems to slow down."
"I watch the brown cloud drift through the air."
"I watch it settle gently, silently."
"Right onto Natsuki's face."

"She stands perfectly still."
"The tip of her nose is brown."
"Her left cheek has a dusting of chocolate."
"Her white kitten apron is now a Dalmatian."

j "Oh no..."
j "Natsuki, I—"
show natsuki 1p at t11 zorder 2
n 1p "..."
"She slowly opens her eyes. They are wide. Dangerous."
"She slowly reaches up, wipes a finger across her nose, and looks at the powder."
"She tastes it."

n 1f "It's..."
n 1k "It's good cocoa."

j "Are... are you going to kill me?"

n 1r "I'm thinking about it."
n 1r "But we don't have time for a murder trial."
n 2b "Clean it. Fast. If the judges see a mess at the station, they dock points for 'culinary hygiene'."

j "Right! On it!"

"I grab a damp cloth. I step closer to her."
"She tilts her head up, closing her eyes."

"I gently wipe the powder from her nose. Then her cheek."
"My hand is hovering inches from her face."
"Up close, I can count her eyelashes."
"She's... really cute when she's not yelling."

n 1o "You missed a spot."
j "Where?"
n 1n "Here."

"She takes the cloth from me and wipes her own chin."
"Her face is bright red, and I don't think it's from the heat of the oven."

n 5u "You're... you're getting it in my eye, you idiot."
j "Sorry! Just trying to be thorough!"
n 5u "Just... batter's ready! Liners in! Move it!"

# ==================================================================================
# ACT 6: THE WAITING GAME
# ==================================================================================

"We work in a frenzy to fill the liners."
"Scoop. Drop. Swirl. Repeat."
"Twenty-four perfect cupcakes slide into the oven."

"We set the timer."
"15 minutes."

"Natsuki leans back against the counter, sliding down until she's sitting on the floor."
"I slide down next to her."

"The chaos of the kitchen continues above us, but down here, hidden by the counter, it's a little pocket of peace."

n 1a "Now we wait."
j "The hardest part."

n 1u "Hey, Jacko?"
j "Yeah?"

n 1u "Do you think they'll like the 'Cat-tastic' theme?"
n 1u "I know it's a bit childish. Making ears out of chocolate and drawing whiskers..."

menu:
    "It's unique and bold.":
        j "It's not childish, Natsuki. It's bold."
        j "Everyone else is doing 'Elegant' or 'Professional.' We're doing 'Personality'."
        j "It stands out."
    "It's who you are.":
        j "It's you, Natsuki."
        j "And you're the best baker I know. If you like it, it's good."
    "Yeah, it's kinda childish.":
        j "I mean, yeah, it is."
        j "But who doesn't like cats? Even grumpy judges like cats."

n 4c "I guess."
n 4b "I just... I want to prove that cute things can be serious too."
n 4b "People always look at me and think 'small', 'cute', 'harmless'."
n 4w "They don't think I can do the hard stuff."
n 4w "I want to shove these cupcakes in their faces and make them admit I'm good."

j "We will. We're going to win."

"She looks at me, hugging her knees."

n 1u "Thanks for... you know. Showing up."
n 1u "Even if you were late."
n 1u "And almost blinded me with cocoa."
n 1u "And nearly ruined the eggs."

j "Okay, okay, I get it! I'm a flawed assistant!"
j "But we make a good team."

n 4c "Don't get mushy. We haven't won yet."

# ==================================================================================
# ACT 7: THE ART OF DECORATING
# ==================================================================================

scene bg baking_comp
with dissolve_scene_full
"The timer cuts through the noise like a gunshot."
show natsuki 2d at t11 zorder 2
n 2d "It's time! Oven mitts! Rack!"

"We pull them out."
"They are perfect."
"Domed tops. No cracks. A rich, dark color."
"The smell hits us—pure chocolate heaven."

n 1g "Okay, rapid cooling. Fan them. Gently!"

"We spend five agonizing minutes fanning the cupcakes with baking sheets."

n 1g "Frosting time. This is it. The make or break."
n 1g "I'll do the pink buttercream base. You do the chocolate ears."
n 1g "Remember the technique I showed you? Squeeze, lift, flick."

j "Squeeze, lift, flick. Got it."

"Natsuki works like a machine. Swirl, swirl, swirl. Perfect pink mounds."
"I follow behind with the chocolate piping bag."

"I do the first one."
"It looks like a sad donkey ear."

j "Ugh."
n 2f "Stop."

"Natsuki grabs my wrist."

n 2f "You're tense. Relax your wrist."
n 1n "Like this."

"She puts her hand over mine."
"Her hand is small, warm, and covered in a fine dusting of sugar."
"She guides my hand."

n 1n "Squeeze... lift... and flick."

"A perfect cat ear appears."

n 4a "See? Easy."
j "Yeah. Easy when you're helping."

n 5c "Just... keep doing that. We have three minutes left!"

# ==================================================================================
# ACT 8: THE JUDGMENT
# ==================================================================================

"We finish the last whisker just as the buzzer sounds."

"Head Judge" "HANDS UP! STEP AWAY FROM THE STATIONS!"

"The room falls silent."
"The only sound is heavy breathing and the ticking of the cooling ovens."

"The judges begin their rounds."
"They start at Station 1."
"They spit out a cookie."
"Ouch."

"They move to Station 5. The Bread Bros."
"Judge Miller pokes the sourdough."
"Judge Miller" "Dense. Overworked. A pity."
z "FUCK YOU AIDEN I THOUGHT YOU SAID KNEEDING THE BREAD WAS THE WAY TO WIN THIS THING."
aiden "FUCK THIS, THIS IS BULLSHIT."

"The Bread Bros look devastated."

"They move to Brad's station."
"His Seven-Layer Mousse Tower is... leaking."
"Judge Sato" "It's melting, son. Structure is key."
"Brad looks like he's going to cry."
"Brad" "I'm so sorry, Judge Sato. I'll fix it."
"Judge Sato" "You cannot fix this. You have failed."

"Finally, they arrive at Station 14."

n 1f "..."
"Natsuki stands at attention, back straight, chin up."
"I stand beside her, trying not to look terrified."

"One set of eyes peer through spectacles at our tray of cat cupcakes."
show ramsay at t21 zorder 2
show natsuki 1f at t22 zorder 2
"Judge Ramsay picks one up. He holds it to the light."

"Judge Ramsay" "Whimsical."

n 1g "..."
"Is that good? Is whimsical good?"

"He breaks it in half. He inspects the crumb."

"Judge Ramsay" "Hmm."

"He takes a bite."
"He chews. Once. Twice."
"He closes his eyes."

"The silence is deafening. I can hear Natsuki's heart beating. Or maybe it's mine."

"Judge Ramsay" "The crumb is... exceptionally light. Almost airy."

"Judge Ramsay takes a bite of the frosting."

"Judge Ramsay" "And the buttercream? Is that a hint of sea salt?"

n 1d "Yes, sir. To balance the richness of the Dutch cocoa and the sweetness of the sponge."
n 1d "It cuts the sugar so it's not cloying."

"Judge Ramsay leans in."
"Judge Ramsay" "And the design. It's... charming. It has character."

"The judges whisper to each other."
"They scribble notes."
"They nod."

"Judge Ramsay looks at Natsuki."
"Judge Ramsay" "Very interesting technique on the folding. Not many students get that right."

"They move on."

"Natsuki holds her breath until they're three stations away."

n 1u "..."
"Then she nearly collapses against my shoulder."

n 1u "They liked them. Jacko, they actually liked them!"
j "Liked them? Ramsay called them 'exceptional'! He hated everyone else's!"
n 1m "Oh my god. Oh my god."

# ==================================================================================
# ACT 9: VICTORY
# ==================================================================================
scene bg baking_comp
with dissolve_scene_full
"We wait for the final tally."
"The Head Judge stands at the podium."

show ramsay at t11 zorder 2
"Judge Ramsay" "It was a difficult decision. We saw a lot of ambition today."
"Judge Ramsay" "But ambition without execution is just a mess."
"Judge Ramsay" "One team showed us that perfect execution, combined with a unique personality, creates a true masterpiece."

"Judge Ramsay" "Third place... The Macaron Sisters."
"Judge Ramsay" "Second place... The Scone Squad."

"Natsuki squeezes my hand. Her grip is like a vice."

"Judge Ramsay" "And First Place... for the 'Chocolate Cat-tastics'..."
"Judge Ramsay" "Station 14! Jacko and Natsuki!"
hide ramsay
show natsuki 1z at t11 zorder 2
n 1z "..."
"Natsuki's jaw drops."
"She freezes."

j "Natsuki? We won."
n 1z "We... we won?"
j "WE WON!"

"I grab her in a hug before I can think about it."
"For a second, she stiffens."
"Then, she hugs me back. Tightly."

n 1y "We did it! We actually beat them!"

"She pulls away, her face beaming. For once, there's no 'tough girl' act."
"Just pure, unadulterated joy."

j "Go get your trophy, Champ."

"She runs up to the front to accept the Golden Whisk."
"Brad is clapping politely, but he looks like he swallowed a lemon."
"Brad" "Congratulations, Natsuki. You're a true nigger."

n 1z "What the fuck did you just say, Brad?"
"Brad" "I said congratulations, Natsuki. You're a true."
n 1z "I'm not a nigger, Brad. I'm a baker."
"Brad" "Yeah, a nigger baker. That's what you are."
n 1z "Fuck you, Brad."
"Brad" "Fuck you, Natsuki. You're a nigger."

"..."
j "What the fuck is wrong with you two?"
j "Anyways Natsuki I gotta get back to Monika shes been waiting for me."
n "Oh alright Jacko I'll see back in club room later I cant wait to celebrate!"
j "See ya later Natsuki and again congratulations!"
"I take my leave as I'm practicall dusted up with flour and cocoa powder."
scene bg corridor 
with wipeleft
j "Monika's gonna kill me..."
stop music fadeout 2.0
scene black
with dissolve_scene_full
jump after_music_baking