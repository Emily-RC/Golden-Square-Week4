class MusicLibrary():
    def __init__(self):
        self._tracks = []

    def add(self, track):
        self._tracks.append(track)

    def all(self):
        return self._tracks 

    def search_by_title(self, keyword):
        # return [self._tracks[1]] 
        # results = []
        # for track in self._tracks:
        #     if track.title == keyword:
        #         results.append(track)
        # return results 
        return [
            track 
            for track in self._tracks 
            if keyword in track.title 
            ]