#Stable room mate problem with incomplete lists and ties
#for kidney swap

class patient_donor_pair():
    def __init__(self, name, prefs):
        self.name = name
        self.prefs = prefs
        self.proposed_to = None
        self.proposed_from = None

def phase_one_proposals(pd_pairs):
    #phase 1, everyone proposes until everyone has someone they have proposed to, unless someone is rejected by everyong
    while not all([pd.proposed_to for pd in pd_paris]] and all([len(pd.prefs) > 0 for pd in pd_pairs]):

        #each person who has not had a proposal accepted propses to the next person on their list
        for pd_name, pd_ob in pd_pairs.items():
            if pd.proposed_to == None:
                first_pref_name = pd_ob.prefs.pop(0)
                first_pref_ob = pd_pairs[first_pref_name]
                #if the pd_pair is in the still in the list of it's first preference it must be better than it's current proposal
                if pd_name in first_pref_ob.prefs:
                    #reject previous match
                    first_pref_prev_proposal = first_pref_ob.proposed_from
                    first_pref_prev_proposal.proposed_to = None
                    #remove the first pref from its old matches preference list
                    first_pref_prev_proposal.pop(0)
                    
                    #replace with new better proposer
                    first_pref_ob.proposed_from = pd_ob
                    #remove everyone after the new proposer in the proposees preference list
                    old_prefs = first_pref_ob.prefs
                    first_pref_ob.prefs= old_prefs[0:(first_w_ob.prefs.index(pd_name)+1)]
                    removed = old_prefs[(first_w_ob.prefs.index(pd_name)+1):]
                    #For all things removed from the preference list remove the first pref symetrically from their list
                    for r in removed:
                        r_ob = pd_pairs[r]
                        r_ob.prefs.remove(first_pref_name)

    return pd

def phase_two_rotations

    

        
    
    
def main(pd_pairs):
    #complete phase one proposals and return the reduced prefence tables for each person
    pd_pairs = phase_one_proposals(pd_pairs)

    #Check to see if any of the people have been rejected by everyone, if so return that there is no stable matching, return false and and empty list of matches
    if there is no stable matching return false and an empty list of matches
    if all([len(pd.prefs) > 0 for pd in pd_pairs]):
        return (False, [])

    #compelte the rotation phase
    pd_pairs = pjase_two_rotations(pd_pairs)

    #Check to see if any of the people have been rejected by everyone, if so return that there is no stable matching, return false and and empty list of matches
    if there is no stable matching return false and an empty list of matches
    if all([len(pd.prefs) > 0 for pd in pd_pairs]):
        return (False, [])

    #If this point is reached there must be a stable matching, return True and who is matched to each other
    
