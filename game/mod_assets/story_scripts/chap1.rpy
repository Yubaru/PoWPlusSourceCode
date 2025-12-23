$ yazz_win = False
label chap1:
$ show_phone_in_quick_menu = False
"..."
# To be pushed to main repo $ renpy.movie_cutscene("mod_assets/cutscenes/chap1intro.webm")
scene white
pause 2.0
play music wefine
show screen chapter_display("The Jackoing' Start") with Dissolve(6.0)
hide screen chapter_display with Dissolve(3.0)
scene bg bedroom
with dissolve
"..."
j "Auggghhhhhhh... someone just end it already."
"The sun is stabbing me right in the retinas through the window. It's too bright for this level of consciousness."
j "Fine, I'm up. The world gets another day of me. Lucky them."
"I begrudgingly peel myself off the mattress like a used bandage and throw on some clothes that are hopefully more clean than they are wrinkled."
"As I scan the room, I’m hit with the realization that I live in a literal dumpster fire. This place is a disaster."
#$ send_phone_message("sayori_chat", "s", "Hey! Are you there?", conversation_label="sayori_conversation_1")
j "I really gotta clean this mess... eventually."
"I stand there in the middle of the mess, staring blankly at a pile of laundry and questioning my life choices."
j "Now where the hell should I even start..."
call bedroom_point_and_click
scene bg bedroom
with dissolve_scene_full
play sound "mod_assets/sfx/phone_message.ogg"
"I’m just about to escape to the kitchen when my pocket starts vibrating like a trapped hornet."
j "A phone call? Already?"
"Who has the audacity to be calling me at this ungodly hour?"
"I pull out my phone and hit answer, preparing to be annoyed."
call monika_conversation_call_1
"..."
j "Alright, alright. I gotta grab those posters from yesterday and haul ass to school."
"Honestly, Monika and I crushed these. We made them from scratch and they actually look like something a professional would make mostly thanks to her, but I did my part."
"I'm glad she actually asked for my help. Usually, I'm just the guy people ignore."
j "MAN SHES HOT AS FUCK."
j "They should be in here somewhere..."
"..."
j "Bingo. Found 'em."
call collect_item("literature_poster") from _call_collect_item
j "Alright, looks like I’m actually ready to face the world. God help us all."
"I grab my bag and march out the door."
scene bg kitchen
with wipeleft
j "I need food. My stomach is eating itself."
"I raid the fridge, but it's a wasteland of empty shelves and mystery jars."
j "Ah, the reliable classic. Good old fashioned ramen."
"I rip the packaging open with my teeth, skip the stove entirely, and dump the seasoning straight onto the dry brick."
"I take a massive, crunchy bite. It sounds like a car crash in my skull."
j "Yeah, that's right. I eat my fucking ramen raw."
j "Cause I'm a fucking raw ass nigga."
"Damn, that hit the spot. Pure sodium. Nothing beneficial about it."
"..."
"Suddenly, my pocket starts buzzing again. The world just won't leave me alone."
$ show_phone_in_quick_menu = True
j "Again?! Are you kidding me?"
"I stare at the phone, seriously considering throwing it out the window."
"But I guess I should check it before I do something I regret."
call show_hint("Hey look at that! There's a new message from someone on your phone! You only have 10 seconds to answer so be quick!")
$ send_phone_message("sayori_chat", "s", "Hey! Are you up yet?", conversation_label="sayori_conversation_1")
"..."
"..."
"..."
if walk_with_sayori:
    j "I guess I'll just walk with Sayori today, what could go wrong?"
    call chap1_walk_with_sayori
else:
    call show_hint("Oops")
    "I crunch down the last of the dry noodles and head out into the morning."
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    scene bg park2
    with wipeleft_scene
    pause 1.5
    scene bg courtyard
    with wipeleft_scene
    play music t3
    stop music fadeout 2.0
    pause 1.5










if walk_with_sayori:
    scene bg corridor 
    with dissolve_scene_full
    "I'm pretty late for the festival, this isn't looking good..."
    "I can see people leaving the club room as I'm heading towards it."
    "I hasten my pace and walk into the club room."
    scene bg club_festival
    with wipeleft
    "..."
    j "Hey. Sorry for the delay. I was just walking with Sayori."
    m "Oh. hey Jacko. I was just about to send someone to find you."
    m "You're really late for the festival. We're already running behind schedule."
    m "I just wish you would have told me you were walking with Sayori."
    j "S-sorry Monika..."
    m "It's fine, Jacko. Just make sure you're here on time next time."
    j "I'll try my best, Monika."
    m "Good. Now, let's get to the festival."
    "Monika looks at you with a disappointed face."
    call rizz_update(points_change=-8)
    jump chap1_mid
scene bg corridor
with dissolve_scene_full
play music t3

