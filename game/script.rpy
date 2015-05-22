﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image hirohito = "Hirohito.png"

# Declare characters used by this game.
define h = Character('Hirohito', color="#c8ffc8", show_two_window=True)
define k = Character('Katsumi', color="#c8ffc8", show_two_window=True)
define m = Character('Mana', color="#c8ffc8", show_two_window=True)
define t = Character('Takashi', color="#c8ffc8", show_two_window=True)
define unknown = Character ('???', color="#c8ffc8", show_two_window=True)

image katsumi_game_neutral = "sprites/FillerSprite.png"
image katsumi_game_happy = "sprites/FillerSprite.png"
image katsumi_game_sad = "sprites/FillerSprite.png"
image katsumi_game_excited = "sprites/FillerSprite.png"
image katsumi_game_angry = "sprites/FillerSprite.png"
image katsumi_game_exhausted = "sprites/FillerSprite.png"

image mana_nuetral = "sprites/FillerSprite.png"
image mana_happy = "sprites/FillerSprite.png"
image mana_sad = "sprites/FillerSprite.png"
image mana_dejected = "sprites/FillerSprite.png"

image dungeon = "backgrounds/FillerBackground.jpg"
image field_dawn = "backgrounds/FillerBackground.jpg"
image field_day = "backgrounds/FillerBackground.jpg"
image field_dusk = "backgrounds/FillerBackground.jpg"
image field_night = "backgrounds/FillerBackground.jpg"
image room_night = "backgrounds/FillerBackground.jpg"


# The game starts here.
label start:
    
    scene dungeon
   
    "Arrows left my bow one after another into the horde I faced."
    
    "They were vicious, burly ogres holding large axes.{w} Each one’s massive frame easily eclipsed my own."
    
    "Enemies like these were child’s play."
    
    "Sure this time the numbers were unusually high, but a problem?{w} Not in the slightest."
    
    "Each ogre fell one after the other.{w} One shot.{w} One kill.{w} It was as simple as that."
    
    "Yet despite the pure efficiency of death I wrought,{w} the ogres continuously poured into the small dungeon corridor."
    
    h "{i}This is new. It’s just my luck some moron would spring a trap and flood the dungeon today.{i}"
    
    "I closed my eyes and traced my fingers along my bow, feeling the intricate grain of the wood.{w} I took a deep breath, breathing in the rancid smell of dungeon air."
    
    "The loud stomps of the ogres came closer and closer."
    
    "As the ogres approached I tightened my focus to the last second.{w} Three ogres fell.{w} The charge faltered.{w} I opened my eyes."
    
    h "It seems like things are starting to get interesting."
    
    "I let loose a hail of arrows.{w} No fewer than three arrows entered my bow at a time."
    
    "These barbaric machines of war raged more and more after each fallen comrade."
    
    "They began charging into each other in rage impeding their job and making mine all the easier."
    
    h "{i}Getting in each other’s way,{w} very symbolic.{/i}"
    
    h "Oh."
    
    "I notice that there’s only a few remaining.{w} A smirk spreads across my face.{w} These poor souls would be the most unfortunate."
    
    "I approach the ogre and slowly reach for an arrow."
    
    unknown "Move it!"
    
    "Someone screams from behind, as the ogres in front fall to a blast of color, are blown away, defeated, and disappear."
    
    show katsumi_game_excited
    
    unknown "Come on!"
    
    "My arm is suddenly in the hand of some strange girl who’s now dragging me along with her as an even larger number of ogres chase us from behind."
    
    hide katsumi_game_excited
    
    "Truly this must be the genius who triggered the trap.{w} Only someone of the greatest intelligence can properly run a train such as this.{w} The complexity and beauty of an angry horde of ogres has no rival."
    
    "It’s just my luck as always."
    
    scene field_day with Dissolve(.5)
    
    show katsumi_game_exhausted
    
    h "Well, that was annoying."
    
    "I spoke to no one in particular–{w} or maybe it was to everyone in the world.{w} Or was it to myself?{w} The girl in front?"
    
    "We were both out of breath at the entrance to the dungeon."
    
    k "Don’t complain.{w} You would have died without me."
    
    "Well excuse me princess."
    
    h "It’s your fault in the first place.{w} Not only did you trigger the trap but you failed to nobly sacrifice yourself for the good of others. What a heartless deed!"
    
    hide katsumi_game_exhausted
    show katsumi_game_angry
    
    k "Just because I messed up doesn’t mean you have to be a jerk about it. Geez."
    
    h "Well your little {i}mistake{/i} cost me a fair amount of experience."
    
    hide katsumi_game_angry
    show katsumi_game_neutral
    
    k "Calm down it’s just a game."
    
    h "Now I’ll have you know-"
    
    hide katsumi_game_neutral
    
    scene black with Dissolve(.5)
    
    "Black. Everything became black."
    
    "That appeared once again."
    
    show mana_nuetral
    
    m "Hirohito, meals are fundamental to keep your body function properly. You ought to take one, now."
    
    "A fake voice entered my ear that drove nails into my head each time it made a sound."
    
    m "And you have been neglecting your studies. Not, not good either, You must–"
    
    h "Enough already."
    
    "I was irritated.{w} If I didn’t stop it, it could keep going forever.{w} I opened my eyes."
    
    scene room_night with Dissolve(.5)
    
    "The gray of my ceiling was such a welcoming sight.{w} The 'wooden' desk that was nothing more than plastic.{w} Everything here was fake and it pretended to be real.{w} The dulled colors and unpleasant feelings, this world was inferior."
    
    "The virtual world was more real than this.{w} Its colorful perfection gave it off as a simulation,{w} but that was part of its charm –it’s aware it’s fake."
    
    "I liked the lack of pretense."
    
    "I took a deep breath, and I could almost actually breathe in the wind I felt against my skin.{w} This thing was too well made."
    
    hide mana_neutral
    show mana_dejected
    
    m "Hirohito...?"
    
    h "{i}Why is a machine hesitating?{/i}"
    
    h "Shut up. Later."
    
    "I felt myself slipping into sleep when the phone rang."
    
    "It was Takashi.{w} That pretty boy who is oh so good at everything.{w} Somehow we had become,{w} acquaintances,{w} you could say."
    
    "He was like everyone else, a puppet happily accepting his predetermined role in society, but I appreciated his honesty in being aware of it.{w} I did not like his insistence on accepting it."
    
    h "Yeah, what is it, Takashi?"
    
    "I’m not very good at talking on the phone, so my voice more unenthusiastic than usual."
    
    t "In a bad mood, I see.{w} Did she interrupt your game again?"
    
    "He laughed.{w} I could tell the laugh was fake. It was a habit of his."
    
    t "I would’ve joined you, but I can’t let my grades slip even a bit, you know how it is."
    
    h "{i}That's just you being pretentious.{/i}"
    
    t "Ah, anyway, what I really called you for was to tell you meet me at the park near your house tomorrow.{w} I need your help with something that I can’t exactly allow myself to do."
    
    h "You know I don’t like surprises. Tell or just keep it to yourself."
    
    t "You’ll like it. Anyway, let’s see–{w} 10 sounds good, right? {w}Okay, then, see you there."
    
    "*Click*"
    
    h "{i}What kind of jerk hangs up like that?{/i}"
    
    "I was too tired to think much about it, and I fell asleep with my cellphone still in my hand."
    
    
    
    return
