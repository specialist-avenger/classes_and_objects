class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)

    def change_name(self, change_name):
        self.name = change_name

    def change_age(self, change_age):
        self.age = change_age

    def add_track(self, add_track):
        self.add_track = self.tracks.append(add_track)

    def get_score(self,):
        print('The Score is',self.score)
        return self.score

        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

# Calling the changed values
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
Bob.get_score()