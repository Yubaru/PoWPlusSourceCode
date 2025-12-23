image mustard = "mod_assets/images/misc/mustard.png"


label takoyaki_story:
scene bg school_outside
j "Let's grab some takoyaki!"
show monika forward anno om at t11
m "You're that hungry already?"
show monika forward anno cm

j "I'm on the verge of becoming feral, Monika. Feed me or lose me."
show monika forward laug om lpoint
m "Dramatic. I like it."
show monika forward laug cm ldown

"I follow Monika through the festival crowd. Lanterns sway gently above us, casting a warm, flickering light over the food stalls."
stop music fadeout 2.0
play music monikat5
scene bg festival_vendor zorder 2
show clouds zorder 1
with dissolve_scene_full
"The smell of sizzling batter hits me like a truck. A {i}delicious{/i} truck."
show monika forward curi om ldown at t11 zorder 3 
j "There it is. The source of all joy and danger."
show monika forward curi cm ldown

show monika forward happ om rdown
m "Ah yes... the holy grail of festival food. Crispy, gooey, and just a little bit risky."
show monika forward happ cm rdown

j "Just how I like my romance."
show monika forward sedu om lpoint
m "Are we talking about takoyaki or each other?"
show monika forward sedu cm ldown

j "...Yes."
show monika forward laug om rdown
"Monika chuckles and pulls me by the sleeve to the front of the stall."
show monika forward laug cm rdown

"I am just niggering myself right now."
show monika forward happ om lpoint
m "One spicy mayo. One classic. One mystery."
show monika forward happ cm ldown

j "Mystery again? Didn't we *just* survive the marshmallow-horseradish combo of death?"
show monika forward sedu om rdown
m "You can't grow if you don't suffer."
show monika forward sedu cm rdown

"The vendor slides us a tray with steamy, golden takoyaki balls. They glisten under the paper lanterns, like tiny, edible suns."
show monika forward happ om lpoint
m "Behold."
show monika forward happ cm ldown

j "Our fried destiny."
"I reach out and grab one. It sizzles in my fingers. Too hot. Too tempting."
j "Cheers."
show monika forward sedu om rdown
m "To poor choices and good company."
show monika forward sedu cm rdown
$ renpy.say(narrator, "We both take a bite. Mine explodes with flavor. Sweet, savory, mustard, and a little crunchy perfection.", interact=False)
stop music fadeout 10.0
$ renpy.pause(5.0, hard=True)
window hide(None)
window auto
$ renpy.pause(3.0, hard=True)
show mustard zorder 100
$ renpy.pause(0.1, hard=True)
hide mustard
play music monikat5
j "Holy fuck, this is actually divine."
show monika forward laug om lpoint
m "I told you. Takoyaki is my religion."
show monika forward laug cm ldown

j "You're the high priestess of octopus."
show monika forward sedu om rdown
m "And you're my loyal, sauce stained disciple."
show monika forward sedu cm rdown

"She licks a bit of mayo off her thumb with perfect elegance. My brain short circuits."
"I will never be normal again."