"I can hear the chaos before I even reach the door. It sounds like a baking competition is merging with a civil war."
n "Ugh, Yuri, can you move that table a little to the left? It's blocking the cupcake flow!"
y "My apologies, Natsuki. I didn't realize it would interfere with your... aesthetic geometry."
m "It's fine, Yuri. Natsuki's just being extra protective of her display. The table is fine where it is."
n "Extra protective?! Excuse me, Monika, but these cupcakes are the main attraction! People aren't coming for the 'deep literature,' they're coming for the frosting!"
"I push the door open, my hands still trembling slightly from the Nuclear Battery coursing through my veins."
scene bg club_day with wipeleft
show monika forward lpoint rhip happ om oe at t11
m "Oh, there you are... Jacko! I was starting to think the crowds had swallowed you whole."
$ CharacterBio.monika.unlock()
call track_character_unlock("monika") from _call_track_character_unlock_1
show monika forward lpoint rhip happ cm oe at t11
play sound cheer
window hide(None)
window auto
show splash_monika_1
show splash_monika_background
show splash_monika_2
pause
stop sound
hide splash_monika_1
hide splash_monika_background
hide splash_monika_2
show monika forward lpoint rhip happ cm oe at t11
j "Hey. Sorry for the delay. Navigating the hallway was like trying to survive a riot."
$ CharacterBio.jacko.unlock()
call track_character_unlock("jacko") from _call_track_character_unlock_2
show monika forward lpoint rhip happ cm oe at t22
show natsuki turned lhip rdown neut om oe at t21
n "About time! Did you bring the goods or what?"
hide monika
show natsuki turned lhip rdown neut cm oe at t11
play sound uncheer
window hide(None)
window auto
show splash_natsuki_1
show splash_natsuki_background
show splash_natsuki_2
pause
stop sound
hide splash_natsuki_1
hide splash_natsuki_background
hide splash_natsuki_2
"I hold up the poster tube like it’s a holy relic. Natsuki snatches a poster out before I can even unsnap the cap."
hide monika
show natsuki turned lhip rdown happ om oe at t11
n "Let’s see if you actually listened to my feedback..."
show natsuki turned lhip rdown happ cm oe at t11
"Natsuki inspects the posters like she's a diamond appraiser looking for flaws."
n 5t "Huh. Not bad. I guess you're good for something besides staring at the walls."
show natsuki turned lhip rdown happ om oe at t21
show yuri turned ldown rdown neut om oe at t22
y "They look very professional, Jacko. The choice of composition is truly striking."
hide natsuki
show yuri turned ldown rdown neut cm oe at t11
play sound uncheer
window hide(None)
window auto
show splash_yuri_1
show splash_yuri_background
show splash_yuri_2
pause
stop sound
hide splash_yuri_1
hide splash_yuri_background
hide splash_yuri_2
show yuri turned ldown rdown neut cm oe at t32
show natsuki turned lhip rdown happ om oe at t31
show monika forward lpoint rhip happ om oe at t33
m "See? I told you he'd come through for us."
hide yuri
hide natsuki
show monika forward lpoint rhip happ cm oe at t11
"Monika beams at me. For a second, the crushing exhaustion of staying up all night vanishes, replaced by a weird, fluttering heat in my chest."
m forward happ om oe "Thanks again, Jacko. Truly. I don't think I could have handled the design aspect while juggling all the logistics."
show monika forward lpoint rhip happ cm oe at t11
j "It was fine. Honestly, I had fun with it. It’s better than staring at a blank notebook."
"The posters are sleek and inviting. 'Welcome to The Literature Club!' is written in a cutesy font across the top. It feels very..."
"Moe."
"I mean, considering the target audience, going for that 'Moe' aesthetic was the move. People love a cute face more than a deep poem."
m forward happ om oe "You've got a killer eye for detail!"
m forward happ om oe "The way you adjusted the header spacing makes it so much more readable. Most people would have just left it cluttered."
show monika forward lpoint rhip happ cm oe at t11
j "First impressions are everything, right? If the poster looks like trash, they’ll think our poems are trash too."
show monika forward lpoint rhip happ cm oe at t11
m forward happ om oe "Exactly. You're a natural, Jacko. Don't let anyone tell you otherwise."
show monika forward lpoint rhip happ cm oe at t11
show monika forward lpoint rhip happ cm oe at t22
show natsuki turned lhip rdown anno om oe at t21
n "Ugh, can we cut the 'artist mutual admiration society' crap? We've got a booth to build!"
show monika forward anno om oe at t22
show natsuki turned lhip rdown anno cm oe at t21
m forward anno om oe "Relax, Natsuki. I'm just acknowledging hard work."
show monika forward anno cm oe at t22
show natsuki turned lhip rdown pout om oe at t21
n "Whatever! The cupcakes are the main attraction! They should be the first thing people see when they walk in!"
"Monika looks slightly embarrassed, or maybe just exhausted by Natsuki's energy. I know the feeling."
show monika forward anno om oe at t33
show natsuki turned lhip rdown happ om oe at t31
show yuri turned ldown rdown neut om oe at t11
y "I have to agree with Monika, despite Natsuki's... enthusiasm. The posters are impressive. Did you use a specific software, or was this hand-rendered?"
show yuri turned ldown rdown neut cm oe
j "A bit of both. Digitized the sketches and then tweaked the vectors until they looked right."
y turned ldown rdown neut om oe "Fascinating. Graphic design has a certain mathematical beauty to it. Perhaps you could show me your process later?"
show yuri turned ldown rdown neut cm oe
n turned ldown rdown anno om oe "Oh, great. Now Yuri's joining the fan club. Can we please focus on the actual festival?"
show natsuki turned ldown rdown anno cm oe
y shy ldown rdown neut om oe "Hmph. I was merely being inquisitive."
hide yuri
"Yuri scoffs softly and drifts back toward the banners, looking a bit miffed."
show monika forward neut om oe at t22
show natsuki turned ldown rdown happ om oe at t21
m forward neut om oe "Alright, team, focus. Jacko, since you're the visual expert, do you mind helping Natsuki with the cupcake display? She needs another pair of hands."
hide monika
n 4e "Wait, what? I don't need help! I've got a system!"
show natsuki turned ldown rdown happ om oe at t11
j "Are you sure? I promise I won't eat any... unless they're falling."
n 5w "Ugh, fine. But don't touch anything unless I give you the green light!"
show natsuki 5r
"Natsuki leads me over to the table. It’s a mountain of sugar and pastel frosting."
n 5s "Okay, here's the deal. Monika wants it to look 'aesthetically pleasing.' I was thinking a color gradient from light pink to dark red. Or maybe a spiral. I can't decide which looks more 'pro'."
show natsuki 5g
j "What if we do a gradient but spread them across the desks? Put a poster and a cupcake at every station. It draws people into the room instead of just clustering them at the door."
n turned doub om oe "Huh... that’s actually not a terrible idea. It’ll be a pain to set up, though."
show natsuki turned ldown rdown neut cm oe
j "We’ve got time. And I’ve got enough caffeine in me to power a small city. Let’s do it."
show natsuki 2a
"Together, we start the painstaking process of arranging the cupcakes across the desks, matching them with the informational flyers."
n 4b "No, no! The frosting peak has to face the door! Pay attention!"
show natsuki 5a
"It’s tedious work, but with Natsuki barking orders and me executing them, it actually starts looking high-end."
n 2l "Okay... okay... that actually looks pretty good. But it needs a little 'pop', you know?"
show natsuki turned neut cm oe
j "What about those tea candles Yuri brought? We could place them opposite the cupcakes to balance the light."
n 1d "Wait, that’s actually smart. For once, you're being useful."
show natsuki 1a
scene black
with wipeleft
"Despite her constant grumbling, Natsuki seems genuinely satisfied. We spend the next twenty minutes placing the candles and finishing the table layout."
hide natsuki
y "Natsuki! Jacko! If you’ve finished your confections, I could use assistance with the main banner."
n "Yeah, yeah! We're coming! Keep your bookmarks on!"
"..."
"The three of us spend the next hour wrestling with heavy fabric and masking tape. We hang the banners high, ensuring they're visible the moment someone walks in."
"..."
"Time blurs into a haze of tape, salt, and the smell of vanilla."
stop music fadeout 2.0
scene bg club_festival with dissolve_scene_full
play music tt1
show natsuki turned ldown rdown happ om oe at t11
n "There! Look at that. It’s a masterpiece. I guess you're not a total disaster after all, Jacko."
show natsuki turned ldown rdown happ cm oe
j "I'll take that as a glowing review."
n cross laug om ce "Don't get cocky. It’s still 90%% my vision. You were just the muscle."
show natsuki cross happ cm oe at t21
show yuri turned happ om oe at t22
y "It is truly magnificent. Our collective efforts are bound to be well-received."
show yuri turned happ cm oe
"Monika walks over, surveying the room. Her eyes wide with genuine surprise."
show natsuki turned ldown rdown happ cm oe at t31
show yuri turned happ cm oe at t33
show monika forward vsur om oe at t11
m "Wow... you three did a spectacular job! The room feels so alive!"
show monika forward neut cm oe
n 4d "Duh. I didn't spend three days baking for it to look 'okay'."
show yuri turned neut cm oe
y turned neut om oe "The atmosphere is indeed quite inviting, Natsuki."
show yuri turned neut cm oe
m forward happ om oe "The festival starts in five minutes. Let's get into our positions!"
n rhip turned happ om ce "Let's show them what a real club looks like!"
hide yuri
hide monika
hide natsuki
"The door swings open, and the first wave of guests pours in. The room immediately hums with chatter and the sound of people being pleasantly surprised by the 'visual designer's' work."
show monika forward lpoint rhip happ om oe at t11
m "Alright, everyone! Let's give them a festival they'll never forget!"
scene black
with wipeleft
"The festival is a blur. The cupcakes disappear faster than Natsuki can plate them. The posters I spent all night on are being picked up and read by everyone."
"Monika is in her element, gracefully handling every guest. Yuri is tucked into a corner, sharing her bookmarks and talking softly about her favorite novels."
scene bg club_festival with wipeleft
j "Looks like the plan actually worked. Who knew?"
show natsuki 5w at t11
n "Yeah, and I'm exhausted. No thanks to your slow hands."
show natsuki 5x
j "Hey, those 'slow hands' made sure your cupcakes didn't fall."
n 2t "Ehehe... whatever. You actually helped a lot. Just... don't go telling anyone I said that. I have a reputation."
j "Your secret is locked in the vault, Natsuki."
show natsuki lhip rhip turned neut cm oe
"The door bursts open again, and a very familiar, very energetic figure barrels in with a tray."
show natsuki 5i at t22
show sayori turned happ om oe at l41
s "I'm here! I'm here! I brought reinforcements!"
show sayori turned happ cm oe at t11
hide natsuki
hide monika
play sound uncheer
window hide(None)
window auto
show splash_sayori_1
show splash_sayori_background
show splash_sayori_2
pause
stop sound
hide splash_sayori_1
hide splash_sayori_background
hide splash_sayori_2
show sayori turned happ cm oe at t31
show monika forward lpoint rhip happ om oe at t11
show natsuki 5i at t33
m forward happ om oe "Sayori! You made it! The timing is perfect, we just ran out of chocolates!"
show monika forward lpoint rhip happ cm oe
s turned happ om oe "I knew it! That's why I made these! Come on, Jacko, try one of the 'Sayori Specials'!"
show sayori turned happ cm oe at t11
show monika forward lpoint rhip happ cm oe at t31
"Sayori shoves a chocolate into my mouth. It's rich, creamy, and actually tastes like it was made with love, rather than spite."
show sayori turned happ cm oe
j "Holy... this is actually incredible. You made these?"
s turned happ om oe "I stayed up all night too! We're like the 'No-Sleep Squad'!"
show sayori turned happ cm oe
n 2q "Excuse me? I also stayed up! And my cupcakes are still the main event!"
show natsuki 2s
s turned happ om oe "Of course they are, Natsuki! Your cupcakes are the talk of the school!"
show sayori turned happ cm oe
n 5t "Damn right they are."
hide sayori
hide natsuki
hide monika
"The room stays packed for the rest of the afternoon. People are actually interested in literature, or at least in the community we've built here."
show sayori turned happ om oe at t11
s "Jacko! Don't let Natsuki eat all the leftovers! Grab a cupcake!"
show sayori turned happ cm oe
j "I'm coming, I'm coming!"
show sayori turned happ cm oe
"As I look around the room at everyone laughing and talking, the exhaustion finally starts to feel worth it. It’s more than just a club. It’s... something else."
hide sayori
"Yuri walks over, clutching a small stack of leather-bound books."
show yuri turned happ om oe at t11
y "I've decided to donate these to the school library in the club's name. It feels right to share the joy of reading."
show yuri turned happ cm oe
j "That's a class act, Yuri. They're lucky to have 'em."
y turned neut om oe "It’s the least I can do. Thank you for making the room look so... inviting for them."
hide yuri
"The sun starts to set, casting long, golden shadows across the clubroom floor. The crowd thins out, leaving just us."
show natsuki rhip lhip turned neut om oe at t11
n "Hey, Jacko! Help me box up these last few cupcakes! We’re celebrating!"
show natsuki rhip lhip turned neut cm oe
j "On it. Lead the way, Boss."
"I help Natsuki pack up the remaining treats. She’s still acting tough, but the way she’s smiling tells the real story."
n turned happ om oe "You were actually useful today. Don't make me repeat it."
show natsuki turned happ cm oe
j "Understood. My lips are sealed."
hide natsuki
"Sayori bounces over, her box empty and her face covered in a small smudge of chocolate."
show sayori turned happ om oe at t11
s "That was the best day ever! Everyone was so happy!"
show sayori turned happ cm oe at t22
show monika forward lpoint rhip happ om oe at t21
m "It really was, Sayori. Thank you for your hard work."
hide sayori
show monika forward lpoint rhip happ cm oe at t11
"Monika watches the last few students leave, her expression glowing with a quiet, fierce pride."
j "We actually did it, huh?"
m lean happ om ce "We did. And we're glad you're a part of it, Jacko. You've become more important to this club than you realize."
show monika lean happ cm ce
"Sayori grins and throws a heavy arm around my shoulder, nearly knocking the wind out of me."
show monika forward lpoint rhip happ cm oe at t21
show sayori turned happ om oe at t22
s "Yeah! You're stuck with us now, visual designer!"
show sayori turned happ cm oe at t33
show monika forward lpoint rhip happ cm oe at t31
show natsuki cross laug om ce at t32
n "Just don't think this means you're off the hook for next week's cleanup!"
show monika forward lpoint rhip happ cm oe at t41
show sayori turned happ cm oe at t44
show yuri turned happ om oe at t42
show natsuki turned happ cm oe at t43
y "I believe Jacko has earned a brief reprieve. He was quite the asset today."
show yuri turned happ cm oe
"Yuri's quiet compliment is the final blow to my cynical armor. I actually feel like I belong here."
show yuri turned happ cm oe
j "Thanks, Yuri. That means a lot. Truly."
"Monika claps her hands, her voice ringing out through the quiet room."
hide sayori
hide natsuki
hide yuri
show monika forward lpoint rhip happ om oe at t11
m "Alright, everyone! Let’s tidy up and then it’s time for our celebratory dinner! We’ve earned it!"
show monika forward lpoint rhip happ cm oe at t11
"The club cheers. As I pick up the empty trays and tape scraps, I find myself actually looking forward to Monday."
show monika forward lpoint rhip happ cm ce at t11
m "This is exactly what I envisioned. A place for everyone... together."
"Monika pauses, her gaze lingering on the empty seats for just a second too long."
m forward nerv om oe "'This almost feels like a dream... I hope it never ends.'"

