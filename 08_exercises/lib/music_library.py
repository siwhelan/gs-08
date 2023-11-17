class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self._tracks = []

    def add(self, track):
        self._tracks.append(track)

    def all(self):
        return self._tracks

    def search_by_title(self, keyword):
        # Returns:
        #   a list of Track instances with titles that include the keyword
        return [track for track in self._tracks if keyword in track.title]