menu:
    "Offer her your last takoyaki":
        j "Here, take mine."
        show monika forward curi om ldown
        m "Really?"
        show monika forward curi cm ldown

        j "Yeah. I already ascended spiritually. Now it's your turn."
        show monika forward sedu om rdown
        m "You're smooth for someone covered in bonito flakes."
        show monika forward sedu cm rdown

        "She picks it up carefully and takes a bite. Her eyes widen."
        show monika forward shoc om ldown
        m "Oh."
        show monika forward shoc cm ldown

        j "What? What's wrong?"
        show monika forward dist om rdown
        m "It's... jalapeño. With chocolate drizzle."
        show monika forward dist cm rdown

        j "I—what?"
        show monika forward dist om ldown
        m "I don't know what I'm feeling."
        show monika forward dist cm ldown

        j "Emotions. Pain. Growth...?"
        show monika forward dist om rdown
        m "Definitely growth. In my sinuses."
        show monika forward dist cm rdown

        call rizz_update(points_change=-2) from _call_rizz_update_12
        "She somehow finishes it like a champ. She's built different."

    "Eat the last one yourself":
        j "Mine."
        show monika forward anno om ldown
        m "Wow. No hesitation."
        show monika forward anno cm ldown

        j "I live dangerously."
        "I pop it in without thinking."
        j "..."
        j "WHY."
        show monika forward curi om rdown
        m "What is it?"
        show monika forward curi cm rdown

        j "Blue cheese. With banana."
        show monika forward laug om lpoint
        m "That's illegal in at least seven prefectures."
        show monika forward laug cm ldown

        j "I've seen god. And he's disappointed."
        show monika forward happ om rdown
        m "But are you still alive?"
        show monika forward happ cm rdown

        j "...Barely."
        show monika forward sedu om lpoint
        m "Then it was worth it."
        show monika forward sedu cm ldown

        "Monika chuckles while I try to scrape the taste off my tongue."
        j "I'm never eating again."
        "Dirty ass nigga."

    "Throw it on the ground and stomp on it":
        j "You know what? Screw this."
        "I throw the last takoyaki on the ground and stomp on it."
        show monika forward shoc om ldown
        m "Jacko! What are you doing?!"
        show monika forward shoc cm ldown

        j "I'm protesting the injustice of this world."
        show monika forward anno om rdown
        "Monika stares at me, wide-eyed."
        m "You're insane."
        show monika forward anno cm rdown

        j "And proud."
        show monika forward anno om ldown
        m "You're going to get us kicked out."
        show monika forward anno cm ldown

        "Suddenly, the takoyaki starts to float up into the air."
        stop music fadeout 5.0
        j "Wait, what?"
        "It hovers for a moment, then bursts into a cloud of confetti."
        show monika forward shoc om rdown
        m "What the hell?!"
        show monika forward shoc cm rdown

        "As the smoke clears, a large being appears in front of us."
        "Is that?"
        j "Yazz!?"
        play music yazz
        show yazzinator at t22 zorder 100
        show monika forward shoc cm rdown at t21
        z "You have summoned me, mortals! I am The Yazzinator!"
        z "How dare you waste my precious takoyaki!"
        j "I didn't mean to! It was a mistake!"
        show monika forward dist om ldown
        m "Wait, is this a prank?"
        show monika forward dist cm ldown

        z "No! I am real! I am the spirit of the festival!"
        z "And I demand you pay for your sins!"
        j "What do you want from us?!"
        z "..."
        z "Blood."
        j "What?!"
        z "Enguard!"
        call battle_start from _call_battle_start_1
        "The Yazzinator disingrates into a cloud of smoke, leaving behind a giant shit stain."
        show monika forward dist om rdown at t11 zorder 100
        j "..."
        show monika forward dist om rdown at t11 zorder 100
        m "..."
        show monika forward dist cm rdown
        $ CharacterBio.yazz.unlock()
        call track_character_unlock("yazz") from _call_track_character_unlock_7

        "Burger Enjoyer."
        call unlock_photo(6) from _call_unlock_photo_10
        "You and Monika pretend that didn't happen."

show monika forward happ om lpoint
"She wipes her hands on a napkin and tosses the tray."
m "Okay, Jacko. We survived the sauce saga."
show monika forward happ cm ldown

j "Barely."
show monika forward sedu om rdown
m "Now comes the real question: what's next?"
show monika forward sedu cm rdown