menu:
    "It's really fun being here with everyone... especially you.":
        j "I gotta admit... it's actually been fun. Being here with everyone... but especially with you, Monika."
        "The caffeine makes the words come out bolder than I intended. My heart is thudding against my ribs like a trapped bird."
        m forward flus blus om "You... you really think so, Jacko? That’s incredibly sweet of you to say..."
        show monika lean happ blus e2
        "She looks away shyly, her cheeks flushing a deeper shade of pink. It’s a good look on her. A dangerous look."
        m forward happ blus om ce "You've been such a cornerstone for this club, Jacko. I'm... I'm really grateful you're here."
        m forward rhip happ blus e1b "But we should probably focus on cleaning up before we get too... distracted, right?"
        j "Right. Duty calls. I'll be over by the supply closet if you need me to carry something heavy."
        call rizz_update(points_change=+2) from _call_rizz_update_5
        show monika lean happ blus cm ce
        "Monika gives me one last lingering smile before turning to help Yuri. My pulse is still racing, and I don't think it's just the Nuclear Battery."
        hide monika
        "Seeing her smile like that makes my world feel a lot less grey."
        j "God, I'm practically vibrating. I need to settle down before I vibrate through the floor."
        stop music
        "..."
        "..."
        "..."
        "Focus, Jacko. Focus."
        jump chap1_mid

    "Monika! I think some people over there have some final questions!":
        j "Hey, Prez! Don't let your fans escape just yet. I think that group over by the door has a few more questions."
        m forward vsur om oe "O-Oh! Of course! I shouldn't leave them hanging!"
        show monika 1l
        "She gives me a quick, apologetic smile before smoothing her skirt and hurrying off to address the group."
        hide monika
        "I watch her go. She switches back into 'President Mode' instantly. It’s impressive, really."
        j "She’s a natural. No wonder she was the star of the Debate Club."
        "I find myself wondering what exactly made her trade the intensity of debate for the quiet of literature. There's a story there."
        j "Ah—"
        "The thought of Monika is cut short as Natsuki drops a stack of empty trays nearby, looking like she’s about to have a meltdown."
        j "Better go help the gremlin before she bites someone."
        jump chap1_mid

    "Let out a pained, caffeine-addled sigh.":
        show monika forward neut e2a
        stop music
        play sound pained_sigh
        "The salt. The caffeine. The lack of sleep. It all hits me at once like a freight train."
        "..."
        "........"
        "..............."
        show monika forward neut e2b
        "I let out a sigh so loud and pained it sounds like a dying whale. The conversation in the room dies instantly."
        "........................"
        show monika forward neut e2c
        "Several guests turn to stare at the source of the noise. I don't care. I'm seeing colors that don't exist."
        "................................."
        show monika forward neut b2c
        "Monika’s smile falters. She looks genuinely concerned—and maybe a little bit mortified."
        m forward curi cm oe "Uhh... Jacko? Is everything alright? You sound like you're in physical pain."
        show monika curi md
        "Monika steps closer, her voice dropping to a sharp whisper in my ear."
        show monika forward rhip b1b mi
        m "Jacko, that was incredibly loud. People are starting to stare. Are you having a reaction to that drink?"
        show monika forward rhip b1b md
        j "I'm fine. I'm raw. I'm peak performance. Leave it alone."
        show monika forward rdown b1b mi
        m "You don't look fine. You look... unstable. Maybe you should take a walk outside? You're being very disruptive."
        m 4e "If you're frustrated with the work, we can talk about it, but you can't just-{nw}"
        show monika forward lsur cm oe at h11
        j "YES! I'M FINE! Holy shit, Monika, know when to shut the fuck up! I'm doing your dirty work, aren't I?!"
        show monika forward sad cm oe
        "The silence that follows is absolute. Even Natsuki stops mid-shout. Monika’s face goes pale, then crumples."
        m "..."
        show monika forward cry cm oe
        m "I... I was just trying to help..."
        "She looks at me with an expression of pure, unadulterated hurt. I can see the tears welling up, and for the first time today, the caffeine fog clears enough for me to realize I’m being a total piece of shit."
        show monika 1q
        "..."
        show monika forward worr cm oe
        "Monika wipes her eyes quickly, her hand trembling."
        m forward worr om oe "Y-yeah. You're right. I’m sorry. I'll just... I'll go help the others."
        show monika forward worr cm ce
        "She turns and walks away, her shoulders hunched. She looks completely dejected."
        hide monika
        "..."
        j "Bitch. Whatever."
        call rizz_update(points_change=-10) from _call_rizz_update_6
        "The air in the room has turned to ice. Everyone is looking at me like I’m a monster."
        "What have you done?"
        call unlock_photo(1) from _call_unlock_photo_6
        # Locked true bad ending label.
        "I grab my bag and walk out. I don't need this."
        scene black
        with dissolve_scene_full
        jump chap1_bad_end

