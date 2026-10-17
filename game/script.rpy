# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Kai = Character("Kai", image ="kai" , color="#7b7b7bff")
define Tiger = Character("Dacia", color="#f8ea24")
define dragon = Character("Alan", color="#f03535")
define A = Character("....")
define alex = Character("Alex")
define B = Character("Bus Driver")

#Dacia Sprite
image Tiger = At("images/Tiger.png",sprite_zoom)
#Kai Sprite
image Kai = At("kai_blinking_anim", sprite_zoom)
image Kai_worry = At("images/Kai_worry.png",sprite_zoom)
image Kai_talk = At("images/Kai_talk.png",sprite_zoom)
#Alan Sprite
image dragon = At("images/dragon.png",sprite_zoom)

#animation
image kai_blinking_anim:
    "images/Kai.png" # File mắt mở
    choice:
        3.5
    choice:
        5.0
    "images/Kai_close.png" # File mắt nhắm
    0.08
    repeat

#side images

# Nếu bạn muốn ảnh nhỏ lại hoặc phóng to để vừa khung thoại:
#image side kai = At("Kai_potrait.png", side_transform)
transform side_transform:
    zoom 0.32
    xalign 0.0
    xoffset 80        # ← chỉnh con số này là chính (50–180 tùy màn hình)
    yalign 1.0
    yoffset -20       # nâng lên tí nếu bị chạm đáy quá

image bg office = im.Scale("images/bg_office.png",1920,1080)
image bg office_pantry = im.Scale("images/Office_pantry.png",1920,1080)
image bg bedroom = im.Scale("images/bedroom.png",1920,1080)
image bg_mirror = im.Scale("images/mirror.png",1920,1080)
image bg bus = im.Scale("images/bus.png",1920,1080)
image bg BS =im.Scale("images/Bus_stop.png",1920,1080)
image bg apartment =im.Scale("images/Apartment.png",1920,1080)
image bg room = im.Scale("images/room.png",1920,1080)
image bg street = im.Scale("images/Street.png",1920,1080)
image bg Pub = im.Scale("images/Pub.png",1920,1080)
init python:
    sprite_zoom = Transform(zoom=0.4)

transform flip:
    xzoom -1.0


