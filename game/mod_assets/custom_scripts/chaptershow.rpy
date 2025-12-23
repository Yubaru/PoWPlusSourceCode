# Chapter display screen definition
screen chapter_display(chapter_title):
#chapter_num is the act number(1,2,3 etc)
#chapter_title is the act name(Hello, Just Monika etc)
    modal True
    
    # Black background
    add "white"
    # Chapter text container
    frame:
        background None
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5
            
            text "[chapter_title]":
                style "chapter_header"
                xalign 0.5
            

# Chapter text styles
#I used the games font here
style chapter_header:
    font "gui/font/Halogen.ttf"
    size 120
    color "#ffffff"
    outlines [(4, "#000000", 0, 0)]
    text_align 0.5

style chapter_title:
    font "gui/font/RifficFree-Bold.ttf"
    size 40
    color "#ffffff"
    outlines [(3, "#000000", 0, 0)]
    text_align 0.5

# Usage example:
# show screen chapter_display("Your act number", "Your act name") with Dissolve(1.0)
# $ renpy.pause(3.0, hard=True)
# hide screen chapter_display with Dissolve(1.0)