label chap1_mid:
stop music fadeout 2.0
scene black
with wipeleft
scene bg club_festival
with wipeleft_scene
play music tt3
"..."
"The clubroom feels quiet for the first time all day. The lingering scent of tea and sugar hangs in the air, mixed with the faint smell of the glue we used for the posters. I glance over at Monika; she’s meticulously smoothing a stray crease on one of the displays, her expression one of focused perfection."
show monika forward lpoint rhip happ om oe at t11
m "Oh, Jacko. You're still here? I thought for sure you would have slipped away to see the rest of the festival by now."
show monika forward lpoint rhip happ cm oe
j "And leave you to handle the final cleanup by yourself? I'm not that much of a slacker."
m forward happ om oe "Always the gentleman. Honestly, the way you handled that last group of visitors... you were so natural. You knew exactly what to say to make them feel welcome."
show monika forward lpoint rhip happ cm oe
"She catches my eye, a warm, genuine smile playing on her lips. It’s the kind of look that makes all the frantic work of the morning feel completely worth it."
j "I just followed your lead, Monika. You kept the energy up even when things got a little chaotic."
m forward happ om oe "Maybe so, but a leader is only as good as the people standing beside her. And today? You were the best partner I could have asked for."
show monika forward nerv cm oe
"She lets out a soft sigh, her eyes drifting across the empty desks. She seems a bit pensive, as if she’s finally letting the weight of the day settle."
m forward nerv om oe "Everything feels so still now, doesn't it? But I can hear the music and the crowds outside. I think... I think I'm ready for a bit of a change of pace. Want to go explore the madness with me?"
show monika forward nerv cm oe

menu:
    "Yeah sure, I got nothing else to do after this!":
        j "Sure, beats sitting here counting the chairs. Let's go see what everyone else has been working on."
        m forward neut om oe "I like that enthusiasm. Well, let's get a move on then, shall we?"
        show monika forward neut cm oe
        j "Lead the way, Captain."
        show monika forward neut cm ce
        "Monika grabs her bag, her movements quick and graceful. As we walk, she seems to be taking everything in with a newfound curiosity."
        m forward dist cm oe "..."
        "She seems a little distant for a second, but she quickly shakes it off and flashes me another smile."
        call rizz_update(points_change=-1) from _call_rizz_update_7                                                                         

    "I'd love to. Let's go right now!":
        j "I thought you'd never ask. Let's get out of here while the halls are still lively."
        show monika forward happ e2a mc
        "Monika’s face lights up, a spark of genuine excitement dancing in her eyes."
        m lean happ blus m3 "That's the spirit! I heard the Music Club has a display that’s so loud you can hear it from the parking lot. We definitely have to check that out."
        show monika lean happ cm ce
        call rizz_update(points_change=+1) from _call_rizz_update_8
        hide monika
        call unlock_photo(2) from _call_unlock_photo_7
        "We step out of the room together, immediately swept up in the bustling energy of the hallway."


scene bg corridor
with wipeleft_scene
"The hallway is a sea of color and noise. Students are running back and forth, and the sound of distant chatter is almost overwhelming."
show monika 1a at t11
j "This is incredible. The school feels like it’s finally woken up."
m forward happ om ce "It's my favorite part of the year. Everyone puts aside their usual cliques and just shares what they love. It's truly inspiring."
show monika forward happ cm ce
j "Well, the Literature Club definitely set a high bar. I didn't see any other booth with as much heart as ours."
m lean happ om ce "You’re sweet, Jacko. A bit of a flatterer, but sweet."
show monika lean happ cm oe
"As we walk, Monika points out the different club displays with the enthusiasm of someone seeing it all for the first time. Suddenly, she pauses, her head tilting toward a nearby doorway."
m forward vsur om oe "Wait—is that a live band? Or just a very enthusiastic sound system? Let's go see!"
show monika forward vsur cm oe
j "Right behind you."
show monika 1j
"I follow her through the crowd, but we’re suddenly cut off by two very familiar, very eccentric faces."
show monika 1a
j "Oh boy. Look who it is."

