# Social Media Analysis Report 

import re


posts = [
    "Just had the best #coffee ever! Starting my day right ☕ #morning #blessed",
    "Can't believe it's already Friday! #weekend #excited #finally",
    "Study session with @sarah_jones and @mike_chen #college #finals #stressed",
    "New movie was incredible! #marvel #cinema #amazing definitely recommend",
    "Pizza night with the squad! #foodie #friends #pizza #perfect",
    "Running late for class again... #college #life #struggle #help",
    "Beautiful sunset today! #nature #photography #peaceful #grateful",
    "Just finished my workout! Feeling strong 💪 #fitness #gym #motivation",
    "Rainy day = perfect for reading #books #cozy #rain #peaceful",
    "Can't decide what to wear today #fashion #style #choices #help",
    "Amazing concert last night! @band_name killed it #music #concert #live",
    "Homemade cookies turned out perfect! #baking #cookies #success #yummy",
    "Traffic is crazy today #commute #traffic #late #frustrated",
    "Love this new song! #music #newrelease #obsessed #repeat",
    "Study break with @roommate_amy #college #break #tired #coffee",
    "Best birthday surprise ever! Thank you @mom_official #birthday #family #love",
    "Trying to adult but failing #adult #life #struggle #help",
    "Perfect weather for a walk! #nature #walk #sunshine #happy",
    "New haircut! What do you think? #hair #change #nervous #opinion",
    "Midnight snack attack #food #midnight #hungry #guilty",
    "Group project meeting at 3pm @team_members #college #project #meeting",
    "Just bought new shoes! #shopping #shoes #retail #therapy",
    "Watching the game with @dad_jokes #sports #family #bonding #fun",
    "Procrastination level: expert #college #procrastination #guilty #help",
    "Farmers market haul! #healthy #food #fresh #weekend",
    "Can't sleep... too much #coffee today #insomnia #mistake #regret",
    "New episode of my favorite show! #tv #binge #excited #weekend",
    "Laundry day again... #adult #chores #boring #necessary",
    "Amazing Thai food tonight! #food #thai #delicious #satisfied",
    "Job interview tomorrow! #nervous #excited #career #future",
    "Beach day with @college_friends #beach #sun #vacation #perfect",
    "Trying to eat healthy but #pizza keeps calling #food #struggle #temptation",
    "New book arrived! #books #reading #excited #weekend",
    "Car broke down again... #car #trouble #frustrated #expensive",
    "Spontaneous road trip! #adventure #friends #spontaneous #excited",
    "Midterm grades are in... #college #grades #nervous #results",
    "Cooking dinner for the first time! #cooking #adult #experiment #wish",
    "Love this #weather! Perfect for outdoor activities #nature #outdoor #active",
    "Movie marathon night! #movies #marathon #popcorn #cozy",
    "New coffee shop discovery! #coffee #discovery #local #support",
    "Graduation is getting closer! #college #graduation #excited #nervous",
    "Roommate drama again... #roommate #drama #college #life",
    "Best #friends forever! Love you guys @bestie1 @bestie2 #friendship",
    "Trying to save money but #shopping keeps happening #money #struggle #budget",
    "Perfect study playlist! #music #study #focus #productivity",
    "Date night with @boyfriend_official #date #love #romantic #happy",
    "Family dinner tonight! #family #dinner #love #grateful",
    "New semester, new me! #college #semester #goals #motivation",
    "Late night gaming session! #gaming #night #fun #addicted",
    "Sunday brunch with @mom_official #brunch #family #sunday #tradition"
]


cleaned_posts = []
all_words = []


for post in posts:
    cleaned = re.sub(r'[^\w\s]', '', post).lower()
    words = cleaned.split()
    cleaned_posts.append(words)
    all_words.extend(words)

total_word = len(all_words)
unique_words = len(set(all_words))
average_post_length = total_word / len(posts)



all_hashtags = []
all_mentions = []
all_links = []

for post in posts:
    hashtags = re.findall(r"#\w+", post)
    all_hashtags.extend(hashtags)

    mentions = re.findall(r"@\w+", post)
    all_mentions.extend(mentions)

    links = re.findall(r"http\S+|www\.\S+", post)
    all_links.extend(links)


def tops(values):
    rank = 0
    frequency = {}
    for item in values:
        if(item in frequency):
            frequency[item] += 1
        else:
            frequency[item] = 1

    rankings = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    top10 = list(rankings.items())[:5]

    for item, count in top10:
        rank += 1
        print(f"{rank}. {item}: {count} times")
    

def tops_with_percentage(values, total):
    rank = 0
    frequency = {}
    for item in values:
        if(item in frequency):
            frequency[item] += 1
        else:
            frequency[item] = 1

    rankings = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    top10 = list(rankings.items())[:10]

    for item, count in top10:
        rank += 1
        percent = (count / total) * 100
        print(f'{rank}. "{item}" - {count} times ({percent:.2f}%)')


print("")
print("=======SOCIAL MEDIA ANALYSIS REPORT=======")
print("")
print("📊 Basic Statistics:")
print("Total Posts:", len(cleaned_posts))
print("Total Words:", total_word)
print("unique Words:", unique_words)
print(f"Average Post Length: {average_post_length:.2f} words")

print("")

print("🔥 Top 10 Most Common Words:")
# tops(all_words)
tops_with_percentage(all_words, total_word)


print("")

print("#️⃣ Popular Hashtags:")
tops(all_hashtags)

print("")

print("👥 Top Mentions:")
tops(all_mentions)
