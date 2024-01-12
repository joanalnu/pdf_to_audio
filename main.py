from gtts import gTTS
import PyPDF2
import os

folder_path = os.path.dirname(os.path.abspath(__file__))

file_name = input("PDF file name ('sample' or 'sample.pdf'): ")
if file_name[0] == '/' and file_name[len(file_name) - 4:len(file_name)] == ".pdf":
   input_path = file_name
elif file_name[0] == '/' and not file_name[len(file_name) - 4:len(file_name)] == ".pdf":
   input_path = file_name + '.pdf'
elif file_name[len(file_name) - 4:len(file_name)] == ".pdf":
  input_path = folder_path + '/' + file_name
else:
  input_path = folder_path + '/' + file_name + '.pdf'

pdfreader = PyPDF2.PdfReader(open(input_path, 'rb'))

full_text = ""

#this read the file for each page and koin altogether into the full_text variable with spaces
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    words = text.split()
    clean_text = ' '.join(words)
    full_text += clean_text + ' '

#convert full_etxt to mp3 file
tts = gTTS(full_text, lang='en')
tts.save(folder_path +'/audio.mp3')
print("Successful conversion!")