scene bg corridor_pov
with wipeleft
play music ba
show yazz 2b at t21
show jacob 1a at t22
$ CharacterBio.jacob.unlock()
call track_character_unlock("jacob") from _call_track_character_unlock_3
"..."
z "Well, well. Look who finally emerged from the poetry dungeon. And he's got the President on his arm."
z 1d "Wandering the halls like a tourist, Jacko? That’s not a very bold look for you."
z 1g "We were going to invite you to the chemistry lab for our 'experimental tasting,' but I see you've found a better offer."
z 2g "Walking with a girl? You're actually being social for once. I'm almost proud."
j "I'm just broadening my horizons, Yazz. You guys should try it. Sunlight is good for you."
j "Besides, I think I'm handling the festival pretty well so far."
ja 3b "Oh, you think so? Let's see your confidence levels then. You got the guts to back up that talk?"
show jacob 3a
j "I've survived the morning rush at the Literature Club. I think I can handle whatever you two are up to."
ja 2e "Pfft—talking big won't help you when things get intense. You’re looking a little overwhelmed already."
z 2b "He's got that 'I just read ten sonnets' look in his eyes. He needs a real jolt to the system."
j "And I suppose you two have exactly what I need?"
z 2j "We’re flavor chemists now, Jacko. We’ve developed a beverage so potent it’ll make your ancestors feel energized."
ja 1i "He’s about to show you the Forbidden Brew."
"Yazz pulls a glass vial from his pocket. The liquid inside is a neon, glowing purple that looks like it belongs in a sci-fi movie."
ja 2j "Careful. One sip and you’ll be able to hear colors and see sound."
show jacob 2a
z 1b "This is the result of three sleepless nights and far too much caffeine. I call it: 'Liquid Love.'"
z 2a "It’s a total game-changer for your social stamina. One bottle and you'll be the life of the party until next Tuesday."
ja 1m "We made it in the back of the Chem room. The teacher thought we were just cleaning the beakers."
show jacob 1a
j "It looks like something you’d use to clean an engine, Yazz. Is it even safe to drink?"
z 2j "It’s made with 'natural' extracts! Mostly. If you count concentrated ambition as an extract."
ja 3q "It tastes like lightning and smells like a mid-life crisis. Want a sample?"
show jacob 1v
show yazz 1b
"Before Jacob can even finish his sentence, Yazz tilts the vial and pours a generous amount into Jacob’s mouth."
ja 1l "Oh... oh my... wow..."
"Jacob’s eyes go wide, and he starts shaking slightly, his face turning a shade of pink that matches the liquid."
play sound scream
show jacob fb
ja "I CAN TASTE THE UNIVERSE! EVERYTHING IS SO VIVID! I CAN FEEL MY HAIR GROWING!"
z 2a "See? Pure energy. Liquid Love: it turns your day into a masterpiece."
j "Okay, now I’m actually curious. I need to see what that feels like."
show yazz 2g at t31
show jacob fb at t32
show monika forward pout om oe at t33
m "Jacko, please tell me you're not actually going to drink that. It looks like it could dissolve a spoon."
j "Don't worry, Monika. I've got a strong stomach."
z 2m "YOU WANT THE VIAL? YOU HAVE TO PROVE YOU’RE WORTHY OF THE RUSH!"
show monika 1o
m "..."
hide monika
show yazz 1b at t21
show jacob fb at t22
z "You want the drink?"
z 2p "THEN YOU MUST CHALLENGE ME IN THE ARENA OF RHYTHM!"
show yazz 2n
j "Just tell me the challenge, Yazz. What do I have to do?"
z 2b "It's simple: 'PULSE POUNDER.' The handheld rhythm game."
show yazz 2a
ja "Pulse Pounder?! I haven't seen a match this high-stakes since the state finals!"
ja "I played a round earlier. My thumbs are literally blistered."
z 1d "It’s the ultimate test of focus and timing. If you can beat my high score, the vial is yours."
j "Fine. Hand over the console. I’m not losing to you today."
z 2b "Simple rules: Keep the beat until your fingers give out. If you miss three notes, you’re done."
ja "You ready, Jacko? This isn't like writing a poem. This is war."
z 1b "You in or out?"
z 1d "Win, and you get the Liquid Love."
z 2b "Lose, and well..."
z 1p "You'll have to buy us lunch for a week. And admit I'm the smarter chemist."
show yazz 2b
j "Deal. I’ve been practicing my reflexes on way harder things than this."
j "Watch and learn, Yazz."
m "I can't believe this is happening in the middle of a school hallway..."
"Monika rubs her forehead, looking like she's wondering how she ended up as the voice of reason."
m "The whole festival is turning into a circus. I should probably intervene, but..."
m "I think I'll let this play out. It’s certainly more interesting than the time Natsuki ate through the club's entire snack budget in one sitting."
stop music fadeout 1.5
play sound flashback
scene bg natsuki_room
with pixellate
play music nbike
show natsukidad 5a at t41
show natsuki 5bg at t44
nd "..."
n "..."
nd 5b "The groceries are gone, Natsuki. I just went shopping yesterday. How is the fridge already empty?"
show natsukidad 5a
n cross casual dist om oe "I was hungry, Dad. I didn't think I had to ask permission to eat."
n cross casual doub om oe "Maybe if you bought things that actually filled me up, I wouldn't have to eat so much of it."
show natsuki cross casual doub cm oe
nd 5h "..."
show natsukidad 1i
"He lets out a long, weary sigh, the sound of someone who’s reached the end of a very long rope."
nd 2f "I'm working as much as I can, Natsuki. I can't just keep buying food for it to disappear in twenty-four hours."
nd 2g "Do you have any idea how much stress I'm under to keep us going?"
n turned casual anno om oe "And you think I'm not stressed? Being hungry all the time makes it hard to focus on anything else."
n turned casual lhip angr om ce "It’s not my fault we’re in this position."
show natsukidad 1k at h41
n cross casual angr om oe "You're always complaining about the money. Just figure it out!"
show natsuki cross casual angr cm oe
nd 1m "..."
show natsukidad 1j
"The air in the room feels heavy and tense, the silence between them thick with things unsaid."
nd 2m "YOU WILL NOT TALK TO ME THAT WAY!"
nd 4l "NATSUKI, GET OVER HERE. WE NEED TO HAVE A REAL TALK ABOUT RESPECT."
n 1bm "Wait—Dad, I didn't mean it like that! I was just—"
show natsukidad 4m at t43
pause 0.1
scene black
play sound smack
stop music fadeout 10.0
"..."
scene bg corridor_pov
play sound flashback
with pixellate
show monika forward nerv cm oe at t11
m "Those memories... they still hurt to think about sometimes."
show monika 1c at t21
show natsuki 5h at t22
n "Yeah. Let's just focus on the here and now, okay? This hallway is crazy enough."
show natsuki 5i
m forward nerv om oe "Right. Back to the challenge."
show monika forward nerv cm oe
"..."
hide monika
hide natsuki
show yazz 1g at t11
j "Ready to see a real master at work, Yazz?"
z 2j "Show me what you've got, Jacko. Let’s see that rhythm."

call meat_beat_mania from _call_meat_beat_mania

