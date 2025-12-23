default choice_leaving_rooftop = None # To track how they decide to leave
label picnic:
    scene bg school_outside
    j "Smells like someone deep fried an entire cookbook out here."
    show monika forward neut rdown om e2a b2a at t11
    m "Welcome to the chaos. That's the Culinary Club somewhere near the gym."
    show monika forward neut rdown cm e2a b2a
    
    j "Please tell me they're handing out free samples before I start gnawing on a booth sign."
    show monika forward happ lpoint om e2c b1a
    m "Not just samples. They're doing picnic boxes this year."
    show monika forward happ lpoint cm e2c b1a
    
    j "You're kidding. Like actual sit down food?"
    show monika forward happ rdown ldown om e2b b1a
    m "Tablecloths, bento trays, hand folded menus... the whole thing."
    show monika forward happ rdown ldown cm e2b b1a
    
    "I follow Monika through the current of the festival crowd. There's a rhythm to it."
    "laughter rippling over music, kids weaving between legs, the soft rustle of hanging decorations brushing against each other."
    "Paper lanterns sway above us, flickering with warm golden light. The sun is bright, casting a warm glow over everything."
    stop music fadeout 2.0
    scene bg festival_vendor zorder 2
    show clouds zorder 1
    with dissolve_scene_full
    play music chy2
    "The smell hits me like a memory savory, sweet, grilled, glazed, fried. It's nostalgia and comfort wrapped in steam."
    "My stomach rumbled a protest. Every direction I look, there's another delicious scent pulling me in."
    "To my left, the sweet, sugary cloud of cotton candy. To my right, the sharp, vinegary tang of something pickled."
    "Straight ahead, the rich, savory aroma of grilled meat. It's a sensory overload, and I'm completely unprepared."
    
    j "This is cheating. Everything smells good. How am I supposed to commit to one stall?"
    show monika forward happ rdown om e2d b1a at t11 zorder 3
    m "That's what makes the Culinary Club different. They're not just feeding you. They're curating an experience."
    show monika forward happ rdown cm e2d b1a
    
    j "Why does that sound mildly threatening coming from you?"
    show monika forward laug lpoint om e1b b1a
    "Monika laughs softly, a light sound that cuts through the festival din. She tugs my sleeve gently, a familiar gesture, steering me away from the immediate temptation."
    show monika forward laug lpoint cm e1b b1a
    
    "We navigate the throng. It's a river of people, flowing around booths and games. Kids chase stray balloons, couples walk hand in hand, groups of friends laugh loudly."
    "The air is thick with the scent of food, the murmur of conversations, and the cheerful, slightly off key sound of a student band playing somewhere in the distance."
    "We pass by a stall selling brightly colored shaved ice."
    "The ice shaving machine whirring rhythmically. Further on, someone is demonstrating traditional calligraphy, their brush moving with practiced ease."
    "Everywhere, there's something to see, something to hear, something to smell."
    "We continue our journey through the festival."
    
    j "I swear, if the Culinary Club hands me food that's prettier than anything I've ever written, I'm going to cry."
    show monika forward happ rdown om e2c b1a
    m "Tears pair well with grilled eggplant. So I've heard."
    show monika forward happ ldown rdown cm e2c b1a
    
    "Her tone is light, teasing, but there's an underlying warmth to it."
    "As we get closer to the gym, the festival noise dips slightly. It's still there energy buzzing at the edges but it's softer here. Focused."
    "Like even the air knows to quiet down for good food."
    
    scene bg school_culinary_booth
    with dissolve_scene_full
    "The Culinary Club has gone absolutely feral in the best way possible. There are tablecloths. Hanging herbs. Tiny signs like they're trying to win the handwriting Olympics."
    "Students in aprons are zooming around like caffeinated ballet dancers. One is torching sugar with terrifying precision."
    "Another folds menus like origami is a competitive sport. Someone's balancing tea cups that look like they belong in a dollhouse."
    # add in aiden image later

    aiden "Yo. You hungry or just here to admire the basil hanging like wind chimes?"
    j "Wait wait wait. Aiden? You're in the Culinary Club?"
    aiden "You say that like it's unknown information?"
    j "I just... nevermind. I'll just take a picnic set."
    aiden "I'm not sure that's a good idea."
    j "Why not?"
    aiden "Well, you see, I'm not exactly sure how to cook for two."
    j "You're not?"
    aiden "Nah. I'm more of a one person show kind of guy."
    j "What the fuck are you even talking about?"
    "Aiden hands Jacko a bento box with a picnic set."
    show monika forward curi rhip om e2a b2a at t11
    "Monika takes it like it's a baby bird made of truffle oil and secrets."
    show monika forward curi rhip cm e2a b2a
    
    aiden "There's a little fortune inside. Festival tradition. No refunds if it causes an existential crisis."
    aiden "See you fuckers later!"
    "Aiden runs off to find his next victim."
    $ CharacterBio.aiden.unlock()
    call track_character_unlock("aiden") from _call_track_character_unlock
    
    show monika forward happ lpoint om e2b b1a
    m "You have some really weird friends Jacko."
    show monika forward happ ldown rhip cm e2b b1a
    
    j "I know. I'm working on it."
    show monika forward curi rdown om e2c b2a
    m "Where do you even eat something like this? I feel like if we open it near loud people it'll take damage."
    show monika forward curi rdown cm e2c b2a
    
    j "The rooftop. Obviously."
    show monika forward happ rdown ldown om e2d b1a
    m "Of course. You planned this. You're always ten steps ahead."
    m "Alright, let's go."
    show monika forward happ rdown ldown cm e2d b1a
    
    j "Lead the way."
    
    scene bg corridor
    with fade
    "We step away from the festival lights and into the quiet of the school building. The sound dims."
    "The floor feels cooler beneath our feet. The only light comes from tall windows, casting long shadows across the walls. It's still bright outside, but the school's interior is shaded and calm."
    "Our steps echoed."
    
    j "Weird how fast the world goes quiet when you're not trying to impress it."
    show monika forward dist rdown om e2b b2a at t11
    m "It's why I like this part of the school. The noise falls away, and all that's left is... what's real."
    show monika forward dist rdown cm e2b b2a
    
    scene bg stairs
    with dissolve
    "Stairwells are usually sterile. But right now, this one feels soft. Like something in between. Not part of the festival. Not part of class. Just a space to pass through gently."
    "I glanced at Monika. She's holding the bento box like it's a story we haven't opened yet."
    "The climb up the stairs is quiet, save for our footsteps. Each step takes us further away from the noise below, closer to the open sky."
    
    j "Think the sun's still high?"
    show monika forward happ lpoint om e2c b1a at t11
    m "Only one way to find out."
    show monika forward happ lpoint cm e2c b1a
    
    scene bg roof
    with fade
    stop music fadeout 4.0
    "The rooftop opens above us like a held breath finally released."
    "The city stretches out far beyond the railing. The sky is a clear blue, vast and open above us."
    show monika forward dist rdown om e2a b2a at t11
    "Monika looks around, assessing the space. The wind tugs at her hair."
    show monika forward dist rdown cm e2a b2a
    
    "Monika spreads out a small picnic cloth. The wind tugs at the corners, playful but not disruptive. She anchors it with smooth stones from her bag."
    
    j "You seriously came prepared."
    show monika forward happ rdown om e2d b1a
    m "The best moments deserve preparation."
    show monika forward happ rdown cm e2d b1a
    
    "She sets the bento box between us, unwrapping it slowly, like a gift too special to rush."
    "You both sat in the bright daylight. The world around you stills."
    "The box between you is open now and so is the moment. Like a held breath has finally been released."
    "A breeze shifted the paper napkins gently, brushing one against your leg like a reminder:"
    "You're here. Pay attention."
    
    show monika forward dist rdown om e2b b2a
    m "Can I ask you something?"
    show monika forward dist rdown cm e2b b2a
    
    j "You don't have to ask. Just say it."
    "That came out more abruptly than I intended, but Monika just laughs and asks her question."
    
    call track_cg_mrail from _call_track_cg_mrail
    show m_cg_rail_1a zorder 4
    show clouds zorder 3
    show y_cg2_dust1 zorder 4
    show y_cg2_dust2 zorder 4
    show y_cg2_dust3 zorder 4
    show y_cg2_dust4 zorder 4
    show m_cg_cafeEvent_shaft1 zorder 4
    show m_cg_cafeEvent_shaft2 zorder 4
    show m_cg_cafeEvent_shaft3 zorder 4
    with dissolve_cg
    
    m "..."
    hide m_cg_rail_1a
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "What makes something matter to you?"
    hide m_cg_rail_1e
    show m_cg_rail_1c zorder 4
    with dissolve_cg
    play music rail
    
    window hide
    $ renpy.pause(8.0, hard=True)
    
    "You looked at her. Not for too long. Just long enough to understand that she actually wanted to know."
    "And then, you started talking. Not like you planned it. Not like you practiced it. Just... like the words had been sitting there, waiting for someone to ask."
    
    hide m_cg_rail_1c
    show m_cg_rail_1a zorder 4
    with dissolve_cg
    
    j "I think... things matter when they change you. Not in a fireworks and confetti way. Not even in a way you notice right away."
    j "But the small kind of change. The kind you only see in hindsight. The kind that sneaked into your voice when you're telling a story three years later, and you realized you told it differently now."
    j "It's not about size. It's about weight. Some things feel light when they happen, but they settled in your chest like they'd been there forever."
    j "Like a quiet look across a classroom. Or the first time someone reads something you wrote and didn't say 'that's nice,' but says, 'I felt that.'"
    j "Or this. Right now."
    
    "You paused. Just because you wanted to make space for the moment."
    hide m_cg_rail_1a
    show m_cg_rail_1c zorder 4
    with dissolve_cg
    window hide
    $ renpy.pause(5.0, hard=True)
    
    hide m_cg_rail_1c
    show m_cg_rail_1a zorder 4
    with dissolve_cg
    
    j "I think... something matters when it makes you want to be a better version of yourself. Even if just for a second."
    j "Like, you looked at someone and thought I want to say the right thing for them. Not because you're trying to impress them. But because they deserved the right thing."
    j "And sometimes you didn't say anything at all. But the wanting, that pull inside you, that's what sticks. That's what leaves a mark."
    
    "You glanced at Monika. She's listening. Really listening. No polite smile. No waiting for her turn to speak. Just... presence."
    hide m_cg_rail_1a
    show m_cg_rail_1b zorder 4
    with dissolve_cg
    
    j "It's also the things that disappear. That sounds weird, but I think things matter when they leave a little silence behind."
    j "Like finishing a manga and just sitting there, staring at the last page. Not ready to close it. Because if you closed it, it meant it was over."
    
    "Monika nodded. Like she got it."
    hide m_cg_rail_1b
    show m_cg_rail_1d zorder 4
    with dissolve_cg
    
    j "Or a conversation that ended with a look, not a goodbye. Because something got said that didn't need words."
    j "Or a song that played on a loop for a week, and then stopped. And your brain still sang it. Quietly."
    j "That's what matters. The things that echoed."
    
    "The breeze shifted again. A cloud passed slowly across the sky. Monika hadn't moved."
    hide m_cg_rail_1d
    show m_cg_rail_1a zorder 4
    with dissolve_cg
    
    j "And I guess... it mattered more when you're seen. Just seen."
    j "Like someone noticed when your voice cracked a little when you talked about your dad. Or when you fidgeted with your sleeve when you're nervous."
    j "And they didn't point it out. They just... made room for it."
    j "That's what you did."
    
    window hide
    $ renpy.pause(15.0, hard=True)
    
    hide m_cg_rail_1a
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "...What do I do?"
    hide m_cg_rail_1e
    show m_cg_rail_1c zorder 4
    with dissolve_cg
    
    j "You made room. For people. For thoughts that didn't quite know how to be said. For quiet."
    "You heard her exhale. Like she'd been holding her breath this whole time."
    
    hide m_cg_rail_1c
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "You don't say things like other people do Jacko."
    hide m_cg_rail_1e
    show m_cg_rail_1a zorder 4
    with dissolve_cg
    
    j "R-really? I mean I try to be a little different."
    
    if haunted_house_completed:
        hide m_cg_rail_1a
        show m_cg_rail_1b zorder 4
        with dissolve_cg
        "HOLY SHIT THANK YOU YURI FOR NOT BEING A FUCKING IDIOT."
        hide m_cg_rail_1b
        show m_cg_rail_1a zorder 4
        with dissolve_cg
    else:
        hide m_cg_rail_1a
        show m_cg_rail_1e zorder 4
        with dissolve_cg
        m "No. You say them like someone who means them."
        hide m_cg_rail_1e
        show m_cg_rail_1d zorder 4
        with dissolve_cg
    
    "You smiled, Like warmth from a fire you didn't notice you were close to."
    
    j "Maybe that's why this mattered. This moment. You. Me. A shared meal on a rooftop."
    j "Because there's no performance here. No roles. Just two people sitting still long enough to feel something."
    
    hide m_cg_rail_1d
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "You made it sound like a poem Jacko..."
    m "Are you sure you're not a poet?"
    hide m_cg_rail_1e
    show m_cg_rail_1b zorder 4
    with dissolve_cg
    
    j "I mean I could be, Monika who's to say?"
    
    window hide
    $ renpy.pause(15.0, hard=True)
    
    hide m_cg_rail_1b
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "Do you think you'll remember this?"
    hide m_cg_rail_1e
    show m_cg_rail_1a zorder 4
    with dissolve_cg
    
    j "I know I will. because it's honest. And things that are honest they don't fade the same way."
    
    hide m_cg_rail_1a
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "They became anchors."
    hide m_cg_rail_1e
    show m_cg_rail_1c zorder 4
    with dissolve_cg
    
    j "Yeah. So even when you drifted, they're still there. Holding something in place."
    
    hide m_cg_rail_1c
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "...That might be the most beautiful thing I've ever heard about a picnic."
    hide m_cg_rail_1e
    show m_cg_rail_1d zorder 4
    with dissolve_cg
    
    $ CharacterBio.jacko.unlock()
    window hide
    $ renpy.pause(10.0, hard=True)
    
    menu(timers = [0, 4, 12], start_time=datetime.datetime.now()):
        "You should hear my speech about you.":
            j "You should hear my speech about you Monika."
            "A warmth spread through you at the thought of it. It felt easy, natural."
            "You could talk about the way her eyes caught the light, the quiet strength in her smile, the surprising depth you'd found in her when you least expected it."
            "It would be a good speech."
            
            hide m_cg_rail_1d
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "Oh? And what would that one be about?"
            hide m_cg_rail_1e
            show m_cg_rail_1a zorder 4
            with dissolve_cg
            
            j "Just... you know. Things. Ways you surprised people. Ways you made them think. Ways you made them feel seen."
            
            hide m_cg_rail_1a
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "That sounds... like a very specific speech."
            hide m_cg_rail_1e
            show m_cg_rail_1c zorder 4
            with dissolve_cg
            
            j "Maybe it is."
            
            hide m_cg_rail_1c
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "I'd like to hear it someday."
            hide m_cg_rail_1e
            show m_cg_rail_1a zorder 4
            with dissolve_cg
            
            j "It's a work in progress. Needs more data."
            
            hide m_cg_rail_1a
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "Is that my cue to continue being surprising?"
            hide m_cg_rail_1e
            show m_cg_rail_1b zorder 4
            with dissolve_cg
            
            j "Consider it permission granted."
            call rizz_update(points_change=+2) from _call_rizz_update
            
        "You should hear my speech about grilled onions.":
            j "You should hear my speech about grilled onions."
            "You said it lightly, a joke to break the weight of the moment, but there's a flicker of something genuine there too."
            "Grilled onions did matter. In their own small, savory way."
            
            hide m_cg_rail_1d
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "Grilled onions? Riveting."
            hide m_cg_rail_1e
            show m_cg_rail_1a zorder 4
            with dissolve_cg
            
            j "Hey, don't knock it till you've heard the full fifteen minutes on caramelization techniques."
            
            hide m_cg_rail_1a
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "Alright, alright. Point taken. There's a time and a place for all speeches."
            hide m_cg_rail_1e
            show m_cg_rail_1b zorder 4
            with dissolve_cg
            
            j "Exactly. Like right now, if you'd like a deep dive into the Maillard reaction..."
            
            hide m_cg_rail_1b
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "I think I'll stick to the present moment, thank you. It's quite interesting enough."
            hide m_cg_rail_1e
            show m_cg_rail_1d zorder 4
            with dissolve_cg
            
            call rizz_update(points_change=-2) from _call_rizz_update_1
            
        "You should hear my speech about your poetry.":
            j "You should hear my speech about your poetry Monika."
            "The words left a slight taste of reverence in your mouth. Her poems... they definitely mattered."
            "They're raw and beautiful and sometimes a little frightening."
            "Saying this felt like stepping onto a different kind of fragile ground."
            
            hide m_cg_rail_1d
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "My poetry?"
            hide m_cg_rail_1e
            show m_cg_rail_1c zorder 4
            with dissolve_cg
            
            "Her voice was softer now, a hint of surprise in it."
            
            j "Yeah. The way you... peeled things open. The way you made vulnerability sound like the bravest thing in the world."
            
            hide m_cg_rail_1c
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "I... I didn't know you felt that way."
            hide m_cg_rail_1e
            show m_cg_rail_1c zorder 4
            with dissolve_cg
            
            j "They mattered. A lot."
            "You met her gaze, letting the sincerity sit between you."
            
            hide m_cg_rail_1c
            show m_cg_rail_1e zorder 4
            with dissolve_cg
            m "Thank you, Jacko. That... meant a great deal."
            hide m_cg_rail_1e
            show m_cg_rail_1d zorder 4
            with dissolve_cg
            
            j "Good. It was meant to."
            call update_mj_art from _call_update_mj_art
            call rizz_update(points_change=+4) from _call_rizz_update_2
    
    window hide
    $ renpy.pause(5.0, hard=True)
    
    hide m_cg_rail_1d
    hide m_cg_rail_1b
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "Save that one for our second rooftop meal."
    stop music fadeout 2.0
    hide m_cg_rail_1e
    show m_cg_rail_1b zorder 4
    with dissolve_cg
    
    j "Is that a promise?"
    
    hide m_cg_rail_1b
    show m_cg_rail_1e zorder 4
    with dissolve_cg
    m "It's a plan."
    hide m_cg_rail_1e

    hide m_cg_rail_1a
    hide m_cg_rail_1b
    hide clouds zorder 3
    hide y_cg2_dust1 zorder 4
    hide y_cg2_dust2 zorder 4
    hide y_cg2_dust3 zorder 4
    hide y_cg2_dust4 zorder 4
    hide m_cg_cafeEvent_shaft1 zorder 4
    hide m_cg_cafeEvent_shaft2 zorder 4
    hide m_cg_cafeEvent_shaft3 zorder 4

    with dissolve_cg
    play music somethingreal
    "The air on the rooftop felt lighter now. The earlier intensity hadn't vanished, but it's mingled with something softer, something shared."
    "Monika reached for the bento box again, her fingers tracing the pattern on the cloth wrap."
    
    show monika forward happ lpoint om e2c b1a at t11
    m "Shall we see what edible poetry awaited?"
    show monika forward happ lpoint cm e2c b1a
    
    j "Lead the way, curator."
    "She smiled, a genuine, unburdened smile that reached her eyes."
    show monika forward happ rdown ldown om e2b b1a
    "Monika carefully unties the ribbon and folded back the cloth, revealing the bento box within. It's made of wood, divided into neat compartments."
    show monika forward happ rdown ldown cm e2b b1a
    "Inside, it's a miniature landscape of flavors and colors."
    "There were glistening slices of something grilled."
    "Arranged neatly over rice. Small, colorful pickles in another section. Bright green edamame. A couple of perfectly rolled pieces of tamagoyaki the Japanese omelet looking soft and slightly sweet."
    "And in a tiny, separate dish, a dollop of vibrant, almost fluorescent green paste wasabi?"
    
    j "Wow. They really went all out."
    
    show monika forward happ rhip lpoint om e2d b1a
    m "I told you. It's an experience."
    show monika forward happ rhip lpoint cm e2d b1a
    
    "She picked up a set of disposable chopsticks, offering one pair to you."
    
    j "Okay, where do we even start?"
    
    show monika forward happ rdown lpoint om e2c b1a
    m "Let's find the note first. Festival tradition, remember?"
    show monika forward happ rdown lpoint cm e2c b1a
    
    "Monika gently sifted through the contents of one of the larger compartments. Her fingers brushed past the grilled slices, the pickles..."
    "Ah, there it was. Tucked beneath a leaf of lettuce."
    "A small, folded piece of paper, tied with a thin string. Simple, but elegant."
    show monika forward happ rdown ldown om e2a b1a
    "She unties the string and unfolded the paper carefully. You leaned closer to read it together."
    show monika forward happ rdown ldown cm e2a b1a
    "The note was handwritten in neat, flowing script."
    "The quiet spaces between the notes were just as important as the melody."
    "You read the line aloud."
    
    j "The quiet spaces between the notes..."
    
    show monika forward happ rhip lpoint om e2b b1a
    m "Just as important as the melody."
    show monika forward happ rhip lpoint cm e2b b1a
    
    "Monika looked up from the note, her gaze thoughtful."
    
    show monika forward dist rdown ldown om e2a b2a
    m "It fit, didn't it? With what we were just talking about."
    show monika forward dist rdown ldown cm e2a b2a
    
    j "Yeah. The things that mattered, even when they weren't loud. The pauses. The silence. The space between words."
    
    show monika forward dist rhip ldown om e2c b2a
    m "The space where things settled."
    show monika forward dist rhip ldown cm e2c b2a
    
    "She refolded the note and placed it carefully back in the box."
    
    show monika forward happ rdown lpoint om e2d b1a
    m "So, what's the first 'note' we should experience?"
    show monika forward happ rdown lpoint cm e2d b1a
    
    "You looked at the bento box again, seeing it differently now. Not just food, but a collection of curated moments."
    
    j "Those grilled slices looked pretty inviting."
    
    show monika forward happ rdown ldown om e2b b1a
    m "They did. Smelled like it might be marinated pork."
    show monika forward happ rdown ldown cm e2b b1a
    "You both reached for the grilled slices at the same time, chopsticks clinking softly."
    "You each took a piece. The meat was tender, slightly smoky, with a hint of sweetness from the marinade."
    show monika forward happ rhip lpoint om e2c b1a
    j "Okay, that's... seriously good."
    show monika forward happ rhip lpoint cm e2c b1a
    
    show monika forward happ rhip lpoint om e2d b1a
    m "Mhm."
    show monika forward happ rhip lpoint cm e2d b1a
    
    "Monika hummed in agreement, savoring the flavor."
    show monika forward curi rdown ldown om e2a b2a
    m "There was a subtle spice, too. Almost like ginger or star anise."
    show monika forward curi rdown ldown cm e2a b2a
    
    show monika forward curi rhip lpoint om e2b b2a
    j "You could pick out individual spices?"
    show monika forward curi rhip lpoint cm e2b b2a
    
    show monika forward happ rdown lpoint om e2c b1a
    m "My palate had been... refined. By necessity."
    show monika forward happ rdown lpoint cm e2c b1a
    
    "She gave you a knowing look. You remembered the chaos of the culinary club booth."
    show monika forward happ rdown ldown om e2d b1a
    j "I'll bet. I just knew it tasted like 'more'."
    show monika forward happ rdown ldown cm e2d b1a
    
    "You took another piece."
    show monika forward curi rhip lpoint om e2a b2a
    m "Try the pickles. They looked like they'd cut through the richness of the meat."
    show monika forward curi rhip lpoint cm e2a b2a
    
    "You took a small, bright pink pickle. It was crisp and slightly tangy, a perfect counterpoint to the grilled pork."
    show monika forward happ rdown ldown om e2b b1a
    j "You're right. That's smart."
    show monika forward happ rdown ldown cm e2b b1a
    
    show monika forward happ rhip lpoint om e2c b1a
    m "The chefs here knew what they were doing."
    show monika forward happ rhip lpoint cm e2c b1a
    
    "You continued eating slowly, deliberately, talking about the different components of the meal."
    "The tamagoyaki was fluffy and sweet, like a soft, comforting cloud."
    "The edamame was simple, salty perfection."
    "You carefully avoided the bright green paste for now."
    show monika forward curi rdown ldown om e2a b2a
    j "So, the note... about the quiet spaces. Do you think they meant it literally, or...?"
    show monika forward curi rdown ldown cm e2a b2a
    
    show monika forward dist rhip lpoint om e2c b2a
    m "I think it was meant to be open to interpretation. Like poetry. It could mean whatever resonated with you in the moment."
    show monika forward dist rhip lpoint cm e2c b2a
    
    show monika forward dist rdown ldown om e2b b2a
    j "For me, it resonated with... well, with us. And with what we were just talking about."
    show monika forward dist rdown ldown cm e2b b2a
    
    show monika forward dist rhip lpoint om e2d b2a
    m "Me too."
    show monika forward dist rhip lpoint cm e2d b2a
    
    "She met your eyes again, and for a moment, the city lights, the festival noise below, the food in front of you it all faded away."
    "There was just the two of you, the quiet space you'd created, and the understanding passing between you without words."
    window hide
    $ renpy.pause(5.0, hard=True)
    show monika forward dist rdown ldown om e2a b2a
    j "It's weird."
    show monika forward dist rdown ldown cm e2a b2a
    
    show monika forward curi rhip lpoint om e2c b2a
    m "What is?"
    show monika forward curi rhip lpoint cm e2c b2a
    
    show monika forward dist rdown ldown om e2b b2a
    j "How... comfortable this was. On a rooftop. In the bright daylight, basically. With someone I argued with half the time."
    show monika forward dist rdown ldown cm e2b b2a
    
    "Monika laughed softly."
    show monika forward laug rdown ldown om e2c b1a
    m "Is that how you saw it? Arguing?"
    show monika forward laug rdown ldown cm e2c b1a
    
    show monika forward dist rhip lpoint om e2d b2a
    j "Debating. Discussing. Spirited exchange of ideas. Whatever you wanted to call it. Point was, it's not... conventionally relaxing."
    show monika forward dist rhip lpoint cm e2d b2a
    
    show monika forward dist rdown ldown om e2a b2a
    m "Maybe conventions were overrated."
    show monika forward dist rdown ldown cm e2a b2a
    
    show monika forward dist rhip lpoint om e2b b2a
    j "Maybe."
    show monika forward dist rhip lpoint cm e2b b2a
    
    "You looked out at the city lights again. They twinkled faintly in the daytime sun."
    show monika forward dist rdown ldown om e2a b2a
    j "It felt like... like we were outside of everything. Watching the world go by."
    show monika forward dist rdown ldown cm e2a b2a
    
    show monika forward dist rhip lpoint om e2c b2a
    m "In our own quiet space."
    show monika forward dist rhip lpoint cm e2c b2a
    
    show monika forward dist rdown ldown om e2b b2a
    j "Yeah. Our own quiet space."
    show monika forward dist rdown ldown cm e2b b2a
    
    "You finished the grilled pork. Monika picked up a piece of tamagoyaki."
    show monika forward curi rhip lpoint om e2a b2a
    m "Are you going to try the wasabi?"
    show monika forward curi rhip lpoint cm e2a b2a
    
    show monika forward curi rdown ldown om e2d b2a
    j "Is that a dare?"
    show monika forward curi rdown ldown cm e2d b2a
    
    show monika forward happ rhip lpoint om e2b b1a
    m "It could be. Or it could be an invitation to experience a different kind of intensity."
    show monika forward happ rhip lpoint cm e2b b1a
    
    show monika forward curi rdown lpoint om e2c b2a
    j "Hmm."
    show monika forward curi rdown lpoint cm e2c b2a
    
    "You looked at the small dish of bright green paste. It practically vibrated with potential heat."
    show monika forward happ rdown ldown om e2d b1a
    j "Okay. Invitation accepted."
    show monika forward happ rdown ldown cm e2d b1a
    
    "You carefully picked up a tiny amount with your chopsticks. Just a smudge."
    "You put it in your mouth with a piece of rice."
    "For a second, nothing happened. Then..."
    "It hit. A clean, sharp heat that shot straight up your nose."
    "Your eyes watered slightly. You tried to keep a straight face."
    show monika forward laug rhip lpoint om e2b b1a
    m "Oh dear. Was that... a significant intensity?"
    show monika forward laug rhip lpoint cm e2b b1a
    
    "Your voice was strained."
    show monika forward anno rdown lpoint om e2c b1a
    j "It was... present."
    show monika forward anno rdown lpoint cm e2c b1a
    
    "Monika giggled."
    show monika forward laug rdown ldown om e2d b1a
    m "You should have taken a smaller amount."
    show monika forward laug rdown ldown cm e2d b1a
    
    show monika forward anno rhip lpoint om e2a b1a
    j "It was a small amount!"
    show monika forward anno rhip lpoint cm e2a b1a
    
    show monika forward laug rdown lpoint om e2c b1a
    m "Perhaps you were more sensitive to 'different kinds of intensity' than you thought."
    show monika forward laug rdown lpoint cm e2c b1a
    
    show monika forward anno rdown ldown om e2b b1a
    j "Hey! I'm just... experiencing the full spectrum of curated flavors!"
    show monika forward anno rdown ldown cm e2b b1a
    
    "She laughed again, a genuine, warm sound."
    show monika forward happ rdown ldown om e2d b1a
    m "Very diplomatic."
    show monika forward happ rdown ldown cm e2d b1a
    
    "You reached for your drink a small bottle of chilled green tea that came with the box and took a long sip."
    "Ah, relief."
    show monika forward happ rhip lpoint om e2c b1a
    j "Okay. Wasabi: experienced. Point taken."
    show monika forward happ rhip lpoint cm e2c b1a
    
    show monika forward happ rdown ldown om e2b b1a
    m "See? Even the challenges were part of the experience."
    show monika forward happ rdown ldown cm e2b b1a
    
    show monika forward anno rhip lpoint om e2a b1a
    j "Yeah, yeah, I get it. Life lessons via spicy paste."
    show monika forward anno rhip lpoint cm e2a b1a
    
    "You both settled back, finishing the last few bites of the bento."
    "The sky above was a vast, clear blue." 
    show monika forward happ rdown ldown om e2d b1a
    j "It was a good picnic."
    show monika forward happ rdown ldown cm e2d b1a
    
    show monika forward happ rhip lpoint om e2b b1a
    m "It was."
    show monika forward happ rhip lpoint cm e2b b1a
    
    "You packed up the chopsticks and the empty containers, putting them back in the box."
    "Monika folded the picnic cloth neatly."

    menu:
        "Suggest heading back to the main festival area.":
            j "Ready to head back to the main festival? Still plenty to see and do."
            show monika forward happ rdown om e2c b1a at t11
            m "Alright. The chaos awaited."
            show monika forward happ rdown cm e2c b1a
            $ choice_leaving_rooftop = "festival"
            "You gathered your things, preparing to rejoin the crowds below."

        "Suggest finding a quiet spot on the school grounds.":
            j "Maybe we could find a quieter spot on the school grounds? Away from the main festival, but not quite back inside."
            show monika forward happ rdown om e2d b1a at t11
            m "That sounded nice. A gentle transition."
            show monika forward happ rdown cm e2d b1a
            $ choice_leaving_rooftop = "school_grounds"
            "You decided to look for a bench under a tree or a less crowded corner of the campus."

        "Suggest just staying on the rooftop a little longer.":
            j "Can we... just stay up here a little longer?"
            show monika forward happ rdown om e2b b1a at t11
            m "Of course."
            show monika forward happ rdown cm e2b b1a
            $ choice_leaving_rooftop = "stay_longer"
            "You settled back down, not quite ready to leave the peaceful quiet of the rooftop."
            scene bg roof
            with dissolve_scene_full

    m "We should probably head down soon. Before someone wondered where the club president disappeared to."
    j "Right. Duty called."

    if choice_leaving_rooftop == "festival":
        show monika forward dist rdown om e2a b2a at t11
        "You walked towards the door leading back inside the school building, ready to dive back into the energy of the festival."
        show monika forward dist rdown cm e2a b2a
        scene bg festival_corridor
        with fade
        "We stepped back inside the school building. The sound of the festival was still distant here."
        "You walked down the stairs, the echo of your footsteps a familiar sound now."
        "The school building felt different on the way down. Less like a place you had to be, more like a place you'd shared a moment in."
        scene bg corridor_pov
        with dissolve
        "Back in the hallway, the light from the windows seemed a little brighter now."
        "You reached the ground floor, the sounds of the festival growing louder as you approached the exit."
        scene bg school_outside
        with fade
        "Stepping back outside, the full force of the festival hit you again the noise, the smells, the energy."
        "It felt different now, though. Like you'd just come from a secret, quieter world."
        show monika forward happ lpoint om e2c b1a
        m "Well, here we were. Back in the chaos."
        show monika forward happ lpoint cm e2c b1a
        j "Wouldn't have it any other way. Mostly."

    elif choice_leaving_rooftop == "school_grounds":
        show monika forward happ lpoint om e2b b1a at t11
        "You walked towards the door leading back inside the school building, looking for a less crowded path."
        show monika forward happ lpoint cm e2b b1a
        scene bg corridor_pov
        with fade
        "We stepped back inside the school building, the sound of the festival muted."
        "Instead of heading straight for the exit, you took a different turn, looking for a quieter route."
        "You walked down a less used stairwell, the silence more profound here."
        scene bg corridor_pov2
        with dissolve
        "The stairs creaked faintly under your weight. It was peaceful, a stark contrast to the main festival area."
        "You reached a side exit, leading out into a grassy area behind the school."
        scene bg school_bench
        with fade
        "The sunlight was softer here, filtered through the leaves of large trees. It was quiet, a few students sitting on benches or studying under trees."
        show monika forward happ lpoint om e2d b1a at t11
        m "This was nice. Thank you for suggesting it."
        show monika forward happ lpoint cm e2d b1a
        j "Sometimes you just needed a break from the noise."
        show monika forward happ lpoint om e2c b1a
        m "Indeed."
        "You found an empty bench and sat down for a moment, the sounds of the festival a distant hum."
        show monika forward happ lpoint om e2b b1a
        m "It was a different kind of quiet space."
        show monika forward happ lpoint cm e2b b1a
        j "Yeah. Still an anchor, though."
        show monika forward happ om e2d b1a
        m "Still an anchor."
        "After a few minutes of comfortable silence, you decided to head back towards the main festival area."
        show monika forward happ lpoint om e2c b1a
        m "Shall we rejoin the festivities?"
        show monika forward happ lpoint cm e2c b1a
        j "Lead the way."
        call unlock_photo(8) from _call_unlock_photo_2
        scene bg school_outside
        with dissolve # Transition back to the main festival area if needed later
    elif choice_leaving_rooftop == "stay_longer":
        show monika forward dist rdown om e2a b2a at t11
        "You settled back down beside Monika, not ready to break the spell of the rooftop's quiet."
        show monika forward dist rdown cm e2a b2a
        "The minutes continued to drift by, the city a distant presence below."
        "You talked a little more, or maybe you just sat in comfortable silence, enjoying the shared moment."
        "The feeling of being in your own quiet space was strong here."
        "Eventually, the light began to soften slightly, hinting that the day was moving on."
        show monika forward dist rdown om e2c b2a
        m "Alright, I think we really should head down now. Before someone sent a search party."
        show monika forward dist rdown cm e2c b2a
        j "Yeah, probably for the best."
        "Reluctantly, you stood up."
        "You walked towards the door leading back inside the school building."
        scene bg corridor_pov
        with fade
        "We stepped back inside the school building. The sound of the festival was still distant here."
        "You walked down the stairs, the echo of your footsteps a familiar sound now."
        "The school building felt different on the way down. Less like a place you had to be, more like a place you'd shared a moment in."
        scene bg corridor_pov2
        with dissolve
        "Back in the hallway, the light from the windows seemed a little brighter now."
        "You reached the ground floor, the sounds of the festival growing louder as you approached the exit."
        scene bg school_outside
        with fade
        "Stepping back outside, the full force of the festival hit you again the noise, the smells, the energy."
        "It felt different now, though. Like you'd just come from a secret, quieter world."
        show monika forward happ lpoint om e2d b1a at t11
        m "Well, here we were. Back in the chaos."
        show monika forward happ lpoint cm e2d b1a
        j "Wouldn't have it any other way. Mostly."
        call unlock_photo(9) from _call_unlock_photo_3
    show monika forward dist rdown om e2b b2a at t11
    "You glanced at Monika. She's looking out at the crowd, a thoughtful expression on her face."
    show monika forward dist rdown cm e2b b2a
    
    j "Hey, Monika?"
    show monika forward curi rdown om e2a b2a
    m "Yes?"
    show monika forward curi rdown cm e2a b2a
    
    j "About that second rooftop meal..."
    show monika forward happ rdown om e2c b1a
    "She turned to you, a hint of a smile playing on her lips."
    m "It's a plan, remember?"
    show monika forward happ rdown cm e2c b1a
    
    j "Just checking."
    show monika forward happ rdown om e2c b1a
    "You smiled back. It felt easy. Natural."
    m "It's a plan, remember?"
    show monika forward happ rdown cm e2c b1a
    
    "The festival buzzed around you, a symphony of sounds and sights."
    "But in the quiet space between you and Monika, there was a different kind of melody playing."
    "And it mattered."
    "You stood there for a moment longer, letting the feeling settle."
    stop music fadeout 2.0
    "Then, together, you stepped back into the flow of the festival crowd, carrying the quiet space with you."
return