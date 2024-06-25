import datetime
import os

def get_today_date():
    return str(datetime.date.today())

def mood_to_int(mood):
   
    mood_mapping = {
        'happy': 2,
        'relaxed': 1,
        'apathetic': 0,
        'sad': -1,
        'angry': -2
    }
    return mood_mapping[mood]

def get_mood_from_user():
    
    valid_moods = ['happy', 'relaxed', 'apathetic', 'sad', 'angry']
    while True:
        mood = input("Please enter your mood today (happy, relaxed, apathetic, sad, angry): ").lower()
        if mood in valid_moods:
            return mood
        print("Invalid mood, please try again.")

def store_mood(mood):
    
    dir_path = 'data'
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, 'mood_diary.txt')
    with open(file_path, 'a') as file:
        file.write(f"{get_today_date()} {mood_to_int(mood)}\n")

def already_entered_today():
    
    file_path = 'data/mood_diary.txt'
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith(get_today_date()):
                    return True
    except FileNotFoundError:
        return False
    return False

def diagnose_mood():
    
    file_path = 'data/mood_diary.txt'
    try:
        with open(file_path, 'r') as file:
            entries = [int(line.strip().split()[-1]) for line in file]
        if len(entries) < 7:
            return
        last_7_moods = entries[-7:]
        mood_counts = {mood: last_7_moods.count(mood) for mood in set(last_7_moods)}
        average_mood = round(sum(last_7_moods) / len(last_7_moods))
        diagnosis = "Your diagnosis: "
        if mood_counts.get(2, 0) >= 5:
            diagnosis += "manic!"
        elif mood_counts.get(-1, 0) >= 4:
            diagnosis += "depressive!"
        elif mood_counts.get(0, 0) >= 6:
            diagnosis += "schizoid!"
        else:
            mood_mapping = {2: 'happy', 1: 'relaxed', 0: 'apathetic', -1: 'sad', -2: 'angry'}
            diagnosis += mood_mapping[average_mood] + "!"
        print(diagnosis)
    except FileNotFoundError:
        print("No mood data available yet.")

def assess_mood():
    
    if already_entered_today():
        print("Sorry, you have already entered your mood today.")
    else:
        mood = get_mood_from_user()
        store_mood(mood)
        diagnose_mood()
