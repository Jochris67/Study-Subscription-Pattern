class VoterDto: #database
    def __init__(self, name, vote):
        self.name = name
        self.vote = vote

class VotingRepo: #simpan ke database
    def __init__(self):
        self.__votes = {"merah" : 0, "biru" : 0, "kuning" : 0}
        
    def get_all_votes(self):
        return_voters = []
        for key, value in self.__votes.items():
            return_voters.append(VoterDto(key, value))
        return return_voters

    def insert_one_vote(self, name):
        self.__votes[name] += 1