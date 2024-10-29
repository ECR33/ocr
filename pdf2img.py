import fitz

filename = "list_ex.pdf" # 割と高解像度で紙をスキャンしたPDF
pdf_file = fitz.open(filename)
num_of_pics = 0

for page in pdf_file:             
    images = page.get_images()
    if not len(images) == 0:
        for image in images:
            num_of_pics += 1 
            xref = image[0]
            img = pdf_file.extract_image(xref)
            out_file = "output/extracted_image{}.png".format(num_of_pics)
            print(out_file)
            with open(out_file, "wb") as f:
                f.write(img["image"])

pdf_file.close()