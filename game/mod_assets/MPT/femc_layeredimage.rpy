default femc_eyepatch = False

# turning this (either here or in the script) on shows an eyepatch over the eye to the player's right side for every sprite, in case you want that
# (would not advise using this with heterochromia since the right eye is the changed one)

default femc_longhair = False

# turning this on gives FeMC longer hair, how fun


#heterochromia script
init python:
    def femc_adjust_attributes(name):
        names = set(name[1:])
        if femc_heterochromia:
            names.add("hc")
        else:
            names.add("nhc")
        return (name[0],)+tuple(names)


#turn this on here or in the script to enable heterochromia, which changes the right eye to blue
default femc_heterochromia = False

define config.adjust_attributes["femc"] = femc_adjust_attributes


# all images are defined here to not have to change them in 2 places with the cross pose (similar to Natsuki's MPT)


image femc_s_face:
    "mod_assets/MPT/femc/s_face.png"



image femc_nose_n1:
    "mod_assets/MPT/femc/nose_n1.png"
image femc_nose_n2:
    "mod_assets/MPT/femc/nose_n2.png"
image femc_nose_n3:
    "mod_assets/MPT/femc/nose_n3.png"
image femc_nose_n4:
    "mod_assets/MPT/femc/nose_n4.png"
image femc_nose_n5:
    "mod_assets/MPT/femc/nose_n5.png"



image femc_mouth_ma:
    "mod_assets/MPT/femc/mouth_ma.png"
image femc_mouth_mb:
    "mod_assets/MPT/femc/mouth_mb.png"
image femc_mouth_mc:
    "mod_assets/MPT/femc/mouth_mc.png"
image femc_mouth_md:
    "mod_assets/MPT/femc/mouth_md.png"
image femc_mouth_me:
    "mod_assets/MPT/femc/mouth_me.png"
image femc_mouth_mf:
    "mod_assets/MPT/femc/mouth_mf.png"
image femc_mouth_mg:
    "mod_assets/MPT/femc/mouth_mg.png"
image femc_mouth_mh:
    "mod_assets/MPT/femc/mouth_mh.png"
image femc_mouth_mi:
    "mod_assets/MPT/femc/mouth_mi.png"
image femc_mouth_mj:
    "mod_assets/MPT/femc/mouth_mj.png"
image femc_mouth_mk:
    "mod_assets/MPT/femc/mouth_mk.png"
image femc_mouth_ml:
    "mod_assets/MPT/femc/mouth_ml.png"
image femc_mouth_ml:
    "mod_assets/MPT/femc/mouth_ml.png"
image femc_mouth_mm:
    "mod_assets/MPT/femc/mouth_mm.png"
image femc_mouth_mn:
    "mod_assets/MPT/femc/mouth_mn.png"
image femc_mouth_mo:
    "mod_assets/MPT/femc/mouth_mo.png"
image femc_mouth_mp:
    "mod_assets/MPT/femc/mouth_mp.png"
image femc_mouth_mq:
    "mod_assets/MPT/femc/mouth_mq.png"
image femc_mouth_mr:
    "mod_assets/MPT/femc/mouth_mr.png"
image femc_mouth_ms:
    "mod_assets/MPT/femc/mouth_ms.png"
image femc_mouth_mt:
    "mod_assets/MPT/femc/mouth_mt.png"
image femc_mouth_mu:
    "mod_assets/MPT/femc/mouth_mu.png"
image femc_mouth_mv:
    "mod_assets/MPT/femc/mouth_mv.png"
image femc_mouth_mw:
    "mod_assets/MPT/femc/mouth_mw.png"
image femc_mouth_mx:
    "mod_assets/MPT/femc/mouth_mx.png"
image femc_mouth_my:
    "mod_assets/MPT/femc/mouth_my.png"



image femc_eyes_e1a:
    "mod_assets/MPT/femc/eyes_e1a.png"
image femc_eyes_e1b:
    "mod_assets/MPT/femc/eyes_e1b.png"
image femc_eyes_e1c:
    "mod_assets/MPT/femc/eyes_e1c.png"
image femc_eyes_e1d:
    "mod_assets/MPT/femc/eyes_e1d.png"
image femc_eyes_e1e:
    "mod_assets/MPT/femc/eyes_e1e.png"
image femc_eyes_e1f:
    "mod_assets/MPT/femc/eyes_e1f.png"
image femc_eyes_e1g:
    "mod_assets/MPT/femc/eyes_e1g.png"
image femc_eyes_e1h:
    "mod_assets/MPT/femc/eyes_e1h.png"
image femc_eyes_e1i:
    "mod_assets/MPT/femc/eyes_e1i.png"
image femc_eyes_e1j:
    "mod_assets/MPT/femc/eyes_e1j.png"
image femc_eyes_e1k:
    "mod_assets/MPT/femc/eyes_e1k.png"
image femc_eyes_e1l:
    "mod_assets/MPT/femc/eyes_e1l.png"
image femc_eyes_e2a:
    "mod_assets/MPT/femc/eyes_e2a.png"
image femc_eyes_e2b:
    "mod_assets/MPT/femc/eyes_e2b.png"
image femc_eyes_e2c:
    "mod_assets/MPT/femc/eyes_e2c.png"
image femc_eyes_e2d:
    "mod_assets/MPT/femc/eyes_e2d.png"
image femc_eyes_e3a:
    "mod_assets/MPT/femc/eyes_e3a.png"
image femc_eyes_e3b:
    "mod_assets/MPT/femc/eyes_e3b.png"
image femc_eyes_e3c:
    "mod_assets/MPT/femc/eyes_e3c.png"
image femc_eyes_e3d:
    "mod_assets/MPT/femc/eyes_e3d.png"
image femc_eyes_e4a:
    "mod_assets/MPT/femc/eyes_e4a.png"
image femc_eyes_e4b:
    "mod_assets/MPT/femc/eyes_e4b.png"
image femc_eyes_e4c:
    "mod_assets/MPT/femc/eyes_e4c.png"
