# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Kai = Character("Kai", image ="kai" , color="#7b7b7bff")
define Tiger = Character("Dacia", image ="tiger" , color="#f8ea24")
define dragon = Character("Alan", image ="dragon" , color="#f03535")
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

# ---------- Ảnh hồ sơ (dùng cho hộp thoại kiểu case file) ----------
# Kai_potrait.png vốn đã gần vuông nên chỉ cần zoom vừa khung, không cần crop.
transform casefile_photo_kai:
    xalign 0.5
    yalign 0.5
    zoom 0.168

# Tiger.png / dragon.png là ảnh toàn thân, cao hơn khung ảnh nhiều.
# Zoom theo chiều ngang rồi neo lên đỉnh (yalign 0.0) để lấy phần đầu,
# phần thân dư bên dưới sẽ bị khung "frame" (clipping True) cắt bớt.
transform casefile_photo_tiger:
    xalign 0.5
    yalign 0.0
    zoom 0.101

transform casefile_photo_dragon:
    xalign 0.5
    yalign 0.0
    zoom 0.081

image side kai = At("images/Kai_potrait.png", casefile_photo_kai)
image side tiger = At("images/Tiger.png", casefile_photo_tiger)
image side dragon = At("images/dragon.png", casefile_photo_dragon)

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
    stop music 
    scene black with dissolve
    A "...So, what do you think about the story I just told you?"
    "Which one, Dad? You tell me like, a dozen stories every day."
    A "Fair point. I'm talking about the story of....."
    "……"


    play music "audio/bus.mp3" fadein 2.0 noloop
    scene bg bus with fade
    B "Next stop: Black Shore. Please mind your belongings as you exit the train"

    "I jolted awake to the piercing screech of the old PA system. My head was throbbing—a gift from the rock-hard seat and the lack of sleep last night"
    "I leaned against the window, gazing out. Through the thick, grey veil of mist, Black Shore slowly began to reveal itself across the shoreline. I stood there for a long time, lost in thought."
    "As we pulled into the station, raindrops started tapping rhythmically against the glass."
    play music "audio/rain.mp3" fadein 2.0 
    show Kai_worry at center
    Kai "(A rainy welcome... honestly, I couldn't have asked for a better start.)"

    scene bg BS with fade
    " The fog swallowed the city’s skyline, and a sharp wind whistled through the old, creaky doors, shaking the trees. It sounded almost like a chorus of voices screaming my name."

    Kai "Does this city... somehow know why I’m here? No, that’s impossible. Just my imagination getting the best of me "

    "I took a deep breath to steady myself. This city wasn't my problem. I was just here to settle some personal business. I didn't pack much—just a backpack and a small bag. I didn't plan on staying long. Just get in, finish the job, and get out."

    "Or maybe I’d be here longer than I thought. Honestly, I didn't have the answer to that yet."

    "The rain wasn't too heavy, but digging through my bags for an umbrella seemed like too much of a hassle. I decided to just brave it and head quickly toward the apartment I'd rented. A little rain never hurt anyone my age."

    "I was mid-stride when a voice called out a name I never expected to hear in a place like this."
    hide Kai_worry
    show Kai at left
    show dragon at right
    with vpunch
    dragon "Oh! {w=0.5}Kai? When did you get back, son?"
 
    hide Kai
    show Kai_worry at left , flip
    "My heart skipped a beat. I turned toward the voice. An old man with a hunched back was waving at me, leaning on his cane as he hobbled over."
    dragon "Why didn't you tell anyone you were coming home?"

    Kai "{w=0.5}Um... do you know me? I think you've mistaken someone else, sir."
    "The old man squinted, studying my face intensely before it finally clicked."

    dragon "Ah, you're not him! But goodness, you're the spitting image of him. You must be his son, haha! Are you moving here to live as well?"

    hide Kai_worry
    show Kai at left ,flip
    Kai "Yes, sir. I've decided to stay for a while to take care of some personal matters."

    dragon "Well, it makes sense. Your father always did love this place."
    "I blinked, caught off guard."
    hide Kai
    show Kai_worry at left ,flip
    Kai "My dad lived here? He never mentioned anything about that to me."

    dragon "Of course he did! He moved here when he was just a lad. Everyone around here knew him—news travels fast in a town this small"

    dragon "He stayed until he was twenty, then left for university. Haven't heard a peep from him since. Tell me, how's your father doing? Is he well?"
    
    hide Kai_worry
    show Kai at left,flip
    Kai "He’s… he’s doing okay, sir. Still tells a lot of stories, though he clearly left this part out."

    dragon "I bet. Some memories are like old houses—easier to leave the doors locked than to clean out the dust. But you have his eyes, kid. The same look that says you’re searching for something you haven't found yet."

    "(Searching? I thought I came here for 'personal business' a simple errand. But looking at this old man’s knowing smile, my heart felt heavy)"

    dragon "Listen, if you’re staying at the old apartments down the road, watch out for the leaky roof in 4B. And if you want to know more about your old man... stop by the 'Rusty Anchor' pub. Ask for Clara. She’s got a memory like an elephant and a grudge to match."

    Kai "Clara? Was she… a friend of his?"

    dragon "Something like that. Welcome home, kid. Even if it’s your first time here."
    hide dragon with dissolve
    "As the old man wave and walk by watched him disappear into the grey mist, i start to walk down the street"
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