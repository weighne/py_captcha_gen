from random import randint
import os
from captcha.image import ImageCaptcha

def get_rand_line(file):
    length = os.stat(file).st_size
    rand_num = randint(0, length)
#    print(rand_num)
    with open(file,"r") as open_file:
        open_file.seek(rand_num)
        open_file.readline()
        return open_file.readline()


file = "diceware_clean.txt"
words = []

while len(words) <= 1:
    word = get_rand_line(file)
#    print(word)
    if (word.strip()).isalpha():
#        print("good!")
        words.append(word.strip())
    else:
#        print("bad!")
        continue
#    print(words)

image = ImageCaptcha(width=500,height=70,fonts=["fonts/arial-bold.ttf",
                                                 "fonts/BebasNeue-Regular.ttf",
                                                 "fonts/PlayfairDisplay-VariableFont_wght.ttf"])
captcha_text = " ".join(words)
#captcha_text = "this is a test of what happens when you enter long ass text"
data = image.generate(captcha_text)
image.write(captcha_text, f"{'_'.join(words)}.png")
