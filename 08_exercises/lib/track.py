class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def format(self):
        # Returns:
        #   a string in the format "TITLE by ARTIST"
        return f"{self.title} by {self.artist}"
