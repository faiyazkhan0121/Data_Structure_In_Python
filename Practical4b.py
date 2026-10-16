class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    # Add a song at the end
    def add_song(self, title, artist):
        new_song = Song(title, artist)

        if self.head is None:
            self.head = new_song
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_song

    # Display all songs
    def show_playlist(self):
        if self.head is None:
            print("Playlist is empty")
            return

        current = self.head
        while current is not None:
            print(current.title, "-", current.artist)
            current = current.next

    # Search for a song
    def search_song(self, title):
        current = self.head

        while current is not None:
            if current.title.lower() == title.lower():
                print("Found:", current.title, "-", current.artist)
                return

            current = current.next

        print("Song not found")

    # Remove a song
    def remove_song(self, title):
        current = self.head
        previous = None

        while current is not None:
            if current.title.lower() == title.lower():
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                print(current.title, "removed")
                return

            previous = current
            current = current.next

        print("Song not found")


# Main program
playlist = Playlist()

playlist.add_song("Blinding Lights", "The Weeknd")
playlist.add_song("Shape of You", "Ed Sheeran")
playlist.add_song("Believer", "Imagine Dragons")
playlist.add_song("Perfect", "Ed Sheeran")

print("My Playlist:")
playlist.show_playlist()

print("\nSearching for a song:")
playlist.search_song("Believer")

print("\nRemoving a song:")
playlist.remove_song("Shape of You")

print("\nUpdated Playlist:")
playlist.show_playlist()