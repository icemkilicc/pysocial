from typing import overload
from collections import Counter
import sys
with open('output.txt', 'w') as f:
    f.write("Welcome to Assignment 3\n")
    f.write("-------------------------------\n")
    with open(sys.argv[1]) as k:
        people = dict()
        for line in k:
            if "\n" in line:                                 #I took each line one by one and checked for \n at the end
                line = line[:-1]                             #and also splited with ":"
                line = line.split(":")
                people[line[0]] = line[1].split()
            else:
                line = line.split(":")
                people[line[0]] = line[1].split()

    def ANU(person):
        if person in people:          #people is a dictionary which is holding network # example George : Mike ...  
            f.write("ERROR: Wrong input type! for'ANU! -- This user already exists!!\n")  
        else:
            people[person] = []
            f.write(f"User '{person}' has been added to the social network successfully\n")
    def DEU(person1):
        if person1 in people:
            f.write(f"User '{person1}' and his/her all relations have been deleted successfully\n")
            del people[str(person1)]
            for i in people:                          # I checked every person in people dict. because they have same friends.
                if people[i] != []:                    # If persons1 in people dictionary I delete it.
                    for j in people[i]:
                        if j == person1:
                            people[i].remove(str(person1))
        else:
            f.write(f"ERROR: Wrong input type! for 'DEU'!--There is no user named '{person1}'!!\n")
 
    def ANF(source_user,target_user):
        if source_user in people:
            if not target_user in people:
                f.write(f"ERROR: Wrong input type! for 'ANF'!--No user named '{target_user}' found!!\n")
            elif target_user in people[source_user]:
                f.write(f"ERROR: A relation between '{source_user}' and '{target_user}' already exists!!\n")
            else:
                if target_user in people:
                    people[source_user].append(target_user)    #If both exist in the dictionary,
                    people[target_user].append(source_user)    #I added them to each other's values
                    f.write(f"Relation between '{source_user}' and '{target_user}' has been added successfully\n")
        else:
            if target_user in people:
                f.write(f"ERROR: Wrong input type! for 'ANF'!--No user named '{source_user}' found!!\n")
            else:
                f.write(f"ERROR: Wrong input type! for 'ANF'!--No user named '{source_user}' and '{target_user}' found!\n")
    def DEF(source_user,target_user):
        if source_user in people:
            if not target_user in people:
                f.write(f"ERROR: Wrong input type! for 'DEF'!--No user named '{target_user}' found!!\n")
            elif not target_user in people[source_user]:
                f.write(f"ERROR: No relation between '{source_user}' and '{target_user}' found!!\n")
            else:
                if target_user in people:                       #If both exist in the dictionary,
                    people[source_user].remove(target_user)     #I deleted them from each other's values
                    people[target_user].remove(source_user)
                    f.write(f"Relation between '{source_user}' and '{target_user}' has been deleted successfully\n")
        else:
            if target_user in people:
                f.write(f"ERROR: Wrong input type! for 'DEF'!--No user named '{source_user}' found!!\n")
            else:
                f.write(f"ERROR: Wrong input type! for 'DEF'!--No user named '{source_user}' and '{target_user}' found!\n")
    def CF(username):
        if username in people:
            lenght = len(people[username])            # I found the length and printed it
            f.write(f"User '{username}' has {lenght} friends\n")      
        else:
            f.write(f"ERROR: Wrong input type! for 'CF'! -- No user named '{username}' found!\n")
            
    def FPF(username, maximum_distance):
        if username in people:
            if maximum_distance == str(2):
                max_dis1 = people[username]
                max_dis2 = [j for i in max_dis1 for j in people[i]]
                over_all = max_dis2 + max_dis1
                over_all = list(set(over_all))         # I added max_dis1 and max_dis2 and first i made set because,
                if username in over_all:               # it may have same elements and I checked to see if her name is on the list
                    over_all.remove(username)           # if it is on the list i removed it
                over_all = sorted(over_all)
                f.write(f"User '{username}' has {len(over_all)} possible friends when maximum distance is 2\n")
                f.write(f"These possible friends:{{{str(over_all)[1:-1]}}}\n") # I converted it string to get rid of list bracket 

            elif maximum_distance == str(3):
                max_dis1 = people[username]
                max_dis2 = [j for i in max_dis1 for j in people[i]]
                max_dis3 = [j for i in max_dis2 for j in people[i]]
                over_all = max_dis2 + max_dis1 + max_dis3
                over_all = list(set(over_all))      # I added max_dis1 and max_dis2,max_dis3 and first i made set because,
                if username in over_all:            # it may have same elements and I checked to see if her name is on the list
                    over_all.remove(username)       # if it is on the list i removed it
                over_all = sorted(over_all)
                f.write(f"User '{username}' has {len(over_all)} possible friends when maximum distance is 3\n")
                f.write(f"These possible friends:{{{str(over_all)[1:-1]}}}\n")

            elif maximum_distance == str(1):
                max_dis1 = sorted(people[username])         # I just printed his or her friends
                f.write(f"User '{username}' has {len(max_dis1)} possible friends when maximum distance is 1\n")
                f.write(f"These possible friends:{{{str(max_dis1)[1:-1]}}}\n")
            else:
                f.write("ERROR: Maximum distance is out of range!!\n")

        else:
            f.write(f"ERROR: Wrong input type! for 'FPF'!--No user named '{username}' found!\n")

    def SF(username,MD):
        if  2<=int(MD)<=3: 
            if username in people:
                friends = people[username]
                suggest_list = [j for i in friends for j in people[i]]   # I added every person in his friends' friends to the list
                for item in suggest_list:                                # I deleted his name from the list
                    if item == username:                      
                        suggest_list.remove(username)
                for item in suggest_list:
                    if item in friends:
                        suggest_list.remove(item)
                suggested_dict = dict(Counter(suggest_list))          #  this dictionary shows how many mutual friends he or she has  
                if str(MD) == str(2):
                    f.write(f"Suggestion List for '{username}' (when MD is 2):\n")
                elif str(MD) ==str(3):
                    f.write(f"Suggestion List for '{username}' (when MD is 3):\n")
                suggested_mutual2 = []
                suggested_mutual3 = []
                suggested_dict = dict(sorted(suggested_dict.items(), key=lambda x: (x[1],x[0])))

                for n in suggested_dict:
                    if str(MD) == str(2):                              # I checked every item in the dictionary,
                        if suggested_dict[n] == 2:                      # And added it to the mutual 2 list if they had 2 mutual friends
                            f.write(f"'{username}' has 2 mutual friends with '{n}'\n") #Added them to the mutual 3 list if they had 3 friends
                            suggested_mutual2.append(n)       
                        elif suggested_dict[n] ==3:
                            f.write(f"'{username}' has 3 mutual friends with '{n}'\n")
                            suggested_mutual2.append(n)
                    elif str(MD) ==str(3):
                        if str(suggested_dict[n]) == str(3):
                            f.write(f"'{username}' has 3 mutual friends with '{n}'\n")
                            suggested_mutual3.append(n)

                suggested_mutual2,suggested_mutual3=sorted(suggested_mutual2),sorted(suggested_mutual3)

                if str(MD) == str(2):     # After I had the lists sorted, I converted them to strings and printed them.
                    f.write(f"The suggested friends for '{username}':{str(suggested_mutual2)[1:-1]}\n")
                elif str(MD) ==str(3):
                    f.write(f"The suggested friends for '{username}':{str(suggested_mutual3)[1:-1]}\n")
            else:
                f.write(f"Error: Wrong input type! for 'SF'! -- No user named '{username}' found!!\n")
        else:
            f.write("Error: Mutually Degree cannot be less than 1 or greater than 4\n")


    with open(sys.argv[2]) as k:
        commands = k.read().splitlines()
        commands = [i.split() for i in commands]
        for i in commands:
            if i[0] == "ANU":
                ANU(i[1])
            elif i[0] == "DEU":
                DEU(i[1])
            elif i[0] == "ANF":
                ANF(i[1],i[2])
            elif i[0] == "DEF":
                DEF(i[1],i[2])
            elif i[0] == "CF":
                CF(i[1])
            elif i[0] == "FPF":
                FPF(i[1],i[2])
            elif i[0] == "SF":
                SF(i[1],i[2])
            else:
                f.write("You entered a wrong input\n")

