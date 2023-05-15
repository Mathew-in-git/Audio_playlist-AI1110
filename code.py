from playsound import playsound
import random

print("Software implementation part of AI1110 audio playlist project")
print()
print("Sit back and enjoy the music :)")


random_array=[]
while len(random_array)<20:
    x=random.randint(1,20)
    if (x) not in random_array:
        random_array.append(x)

j=1
while(j<=20):
    playsound(f"audiofiles/song{random_array[j]}-audio.mp3")
    j=j+1

