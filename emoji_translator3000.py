emoji_human= {
 "happy" : {
     "smile":"",
     "big_smile":"☺️",
     "open_smile":"😄",
     "wide_smile":"😁",
     "grin":"😆",
     "laugh":"😂",
     "laugh_intense":"🤣",
     "fall_in_love":"🥰",
 },
 "sad" :{
     "frown":"🙁",
     "frown_intense":"☹️",
     "downcast":"😓",
     "almost_cry":"😢",
     "crying":"😭",
     "heartbroken":"💔",
     "fraustrate":"😣",
     "fraustrate_intense":"😖",
     "fraustrate":"😣",

 },
 "angry":{
     "angry":"😠",
     "angry_horns":"👿",
     "angry_red":"😡",
     "swear":"🤬",
     "symbol":"💢",
     "steamblowing":"😤",

 },
 "suprised":{
     "shocked":"😮",
     "oops":"🫢",
     "shocked_intense":"😲",
     "mindblowing":"🤯",
     "screaming":"😱",
     "peeking_eye":"🫣",
    
 },
 "loved":{
     "heart":"❤️",
     "beating_heart":"💓",
     "sparkling":"💖",
     "gift":"💝",
     "flower":"🌹",
     "bouquet":"💐",
     "kiss":"😘",
     "mini_kiss":"😚",
     
 },
}

mood = input("Tell me your mood, : ").lower()

if mood in emoji_human:
    # Ask user what emotion they’re feeling under that mood
    emotion = input(f"Describe the feeling under '{mood}' (e.g., shocked, fall in love): ").lower()

    # Collect matching emojis
    matches = []
    for key, emoji in emoji_human[mood].items():
        if emotion in key:
            matches.append(f"{key}: {emoji}")
    
    # Show results
    if matches:
        print("Here are the matching emojis:")
        for match in matches:
            print(match)
    else:
        print("No matching emotion found for that description.")
else:
    print("Sorry, I don't know that mood...")