default nickname = False
menu:
    "Ask Monika out on a desert date":
        j "Dessert?"
        show monika forward curi om ldown
        m "Ooooh... what do you have in mind?"
        show monika forward curi cm ldown

        j "Crepes. I saw a place that rolls them like burritos."
        show monika forward happ om rdown
        m "That's either genius or blasphemy. Let's go."
        show monika forward happ cm rdown

        "We head off toward the glowing dessert stand."
        menu:
            j "..."
            "Give her a weird nickname":
                j "From now on, you are... The Octo Queen."
                show monika forward dist om ldown
                m "I... what?"
                show monika forward dist cm ldown

                j "You conquered the balls. You get a title."
                show monika forward anno om rdown
                m "Why does this sound like a weird fantasy anime?"
                show monika forward anno cm rdown

                j "Because it is. And I'm the sidekick who dies tragically."
                show monika forward happ om lpoint
                m "No, you're the chaotic gremlin who keeps things interesting."
                show monika forward happ cm ldown

                j "That's the nicest insult I've ever gotten."
                show monika forward sedu om rdown
                m "You're welcome."
                show monika forward sedu cm rdown

                "You both laugh and head toward the dessert stand."
                $ nickname = True
                "..."

            "Ask Monika what she really thought":
                j "So... what did you really think of the takoyaki?"
                show monika forward happ om lpoint
                m "Honestly? Best part of my day."
                show monika forward happ cm ldown

                j "Really?"
                show monika forward sedu om rdown
                m "Yeah. Not just the food."
                show monika forward sedu cm rdown

                j "Oh?"
                show monika forward flus om ldown
                m "It's rare I get to just be... me. Not the club president. Not the perfectionist. Just Monika. With someone who makes me laugh."
                show monika forward flus cm ldown

                j "Wow."
                show monika forward happ om rdown
                m "So thank you."
                show monika forward happ cm rdown

                j "I didn't do anything."
                show monika forward sedu om lpoint
                m "You showed up. That's enough."
                show monika forward sedu cm ldown

                j "I think... this is my favorite part of the festival."
                show monika forward flus om rdown
                m "Same."
                show monika forward flus cm rdown

                "She smiles at me. And somehow, the takoyaki moment feels like more than just food. It feels like something real."
                "Something that might matter later."
                "You both laugh and head toward the dessert stand."
                call rizz_update(points_change=+2) from _call_rizz_update_13
                "..."

    "Hey...":
        stop music fadeout 5.0
        j "Hey... you wanna sit for a while?"
        show monika forward curi om ldown
        m "Hmm?"
        show monika forward curi cm ldown

        j "That tree over there. Looks quiet. No food stalls. No games. Just... peace."
        show monika forward happ om rdown
        m "...Yeah. That sounds nice."
        show monika forward happ cm rdown

        scene bg cherrytree zorder 2
        show clouds zorder 1
        with dissolve_cg
        "Everything feels softer away from the crowd. The hum of festival noise fades into the distance."
        "The lanterns don't reach this far, except for one swaying above the sakura branches its glow casting shadows that feel like they belong in a memory."
        "We sit beneath the tree. The grass is cool. The breeze carries faint scents of sugar, oil, and the fading laughter of strangers."
        show monika forward dist om ldown at t11 zorder 100
        "Monika hugs her knees to her chest, staring ahead at nothing in particular."
        m "You know... I don't really get to do this."
        show monika forward dist cm ldown

        j "Do what?"
        show monika forward dist om rdown
        m "Nothing. Just... sit. Exist. Without expectation."
        show monika forward dist cm rdown

        j "What do you mean Monika?"
        show monika forward dist om ldown
        "She lets out a quiet breath, like she's been holding it all night."
        show monika forward dist cm ldown

        show cherry_blossoms_falling1 zorder 5
        show cherry_blossoms_falling2 zorder 5
        show cherry_blossoms_falling3 zorder 5
        show cherry_blossoms_falling4 zorder 5
        show cherry_blossoms_falling5 zorder 5
        show cherry_blossoms_falling6 zorder 5
        show cherry_blossoms_falling7 zorder 5 
        show cherry_blossoms_falling8 zorder 5
        show y_cg2_dust1 zorder 6
        show y_cg2_dust2 zorder 6
        show y_cg2_dust3 zorder 6 
        show y_cg2_dust4 zorder 6
        show monika forward dist om rdown
        play music abyss
        m "People always see me as the girl who has it together. The president. The planner. The one who fixes things when they go wrong."
        show monika forward dist cm rdown

        m "And I've played that role so well that sometimes I forget how to be anything else."

        j "Is it really that hard to just... stop?"
        show monika forward dist om ldown
        m "It is when the moment you stop, people start to notice. They ask what's wrong. They assume something's broken."
        show monika forward dist cm ldown

        m "It's easier to keep performing. To keep smiling. Keep talking. Keep leading."

        m "Even when I'm tired of it."

        "She pauses. A petal floats down and lands gently in her lap. She doesn't move it."
        show monika forward dist om rdown
        m "I used to think being strong meant being above it all. Not showing cracks. Not needing help."
        show monika forward dist cm rdown

        m "But sometimes I wonder if I ever gave myself permission to be human."

        j "Do you want that?"
        show monika forward dist om ldown
        m "...Yeah. I think I do. Even if I'm not sure how."
        show monika forward dist cm ldown

        "Another long silence. Not uncomfortable just still."
        show monika forward dist om rdown
        m "You know the worst part?"
        show monika forward dist cm rdown

        j "What?"
        show monika forward dist om ldown
        m "I've surrounded myself with people I care about... and I still feel lonely most of the time."
        show monika forward dist cm ldown

        m "Because no matter how close I get, there's always a piece of me that stays locked away. The part I can't show. The part that's... tired. Afraid. Small."

        m "And I wonder if anyone would even like that part."

        j "I think... people would understand more than you think."
        show monika forward dist om rdown
        m "Maybe. But I've been that 'Monika' for so long, I don't know if I remember how to be anyone else."
        show monika forward dist cm rdown

        hide cherry_blossoms_falling1
        hide cherry_blossoms_falling2
        hide cherry_blossoms_falling3
        hide cherry_blossoms_falling4
        hide cherry_blossoms_falling5
        hide cherry_blossoms_falling6
        hide cherry_blossoms_falling7
        hide cherry_blossoms_falling8
        hide y_cg2_dust1
        hide y_cg2_dust2
        hide y_cg2_dust3
        hide y_cg2_dust4
        "She finally brushes the petal off her lap. It catches the wind and vanishes into the air."
        show monika forward dist om ldown
        m "I used to write poems. All the time."
        show monika forward dist cm ldown

        j "Why'd you stop?"
        show monika forward dist om rdown
        m "Because they started getting too real. Too raw. And I didn't want to admit how much of myself was bleeding into the page."
        show monika forward dist cm rdown

        m "It's one thing to lead a literature club. It's another to let people read the parts of you you've spent your whole life hiding."

        "She goes quiet again, eyes fixed on the shadows between the branches."
        j "Do you miss it?"
        show monika forward dist om ldown
        m "...Everyday."
        show monika forward dist cm ldown

        j "Then maybe you should write again. Not for anyone else. Just for you."
        show monika forward dist om rdown
        "Monika turns her head slightly. Just enough to look at me."
        m "Maybe I will."
        hide monika
        call track_cg_msit from _call_track_cg_msit 
        show m_cg_backround zorder 3
        show m_cg_1a zorder 4
        show y_cg2_dust1 zorder 5
        show y_cg2_dust2 zorder 5
        show y_cg2_dust3 zorder 5 
        show y_cg2_dust4 zorder 5
        show cherry_blossoms_spiraling1 zorder 5
        show cherry_blossoms_spiraling2 zorder 5
        show cherry_blossoms_spiraling3 zorder 5
        show cherry_blossoms_spiraling4 zorder 5
        show cherry_blossoms_spiraling5 zorder 5
        show cherry_blossoms_spiraling6 zorder 5
        show cherry_blossoms_spiraling7 zorder 5
        show cherry_blossoms_spiraling8 zorder 5
        show cherry_blossoms_spiraling9 zorder 5
        show cherry_blossoms_spiraling10 zorder 5
        show m_cg_cafeEvent_shaft1 zorder 6
        show m_cg_cafeEvent_shaft2 zorder 6
        show m_cg_cafeEvent_shaft3 zorder 6
        with dissolve_cg
        hide clouds
        hide cherrytree
        "..."
        "The wind picks up slightly. More petals begin to spiral around the air, like it knows our presence."
        hide m_cg_1a
        show m_cg_1c zorder 4
        with dissolve_cg
        m "You ever feel like you’re stuck between who you are and who you’re supposed to be?"
        j "All the time."
        m "Yeah. That’s the worst kind of trap. The invisible kind."
        "She unfolds her arms and leans back on her hands, staring up at the sky."
        m "I think that’s why I like the stars."
        j "Why?"
        m "Because they don’t need to explain themselves. They just are. Burning. Existing. Light years away from anything that could ever hurt them."
        m "Sometimes I wish I could be like that. Distant. But beautiful."
        j "You already are."
        "She doesn’t respond to that. Not because she didn’t hear me. But because she’s somewhere else now. In a quieter place inside her own head."
        "A place she doesn’t get to visit often."
        "The petals continue falling in slow motion, like the sun’s holding its breath."
        m "Thanks for sitting with me."
        j "Of course."
        m "It’s easier to talk when someone’s just... listening. Not trying to fix it. Not waiting to speak. Just... there."
        j "Then I’ll be here. As long as you need."
        hide m_cg_1c
        show m_cg_1a zorder 4
        with dissolve_cg
        stop music fadeout 5.0
        "She closes her eyes for a moment, just letting herself be."
        m "...This is the first time I’ve felt like myself in a long time."
        "No smile. No performance. Just Monika."
        show cherry_blossoms_falling1 zorder 5
        show cherry_blossoms_falling2 zorder 5
        show cherry_blossoms_falling3 zorder 5
        show cherry_blossoms_falling4 zorder 5
        show cherry_blossoms_falling5 zorder 5
        show cherry_blossoms_falling6 zorder 5
        show cherry_blossoms_falling7 zorder 5
        show cherry_blossoms_falling8 zorder 5
        window hide
        play sound monikas_tree
        $ renpy.pause(65.0, hard=True)
        "..."
        hide m_cg_1a
        show m_cg_1b zorder 4
        with dissolve_cg
        m "Okay. I think I’m ready to go back now."
        j "Yeah?"
        m "Yeah. But... thank you. Really."
        m "I really love spending time with you Jacko."
        m "We should do this more often but {i}outside{/i} of school."
        "Monika laughs nervously."
        j "Anytime."
        hide m_cg_backround
        hide m_cg_1b
        hide cherry_blossoms_falling1
        hide cherry_blossoms_falling2
        hide cherry_blossoms_falling3
        hide cherry_blossoms_falling4
        hide cherry_blossoms_falling5
        hide cherry_blossoms_falling6
        hide cherry_blossoms_falling7
        hide cherry_blossoms_falling8
        hide cherry_blossoms_spiraling1
        hide cherry_blossoms_spiraling2
        hide cherry_blossoms_spiraling3
        hide cherry_blossoms_spiraling4
        hide cherry_blossoms_spiraling5
        hide cherry_blossoms_spiraling6
        hide cherry_blossoms_spiraling7
        hide cherry_blossoms_spiraling8
        hide cherry_blossoms_spiraling9
        hide cherry_blossoms_spiraling10
        hide m_cg_cafeEvent_shaft1
        hide m_cg_cafeEvent_shaft2
        hide m_cg_cafeEvent_shaft3
        hide y_cg2_dust1
        hide y_cg2_dust2
        hide y_cg2_dust3
        hide y_cg2_dust4
        scene bg cherrytree zorder 2
        show clouds zorder 1
        with dissolve_cg
        "She stands, brushes grass off her skirt, and stretches like someone waking up from a long, strange dream."
        show monika forward happ cm at t11 zorder 100
        j "You wanna find that dessert stand?"
        show monika forward happ om rhip
        m "Yeah. Let’s ruin our digestive systems."
        show monika forward happ blus cm rdown
        j "Finally. A goal worth believing in."
        

