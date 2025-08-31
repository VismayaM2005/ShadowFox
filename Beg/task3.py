justice_league = ["Superman","Batman","Wonder Woman", "Flash", "Aquaman" , "Green Lantern"]
number=len(justice_league)
print("Task 3")
#1. Calculate the number of members in the Justice League.
print(f"Number of members in justice league :{number}")

#2.Batman recruited Batgirl and Nightwing as new members. Add them to your list.
justice_league.append('Batgirl')
justice_league.append('Nightwing')
print(f"After adding new members: {justice_league}")

#3. Wonder Woman is now the leader of the Justice League. Move her to the beginning of the list.
justice_league.remove('Wonder Woman')
justice_league.insert(0,'Wonder Woman',)
print(f"New list after the leader is selected: {justice_league}")

#4. Aquaman and Flash are having conflicts, and you need to separate them. Choose either "Green Lantern" or "Superman" and move them in between Aquaman and Flash.
justice_league.remove('Superman')
flash_index=justice_league.index("Flash")
justice_league.insert(flash_index+1,"Superman")
print("After separating Aquaman & Flash:", justice_league)

#5.  Replace team with new members
justice_league=["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team assembled by Superman:", justice_league)

#6 Sort the Justice League alphabetically and show near leader.
justice_league.sort()
print(f"Sorted team: {justice_league}")
print(f"New leader: {justice_league[0]}")