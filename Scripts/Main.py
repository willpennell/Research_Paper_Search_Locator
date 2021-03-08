#! python3
# Main.py - enter folder path location and keyword or search term, this will read all pdfs in and add all the sentences that contains keyword into a txt file.
import re, os, pdfFormat
from pathlib import Path
#Inputs for file location and keyword
keyword = input('Enter Keyword/Search term: ')
location = Path(input('Enter FOLDER location: '))
searchRegex = re.compile(f'[^.?!]*(?<=[.?\s!]){keyword}[a-zA-Z]*(?=[\s.?!])[^.?!]*[.?!]')

os.chdir(location)
keywordFolder = pdfFormat.folderCreator(location, keyword)
print(keywordFolder)
for foldername, subfolders, filenames in os.walk(location):
    #Loop through each PDF in folder
    for filename in filenames:
        if filename.endswith('.pdf'):
            print(filename)
            rawText = pdfFormat.PDF2Text(filename)
            sentences = re.findall(searchRegex, rawText)
            if len(sentences) > 0:
                newFileName = pdfFormat.fileRenamer(filename, keyword)
                #Create new folder named findings
                KeywordFileLocation = open(Path(keywordFolder / newFileName), 'w', encoding='utf-8')
                KeywordFileLocation.write('---' + filename + '---\n\n\n\n')
                for sentence in sentences:
                    KeywordFileLocation.write(sentence + '\n')
                KeywordFileLocation.close()
 
            else:
                print(f'No sentences containing {keyword} in {filename}.')