image femc_eyes_e4d:
    "mod_assets/MPT/femc/eyes_e4d.png"
image femc_eyes_e4e:
    "mod_assets/MPT/femc/eyes_e4e.png"
image femc_eyes_e0a:
    "mod_assets/MPT/femc/eyes_e0a.png"
image femc_eyes_e0b:
    "mod_assets/MPT/femc/eyes_e0b.png"
image femc_eyes_e0c:
    "mod_assets/MPT/femc/eyes_e0c.png"



image femc_brow_b1a:
    "mod_assets/MPT/femc/brow_b1a.png"
image femc_brow_b1b:
    "mod_assets/MPT/femc/brow_b1b.png"
image femc_brow_b1c:
    "mod_assets/MPT/femc/brow_b1c.png"
image femc_brow_b1d:
    "mod_assets/MPT/femc/brow_b1d.png"
image femc_brow_b1e:
    "mod_assets/MPT/femc/brow_b1e.png"
image femc_brow_b1f:
    "mod_assets/MPT/femc/brow_b1f.png"
image femc_brow_b2a:
    "mod_assets/MPT/femc/brow_b2a.png"
image femc_brow_b2b:
    "mod_assets/MPT/femc/brow_b2b.png"
image femc_brow_b2c:
    "mod_assets/MPT/femc/brow_b2c.png"
image femc_brow_b3a:
    "mod_assets/MPT/femc/brow_b3a.png"
image femc_brow_b3b:
    "mod_assets/MPT/femc/brow_b3b.png"



image femc_s_scream:
    "mod_assets/MPT/femc/s_scream.png"
image femc_s_shocked:
    "mod_assets/MPT/femc/s_shocked.png"
image femc_s_dizzy:
    "mod_assets/MPT/femc/s_dizzy.png"
image femc_s_tired:
    "mod_assets/MPT/femc/s_tired.png"
image femc_s_furious:
    "mod_assets/MPT/femc/s_furious.png"
image femc_s_oof:
    "mod_assets/MPT/femc/s_oof.png"
image femc_s_ehehe:
    "mod_assets/MPT/femc/s_ehehe.png"


image femc_s_patch:
    "mod_assets/MPT/femc/s_patch.png"
image femc_s_patchlank:
    "mod_assets/MPT/femc/s_patchblank.png"


image femc_s_hairbow:
    "mod_assets/MPT/femc/s_hairbow.png"
image femc_s_haircliip:
    "mod_assets/MPT/femc/s_hairclip.png"


image femc_s_hand:
    "mod_assets/MPT/femc/s_hand.png"
image femc_s_sigh:
    "mod_assets/MPT/femc/s_sigh.png"
    

image femc_s_longhair:
    "mod_assets/MPT/femc/s_longhair.png"
image femc_s_shorthair:
    "mod_assets/MPT/femc/s_shorthair.png"



image femc_1cl:
    "mod_assets/MPT/femc/1cl.png"
image femc_1l:
    "mod_assets/MPT/femc/1l.png"
image femc_1dl:
    "mod_assets/MPT/femc/1dl.png"
image femc_1bl:
    "mod_assets/MPT/femc/1bl.png"
image femc_1blb:
    "mod_assets/MPT/femc/1blb.png"
image femc_2cl:
    "mod_assets/MPT/femc/2cl.png"
image femc_2l:
    "mod_assets/MPT/femc/2l.png"
image femc_2dl:
    "mod_assets/MPT/femc/2dl.png"
image femc_2bl:
    "mod_assets/MPT/femc/2bl.png"
image femc_2blb:
    "mod_assets/MPT/femc/2blb.png"
image femc_3c:
    "mod_assets/MPT/femc/3c.png"
image femc_3:
    "mod_assets/MPT/femc/3.png"
image femc_3d:
    "mod_assets/MPT/femc/3d.png"
image femc_3b:
    "mod_assets/MPT/femc/3b.png"
image femc_3bb:
    "mod_assets/MPT/femc/3bb.png"
image femc_4cl:
    "mod_assets/MPT/femc/4cl.png"
image femc_4l:
    "mod_assets/MPT/femc/4l.png"
image femc_4dl:
    "mod_assets/MPT/femc/4dl.png"
image femc_4bl:
    "mod_assets/MPT/femc/4bl.png"
image femc_4blb:
    "mod_assets/MPT/femc/4blb.png"
image femc_5cl:
    "mod_assets/MPT/femc/5cl.png"
image femc_5l:
    "mod_assets/MPT/femc/5l.png"
image femc_5dl:
    "mod_assets/MPT/femc/5dl.png"
image femc_5bl:
    "mod_assets/MPT/femc/5bl.png"
image femc_5blb:
    "mod_assets/MPT/femc/5blb.png"

image femc_1cr:
    "mod_assets/MPT/femc/1cr.png"
image femc_1r:
    "mod_assets/MPT/femc/1r.png"
image femc_1dr:
    "mod_assets/MPT/femc/1dr.png"
image femc_1br:
    "mod_assets/MPT/femc/1br.png"
image femc_1brb:
    "mod_assets/MPT/femc/1brb.png"
image femc_2cr:
    "mod_assets/MPT/femc/2cr.png"
image femc_2r:
    "mod_assets/MPT/femc/2r.png"
image femc_2dr:
    "mod_assets/MPT/femc/2dr.png"
image femc_2br:
    "mod_assets/MPT/femc/2br.png"
image femc_2brb:
    "mod_assets/MPT/femc/2brb.png"


image femc_hc_e1a:
    "mod_assets/MPT/femc/hc_e1a.png"
image femc_hc_e1b:
    "mod_assets/MPT/femc/hc_e1b.png"
image femc_hc_e1c:
    "mod_assets/MPT/femc/hc_e1c.png"
image femc_hc_e1d:
    "mod_assets/MPT/femc/hc_e1d.png"
image femc_hc_e1e:
    "mod_assets/MPT/femc/hc_e1e.png"
image femc_hc_e1f:
    "mod_assets/MPT/femc/hc_e1f.png"
