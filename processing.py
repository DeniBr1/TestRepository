from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap


class Process:
    def __init__(self, name_photo, reply_mess, reply_fullname):
        self.name_photo = name_photo
        self.r_mess = reply_mess
        self.reply_fullname = reply_fullname

    def paint_text(self):
        print("Полное имя: " + str(self.reply_fullname))
        print("Текст: " + str(self.r_mess))
       # self.r_mess = '\n'.join(wrap(self.r_mess, width=50))
        adress = "image/" + str(self.name_photo)
        print(adress)
        image = Image.open("1231312.jpg")
        img = Image.open(adress)
        autor = "\n\n(c) " + str(self.reply_fullname)

        width = 64
        height = 64
        fon_w = 400

        oper1 = len(self.r_mess) / 50
        fon_h = 100 + (15 * int(oper1))
        resized_img = img.resize((width, height), Image.ANTIALIAS)
        resized_imgg = image.resize((fon_w, fon_h), Image.ANTIALIAS)

        draw = ImageDraw.Draw(resized_imgg)
        font = ImageFont.truetype("123.ttf", 20)
        font2 = ImageFont.truetype("123.ttf", 13)

        draw.text((100, 0), 'Цитата', (255, 255, 255), font=font)

        draw.text((100, 25), self.r_mess + autor, (255, 255, 255), font=font2)

        resized_imgg.paste(resized_img, (10, 25))
        res = "image/1" + str(self.name_photo)
        resized_imgg.save(res)
        return res