scene bg festival_vendor zorder 2
show clouds zorder 1
with dissolve_scene_full
play music somethingreal
"The stand is lit up like a neon fever dream. Strings of pink and yellow lights crisscross above, and a cartoon strawberry waves at us from a spinning sign that squeaks every full rotation."
"A teenager in a frog onesie flips crepes with terrifying confidence. Next to him, a guy with a clipboard is just standing there rating them like it's a sport."
"On the chalkboard menu, flavors range from whimsical to war crimes:"
"'Choco Love Explosion,' 'Banana Beef Supreme,' 'Peanut Butter Meltdown,' 'Ghost Pepper Redemption,' and just... 'Don't.'"
show monika forward happ om rdown at t11 zorder 100
m "Okay. This looks like a mistake waiting to happen. I love it."
show monika forward happ cm rdown

j "Let's commit to something irrational."
show monika forward happ om rdown
m "You first. I want to see how much you value your life."
show monika forward happ cm rdown

j "Alright... Give me a 'Don't.'"
vendor "Brave. Or stupid."
j "There's a fine line. I dance on it."
"The vendor goes to work flipping, drizzling, sprinkling questionable powders until he presents me with a crepe that looks like it might require an exorcism."
show monika forward curi om ldown
"Monika takes her time. Reads every name twice. Tilts her head."
m "Give me... the Choco Love Explosion. But add strawberries. And mochi."
show monika forward curi cm ldown

