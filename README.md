Hi!
This is code that converts PDF files into audible .mp3 files.

The most popular file format is PDF and we read those all the time. My aim is to provide a tool that translates PDF reading into listening. This is made by reading a PDF and converting it into an audio (.mp3). This program makes reading (or listening) to documents more accessible for those who encounter difficulties or are uneable to read and easier to those who are tired of readingm because they read PDFs all day and night. Also, alternating between reading and listening improves the eye health, as reading for long period on a screen is perjudicial for the human eye. However, we also warn that hearing too loud, with or without headphones, can also damage you ear.

This code is inspired on the code you can see here: https://github.com/TiffinTech/python-pdf-audo/blob/main/main.py, which is explained in this video: https://www.youtube.com/watch?v=LXsdt6RMNfY. The source of the 'sample.pdf' file is this: https://www.africau.edu/images/default/sample.pdf.

However, the modernisation of the libraries since the publication of that code brought me to the update of the code and rewriting. In that meaning, the code is inspired in the above metioned sources, but I provided it with various updates.

In order to use the program you will need to install some python libraries: gTTS and PyPDF2. You can do that by typing "pip install _libary_name_" in your terminal or shell.

We used the following version of each library:

  gTTS   2.5.0
  
  PyPDF2 3.0.1

Furthermore, if you can type the file paths manually. However, by using 'import os' we can extract the folder path of the python file and use it to save the ouput. We also use this folder path to read the .pdf input, so the .pdf you want to use must be saved into the same folder as the 'main.py' file.

When you run the code you will have to type the PDF file's name. You can type the name: 'example_name' or with the PDF ending 'example_name.pdf", the code will automatically detect it and find the file. Moreover, if you want to convert a PDf file outside the program folder (of the main.py file) you can type the full path to your PDF file starting with an '/' and the program will find the file in your computer, for example: '/Users/my_macbook/Desktop/my_PDF_file' or '/Users/my_macbook/Desktop/my_PDF_file.pdf'.

Regarding the output, this '.mp3' can be added to VLC and Apple Music apps, as well as for video editting, creating podcasts from scripts and much many applications.

We do not take responsibility of the use of this tool.

We recommend you to save and organize your files so that any output is loosen, we do not take resposibility for loosen information.

For any doubts or comments please contact me at 'joanalnu5@gmail.com'.

Happy hearing!
