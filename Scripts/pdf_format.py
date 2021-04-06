import re, pdfminer.high_level, os
from pathlib import Path

class PdfFormat:
    """ Class for pdf extraction """

    def __init__(self):
        """ initialises location, keyword and regex """
        self.keyword = input('Enter Keyword/Search term: ')
        self.location = Path(input('Enter FOLDER location: '))
        self.searchRegex = re.compile(f'[^.?!]*(?<=[.?\s!]){self.keyword}[a-zA-Z]*(?=[\s.?!])[^.?!]*[.?!]')
        self.introRef = re.compile(r'introduction(.*)references')

    def pdf_2_text(self, filename):
        """ Tidies up pdf text and converts to string """
        self.text = pdfminer.high_level.extract_text(filename)
        self.text = self.text.lower()
        self.text = self.text.replace('\n\n', '\n')
        self.text = self.text.replace('-\n', '')
        self.text = self.text.replace('\n', ' ')
        try:
            parsedText = re.search(self.introRef, self.text)
            self.text = parsedText.group(1)
        except:
            print('No Introduction or References to parse between.')
        return self.text
    
    def file_renamer(self, fileName):
        """ Renames filename """
        self.fileName = fileName.replace(' ', '_')
        self.fileName = self.fileName.replace('.pdf', '')
        newFileName = self.keyword.upper() + '_' + fileName + '.txt'
        return newFileName

    def folder_creator(self):
        """ Create folder """
        os.makedirs(self.location / self.keyword.upper(), exist_ok=True)
        keywordFolder = Path(self.location / self.keyword.upper())
        return keywordFolder
    
    def pdf_walk(self):
        os.chdir(self.location)
        self.keywordFolder = self.folder_creator()
        print(self.keywordFolder)
        for foldername, subfolders, filenames in os.walk(self.location):
            #Loop through each PDF in folder
            for filename in filenames:
                if filename.endswith('.pdf'):
                    print(filename)
                    self.rawText = self.pdf_2_text(filename)
                    sentences = re.findall(self.searchRegex, self.rawText)
                    if len(sentences) > 0:
                        newFileName = self.file_renamer(filename)
                        #Create new folder named findings
                        KeywordFileLocation = open(Path(self.keywordFolder / newFileName), 'w', encoding='utf-8')
                        KeywordFileLocation.write('---' + filename + '---\n\n\n\n')
                        for sentence in sentences: 
                            KeywordFileLocation.write(sentence + '\n')
                        KeywordFileLocation.close()
                    else:
                        print(f'No sentences containing {self.keyword} in {filename}.')