# The game starts here.
label start:

    stop music fadeout 2.0

    scene black
    with Dissolve(2.0)

    pause 1.0

    play sound "audio/static.ogg"

    A "...Tell me something."

    pause .7

    A "After everything I told you..."

    pause .4

    A "What do you think?"

    "..."

    "I stayed quiet."

    "Not because I didn't know what to say."

    "Because I genuinely had no idea which story he was talking about."

    "Dad had spent years filling my head with stories."

    "Ghosts."

    "Shipwrecks."

    "People who vanished without a trace."

    "Old fishermen."

    "Things crawling out of the sea."

    "By now they'd all blended together."

    "I rubbed my forehead."

    Kai "You're gonna have to narrow it down."

    Kai "You've told me... what?"

    Kai "A few hundred?"

    pause .6

    A "*Chuckles.*"

    pause .5

    A "Fair enough."

    pause .7

    A "Then let's try this again."

    pause .8

    A "...Black Shore."

    stop sound

    scene black
    with Dissolve(2.5)

    play ambience "audio/rain.ogg" fadein 2.0
    play music "audio/bus.mp3" fadein 2.0

    scene bg bus
    with Dissolve(2.0)

    show Kai at center
    with dissolve

    pause .8

    B "Next stop..."

    pause .5

    B "Black Shore."

    pause .5

    B "Please check your belongings before leaving."

    play sound "audio/brake.ogg"

    with hpunch

    "The bus jerked to a stop."

    "..."

    "I slowly opened my eyes."

    Kai "(Fuck...)"

    Kai "(My neck.)"

    "I reached behind my shoulder and stretched."

    "Everything hurt."

    "Sleeping on a bus had somehow managed to make every muscle in my body hate me."

    Kai "(Fantastic.)"

    Kai "(Six hours on a bus just to arrive feeling like I got hit by a truck.)"

    "Outside..."

    "Rain."

    "Nothing but rain."

    "Water crawled across the windows in long silver lines."

    "Beyond them..."

    "An unfamiliar town slowly came into focus."

    "Old buildings."

    "Rusted streetlights."

    "Telephone poles leaning just enough to make you wonder how they were still standing."

    Kai "(...)"

    Kai "(So this is Black Shore.)"

    pause .6

    Kai "(Dad made this place sound unforgettable.)"

    pause .6

    Kai "(Looks like somewhere people forgot on purpose.)"

    play sound "audio/bus_door.ogg"

    "The doors hissed open."

    stop music fadeout 2.0

    scene bg BS
    with Dissolve(2.0)

    play ambience "audio/rain.ogg" fadein 2.0

    show Kai at left
    with dissolve

    "Cold air hit my face."

    "It smelled like wet concrete."

    "...and salt."

    "The sea wasn't visible."

    "But I could hear it."

    "Somewhere beyond the fog."

    play sound "audio/bus_leave.ogg"

    "The bus pulled away."

    pause 1

    "Its engine disappeared into the distance."

    pause .8

    "..."

    "Silence."

    pause .8

    Kai "(Well...)"

    Kai "(Guess this is home for a while.)"

    "I checked my phone."

    "One bar."

    Kai "(Of course.)"

    Kai "(Would've been weird if something actually worked today.)"

    show dragon at right
    with moveinright

    dragon "...Kai?"

    pause .5

    dragon "Is that you?"

    hide Kai
    show Kai_worry at left
    with dissolve

    Kai "Hm?"

    "I looked toward the voice."

    "A large dragon stood near the station."

    "Arms crossed."

    "Watching me."

    "Not in a threatening way."

    "...Just..."

    "...Like he'd seen a ghost."

    dragon "...No."

    dragon "You're not him."

    pause .5

    dragon "...You're his son."

    Kai "..."

    Kai "You knew my dad?"

    dragon "Long time ago."

    dragon "Before this town changed."

    pause .8

    Kai "Changed?"

    dragon "..."

    dragon "Forget I said that."

    pause .8

    Kai "(Great.)"

    Kai "(Been here less than five minutes...)"

    Kai "(Already getting cryptic old man dialogue.)"

    dragon "*laughs quietly*"

    dragon "You've got his attitude."

    Kai "Yeah."

    Kai "I've heard that before."

    dragon "..."

    dragon "He used to stand exactly where you're standing."

    dragon "Always looking at the sea."

    dragon "...Like he was waiting for something."

    "Something about the way he said it..."

    "...Made my stomach tighten."

    "I wanted to ask more."

    "Instead..."

    "I looked toward the ocean."

    "The waves kept crashing."

    "Steady."

    "Slow."

    "Like they'd been repeating the same sentence..."

    "...for years."

    scene black
    with Dissolve(2.5)

    centered "{size=45}CHAPTER ONE{/size}"

    pause 1

    centered "{size=28}The Town That Never Forgot{/size}"

scene bg BS
with Dissolve(2.0)
hide Kai_worry
show Kai at left,flip
Kai "He’s… he’s doing okay, sir. Still tells a lot of stories, though he clearly left this part out."

dragon "I bet. Some memories are like old houses—easier to leave the doors locked than to clean out the dust. But you have his eyes, kid. The same look that says you’re searching for something you haven't found yet."

"(Searching? I thought I came here for 'personal business' a simple errand. But looking at this old man’s knowing smile, my heart felt heavy)"

dragon "Listen, if you’re staying at the old apartments down the road, watch out for the leaky roof in 4B. And if you want to know more about your old man... stop by the 'Rusty Anchor' pub. Ask for Clara. She’s got a memory like an elephant and a grudge to match."

