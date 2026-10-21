class Player:
    def __init__(self):
        self.name = "Guest"
        self.score = 0
    def set_name(self, new_name):
        self.name = new_name
        # 1st bug forget to pass self parameter 
    def set_score(self,new_score):
        self.score = new_score
    def get_name(self):
        print(self.name)
    def get_score(self):
        return self.score # 2nd bug variable is score not scores 
    def display(self):
        print(f"Player: {self.get_name()}")
        print(f"Score: {self.get_score()}")
player = Player()
player.set_name("Riya")
player.set_score(250)
player.display()