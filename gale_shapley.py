
class person():
    def __init__(self, name, gender, prefs):
        self.name = name
        self.gender = gender
        #prefs is a list of names
        self.prefs = prefs
        #used to store the person object of the match
        self.match = None

#Makes a stable matching of the men and women in the inpurt dictionaries, such that men and women are either matched with a person of the opposite sex or are single
#Input: Dictionary of men {name:object} and dictionary of women {name: object"
#Output: Stable matching [(m1,w1), (m2,w2)...]
def make_stable_match(men, women):
    stable_match = False
    while not stable_match:
        stable_matches = []
        #all the men make their proposals
        for m_name, m_ob in men.items():

            #If the man is not currently matched he proposes to his next preference
            if not m_ob.match:
                if len(m_ob.prefs) > 0:
                    first_w_name = m_ob.prefs.pop(0)
                    first_w_ob = women[first_w_name]
                
                    #If the man is a higher preference then current match (it appears in the remaining prefs)
                    if m_name in first_w_ob.prefs:
                        #The womens old match is reject, so his match is removed
                        if first_w_ob.match:
                            prev_man_ob = first_w_ob.match 
                            prev_man_ob.match = None
                        #Accept the new mans proposal by updating his match to the woman
                        m_ob.match = first_w_ob
                        #Update the womens match 
                        first_w_ob.match = m_ob
                        #Remove the preferences list from then new match onwards
                        first_w_ob.prefs = first_w_ob.prefs[0:first_w_ob.prefs.index(m_name)]

                        #If there weas a proposal it means that it was not stable yet
                        stable_matches.append(False)
                else:
                    #If he is out of acceptable women then there is no proposal
                    stable_matches.append(False)

            else:
                #if there was no proposal it means that this match hasn't changed
                stable_matches.append(True)

        #If there were no proposals it is a stable match
        if all(stable_matches):
            stable_match = True

    return men, women 

file_name = "test1.txt"
f = open(file_name, "r")
gender = "Male"
men = {}
women = {}
for line in f:
    if line == "\n":
        gender = "Female"
    else:
        line = line.strip(" ").strip("\n")
        line = line.split(":")
        name = line[0]
        prefs = line[1].split(",")
        if gender == "Male":
            men[name] = person(name, gender, prefs)
        else:
            women[name] = person(name, gender, prefs)
men,women = make_stable_match(men, women)

for m, ob in men.items():
    print m
    print ob.match.name
    print " "
print " "

for m, ob in women.items():
    print m
    print ob.match.name
    print " "
    