vendor "We call that one 'Heartbreak Insurance.'"
show monika forward happ om rdown
m "Perfect."
show monika forward happ cm rdown

call collect_item("ice_cream") from _call_collect_item_5
"They hand us our crepes in thick paper wraps printed with tiny hearts and little devils."
"We find an empty bench. Just far enough from the crowd that it feels like its own little space."
scene bg school_bench
with wipeleft_scene
show monika forward happ om rdown at t11 zorder 3
m "Okay. On three?"
show monika forward happ cm rdown

j "Always."
show monika forward happ om rdown
m "One..."
show monika forward happ cm rdown

j "Two..."
show monika forward happ om rdown
mj "Three."
show monika forward happ cm rdown

"We both bite."
"Mine hits like an apocalypse. First it's sweet chocolate, maybe? then sour, then hot, then something else. Like betrayal. Like regret distilled into flavor."
j "This crepe just attacked my character flaws."
show monika forward happ om rdown
m "That's fair. You did order the one labeled 'Don't.'"
show monika forward happ cm rdown

"She bites hers, chews thoughtfully. Her eyes close."
show monika forward happ om rdown
m "Mmm. Okay. That's actually amazing."
show monika forward happ cm rdown

j "What's in it?"
show monika forward happ om rdown
m "Chocolate, strawberry, mochi, a bit of salt... and the will to live."
show monika forward happ cm rdown