Kai "Clara? Was she… a friend of his?"

dragon "Something like that. Welcome home, kid. Even if it’s your first time here."
hide dragon with dissolve
"As the old man waved and walked by, I watched him disappear into the grey mist. I started to walk down the street."
hide Kai
show Kai at center
Kai "'Welcome home' he said. The words felt foreign, like a coat that didn't quite fit."
hide Kai
stop music
show Kai at center
scene bg apartment with fade
play music "audio/Door.mp3" fadein 0.5 noloop
"I finally reached the apartment building. It was a crumbling brick structure that looked like it was being held together by the ivy crawling up its sides. My key struggled in the lock, protesting with a metallic screech before finally giving way."
scene bg room with fade
"The room was small, smelling of pine sol and old paper. I dropped my backpack on the floor and slumped onto the bed."
show Kai_worry at center
Kai "Twenty years... Dad, what were you doing here for twenty years?"

"I reached into the side pocket of my bag and pulled out the only lead I had: an old, yellowed photograph I’d found hidden in one of his books back home. It was a picture of a young man—my father—standing in front of a lighthouse, laughing with a girl whose face had been carefully cut out of the photo"

Kai "The town is small, the old man said. Everyone knows everyone."

"I looked out the window. The rain was picking up, blurring the line between the sky and the sea. If I wanted answers, I’d have to start at the 'Rusty Anchor.' But a part of me wondered... was I ready to find out who my father really was before he became 'Dad'"
    
"I stood there for a second, watching the spot where the old man had been. The mist seemed to swallow his footsteps instantly. 'The Rusty Anchor... Clara...' I muttered the names to myself, letting them sink in."

Kai "So this is where you grew up, Dad... Why does it feel like you’re still hiding something, even from hundreds of miles away?"
hide Kai_worry
scene black with fade
"I reached into my bag and pulled out a small, leather-bound notebook. Tucked inside was an old, faded photograph I’d found in the attic back home"
    
"(The photo shows a young man resembling the protagonist standing in front of a lighthouse. Beside him is a girl, but her face has been intentionally scratched out.)"

Kai "If the old man was right... everyone here knew you. Which means someone in this town knows who she is."
play music "audio/Thunder.mp3" fadein 2.0 noloop

"A sudden flash of lightning illuminated the room. For a split second, I saw a reflection in the window glass that wasn't mine. I spun around, heart hammering against my ribs."
with vpunch
Kai "Who's there?!"
"Empty. Just the shadows of the rain dancing on the walls. I’m getting jumpy. Maybe the old man’s talk about 'stories' was getting to my head"
scene bg room with fade
show Kai_worry at center
"I looked at the clock. It was getting late, and the rain showed no signs of stopping. I had two choices: stay here and try to make sense of the few things I brought, or head out into the wet night to find that pub."
label Choice_matter:
menu:
    "Go to 'The Rusty Anchor' now.":
        "You're too restless to wait. Maybe a drink and some answers will clear your head."
        jump The_Rusty_Anchor

    "Examine the apartment more closely.":
        "Something feels off about this place. You want to see if the previous tenant left anything behind."
        jump Examine_the_apartment_more_closely

    "Try to call Dad.":
        "You need to hear his voice. Even if he lies, you might catch something in his tone."
        jump Try_to_call_Dad

