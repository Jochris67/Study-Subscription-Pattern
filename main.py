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

class VotingServices: #terima input dari UI
    def __init__(self):
        self.voting_repo = VotingRepo()

    def get_all_votes(self):
        return self.voting_repo.get_all_votes()

    def add_one_vote(self, name):
        self.voting_repo.insert_one_vote(name)

class VotingUI: #terima input dari user
    def __init__(self):
        self.candidate = []
        self.voting_services = VotingServices()
    
    def display(self):
        while True:
            for i in self.voting_services.get_all_votes():
                print(f"nama: {i.name} -> jumlah: {i.vote}")

            vote = int(input("pilih tim no:"))

            if vote == 1:
                self.voting_services.add_one_vote("merah") #masukin input ke services
            elif vote == 2:
                self.voting_services.add_one_vote("biru") #masukin input ke services
            elif vote == 3:
                self.voting_services.add_one_vote("kuning") #masukin input ke services
            elif vote == 4:
                print("terima kasih sudah voting")
                break
            else:
                print("angka tidak valid")


if __name__ == "__main__":
    campain = VotingUI()
    campain.display()