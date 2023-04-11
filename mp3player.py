import pygame
from queue import Queue

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def empty(self):
#         return len(self.queue) == 0

#     def put(self, item):
#         self.queue.append(item)

#     def get(self):
#         if self.empty():
#             return None
#         return self.queue.pop(0)


# Inisialisasi Pygame
pygame.init()

# Inisialisasi queue playlist
playlist = Queue()

# Fungsi untuk menambahkan lagu ke playlist
def antrian(song):
    playlist.put(song)
    print('Added', song, 'to playlist')
    print('--------------------------')
    
# Fungsi untuk melompat ke lagu berikutnya pada playlist
def nextSong():
    pygame.mixer.music.stop()
    if not playlist.empty():
        next_song = playlist.get()
        print('Now playing:', next_song)
        print('----------------')
        pygame.mixer.music.load(next_song)
        pygame.mixer.music.play()
    else:
        print('Pemutar Berhenti, Antrian kosong')

# Tambahkan beberapa lagu ke playlist
antrian('dog.mp3')
antrian('cat.mp3')
antrian('horse.mp3')
antrian('cow.mp3')

# Putar lagu pertama dari playlist
if not playlist.empty():
    song = playlist.get()
    print('Now playing:', song)
    print('----------------')
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    

while True:
    # Cek apakah musik telah selesai diputar
    if not pygame.mixer.music.get_busy() and not playlist.empty():
        nextSong()  # memanggil fungsi nextSong() untuk memutar lagu selanjutnya
    elif not pygame.mixer.music.get_busy() and playlist.empty():
        print('Antrian kosong')
        break