label The_Rusty_Anchor:
    "I couldn't just sit there. The silence in that apartment was too loud, and the mystery of the scratched-out face in the photo was burning a hole in my pocket."
    play music "audio/Door.mp3" noloop
    "I grabbed my jacket and headed back out."

    play music "audio/Rain.mp3"
    scene bg street with fade
    
    "The town at night felt different. The streetlights were dim, casting long, distorted shadows on the cobblestones. I followed the smell of saltwater and cheap tobacco until I saw a neon sign flickering through the rain: The Rusty Anchor."
    play music "audio/Pub.mp3" 
    scene bg Pub with fade
    "As soon as I stepped inside, the room went quiet for a heartbeat. A dozen pairs of eyes—mostly weathered sailors and locals—tracked me from the bar to the door. I felt like an intruder in a library."

    "You look lost, kid. Or just wet. We don't get many strangers this time of year."
    show Kai at center
    Kai "I'm looking for Clara. An old man at the station said I could find her here."
    "The barman paused, wiping a glass with a rag that looked older than me. He tilted his head toward a corner booth, shrouded in shadows."
    "She not around lately but you can talk to Dacia the tiger at Corner table. But a word of advice? Watch your tone.He not too frienly to deal with"

    "As I approached, the triangular ears atop his head flicked. He was a tiger beastman, his fur patterned with dark stripes and his massive arms covered in old scars. He was swirling a glass of strong liquor, staring intensely into the amber liquid"
    show Kai at left , flip
    Kai "Excuse me... are you Dacia?"

    show Tiger at right
    Tiger "(Growls deep in his throat, voice like grinding stones)"
    Tiger "Keep walking before I use your head to mop the floor, brat."
    
    hide Kai
    show Kai_worry at left, flip
    Kai "I'm not here for trouble. I just want to ask about someone who lived here twenty years ago. His name was—"

    Tiger "I don't give a damn. Kid, you smell that? That's the stench of trouble. And you're reeking of it."
    
    "I didn't flinch. I pulled out the faded photo and slid it onto the scratched wooden table."
    Kai "Do you know who the woman with the erased face is?"

    "He glances at the photo, then freezes. His pupils narrow into sharp vertical slits"
    stop music
    with vpunch
    Tiger "Dammit... where the hell did you get this?"

    Kai "It belonged to my father."

    "He stands up abruptly. His towering height looms over me, radiating pure pressure. He grabs my shirt, yanking me close"
    Tiger "So you're that coward's son? He’s still breathing? While Elena had to..."
    "He grinds his teeth and shoves me back as if he’d just touched something filthy"
    Tiger "Listen close, kid. Your father owes this town—and he owes me—a life. Don't go parading that face around here unless you want to end up at the bottom of the ocean."
    "My chest ached where he’d grabbed me. The heavy scent of wet fur and cheap whiskey lingered in the air. Dacia didn't just look angry; he looked like a man who had been mourning for twenty years and had finally found someone to blame"
    "He slumped back into his seat, his tail lashing irritably against the wooden stool"
    Tiger "Why are you even here? To play detective? To find some 'closure' for your old man?"
    Kai "I'm here because he won't talk. Because every time I ask about his past, he looks right through me. I found the photo. I found the name Elena. I just want to know why she’s gone."
    "He lets out a dry, hacking laugh"
    Tiger "Why she's gone? She's gone because your father was a coward who chose his future over her life. They were at the lighthouse during the Great Storm. Only one of them came back down those stairs."
    Kai "You think he... pushed her?"
    "His eyes flash with a predatory gold light"
    Tiger "It doesn't matter what I think. The sea took her, but your father was the one who led her to the edge. And then he ran. He didn't stay for the funeral. He didn't stay to help us search the cliffs. He just... vanished."
    "The pub was silent now. Even the bartender had stopped wiping glasses. Every eye was on me—the son of the man who broke this town’s heart"
    Tiger "If you want the truth so bad, stop bothering me. Go to the North Point. The old lighthouse is still there, rotting just like the memories."
    Kai "Is someone living there?"
    Tiger "Nobody living. Just the old Keeper. He doesn't like humans, and he hates beastmen even more. But he saw everything that night. He's the only one left who knows if Elena fell... or if she was thrown."
    "He turns his back to me, finishing his drink in one gulp"
    Tiger "Now get out of my sight. Before I forget that you're just a kid and start seeing your father’s face again."
    return 

label Examine_the_apartment_more_closely:
    Kai "UwU"
    return
label Try_to_call_Dad:
    Kai "OwO"
    return