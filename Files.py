"""
    Import all libraries bibliotecas what i am using at the script
"""
import shutil
import time
import os

class Files:
    def __init__(self):
        pass

    '''
        Copy any file
    '''
    def copy(self, path: str = None, file: str = None, destiny: str = None):
        self._pathFileComplet = os.path.join(path, file)
        shutil.copy2(self._pathFileComplet, destiny)

    '''
        create a new folder from  of specifications what past and copy at the a place for other
    '''
    def craeteForlderAndCopy(self, name_folder: str = None, path : str = None, file: str = None, destiny: str = None):
        self._nameFolder = name_folder

        if not os.path.exists(name_folder):
            os.makedirs(self._nameFolder, exist_ok=True)
            self.copy(path, file, destiny)

        else:
            self.copy(path, file, destiny)

    '''
        Create folder from especigications 
    '''
    def create(self, name_folder: str = None):
        if not os.path.exists(name_folder):
            os.makedirs(name_folder, exist_ok=True)

    '''
        Rename alls files whet have at folfer
        Enough to spend the path and name at the files together the extension
        Must be spend a the format at list  
    '''
    def renameFiles(self, path: str = None, files: str = None, extension: str = None):

        itens = os.listdir(path)

        for i in range(len(itens)):
            self._folder = os.path.join(path, itens[i])
            self._renameFile = os.path.join(path, files[i])

            os.rename(self._folder, f'{self._renameFile}.{extension}')
            print(self._folder)

    '''
        Check if files is at folder if not have wait teh download or something like that
    '''
    def checkFileWithExtension(self, directory, extension):
        self._check = True
        while self._check:
            time.sleep(2)
            try:
                for file_name in os.listdir(directory):
                    if file_name.endswith(extension):
                        self._check = False
            except:
                self._check = True

    def delete(self, path):
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)  # Remove the file
            elif os.path.isdir(path):
                shutil.rmtree(path)  # Remove the directory and its contents