if yazz_win:
    scene bg corridor_pov
    show yazz 1f at t11
    z "Whoa... I actually feel a little lightheaded. That was intense."
    show yazz 1n at t11
    "Yazz wipes his forehead, his hands still trembling slightly from the speed of the game."
    z 2b "You were good, Jacko. But you were distracted. You kept looking over at Monika like you were seeking approval."
    show yazz 2a
    j "She’s a supportive friend, Yazz. Her presence is motivating."
    show jacob fb at t22
    show yazz 1i at t21
    ja "It’s like the old saying goes: 'A man with a goal is strong, but a man with an audience is unstoppable.'"
    ja "My grandpa taught me that when I was just a kid."
    j "Can we go five minutes without a quote from your mysterious grandfather?"
    z 2h "He’s a wise man, Jacko. Truly."
    z 1l "But look, you won. I'm a man of my word."
    z 2b "Here. The Liquid Love is yours. Use it carefully—it’s got a kick."
    call collect_item("liquid_love") from _call_collect_item_1
    show yazz 2a
    j "I’ll save it for an emergency. Thanks, guys."
    j "I'm going to find Yuri later. She might actually appreciate the... unique aroma of this stuff."
    z 2b "She’s got a sophisticated palate. She’ll love it."
    z 2j "Good luck out there, you two."
    show yazz smile
    "Yazz flashes a grin that’s just a little too wide, looking genuinely pleased."
    j "We'll see you later. Enjoy the rest of the festival!"
    z 2b "We will! We’ve got more 'chemistry' to do!"
    show yazz 2a
    ja "HAVE A PRODUCTIVE AFTERNOON, CITIZENS!"
    hide yazz
    hide jacob
    "Yazz and Jacob head off toward the science wing, their energy still noticeably higher than everyone else's."
    show monika 2b at t11
    m "Well... that was certainly a detour. I think the hallway is finally clearing up a bit."
    "Monika and I continue our walk, the glow of the purple vial in my pocket a strange reminder of how weird this school can be."
    call unlock_photo(3) from _call_unlock_photo_8
    "..."
    scene black
    with dissolve_scene_full
    jump chap1_end
else:
    scene bg corridor_pov
    j "My fingers... I can't feel my fingers..."
    play sound fail
    "A heavy silence falls over our group. Yazz and Jacob look down at me, shaking their heads with exaggerated disappointment."
    show yazz smile at t11
    z "Oof. That was a rough one, Jacko. You hit a wall and just... kept hitting it."
    show yazz smile at t21
    show jacob fb at t22
    ja "You lacked the focus, my friend. You should have meditated with me this morning. My grandpa says a cluttered mind leads to cluttered thumbs."
    hide yazz
    show jacob fb at t11
    "Jacob pulls a small, plastic medal from his pocket—it looks like it came from a cereal box—and holds it out mockingly."
    "The energy drain is real. I feel like I've just run a marathon with my hands."
    scene bg gameover
    play sound crimson
    "..."
    "I find myself staring at the floor, the 'Game Over' feeling washing over me in waves. It’s just a game, but losing to Yazz feels like a blow to my very soul."
    "Monika’s voice is soft, a mix of pity and amusement."
    show monika forward dist om oe at t44
    m "Well, even with the odds in your favor, you managed to find the one way to lose. I'm almost impressed by the bad luck."
    show monika forward dist cm oe
    "A tall, imposing figure in a suit walks by, looking down at us with a stern expression."
    "It’s an older alumnus, his face a mask of disappointment."
    show monika forward neut e1d
    show jdad at t11
    g "PATHETIC. IN MY DAY, WE PLAYED GAMES WITH HONOR. WE DIDN'T LET OUR FRIENDS DOWN. LOOK AT YOU. NO SPIRIT."
    "Jacob actually starts tearing up at the man's words."
    play sound crimson
    show jacob fb at t41
    ja "HE’S RIGHT! WE’VE LOST THE OLD WAYS! FORGIVE US, ELDER!"
    "The man tosses a crumpled flyer for 'Respect and Discipline' at my feet."
    g "TRY AGAIN LATER. IF YOU HAVE THE CHARACTER FOR IT."
    "The world feels a bit darker as the 'Game Over' sensation takes hold. I think I need a break."
    pause 5.0
    $ renpy.quit()

label chap1_end:
scene bg stairs
with wipeleft
"The stairs feel a bit more crowded than usual as students rush up and down, eager to see the next performance."
pause 1.0
scene bg corridor_reverse
with wipeleft
"The hallways are lined with colorful streamers and posters, giving the familiar school a completely different feel."
pause 1.0
scene bg music_room
with wipeleft
"After weaving through the crowd, the heavy oak doors of the Music Room finally come into view."
play music chy2
$ send_phone_message("natsuki_chat", "n", "yo! i need some help at the baking competition!", conversation_label="natsuki_conversation_1")
j "Woah..."
"The room is massive, with high ceilings that make the chatter of the students echo beautifully."
"The air here is cool, smelling of polished wood and expensive rosin. Monika steps in behind me, her eyes widening as she takes it all in."
show monika forward vsur om oe at t11
m "Look at this place! The Music Club always goes all out for the festival."
m forward happ om oe "I didn't realize they were this busy today. It’s like a whole different world in here."
show monika forward happ cm oe
j "It’s impressive. They’ve even got a grand piano front and center."
m lean happ blus e3 "Jacko, look! That's a Steinway concert grand. The finish is absolutely stunning."
m "Do you think... do you think they’d mind if a guest tried the keys?"
j "Wait, you actually know how to play? I didn't know you were a pianist."
m forward lpoint rhip laug cm oe "I’ve been practicing for years, actually. My parents started me on lessons when I was young, and it eventually became one of my favorite ways to relax."
show monika forward ldown rdown happ blus cm oe
"She smiles softly, her fingers tracing a melody in the air. Suddenly, a student with a clipboard and a bright smile approaches us."
show monika forward happ cm oe at t21
show femc turned happ om oe at t22
c "Hello! Are you two here to audition for the 'Musical Evolution' performance?"
show femc turned happ cm oe
j "Auditions? Oh, we were just stopping by to see the instruments."
m forward happ om oe "The Spring Audition, right? I saw the posters earlier. Is the schedule still open for walk-ins?"
show monika forward happ cm oe
c turned lhip happ om oe "We’re looking for a few more soloists! Our lead pianist had an emergency and had to head home early."
show femc turned happ cm oe
m forward happ om oe "Oh, that’s a shame. What kind of pieces are you looking for?"
show monika forward happ cm oe
c turned lup mc oe "Anything! We’re covering everything from classical pieces to modern pop arrangements. We just need someone with a good ear and a lot of heart."
c turned ldown om ce "Someone with... well, someone who looks as composed as you do."
show femc turned cm oe
m forward happ om ce "Well... if you're really in a bind, I might be able to help out. Just for a bit."
show monika forward happ cm oe
j "And here I was thinking we were just taking a walk. You’re full of surprises, Monika."
m forward nerv blus om oe "Don't get too excited, Jacko. I’m a bit out of practice."
show monika forward nerv blus cm oe
c turned neut mc "That would be amazing! The piano was just tuned this morning. Would you like to play something for us?"
hide femc
show monika forward nerv blus cm oe at t11
j "Go for it, Monika. I’d love to hear what you can do."
m forward nerv om oe "You really want to hear me play? It's been a while since I played for anyone."
show monika forward nerv cm oe
j "Are you kidding? I’ve been waiting to hear this since you mentioned the lessons. You’ll be great."
show monika forward pout blus cm ce
"Monika takes a deep breath, smoothing out her skirt as she steadies herself."
m forward happ om oe "Fine. But you have to promise to be a supportive audience member."
show monika forward happ blus cm oe
j "I’ll be right here. Front row."
m forward nerv blus om oe "J-Jacko... you're making me more nervous."
show monika forward nerv blus cm oe at t21
show femc turned happ om oe at t22
c "Perfect! Take your seat whenever you're ready."
show femc turned happ cm oe
m forward happ om oe "I'll play something I've been working on myself. It's still a little rough, but I like it."
show monika forward happ cm oe
j "You write your own music too? Is there anything you can't do?"
show monika lean blus cm oe
"Monika gives a soft, genuine laugh."
m lean happ blus om "I just like to experiment. It's about finding a way to express things that words can't quite capture."
show monika forward happ blus cm oe
"Monika walks over to the piano. As she sits down, the noise in the room seems to settle into a respectful quiet."






