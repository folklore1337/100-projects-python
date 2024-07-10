from mutagen.easyid3 import EasyID3
import pygame
from tkinter.filedialog import askopenfilenames
from tkinter import *
from tkinter import ttk
import time

pygame.init()

class FrameApp(Frame):
    def __init__(self, master):
        super(FrameApp, self).__init__(master)
        self.grid()
        self.paused = False
        self.playlist = list()
        self.actual_song = 0

        self.b1 = Button(self, text="Play", command=self.play_music, width=20)
        self.b1.grid(row=1, column=0)

        self.b2 = Button(self, text="Previous", command=self.previous_song, width=20)
        self.b2.grid(row=2, column=0)

        self.b3 = Button(self, text="Toggle", command=self.toggle, width=20)
        self.b3.grid(row=3, column=0)

        self.b4 = Button(self, text="Next", command=self.next_song, width=20)
        self.b4.grid(row=4, column=0)

        self.b5 = Button(self, text="Add to list", command=self.add_to_list, width=20)
        self.b5.grid(row=5, column=0)

        self.b6 = Button(self, text="Delete from list", command=self.delete_from_list, width=20)
        self.b6.grid(row=6, column=0)

        self.label1 = Label(self)
        self.label1.grid(row=7, column=0)

        self.output = Text(self, wrap=WORD, width=50, height=10)
        self.output.grid(row=8, column=0)

        self.progress = ttk.Progressbar(self, orient=HORIZONTAL, length=300, mode='determinate')
        self.progress.grid(row=9, column=0)

        self.volume_label = Label(self, text="Volume")
        self.volume_label.grid(row=10, column=0)

        self.volume_slider = Scale(self, from_=0, to=1, orient=HORIZONTAL, resolution=0.1, command=self.set_volume)
        self.volume_slider.set(0.5)
        pygame.mixer.music.set_volume(0.5)
        self.volume_slider.grid(row=11, column=0)

        self.SONG_END = pygame.USEREVENT + 1

    def add_to_list(self):
        directory = askopenfilenames()
        for song_dir in directory:
            self.playlist.append(song_dir)
        self.update_output()

    def delete_from_list(self):
        selected_index = self.output.index(SEL_FIRST).split('.')[0]
        if selected_index:
            selected_index = int(selected_index) - 1
            if selected_index < len(self.playlist):
                self.playlist.pop(selected_index)
                self.update_output()

    def update_output(self):
        self.output.delete(0.0, END)
        for key, item in enumerate(self.playlist):
            try:
                song = EasyID3(item)
                song_data = f"{key + 1} : {song['title'][0]} - {song['artist'][0]}"
            except Exception as e:
                song_data = f"{key + 1} : {item}"
            self.output.insert(END, song_data + '\n')

    def song_data(self):
        try:
            song = EasyID3(self.playlist[self.actual_song])
            song_data = f"Now playing: Nr:{self.actual_song + 1} {song['title'][0]} - {song['artist'][0]}"
        except Exception as e:
            song_data = f"Now playing: Nr:{self.actual_song + 1} {self.playlist[self.actual_song]}"
        return song_data

    def play_music(self):
        if not self.playlist:
            return
        directory = self.playlist[self.actual_song]
        pygame.mixer.music.load(directory)
        pygame.mixer.music.play(1, 0.0)
        pygame.mixer.music.set_endevent(self.SONG_END)
        self.paused = False
        self.label1['text'] = self.song_data()
        self.update_progress_bar()

    def check_music(self):
        for event in pygame.event.get():
            if event.type == self.SONG_END:
                self.next_song()

    def toggle(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        elif not self.paused:
            pygame.mixer.music.pause()
            self.paused = True

    def get_next_song(self):
        if self.actual_song + 1 < len(self.playlist):
            return self.actual_song + 1
        else:
            return 0

    def next_song(self):
        self.actual_song = self.get_next_song()
        self.play_music()

    def get_previous_song(self):
        if self.actual_song - 1 >= 0:
            return self.actual_song - 1
        else:
            return len(self.playlist) - 1

    def previous_song(self):
        self.actual_song = self.get_previous_song()
        self.play_music()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

    def update_progress_bar(self):
        current_time = pygame.mixer.music.get_pos() / 1000
        total_time = self.get_song_length(self.playlist[self.actual_song])
        self.progress['value'] = (current_time / total_time) * 100
        if pygame.mixer.music.get_busy():
            self.after(1000, self.update_progress_bar)

    def get_song_length(self, filename):
        try:
            audio = EasyID3(filename)
            length = audio.info.length
            return length
        except Exception as e:
            return 180

root = Tk()
root.geometry("350x500")
app = FrameApp(root)

while True:
    app.check_music()
    app.update()
