''' easyocr testing '''
import easyocr

reader = easyocr.Reader(['en'])

result = reader.readtext("images/tesseract_training_data.png")

#print(result)

for item in result:
    label = item[1]
    print(label)
    #, end=' '
