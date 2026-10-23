class Singer:
    def __init__(self, singing_level):
        self.singing_level = singing_level

    def show_singing(self):
        print(f"Singing Level: {self.singing_level}")


class Dancer:
    def __init__(self, dancing_level):
        self.dancing_level = dancing_level

    def show_dancing(self):
        print(f"Dancing Level: {self.dancing_level}")


class Painter:
    def __init__(self, painting_level):
        self.painting_level = painting_level

    def show_painting(self):
        print(f"Painting Level: {self.painting_level}")


class ClubMember(Singer, Dancer, Painter):
    def __init__(self, member_name, singing_level, dancing_level, painting_level):
        Singer.__init__(self, singing_level)
        Dancer.__init__(self, dancing_level)
        Painter.__init__(self, painting_level)
        self.member_name = member_name

    def total_score(self):
        return self.singing_level + self.dancing_level + self.painting_level

    def grade(self):
        if self.total_score() >= 20:
            return "Star"
        else:
            return "Rising"

    def display_member(self):
        print(f"Member: {self.member_name}")
        self.show_singing()
        self.show_dancing()
        self.show_painting()
        print(f"Total Talent Score: {self.total_score()}")
        print(f"Grade: {self.grade()}")


# Testing Sample Input 1
member1 = ClubMember("Diya", 7, 8, 6)
member1.display_member()

print()  # Blank line between tests

# Testing Sample Input 2
member2 = ClubMember("Kabir", 4, 3, 5)
member2.display_member()