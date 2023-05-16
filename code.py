from playsound import playsound
import random

print("Software implementation part of AI1110 audio playlist project")
print()
print("Sit back and enjoy the music :)")

while True:
    random_array=random.sample(range(1,21),k=20)

    j=1
    while(j<=20):
        playsound(f"audiofiles/song{random_array[j]}-audio.mp3")
        j=j+1
    ch=input("Do you want to stop the music(y/n)")
    if ch=='y':
        break
    else:
        continue
    