image femc_hc_e1g:
    "mod_assets/MPT/femc/hc_e1g.png"
image femc_hc_e1h:
    "mod_assets/MPT/femc/hc_e1h.png"
image femc_hc_e1i:
    "mod_assets/MPT/femc/hc_e1i.png"
image femc_hc_e1j:
    "mod_assets/MPT/femc/hc_e1j.png"
image femc_hc_e1k:
    "mod_assets/MPT/femc/hc_e1k.png"
image femc_hc_e1l:
    "mod_assets/MPT/femc/hc_e1l.png"
image femc_hc_e2a:
    "mod_assets/MPT/femc/hc_e2a.png"
image femc_hc_e2b:
    "mod_assets/MPT/femc/hc_e2b.png"
image femc_hc_e2c:
    "mod_assets/MPT/femc/hc_e2c.png"
image femc_hc_e2d:
    "mod_assets/MPT/femc/hc_e2d.png"
image femc_hc_e3a:
    "mod_assets/MPT/femc/hc_e3a.png"
image femc_hc_e3b:
    "mod_assets/MPT/femc/hc_e3b.png"
image femc_hc_e3c:
    "mod_assets/MPT/femc/hc_e3c.png"
image femc_hc_e3d:
    "mod_assets/MPT/femc/hc_e3d.png"
image femc_hc_e4a:
    "mod_assets/MPT/femc/hc_e4a.png"
image femc_hc_e4b:
    "mod_assets/MPT/femc/hc_e4b.png"
image femc_hc_e4c:
    "mod_assets/MPT/femc/hc_e4c.png"
image femc_hc_e4d:
    "mod_assets/MPT/femc/hc_e4d.png"
image femc_hc_e4e:
    "mod_assets/MPT/femc/hc_e4e.png"
image femc_hc_e0a:
    "mod_assets/MPT/femc/hc_e0a.png"
image femc_hc_e0b:
    "mod_assets/MPT/femc/hc_e0b.png"
image femc_hc_e0c:
    "mod_assets/MPT/femc/hc_e0c.png"

image femc_hc_scream:
    "mod_assets/MPT/femc/hc_scream.png"
image femc_hc_shocked:
    "mod_assets/MPT/femc/hc_shocked.png"
image femc_hc_dizzy:
    "mod_assets/MPT/femc/hc_dizzy.png"
image femc_hc_tired:
    "mod_assets/MPT/femc/hc_tired.png"
image femc_hc_furious:
    "mod_assets/MPT/femc/hc_furious.png"
image femc_hc_oof:
    "mod_assets/MPT/femc/hc_oof.png"
image femc_hc_ehehe:
    "mod_assets/MPT/femc/hc_ehehe.png"


