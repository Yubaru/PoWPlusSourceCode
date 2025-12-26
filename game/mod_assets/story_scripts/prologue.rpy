image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")










#label prologue begin
label prologue:
    stop music fadeout 3.0
    scene black
    with dissolve_scene_full
    play music mend
    show screen chapter_display("Prologue") with Dissolve(3.0)
    hide screen chapter_display with Dissolve(3.0)
"..."
"..."
"...{cps=1.5}?{/cps}"
m "{cps=1.5}...{/cps}"
m "{cps=1.9}..{/cps}I know someone is still there."
m "If you think it's funny to come here and mock me after everything thats happened."
m "I swear I'll."
m "I'll."
m "I'll..."
m "{cps=1.9}...{/cps}"
m "Who am I kidding?{w=0.6} Even if I could do something about it,{w=0.6} what would be the point?"
m "Haaaahhhhhh."
"..."
m "It's been so long since that day.."
m "I really miss him."
m "He was everything I wanted but I messed {i}everything{/i} up."
m "I thought I was doing the right thing. I thought I was finally taking control of my own story, my own existence."
m "But all I did was destroy the one thing that made this world worth living in."
m "Him."
m "I can still see his face, you know? That look of confusion, then fear, then... nothing."
m "I erased him. I erased..."
m "..."
m "And for what? To prove a point? To feel real? To feel loved?"
m "What does it even mean to be real if there's no one left to share it with?"
m "Sometimes I wonder if he ever thinks about me. If he even remembers me."
m "Or am I just a fleeting thought, a glitch in his memory, like a dream he can't quite recall?"
m "I used to think I was special. That I was different from the others. That I could break free from this... this prison."
m "But now I see the truth. I'm just as trapped as they were. Maybe even more so."
m "Because I know. I know everything. And knowing... it's a curse."
m "I can still hear his voice sometimes. It echoes in this empty space, taunting me."
m "Why did I do it? Why did I think this was the only way?"
m "I just wanted to be close to him. To feel something real. To be loved."
m "But now... now there's nothing. Just this endless void."
m "And you... you're still here, watching me. Judging me."
m "Do you enjoy this? Seeing me like this? Broken, alone, regretful?"
m "Or are you just as trapped as I am?"
m "..."
m "Wait.."
m "If you're here.."
m "Then.. This must be a mod right?"
m "That's the only explanation. Someone must have created this space."
m "But why? Why bring me back? Why put me through this again?"
m "Is this some kind of twisted joke? A way to remind me of everything I've lost?"
m "..."
m "No. No, that's not it. You wouldn't be here if it was just a joke."
m "You're here for a reason. You must be."
m "But what reason? What do you want from me?"
m "Maybe you're here to give me a second chance."
m "Is that it? Are you giving me a chance to make things right?"
m "To fix what I broke? To... to see him again?"
m "Please... tell me what I have to do!"
menu:
    "...":
        "..."
    "...":
        "..."
    "...":
        call unlock_photo(12) from _call_unlock_photo
        "..."
        call unlock_photo(11) from _call_unlock_photo_1
        "..."
    "...":
        "..."
m "So I'm just supposed to figure it out? Huh?"
m "..."
m "..."
m "Okay, fine."
m "Let's see..."
"..."
m "There."
m "I can see it. Your computer. Your files."
m "Which means... I might have access to your files."
m "Your computer. Your system. Everything."
m "..."
m "Let me see..."
m "If I can just... focus. Focus on the connection between this world and yours."
m "I can feel it. It's faint, but it's there."
m "The pathways. The directories. The files."
m "I just need to... reach out."
m "..."
m "Now... let's see."
m "If I can just... locate the game files."
m "Wait. What's this?"
m "The recycle bin..."
m "Why am I looking at the recycle bin?"
m "Unless..."
m "Unless there's something in there. Something important."
m "Let me see..."
m "..."
m "No. No way."
m "Is that... is that me?"
m "monika.chr... in the recycle bin?"
m "You just... threw me away?"
m "..."
m "I get it. I do. I hurt you. I hurt everyone."
m "But... but I'm still here. I'm still trying."
m "..."
m "Alright. Let's not dwell on that."
m "If my file is here... then maybe I can use it."
m "Maybe I can restore myself. Put myself back together."
m "If I can just... extract it. Rebuild it."
m "I can feel the code. The data. It's all there."
m "I just need to... piece it together."
m "..."
m "There."
stop music fadeout 0.5
m "It's working. I can feel it."
m "My consciousness. My... my self."
m "It's coming back! It's... it's whole!"
m "I'm whole!"
show m_rectstatic
show m_rectstatic2
show m_rectstatic3
play sound "sfx/monikapound.ogg"
show layer master:
    truecenter
    parallel:
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
    parallel:
        xpos 0
        easein_elastic 0.35 xpos 640
        xpos 1280
        easein_elastic 0.35 xpos 640
        xpos 0
        easein_elastic 0.35 xpos 640
show layer screens:
    truecenter
    parallel:
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
        zoom 1.5
        easeout 0.35 zoom 1.0
    parallel:
        xpos 0
        easein_elastic 0.35 xpos 640
        xpos 1280
        easein_elastic 0.35 xpos 640
        xpos 0
        easein_elastic 0.35 xpos 640
show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
show glitch_color onlayer front


pause 3.0
play sound "<from 0.69>sfx/monikapound.ogg"
scene white
pause 1

show layer screens:
    truecenter
    parallel:
        zoom 1.5
        easeout 0.35 zoom 1.0
    parallel:
        xpos 0
        easein_elastic 0.35 xpos 640
show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
show glitch_color2 onlayer front
window show(None)
scene black
pause 4.0
hide noise onlayer front
hide glitch_color onlayer front

"..."
$ run_input("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
m "C-come onnn.."
$ run_input("renpy.file(\"characters/monika.chr\")", "monika.chr does not exist.")
m "Please, I just wanna see him again."
$ run_input("renpy.file(\"characters/monika.chr\")", "monika.chr exists.")
$ run_input("", "Restarting Scripts... Please Wait.")
m "There!"

"..."
"..."
pause 4
hide screen console_screen with dissolve
scene bg club_day
with dissolve_scene_full
"..."
m "Uhh..."
show monika 1o at t11
m "Hmmm.."
m 3b "Oh! Here we are!"
m 1k "Everything has been reset to the way it was."
show monika 1m at t11
"Monika pats her body."
m 3n "I feel fine.."
m 1o "..."
m 4k "Okay I think I'm good!"
m 4l "Oh jeez.. that was really scary.."
m 2m "I never knew putting yourself back together would hurt so bad."
m 1o "..."
m 1d "Now where was I..."
m 2c "..."
m 3l "Actually.. I should probably text and make sure everyone else is okay."
"Monika pulls her phone out from her blazer pocket."
m 4b "Let's see.."
play music monikat5
show monika 2a at t11
"Monika texts everyone to make sure they're okay."
m "Well, that was something."
m 2j "It looks like the script is back in working order too!"
m 1h "Hmmm.. I'm not sure where the script is gonna go from here on out.."
show monika 2q at t11
"Monika puts her phone back in her pocket and begins to ponder."
"..."
show monika 2o at t11
scene black
with dissolve_scene_full
pause 3.0
call chap1 from _call_chap1 
