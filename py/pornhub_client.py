from pornhub_api import PornhubApi
api = PornhubApi()

print("PornHub Client v1.0")
print("Copyright (c) 2021 miniprime1\n")

print("Options")
print("1. Recommended Videos")
print("2. Search Video")
print("3. Get Video by ID")
print("4. Install Required API")
option = input("Enter choice: ")

if option == "1":
    import random
    tags = random.sample(api.video.tags("f").tags, 5)
    category = random.choice(api.video.categories().categories)
    result = api.search.search(ordering="mostviewed", tags=tags, category=category)
    recommend = []
    for i in range(5): recommend.append(result.videos[i])
    print("\n", end="")
    print("-"*21 + "Recommended Videos" + "-"*21)
    for vid in recommend: print(f"\nTitle: {vid.title} \nURL: {vid.url}")
    print("\n" + "-"*60)

elif option == "2":
    print("\n", end="")
    s = input("PornHub Search: ")
    data = api.search.search(s, ordering="mostviewed")
    result = []
    for i in range(5): result.append(data.videos[i])
    print("\n", end="")
    print("-"*23 + "Search Result" + "-"*23)
    for vid in result: print(f"\nTitle: {vid.title} \nURL: {vid.url}")
    print("\n" + "-"*60)

elif option == "3":
    print("\n", end="")
    id = input("Enter ID: ")
    try: 
        video = api.video.get_by_id(id).video
        print("\n" + "-"*27 + "Result" + "-"*27)
        print(f"\nTitle: {video.title} \nURL: {video.url}")
        print("\n" + "-"*60)
    except: 
      print(f"\nError: cannot get video from this id: '{id}'")

elif option == "4":
    import sys, os
    os.system(f"{sys.executable} -m pip install pornhub-api")

else:
    print("Error: invalid choice")