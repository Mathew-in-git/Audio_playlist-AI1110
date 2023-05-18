import random 
import pygame

pygame.mixer.init()

rand_array=random.sample(range(1,21),k=20)
file=[]
for i in rand_array:
    file.append(f"song{rand_array[i-1]}-audio.mp3")

for i in file:
    print(i)
    pygame.mixer.music.load(f"audio/{i}")
    pygame.mixer.music.play()

    x=input("Press n to go to next song :")
    if x=='n':
        pygame.mixer.music.stop()


