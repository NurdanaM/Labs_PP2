import pygame 
import os

pygame.init()
pygame.mixer.init()

#папка с музыкой 
mfolder = "/Users/nurdanam/Desktop/musicfolder"

#получение списка mp3 файлов
musiclist = [f for f in os.listdir(mfolder) if f.endswith(".mp3")]

if not musiclist:
    print("No available music files")
    exit()

current_song_idx = 0

#функции для воспроизведения музыки 
def play_music():
    pygame.mixer.music.load(os.path.join(mfolder, musiclist[current_song_idx]))
    pygame.mixer.music.play()
    print(f"Now playing: {musiclist[current_song_idx]}")

#функции для остановки музыки  
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped")

#функции для переключения на следующий трек 
def next_music():
    global current_song_idx
    current_song_idx = (current_song_idx + 1 ) % len(musiclist)
    play_music()

#функции для переключения на предыдущий трек
def previous_music():
    global current_song_idx
    current_song_idx = (current_song_idx - 1) % len(musiclist)
    play_music()
 

play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: #клавиша "P" - PLAY/PAUSE
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Music paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Music resumed")

            if event.key == pygame.K_s: #клавиша "S" - STOP
                stop_music()
            
            if event.key == pygame.K_n: #клавиша "N" - NEXT SONG
                next_music()
                    
            if event.key == pygame.K_b: #клавиша "B" - PREVIOUS SONG
                previous_music()

pygame.quit()