j "I want that."
show monika forward happ om rdown
m "You chose pain. I chose balance."
show monika forward happ cm rdown

j "Teach me your ways."
"She offers a bite of hers. I lean in and take it."
call track_cg_mjtogether from _call_track_cg_mjtogether
show mj_cg_backround zorder 3
show mj_cg zorder 4
show y_cg2_dust1 zorder 5
show y_cg2_dust2 zorder 5
show y_cg2_dust3 zorder 5 
show y_cg2_dust4 zorder 5
show m_cg_cafeEvent_shaft1 zorder 6
show m_cg_cafeEvent_shaft2 zorder 6
show m_cg_cafeEvent_shaft3 zorder 6
with dissolve_cg
j "...Okay, yeah. That's incredible."
show monika forward happ om rdown
m "You have goo on your face."
show monika forward happ cm rdown

"She hands me a napkin without judgment. Just quiet amusement."
show monika forward happ om rdown
m "This... is nice."
show monika forward happ cm rdown

j "Yeah."
show monika forward happ om rdown
m "Like... actually nice. Not performatively fun. Just... normal."
show monika forward happ cm rdown

j "That's rare for you, huh?"
show monika forward dist om ldown
m "Rare for both of us, I think."
show monika forward dist cm ldown

"The crepes disappear slowly. Not because we're not hungry but because neither of us wants to rush."
"Somewhere in the distance, someone drops a prize goldfish. Someone else screams about losing at ring toss."
"But here, it's quiet. Just the flickering lantern, the sugary air, and two paper wrappers slowly crumpling in our hands."
show monika forward dist om ldown
m "Can I tell you something weird?"
show monika forward dist cm ldown

j "You kind of have to now."
show monika forward dist om ldown
m "This is the kind of moment I used to write about. Back before I stopped writing. Back when I thought simple things mattered."
show monika forward dist cm ldown

j "They do."
show monika forward dist om ldown
m "Yeah. I'm starting to remember that."
show monika forward dist cm ldown

j "We could make this a tradition. Bad crepes, quiet benches, soft lights."
show monika forward flus om rdown
m "...Yeah. I'd like that."
show monika forward flus cm rdown

"She smiles not the practiced one, but the kind that fades in slow and stays a second too long."
show monika forward happ om rdown
m "Okay. What now?"
show monika forward happ cm rdown

j "We wander. Find something cursed. Break at least one unspoken rule."
show monika forward happ om rdown
m "But gently. Respectfully."
show monika forward happ cm rdown

j "Of course. We're chaotic, not evil."
"She tosses her wrapper into a nearby bin and stands."
hide monika
hide mj_cg_backround
hide mj_cg
hide m_cg_cafeEvent_shaft1
hide m_cg_cafeEvent_shaft2
hide m_cg_cafeEvent_shaft3
hide y_cg2_dust1
hide y_cg2_dust2
hide y_cg2_dust3
hide y_cg2_dust4
with dissolve_cg
scene bg school_bench
if nickname:
    j "Let's go, Octo Queen."
    show monika forward happ om rdown at t11 zorder 100
    m "Lead the way, Sauce Gremlin."
    show monika forward happ cm rdown
    call unlock_photo(7) from _call_unlock_photo_11 
else:
    j "Let's go, Monika."
    show monika forward happ om rdown at t11 zorder 100
    m "Lead the way, Jacko."
    show monika forward happ cm rdown
scene black
with dissolve_scene_full
stop music fadeout 2.0
"Back into the noise. But a little lighter. A little more grounded. Like the crepes didn't just fill our stomachs they bought us a moment of peace."
call update_mj_art from _call_update_mj_art_3 
return