c turned happ om ce "Take your time, President."
hide femc
show monika forward worr blus om oe at t11
if natsuki_baking_help:
    j "Hey Monika I need to go somewhere for a little bit actually, do you mind if I leave and come back?"
    m "Oh! uh sure, i'll be here waiting for you Jacko."
    m "I'll just do my thing here and you can come back when you're done."
    j "Thanks so much Monika! I promise I'll be back soon."
    m "Bye..."
    jump natsuki_baking_help
m "Okay... deep breaths. Here we go."
show monika worr blus cm oe
"..."
scene black
with dissolve_scene_full
"The music starts softly—a single, clear melody that fills the room. It’s a beautiful, slightly melancholy tune that seems to speak of hidden feelings and quiet dreams."
"For a few minutes, everything else disappears. There’s only the music and the sight of Monika, completely lost in the notes she’s playing."
pause 2.0

jump after_music

label after_music:
scene bg corridor_reverse
with dissolve_scene_full
stop music fadeout 2.0
"As we step back out into the hallway, a few Music Club members follow us, still talking about the performance."
show femc turned happ om oe at t21
c "That was incredible! The emotion you put into that piece... please, won't you consider joining the ensemble?"
show monika forward vsur blus om oe at t22
m forward happ blus om oe "I'm so glad you liked it! But I already have my hands full with my own club duties."
show monika forward happ blus cm oe
m forward happ om oe "As the Literature Club President, I really need to be there for my members."
show monika forward happ cm oe
c turned happ om oe "A Club President?! That makes so much sense now!"
show femc turned happ cm oe
m forward happ om oe "Does it? I thought I was being pretty low-key."
show monika forward happ cm oe
c turned lhip happ om oe "Most Presidents look so stressed out during the festival, but you seem like you’re actually enjoying yourself!"
show femc turned lhip happ cm oe
m forward rhip happ om oe "Well, we worked really hard to get everything ready early this morning, so now we can actually appreciate the festival."
show monika forward rhip happ cm oe
j "Yeah, we’re a pretty efficient team. Poetry and organization go hand-in-hand."
"I decide not to mention the chaotic run-in with Yazz earlier."
c turned lhip happ om oe "That’s amazing! We’re still trying to get our choir together!"
show femc turned lhip happ cm oe
"Students nearby are whispering to each other, clearly impressed by Monika’s talent."
"A girl with a calm, refined presence steps out from the Music Room, the crowd parting to let her through."
show kotonoha turned happ om oe at t11
play music somethingreal
who "Let's not overwhelm our guests. They have a festival to enjoy."
show kotonoha turned happ cm oe
"The girl turns to Monika with a respectful nod."
who "I know that feeling. Making sure everything is perfect for your club while trying to find a moment for yourself... it’s a lot of work."
show kotonoha turned happ cm oe
j "Are you in charge here?"
show kotonoha turned happ cm oe
p "I suppose I am. I try to keep the music playing, at least."
show kotonoha turned happ cm oe
k turned happ om oe "I’m Kotonoha, the President of the Music Club. It’s a pleasure to meet a fellow President."
show kotonoha turned happ cm oe
m forward happ om oe "I'm Monika. Your club members are very talented, Kotonoha. You've done a wonderful job with the displays."
show monika forward happ cm oe
m forward rhip happ om oe "I’d love to stay longer, but I promised Jacko we’d explore the courtyard."
show monika forward rhip happ cm oe
k turned lhip happ om oe "I understand. Our time today is precious. Thank you for sharing your music with us—it’s rare to hear someone play with such sincerity."
show kotonoha turned lhip happ cm oe
c turned rhip happ om oe "But President! If she could just play one more—"
show femc turned rhip happ cm oe
k turned lhip happ om oe "Now, now. We shouldn't keep them. They have memories to make."
show kotonoha turned lhip happ cm oe
k turned lhip happ om oe "The piano is always here, Monika. You’re welcome back anytime."
show kotonoha turned lhip happ cm oe
m forward rhip happ om oe "Thank you. It’s nice to know there’s a quiet place to escape to."
show monika forward rhip happ cm oe
j "We’ll be looking forward to your club’s main show later, Kotonoha."
k turned lhip happ om oe "We’ll do our best to live up to the standard you set. Enjoy the festival!"
show kotonoha turned lhip happ cm oe
hide femc
"Kotonoha waves as she leads her club members back inside to prepare for their next event."
k turned lhip happ om oe "Have a wonderful time on your date, you two!"
show kotonoha turned lhip happ cm oe
hide kotonoha
"She gives a cheerful wave before disappearing into the room, leaving us standing in the hallway."
j "..."
m forward happ blus om oe "..."
show monika forward happ blus cm oe at t11
"The hallway is a bit quieter now, the sound of the piano still lingering in my mind."
m forward nerv blus om oe "A 'festival date.' People certainly jump to conclusions quickly, don't they?"
show monika forward nerv blus cm oe
j "I mean... we are spending the whole day together. It’s a pretty easy mistake to make."
"My heart is racing, and I hope she can't tell."
m forward nerv om oe "I suppose so. It's just... nice to be seen that way for a change."
show monika forward nerv cm oe
j "Yeah. And for what it's worth, that was the most beautiful thing I’ve heard all day."
j "You really have a gift, Monika."

menu:
    "We should get you on the roof with a piano.":
        j "We should find a way to get a piano on the roof. You could play for the whole school."
        m forward lsur blus om oe "E-eh? The roof? Can you imagine trying to move a grand piano up all those flights of stairs?"
        j "I’d help carry it! Everyone deserves to hear you play. It would be the highlight of the whole festival."
        "Monika starts to laugh, a sweet, bright sound that makes me smile along with her."
        m forward laug blus om oe "Ahaha~ Jacko, you have the most impossible, sweet ideas. You’re such a dreamer."
        j "Maybe. But a dreamer with good taste."
        m forward happ blus om oe "..."
        j "..."
        "We stand there for a moment, the atmosphere between us soft and warm."
        call rizz_update(points_change=-1) from _call_rizz_update_9
        m forward happ om oe "Come on, dreamer. Let's see what else the festival has for us."
        jump chap1_ending


    "The piano looked happy.":
        j "You know, even the piano seemed happy while you were playing it."
        j "It’s like it finally found someone who truly understood it."
        m forward curi blus om oe "..E-eh? Happy? It’s just an instrument, Jacko."
        "Monika twirls a strand of her hair around her finger, looking down at her shoes with a shy smile."
        m forward happ blus om oe "That’s a very poetic way to put it. You’ve definitely been spending too much time in the Literature Club."
        j "I’m serious. You made it sound perfect. Like you two were in complete harmony."
        "Monika looks up, her eyes shining with a warmth I haven't seen before."
        m forward happ blus om oe "Y-you really think so? It wasn't too much?"
        j "It was perfect, Monika. I didn't want it to end."
        "She smiles, her whole face lighting up with genuine happiness."
        m forward happ blus om oe "Thank you, Jacko. Hearing you say that... it means a lot more than you know."
        call rizz_update(points_change=+4) from _call_rizz_update_10
        jump chap1_ending

    "…You missed a note.":
        j "That was good! Though... I think you might have missed a note near the end of the second part."
        m forward happ om oe "..."
        "The air suddenly feels a little colder, and Monika's smile falters for a split second."
        m forward angr om oe "Did I? How interesting."
        m forward angr om oe "I've practiced that piece dozens of times. My memory is usually very reliable."
        m forward angr om oe "Perhaps you’d like to give it a try and show me where I went wrong, Jacko?"
        "Monika’s gaze is intense, and for a second, I feel like I’ve said exactly the wrong thing."
        j "W-well... I’m no expert! It just sounded a little... different? It was still great though!{nw}"
        m forward vang om oe "If you’re no expert, maybe you should just appreciate the music instead of looking for flaws. It’s hard enough playing for people as it is."
        m forward sad om oe "..."
        m forward happ om oe "Ahaha~ Sorry, Jacko! I’m being way too sensitive. I guess I’m just a bit of a perfectionist."
        m forward happ om oe "Let’s just keep going. I shouldn't let a little critique get to me, right?"
        "She laughs, but it doesn't sound as bright as it did before, and she starts walking a bit faster."
        j "Y-yeah... sorry, I was just teasing... wait up!"
        "I feel a knot in my stomach. I definitely should have kept that thought to myself."
        call unlock_photo(4) from _call_unlock_photo_9
        "Way to kill the mood, Jacko."
        call rizz_update(points_change=-3) from _call_rizz_update_11
        jump chap1_ending


