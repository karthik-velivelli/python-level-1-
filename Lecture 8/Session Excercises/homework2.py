class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class EBook(Book):
    def __init__(self, title, author, file_size_mb):
        super().__init__(title, author)
        self.file_size_mb = file_size_mb

    def describe_ebook(self):
        self.describe_book()
        print(f"File Size: {self.file_size_mb} MB")


class AudioBook(EBook):
    def __init__(self, title, author, file_size_mb, narrator, duration_minutes):
        super().__init__(title, author, file_size_mb)
        self.narrator = narrator
        self.duration_minutes = duration_minutes

    def listening_hours(self):
        return self.duration_minutes / 60

    def describe_audiobook(self):
        self.describe_ebook()
        print(f"Narrator: {self.narrator}")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Listening Time: {self.listening_hours():.1f} hours")



audio1 = AudioBook("Tales of the River", "Meera Das", 180, "Arun Rao", 150)
audio1.describe_audiobook()

print()  


audio2 = AudioBook("Night Train", "Kabir Sen", 95, "Isha Nair", 90)
audio2.describe_audiobook()