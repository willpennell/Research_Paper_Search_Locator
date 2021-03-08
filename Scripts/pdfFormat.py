import re, pdfminer.high_level, os
from pathlib import Path

introRef = re.compile(r'introduction(.*)references')

def PDF2Text(filename):
    #Tidies up pdf text and converts to string
    text = pdfminer.high_level.extract_text(filename)
    text = text.lower()
    text = text.replace('\n\n', '\n')
    text = text.replace('-\n', '')
    text = text.replace('\n', ' ')
    try:
        parsedText = re.search(introRef, text)
        text = parsedText.group(1)
    except:
        print('No Introduction or References to parse between.')
    return text

def fileRenamer(fileName, keyword):
    fileName = fileName.replace(' ', '_')
    fileName = fileName.replace('.pdf', '')
    newFileName = keyword.upper() + '_' + fileName + '.txt'
    return newFileName

def folderCreator(location, keyword):
    os.makedirs(location / keyword.upper(), exist_ok=True)
    keywordFolder = Path(location / keyword.upper())
    return keywordFolder