layeredimage femc turned: #definitions are for her facing turned.

    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at Flatten
    
    always "femc_s_face" #We always use the basic face.
    

    group eyes:
        attribute nhc default null
        attribute hc null

    group outfit:
        
        attribute uniform default null #normal uniform
        attribute vest null #uniform without the blazer jacket
        attribute jacket null #wearing a green jacket
        attribute shirt null #a white shirt with a green jacket tied around the waist
        attribute shirt2 null #a short sleeved white shirt, no jacket around waist
   
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        attribute owo null #owo
        attribute sus null #suspicious of someone
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template! #who the FUCK uses moods unironically
    
    
    
    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc. #this implies emotions are consciously controlled which can be wrong #also it would work the exact same i think if you didnt use moods and most people dont use moods
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
        attribute pale null #no color in cheeks. defaults for n
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute ldown default if_any(["uniform"]):
            "femc_1cl"
        attribute ldown default if_any(["vest"]):
            "femc_1l"
        attribute ldown default if_any(["jacket"]):
            "femc_1dl"
        attribute ldown default if_any(["shirt"]):
            "femc_1bl"
        attribute ldown default if_any(["shirt2"]):
            "femc_1blb"
        attribute lhip if_any(["uniform"]):
            "femc_2cl"
        attribute lhip if_any(["vest"]):
            "femc_2l"
        attribute lhip if_any(["jacket"]):
            "femc_2dl"
        attribute lhip if_any(["shirt"]):
            "femc_2bl"
        attribute lhip if_any(["shirt2"]):
            "femc_2blb"
        attribute lup if_any(["uniform"]):
            "femc_4cl"
        attribute lup if_any(["vest"]):
            "femc_4l"
        attribute lup if_any(["jacket"]):
            "femc_4dl"
        attribute lup if_any(["shirt"]):
            "femc_4bl"
        attribute lup if_any(["shirt2"]):
            "femc_4blb"
        attribute lpen if_any(["uniform"]):
            "femc_5cl"
        attribute lpen if_any(["vest"]):
            "femc_5l"
        attribute lpen if_any(["jacket"]):
            "femc_5dl"
        attribute lpen if_any(["shirt"]):
            "femc_5bl"
        attribute lpen if_any(["shirt2"]):
            "femc_5blb"
    
    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5)
        attribute rdown default if_any(["uniform"]):
            "femc_1cr"
        attribute rdown default if_any(["vest"]):
            "femc_1r"
        attribute rdown default if_any(["jacket"]):
            "femc_1dr"
        attribute rdown default if_any(["shirt"]):
            "femc_1br"
        attribute rdown default if_any(["shirt2"]):
            "femc_1brb"
        attribute rhip if_any(["uniform"]):
            "femc_2cr"
        attribute rhip if_any(["vest"]):
            "femc_2r"
        attribute rhip if_any(["jacket"]):
            "femc_2dr"
        attribute rhip if_any(["shirt"]):
            "femc_2br"
        attribute rhip if_any(["shirt2"]):
            "femc_2brb"
    
    if femc_longhair:
        "femc_s_longhair"
    else:
        "femc_s_shorthair"

    group nose: 
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "femc_nose_n1"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "femc_nose_n2"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "femc_nose_n3"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "femc_nose_n4"
        attribute nose default if_any(["pale"]):#default nose when "no color in cheeks"
            "femc_nose_n5"
        
        
        #All noses - truncated tags:
        attribute n1:
            "femc_nose_n1"
        attribute n2:
            "femc_nose_n2"
        attribute n3:
            "femc_nose_n3"
        attribute n4:
            "femc_nose_n4"
        attribute n5: #for if you want not even default blush
            "femc_nose_n5"
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","nerv"]):
            "femc_mouth_ma"
        attribute cm default if_any(["neut","worr","anno","dist","doub"]):
            "femc_mouth_md"
        attribute cm default if_any(["lsur","curi"]):
            "femc_mouth_me"
        attribute cm default if_any(["vsur","pout"]):
            "femc_mouth_mf"
        attribute cm default if_any(["shoc"]):
            "femc_mouth_mi"
        attribute cm default if_any(["cry","sad","angr","flus"]):
            "femc_mouth_mj"
        attribute cm default if_any(["vang","pani"]):
            "femc_mouth_mm"
        attribute cm default if_any(["laug","sedu"]):
            "femc_mouth_mn"
        attribute cm default if_any(["yand"]):
            "femc_mouth_mo"
        attribute cm default if_any(["owo"]):
            "femc_mouth_mt"
        attribute cm default if_any(["sus"]):
            "femc_mouth_mw"
        
        #Open Mouths:
        attribute om if_any(["happ","sedu"]):
            "femc_mouth_mb"
        attribute om if_any(["yand","laug"]):
            "femc_mouth_mc"
        attribute om if_any(["neut","dist"]):
            "femc_mouth_me"
        attribute om if_any(["worr","vsur","pout"]):
            "femc_mouth_mg"
        attribute om if_any(["flus","anno"]):
            "femc_mouth_mh"
        attribute om if_any(["lsur","curi"]):
            "femc_mouth_mi"
        attribute om if_any(["sad"]):
            "femc_mouth_mk"
        attribute om if_any(["cry","shoc"]):
            "femc_mouth_ml"
        attribute om if_any(["vang","angr","doub","pani"]):
            "femc_mouth_mq"
        attribute om if_any(["nerv"]):
            "femc_mouth_ms"
        attribute om if_any(["owo","sus"]):
            "femc_mouth_mf"
        
        
        ###All mouths - truncated tags:
        attribute ma:
            "femc_mouth_ma"
        attribute mb:
            "femc_mouth_mb"
        attribute mc:
            "femc_mouth_mc"
        attribute md:
            "femc_mouth_md"
        attribute me:
            "femc_mouth_me"
        attribute mf:
            "femc_mouth_mf"
        attribute mg:
            "femc_mouth_mg"
        attribute mh:
            "femc_mouth_mh"
        attribute mi:
            "femc_mouth_mi"
        attribute mj:
            "femc_mouth_mj"
        attribute mk:
            "femc_mouth_mk"
        attribute ml:
            "femc_mouth_ml"
        attribute mm:
            "femc_mouth_mm"
        attribute mn:
            "femc_mouth_mn"
        attribute mo:
            "femc_mouth_mo"
        attribute mp:
            "femc_mouth_mp"
        attribute mq:
            "femc_mouth_mq"
        attribute mr:
            "femc_mouth_mr"
        attribute ms:
            "femc_mouth_ms"
        attribute mt:
            "femc_mouth_mt"
        attribute mu:
            "femc_mouth_mu"
        attribute mv:
            "femc_mouth_mv"
        attribute mw:
            "femc_mouth_mw"
        attribute mx:
            "femc_mouth_mx"
        attribute my:
            "femc_mouth_my"
    
    

    group nhc if_any "nhc":

            #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","pout","curi"]):
            "femc_eyes_e1a"
        attribute oe default if_any(["worr","flus","dist"]):
            "femc_eyes_e1b"
        attribute oe default if_any(["angr","sedu","doub"]):
            "femc_eyes_e1d"
        attribute oe default if_any(["cry"]):
            "femc_eyes_e1g"
        attribute oe default if_any(["vang","vsur","lsur"]):
            "femc_eyes_e2a"
        attribute oe default if_any(["nerv"]):
            "femc_eyes_e2b"
        attribute oe default if_any(["pani","shoc"]):
            "femc_eyes_e2d"
        attribute oe default if_any(["yand"]):
            "femc_eyes_e3a"
        attribute oe default if_any(["owo"]):
            "femc_eyes_e1j"
        attribute oe default if_any(["sus"]):
            "femc_eyes_e1l"
        attribute oe default if_any(["anno"]):
            "femc_eyes_e1k"
            
            #Default Closed eyes:
        attribute ce if_any(["neut","anno","vang","shoc","worr","sad","angr","lsur","vsur","pani","dist","worr","sus"]):
            "femc_eyes_e4a"
        attribute ce if_any(["happ","laug","flus","yand","pout","sedu","nerv","curi","doub","owo"]):
            "femc_eyes_e4b"
        attribute ce if_any(["cry"]):
            "femc_eyes_e4e"
        
            
            ###All eyes - truncated tags:
        attribute e1a:
            "femc_eyes_e1a"
        attribute e1b:
            "femc_eyes_e1b"
        attribute e1c:
            "femc_eyes_e1c"
        attribute e1d:
            "femc_eyes_e1d"
        attribute e1e:
            "femc_eyes_e1e"
        attribute e1f:
            "femc_eyes_e1f"
        attribute e1g:
            "femc_eyes_e1g"
        attribute e1h:
            "femc_eyes_e1h"
        attribute e1i:
            "femc_eyes_e1i"
        attribute e1j:
            "femc_eyes_e1j"
        attribute e1k:
            "femc_eyes_e1k"
        attribute e1l:
            "femc_eyes_e1l"
        attribute e2a:
            "femc_eyes_e2a"
        attribute e2b:
            "femc_eyes_e2b"
        attribute e2c:
            "femc_eyes_e2c"
        attribute e2d:
            "femc_eyes_e2d"
        attribute e3a:
            "femc_eyes_e3a"
        attribute e3b:
            "femc_eyes_e3b"
        attribute e3c:
            "femc_eyes_e3c"
        attribute e3d:
            "femc_eyes_e3d"
        attribute e4a:
            "femc_eyes_e4a"
        attribute e4b:
            "femc_eyes_e4b"
        attribute e4c:
            "femc_eyes_e4c"
        attribute e4d:
            "femc_eyes_e4d"
        attribute e4e:
            "femc_eyes_e4e"
        attribute e0a:
            "femc_eyes_e0a"
        attribute e0b:
            "femc_eyes_e0b"
        attribute e0c:
            "femc_eyes_e0c"
    
    group hc if_any "hc":
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","pout","curi"]) if_all "hc":
            "femc_hc_e1a"
        attribute oe default if_any(["worr","flus","dist"]) if_all "hc":
            "femc_hc_e1b"
        attribute oe default if_any(["angr","sedu","doub"]) if_all "hc":
            "femc_hc_e1d"
        attribute oe default if_any(["cry"]) if_all "hc":
            "femc_hc_e1g"
        attribute oe default if_any(["vang","vsur","lsur"]) if_all "hc":
            "femc_hc_e2a"
        attribute oe default if_any(["nerv"]) if_all "hc":
            "femc_hc_e2b"
        attribute oe default if_any(["pani","shoc"]) if_all "hc":
            "femc_hc_e2d"
        attribute oe default if_any(["yand"]) if_all "hc":
            "femc_hc_e3a"
        attribute oe default if_any(["owo"]) if_all "hc":
            "femc_hc_e1j"
        attribute oe default if_any(["sus"]) if_all "hc":
            "femc_hc_e1l"
        attribute oe default if_any(["anno"]) if_all "hc":
            "femc_hc_e1k"
            
            #Default Closed eyes:
        attribute ce if_any(["neut","anno","vang","shoc","worr","sad","angr","lsur","vsur","pani","dist","worr","sus"]) if_all "hc":
            "femc_hc_e4a"
        attribute ce if_any(["happ","laug","flus","yand","pout","sedu","nerv","curi","doub","owo"]) if_all "hc":
            "femc_hc_e4b"
        attribute ce if_any(["cry"]) if_all "hc":
            "femc_hc_e4e"
        
            
            ###All eyes - truncated tags:
        attribute e1a:
            "femc_hc_e1a"
        attribute e1b:
            "femc_hc_e1b"
        attribute e1c:
            "femc_hc_e1c"
        attribute e1d:
            "femc_hc_e1d"
        attribute e1e:
            "femc_hc_e1e"
        attribute e1f:
            "femc_hc_e1f"
        attribute e1g:
            "femc_hc_e1g"
        attribute e1h:
            "femc_hc_e1h"
        attribute e1i:
            "femc_hc_e1i"
        attribute e1j:
            "femc_hc_e1j"
        attribute e1k:
            "femc_hc_e1k"
        attribute e1l:
            "femc_hc_e1l"
        attribute e2a:
            "femc_hc_e2a"
        attribute e2b:
            "femc_hc_e2b"
        attribute e2c:
            "femc_hc_e2c"
        attribute e2d:
            "femc_hc_e2d"
        attribute e3a:
            "femc_hc_e3a"
        attribute e3b:
            "femc_hc_e3b"
        attribute e3c:
            "femc_hc_e3c"
        attribute e3d:
            "femc_hc_e3d"
        attribute e4a:
            "femc_hc_e4a"
        attribute e4b:
            "femc_hc_e4b"
        attribute e4c:
            "femc_hc_e4c"
        attribute e4d:
            "femc_hc_e4d"
        attribute e4e:
            "femc_hc_e4e"
        attribute e0a:
            "femc_hc_e0a"
        attribute e0b:
            "femc_hc_e0b"
        attribute e0c:
            "femc_hc_e0c"
    

    
    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","yand","owo","lsur"]):
            "femc_brow_b1a"
        attribute brow default if_any(["cry","worr","shoc","laug","sad","flus","pani","worr","nerv"]):
            "femc_brow_b1b"
        attribute brow default if_any(["anno","sedu"]):
            "femc_brow_b1c"
        attribute brow default if_any(["vang","angr"]):
            "femc_brow_b1e"
        attribute brow default if_any(["vsur"]):
            "femc_brow_b2a"
        attribute brow default if_any(["dist","pout"]):
            "femc_brow_b1d"
        attribute brow default if_any(["curi"]):
            "femc_brow_b1f"
        attribute brow default if_any(["sus"]):
            "femc_brow_b3b"
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["doub"]) if_all(["oe"]) if_not(["ce"]):
            "femc_brow_b1f"
        attribute brow default if_any(["doub"]) if_all(["ce"]) if_not(["oe"]):
            "femc_brow_b3b"
        
        
        #All eyebrows - truncated tags:
        attribute b1a:
            "femc_brow_b1a"
        attribute b1b:
            "femc_brow_b1b"
        attribute b1c:
            "femc_brow_b1c"
        attribute b1d:
            "femc_brow_b1d"
        attribute b1e:
            "femc_brow_b1e"
        attribute b1f:
            "femc_brow_b1f"
        attribute b2a:
            "femc_brow_b2a"
        attribute b2b if_any(["e4e","e4d","e0c","e1k","e3d","e1i","e1d","e1c","e4a","e4b","ce"]):
            "femc_brow_b2b"
        attribute b2c if_any(["e4e","e4d","e0c","e1k","e3d","e1i","e1d","e1c","e4a","e4b","ce"]):
            "femc_brow_b2c"
        attribute b3a if_any(["e4e","e4d","e0c","e1k","e3d","e1i","e1d","e1c","e4a","e4b","e4c","ce"]):
            "femc_brow_b3a"
        attribute b3b if_any(["e0c","e1f","e4a","e4b","e4c","e4d","e4e","e1l","e1c","e1d","e3d","ce"]):
            "femc_brow_b3b"
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face. #get extra'd bitch
    group nhc_special if_any "nhc":
        attribute scream if_any(["n3","n4","blus","blaw"]): #natsuki scream
            "femc_s_scream"
        attribute shocked if_any(["n1","n2","awkw","nobl"]): #the like dot eyes anime scream thingy
            "femc_s_shocked"
        attribute dizzy: #confused spiral eye thingy
            "femc_s_dizzy"
        attribute tired if_any(["n1","n2","n5","awkw","nobl","pale"]): #bags under eyes
            "femc_s_tired"
        attribute furious: #very angry
            "femc_s_furious"
        attribute oof if_any(["n1","n2","awkw","nobl"]): #lines/shadows over face, no eyes/eyebrows
            "femc_s_oof"
        attribute ehehe: #ashamed/wincing from embarrasment
            "femc_s_ehehe"

    group hc_special if_any "hc":
        attribute scream if_any(["n3","n4","blus","blaw"]): #natsuki scream
            "femc_hc_scream"
        attribute shocked if_any(["n1","n2","awkw","nobl"]): #the like dot eyes anime scream thingy
            "femc_hc_shocked"
        attribute dizzy: #confused spiral eye thingy
            "femc_hc_dizzy"
        attribute tired if_any(["n1","n2","n5","awkw","nobl","pale"]): #bags under eyes
            "femc_hc_tired"
        attribute furious: #very angry
            "femc_hc_furious"
        attribute oof if_any(["n1","n2","awkw","nobl"]): #lines/shadows over face, no eyes/eyebrows
            "femc_hc_oof"
        attribute ehehe: #ashamed/wincing from embarrasment
            "femc_hc_ehehe"

    if femc_eyepatch:
        "femc_s_patch"
    else:
        "femc_s_patchblank"

    group hairpiece: #you can change the default attribute if you want to always have a hairpiece
        attribute bow:
            "femc_s_hairbow"
        attribute clip:
            "femc_s_hairclip"

    group extras:
        attribute thonk:
            "femc_s_hand"
        attribute sigh:
            "femc_s_sigh"
    