label after_music_baking:
scene bg corridor_reverse
"As I'm walking back from the baking compitiion, I'm wiping away all of debris off of my clothes."
j "Man I should've worn an apron or something man..."
j "Hmm?"
"I see Monika across the hallway with a group of students."
j "I wonder whats going on.."
"The more I approach more and more students begin going back into the music room until theres only one more person left."
who "We’ll do our best to live up to the standard you set. Enjoy the festival!"
"..."
"I eventually reach Monika."
m "Oh. hey Jacko..."
j "Hey Monika, sorry about the sudden disapearence I had to help Natsuki with something."
m "Uh-huh."
"Monika scoffs and points her head away from me."
m "I see you really dusted up from all the baking."
j "Wait how did?"
j "Oh right the dust."
j "Yeah she really needed help Monika I didnt wanna leave you alone I swear."
j "Here look."
"I pull out a cupcake wrapped in tin foil."
j "I snagged one before I left I wanted to give this to you, I baked this one."
"Monika slowly tilts her head towards the cupcake and takes it from my hands."
j "Tell me what you think-"
"Before I can even finish Monika scarffs down the cupcake like theres no tomorrow."
m "Wofh thisf ish sooo gooddd."
"Monika can barely talk wth the cupcake in her mouth."
"..."
"Finally she gives on big GULP."
m "Ahhhhhhh. I just love her cupcake recipe especially if your the one who baked em' Jacko."
j "Yeah your, welcome Monika."
m "All will be forgiven Jacko, don't worry I just wish you were there to listen to my song."
j "I bet it was really beautiful Monika. Maybe soon you can show me that song in private!"
m "Ohhh, maybe I will."
m "But for real lets try to enjoy the rest of the festival."
j "Sure thing Mon-ika."
"..."

label chap1_ending:
"Monika turns back to me after a moment, her cheerful expression returning as she looks toward the exit."
show monika forward happ blus om oe at t11
m forward happ blus om oe "Let's head outside! I can smell the food stalls from here, and I'm definitely ready for a snack. Coming?"
j "You bet. I'm right behind you!"
"We step out into the courtyard, leaving the quiet halls behind as the warm afternoon sun hits us."
scene bg school_outside
with dissolve_scene_full
"The school courtyard is bustling with life. Brightly colored booths line the walkways, their banners waving in the warm afternoon breeze."
"The air is filled with the delicious scents of grilled meat and sweet treats, mixed with the sounds of laughter and music from the game area."
show monika forward lpoint rhip happ om oe at t11
m "Isn't this wonderful? I love how the school feels so much more alive during the festival. It's like everyone finally let their guard down."
show monika forward lpoint rhip happ cm oe
j "It really is something else. The energy out here is amazing compared to the quiet hallways."
m forward curi om oe "There’s always something new to discover. You never know what kind of creative things the other clubs have come up with."
show monika forward curi cm oe
j "Like what? What's the most interesting thing you've seen at one of these?"
m curi om oe "The Science Club once spent the whole festival making this neon-colored slime. It was a bit messy, but the courtyard smelled like strawberries for a week!"
show monika forward curi cm oe
j "Strawberries? That’s definitely an improvement over the usual classroom smells."
m forward happ om oe "Ahaha! Exactly. It’s just nice to see everyone having a good time and forgetting about their studies for a while."
show monika forward happ cm oe
j "I’m all for that. But mostly, I’m for the food. I’m starving."
m forward happ om oe "I agree! We should definitely find something to eat before we run out of energy. Lead the way, my culinary expert."
show monika forward happ cm oe
j "Alright, let's see our options."
m forward neut om oe "That takoyaki stall has a huge line, so it must be worth the wait. Or..."
show monika forward neut cm oe
m "There’s a 'Mystery Skewer' booth over there. No labels, just a sign saying 'Surprise Your Taste Buds.'"
show monika forward neut cm oe
j "Mystery skewers? I don't know if I'm brave enough for a surprise like that right now."
m forward lsur om oe "Oh, where’s your sense of adventure? It could be the best thing you've ever tasted! That's half the fun of a festival."
show monika forward lsur cm oe
j "I think I'll stick with the takoyaki. I like knowing what I’m about to eat."
m forward happ om oe "Fair enough! But don't look at me with puppy-dog eyes if I end up finding something amazing at the other stalls later."
show monika forward happ cm oe
j "I’ll try to contain my jealousy."

"As we start walking toward the takoyaki stall, Monika suddenly stops, her eyes catching a small game booth tucked away between two larger stalls."
show monika forward lpoint rhip lsur om oe
m "Oh, look! Ring toss! I haven't played this in years."
show monika forward lpoint rhip lsur cm oe
j "You want to play ring toss? I didn't think you'd be the type to get into carnival games."
m forward happ om oe "Why not? It looks like fun! Besides, I have a feeling I might still be pretty good at it."
show monika forward happ cm oe
j "Alright, show me what you've got. If you win, I'll admit you're a master of more than just the piano."

"Monika steps up to the booth, looking surprisingly focused. She hands over a few tickets and takes the wooden rings, weighing them in her hand for a moment."
"She takes a deep breath and tosses them one after another. To my surprise, each one lands perfectly over the target bottles. One, two, three."
j "Whoa! You really were serious. That was impressive."
m forward happ om oe "I told you I had a good feeling about it! It’s all about the flick of the wrist and a little bit of focus."
"The student running the booth looks impressed as they hand Monika a small, fluffy stuffed bear with a tiny red ribbon around its neck."
"She turns to me, her face glowing with a triumphant, happy grin."
show monika forward happ om oe
m "Here, Jacko. A gift for my favorite club member."
show monika forward happ cm oe
j "For me? You're the one who won it, though!"
m forward lsur om oe "Consider it a souvenir of our day out together. It’s cute, isn’t it? And look, it even has a ribbon like mine."
call collect_item("small_bear") from _call_collect_item_2
"I take the bear from her. It’s soft and small, but holding it makes me feel a strange sense of warmth. It’s just a silly prize, but it feels special coming from her."
j "Thanks, Monika. I’ll keep it in a safe place, I promise."
show monika forward happ om oe
call update_mj_art from _call_update_mj_art_2
m "You’d better! I’ll be checking to see if it’s still on your desk later."
show monika forward happ cm oe
m "So... what’s next on the agenda, Jacko? There’s still so much of the festival left to see!"
show monika forward happ cm oe
j "Hmmmm..."
"I look around at the colors and the happy crowds. For the first time today, everything feels right."
call loading_screen_start
stop music fadeout 2.0
jump mid_point_choices