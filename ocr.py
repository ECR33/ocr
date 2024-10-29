from PIL import Image
import pyocr
import cv2
# from google.colab.patches import cv2_imshow

# pyocrが使えることを確認する
tools = pyocr.get_available_tools()
print(tools)
# tesseractのみダウンロードしたため0番目を指定
tool = tools[0]
print(tool.get_name())

# Tesseract (sh)と出力されればOK

# img1_path = "output/extracted_image1.png"
# img1 = Image.open(img1_path)

# txt1 = tool.image_to_string(
#     img1,
#     lang='jpn+eng',
#     builder=pyocr.builders.TextBuilder(tesseract_layout=6)
# )

# print(txt1)

# outpath = "text/page1.txt"

# with open(outpath, mode="w") as f:
#   f.write(txt1)


import os

files = os.listdir("jpg")
fs = sorted(files)
for file in fs:
  print(file)
  
  img1 = Image.open(f"jpg/{file}")
  txt1 = tool.image_to_string(
      img1,
      lang='jpn+eng',
      builder=pyocr.builders.TextBuilder(tesseract_layout=6)
  )
 
  with open(f"text0/{file[:-4]}.txt", mode="w") as f:
    f.write(txt1)