layeredimage femc cross: #definitions for crossed arms (almost all copied over)

    
    #This makes the sprite one single texture, instead of multiple textures on top of each other.
    #This fixes certain problems like alpha fadein/fadeout looking strange, at the cost of some performance.
    at Flatten
    
    always "femc_s_face" #We always use the basic face.
    
    group outfit:
        
        attribute uniform default null #normal uniform
        attribute vest null #uniform without the blazer jacket
        attribute jacket null #wearing a green jacket
        attribute shirt null #a white shirt with a green jacket tied around the waist
        attribute shirt2 null #a short sleeved white shirt, no jacket around waist
   
    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        attribute owo null #owo
        attribute sus null #suspicious of someone
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template! #who the FUCK uses moods unironically
    

    group eyes:
        attribute nhc default null
        attribute hc null
    
    
    group blush: #These are intentionally separate from mood; the idea being that these aren't consciously controlled by the character - rather, they're a result of their emotions making them blush/sweat/etc. #this implies emotions are consciously controlled which can be wrong #also it would work the exact same i think if you didnt use moods and most people dont use moods
        attribute nobl default null #Default, no blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
        attribute pale null #no color in cheeks. defaults for n
    

    always:
        "femc_3c" if_any(["uniform"])
    always:
        "femc_3" if_any(["vest"])
    always:
        "femc_3d" if_any(["jacket"])
    always:
        "femc_3b" if_any(["shirt"])
    always:
        "femc_3bb" if_any(["shirt2"])

    
    if femc_longhair:
        "femc_s_longhair"
    else:
        "femc_s_shorthair"

    group nose: 
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "femc_nose_n1"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "femc_nose_n2"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "femc_nose_n3"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "femc_nose_n4"
        attribute nose default if_any(["pale"]):#default nose when "no color in cheeks"
            "femc_nose_n5"
        
        
        #All noses - truncated tags:
        attribute n1:
            "femc_nose_n1"
        attribute n2:
            "femc_nose_n2"
        attribute n3:
            "femc_nose_n3"
        attribute n4:
            "femc_nose_n4"
        attribute n5: #for if you want not even default blush
            "femc_nose_n5"
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","nerv"]):
            "femc_mouth_ma"
        attribute cm default if_any(["neut","worr","anno","dist","doub"]):
            "femc_mouth_md"
        attribute cm default if_any(["lsur","curi"]):
            "femc_mouth_me"
        attribute cm default if_any(["vsur","pout"]):
            "femc_mouth_mf"
        attribute cm default if_any(["shoc"]):
            "femc_mouth_mi"
        attribute cm default if_any(["cry","sad","angr","flus"]):
            "femc_mouth_mj"
        attribute cm default if_any(["vang","pani"]):
            "femc_mouth_mm"
        attribute cm default if_any(["laug","sedu"]):
            "femc_mouth_mn"
        attribute cm default if_any(["yand"]):
            "femc_mouth_mo"
        attribute cm default if_any(["owo"]):
            "femc_mouth_mt"
        attribute cm default if_any(["sus"]):
            "femc_mouth_mw"
        
        #Open Mouths:
        attribute om if_any(["happ","sedu"]):
            "femc_mouth_mb"
        attribute om if_any(["yand","laug"]):
            "femc_mouth_mc"
        attribute om if_any(["neut","dist"]):
            "femc_mouth_me"
        attribute om if_any(["worr","vsur","pout"]):
            "femc_mouth_mg"
        attribute om if_any(["flus","anno"]):
            "femc_mouth_mh"
        attribute om if_any(["lsur","curi"]):
            "femc_mouth_mi"
        attribute om if_any(["sad"]):
            "femc_mouth_mk"
        attribute om if_any(["cry","shoc"]):
            "femc_mouth_ml"
        attribute om if_any(["vang","angr","doub","pani"]):
            "femc_mouth_mq"
        attribute om if_any(["nerv"]):
            "femc_mouth_ms"
        attribute om if_any(["owo","sus"]):
            "femc_mouth_mf"
        
        
        ###All mouths - truncated tags:
        attribute ma:
            "femc_mouth_ma"
        attribute mb:
            "femc_mouth_mb"
        attribute mc:
            "femc_mouth_mc"
        attribute md:
            "femc_mouth_md"
        attribute me:
            "femc_mouth_me"
        attribute mf:
            "femc_mouth_mf"
        attribute mg:
            "femc_mouth_mg"
        attribute mh:
            "femc_mouth_mh"
        attribute mi:
            "femc_mouth_mi"
        attribute mj:
            "femc_mouth_mj"
        attribute mk:
            "femc_mouth_mk"
        attribute ml:
            "femc_mouth_ml"
        attribute mm:
            "femc_mouth_mm"
        attribute mn:
            "femc_mouth_mn"
        attribute mo:
            "femc_mouth_mo"
        attribute mp:
            "femc_mouth_mp"
        attribute mq:
            "femc_mouth_mq"
        attribute mr:
            "femc_mouth_mr"
        attribute ms:
            "femc_mouth_ms"
        attribute mt:
            "femc_mouth_mt"
        attribute mu:
            "femc_mouth_mu"
        attribute mv:
            "femc_mouth_mv"
        attribute mw:
            "femc_mouth_mw"
        attribute mx:
            "femc_mouth_mx"
        attribute my:
            "femc_mouth_my"
    
    

    group nhc if_any "nhc":

            #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","pout","curi"]):
            "femc_eyes_e1a"
        attribute oe default if_any(["worr","flus","dist"]):
            "femc_eyes_e1b"
        attribute oe default if_any(["angr","sedu","doub"]):
            "femc_eyes_e1d"
        attribute oe default if_any(["cry"]):
            "femc_eyes_e1g"
        attribute oe default if_any(["vang","vsur","lsur"]):
            "femc_eyes_e2a"
        attribute oe default if_any(["nerv"]):
            "femc_eyes_e2b"
        attribute oe default if_any(["pani","shoc"]):
            "femc_eyes_e2d"
        attribute oe default if_any(["yand"]):
            "femc_eyes_e3a"
        attribute oe default if_any(["owo"]):
            "femc_eyes_e1j"
        attribute oe default if_any(["sus"]):
            "femc_eyes_e1l"
        attribute oe default if_any(["anno"]):
            "femc_eyes_e1k"
            
            #Default Closed eyes:
        attribute ce if_any(["neut","anno","vang","shoc","worr","sad","angr","lsur","vsur","pani","dist","worr","sus"]):
            "femc_eyes_e4a"
        attribute ce if_any(["happ","laug","flus","yand","pout","sedu","nerv","curi","doub","owo"]):
            "femc_eyes_e4b"
        attribute ce if_any(["cry"]):
            "femc_eyes_e4e"
        
            
            ###All eyes - truncated tags:
        attribute e1a:
            "femc_eyes_e1a"
        attribute e1b:
            "femc_eyes_e1b"
        attribute e1c:
            "femc_eyes_e1c"
        attribute e1d:
            "femc_eyes_e1d"
        attribute e1e:
            "femc_eyes_e1e"
        attribute e1f:
            "femc_eyes_e1f"
        attribute e1g:
            "femc_eyes_e1g"
        attribute e1h:
            "femc_eyes_e1h"
        attribute e1i:
            "femc_eyes_e1i"
        attribute e1j:
            "femc_eyes_e1j"
        attribute e1k:
            "femc_eyes_e1k"
        attribute e1l:
            "femc_eyes_e1l"
        attribute e2a:
            "femc_eyes_e2a"
        attribute e2b:
            "femc_eyes_e2b"
        attribute e2c:
            "femc_eyes_e2c"
        attribute e2d:
            "femc_eyes_e2d"
        attribute e3a:
            "femc_eyes_e3a"
        attribute e3b:
            "femc_eyes_e3b"
        attribute e3c:
            "femc_eyes_e3c"
        attribute e3d:
            "femc_eyes_e3d"
        attribute e4a:
            "femc_eyes_e4a"
        attribute e4b:
            "femc_eyes_e4b"
        attribute e4c:
            "femc_eyes_e4c"
        attribute e4d:
            "femc_eyes_e4d"
        attribute e4e:
            "femc_eyes_e4e"
        attribute e0a:
            "femc_eyes_e0a"
        attribute e0b:
            "femc_eyes_e0b"
        attribute e0c:
            "femc_eyes_e0c"
    
    group hc if_any "hc":
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad","pout","curi"]) if_all "hc":
            "femc_hc_e1a"
        attribute oe default if_any(["worr","flus","dist"]) if_all "hc":
            "femc_hc_e1b"
        attribute oe default if_any(["angr","sedu","doub"]) if_all "hc":
            "femc_hc_e1d"
        attribute oe default if_any(["cry"]) if_all "hc":
            "femc_hc_e1g"
        attribute oe default if_any(["vang","vsur","lsur"]) if_all "hc":
            "femc_hc_e2a"
        attribute oe default if_any(["nerv"]) if_all "hc":
            "femc_hc_e2b"
        attribute oe default if_any(["pani","shoc"]) if_all "hc":
            "femc_hc_e2d"
        attribute oe default if_any(["yand"]) if_all "hc":
            "femc_hc_e3a"
        attribute oe default if_any(["owo"]) if_all "hc":
            "femc_hc_e1j"
        attribute oe default if_any(["sus"]) if_all "hc":
            "femc_hc_e1l"
        attribute oe default if_any(["anno"]) if_all "hc":
            "femc_hc_e1k"
            
            #Default Closed eyes:
        attribute ce if_any(["neut","anno","vang","shoc","worr","sad","angr","lsur","vsur","pani","dist","worr","sus"]) if_all "hc":
            "femc_hc_e4a"
        attribute ce if_any(["happ","laug","flus","yand","pout","sedu","nerv","curi","doub","owo"]) if_all "hc":
            "femc_hc_e4b"
        attribute ce if_any(["cry"]) if_all "hc":
            "femc_hc_e4e"
        
            
            ###All eyes - truncated tags:
        attribute e1a:
            "femc_hc_e1a"
        attribute e1b:
            "femc_hc_e1b"
        attribute e1c:
            "femc_hc_e1c"
        attribute e1d:
            "femc_hc_e1d"
        attribute e1e:
            "femc_hc_e1e"
        attribute e1f:
            "femc_hc_e1f"
        attribute e1g:
            "femc_hc_e1g"
        attribute e1h:
            "femc_hc_e1h"
        attribute e1i:
            "femc_hc_e1i"
        attribute e1j:
            "femc_hc_e1j"
        attribute e1k:
            "femc_hc_e1k"
        attribute e1l:
            "femc_hc_e1l"
        attribute e2a:
            "femc_hc_e2a"
        attribute e2b:
            "femc_hc_e2b"
        attribute e2c:
            "femc_hc_e2c"
        attribute e2d:
            "femc_hc_e2d"
        attribute e3a:
            "femc_hc_e3a"
        attribute e3b:
            "femc_hc_e3b"
        attribute e3c:
            "femc_hc_e3c"
        attribute e3d:
            "femc_hc_e3d"
        attribute e4a:
            "femc_hc_e4a"
        attribute e4b:
            "femc_hc_e4b"
        attribute e4c:
            "femc_hc_e4c"
        attribute e4d:
            "femc_hc_e4d"
        attribute e4e:
            "femc_hc_e4e"
        attribute e0a:
            "femc_hc_e0a"
        attribute e0b:
            "femc_hc_e0b"
        attribute e0c:
            "femc_hc_e0c"
    
    
    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","yand","owo","lsur"]):
            "femc_brow_b1a"
        attribute brow default if_any(["cry","worr","shoc","laug","sad","flus","pani","worr","nerv"]):
            "femc_brow_b1b"
        attribute brow default if_any(["anno","sedu"]):
            "femc_brow_b1c"
        attribute brow default if_any(["vang","angr"]):
            "femc_brow_b1e"
        attribute brow default if_any(["vsur"]):
            "femc_brow_b2a"
        attribute brow default if_any(["dist","pout"]):
            "femc_brow_b1d"
        attribute brow default if_any(["curi"]):
            "femc_brow_b1f"
        attribute brow default if_any(["sus"]):
            "femc_brow_b3b"
        
        #The following brows are for moods that differ between open and closed eyes:
        attribute brow default if_any(["doub"]) if_all(["oe"]) if_not(["ce"]):
            "femc_brow_b1f"
        attribute brow default if_any(["doub"]) if_all(["ce"]) if_not(["oe"]):
            "femc_brow_b3b"
        
        
        #All eyebrows - truncated tags:
        attribute b1a:
            "femc_brow_b1a"
        attribute b1b:
            "femc_brow_b1b"
        attribute b1c:
            "femc_brow_b1c"
        attribute b1d:
            "femc_brow_b1d"
        attribute b1e:
            "femc_brow_b1e"
        attribute b1f:
            "femc_brow_b1f"
        attribute b2a:
            "femc_brow_b2a"
        attribute b2b if_any(["e4e","e4d","e0c","e1k","e3d","e1i","e1d","e1c","e4a","e4b","ce"]):
            "femc_brow_b2b"
        attribute b2c if_any(["e4e","e4d","e0c","e1k","e3d","e1i","e1d","e1c","e4a","e4b","ce"]):
            "femc_brow_b2c"
        attribute b3a if_any(["e4e","e4d","e0c","e1k","e3d","e1i","e1d","e1c","e4a","e4b","e4c","ce"]):
            "femc_brow_b3a"
        attribute b3b if_any(["e0c","e1f","e4a","e4b","e4c","e4d","e4e","e1l","e1c","e1d","e3d","ce"]):
            "femc_brow_b3b"
    
    
    #This group is intentionally last on this list, so it will render over top of every other thing on the face. #get extra'd bitch
    group nhc_special if_any "nhc":
        attribute scream if_any(["n3","n4","blus","blaw"]): #natsuki scream
            "femc_s_scream"
        attribute shocked if_any(["n1","n2","awkw","nobl"]): #the like dot eyes anime scream thingy
            "femc_s_shocked"
        attribute dizzy: #confused spiral eye thingy
            "femc_s_dizzy"
        attribute tired if_any(["n1","n2","n5","awkw","nobl","pale"]): #bags under eyes
            "femc_s_tired"
        attribute furious: #very angry
            "femc_s_furious"
        attribute oof if_any(["n1","n2","awkw","nobl"]): #lines/shadows over face, no eyes/eyebrows
            "femc_s_oof"
        attribute ehehe: #ashamed/wincing from embarrasment
            "femc_s_ehehe"

    group hc_special if_any "hc":
        attribute scream if_any(["n3","n4","blus","blaw"]): #natsuki scream
            "femc_hc_scream"
        attribute shocked if_any(["n1","n2","awkw","nobl"]): #the like dot eyes anime scream thingy
            "femc_hc_shocked"
        attribute dizzy: #confused spiral eye thingy
            "femc_hc_dizzy"
        attribute tired if_any(["n1","n2","n5","awkw","nobl","pale"]): #bags under eyes
            "femc_hc_tired"
        attribute furious: #very angry
            "femc_hc_furious"
        attribute oof if_any(["n1","n2","awkw","nobl"]): #lines/shadows over face, no eyes/eyebrows
            "femc_hc_oof"
        attribute ehehe: #ashamed/wincing from embarrasment
            "femc_hc_ehehe"


    if femc_eyepatch:
        "femc_s_patch"
    else:
        "femc_s_patchblank"

    group hairpiece: #you can change the default attribute if you want to always have a hairpiece
        attribute bow:
            "femc_s_hairbow"
        attribute clip:
            "femc_s_hairclip"

    group extras:
        attribute thonk:
            "femc_s_hand"
        attribute sigh:
            "femc_s_sigh"
    
