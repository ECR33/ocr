import os
import easyocr
import cv2
reader = easyocr.Reader(['ja', 'en']) 


dir = "img_name" # 必要な部分のみ切り出した画像が格納されたフォルダ

files = os.listdir(dir)
fs = sorted(files)
for file in fs:
    print(file)
    result2 = reader.readtext(f"{dir}/{file}", detail=0)  # 文章のみ
    with open(f"text/{file[:-4]}.txt", mode="w") as f:
        for text in result2:
            f.write(f"{text}\n")
