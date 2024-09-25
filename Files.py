__version__ = '1.1.2'
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
    def copy(self, path: str = None, file: str = None, destiny: str = None) -> None:
        self._pathFileComplet = os.path.join(path, file)
        shutil.copy(self._pathFileComplet, destiny)

    '''
        create a new folder from  of specifications what past and copy at the a place for other
    '''
    def craeteForlderAndCopy(self, name_folder: str = None, path : str = None, file: str = None, destiny: str = None) -> None:
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
    def renameFiles(self, path: str = None, files: str = None, extension: str = None) -> None:

        itens = os.listdir(path)

        for i in range(len(itens)):
            self._folder = os.path.join(path, itens[i])
            self._renameFile = os.path.join(path, files[i])

            self._name, self._extension = os.path.splitext(itens[i]) 

            if self._extension != extension:
                print('if')
                os.rename(self._folder, f'{self._renameFile.replace(f"{self._extension}", "")}.{extension}')

    '''
        Check if files is at folder if not have wait teh download or something like that
    '''
    def check_file_with_extension(self, directory, extension) -> None:
        self._check = True
        while self._check:
            time.sleep(2)
            try:
                for file_name in os.listdir(directory):
                    if file_name.endswith(extension):
                        self._check = False
            except:
                self._check = True
        
    def delete(self, path) -> None:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)  # Remove the file
            elif os.path.isdir(path):
                shutil.rmtree(path)  # Remove the directory and its contents
    
    def move_file(self, nameFile, destinyFile) -> None:
            self._destination_path = os.path.join(destinyFile, os.path.basename(nameFile))
            shutil.move(nameFile, self._destination_path)
                
    def create_text(self, nameFile) -> None:
        self._nameFile = nameFile

        with os.fdopen(os.open(self._nameFile, os.O_WRONLY | os.O_CREAT), 'wb') as file:
            pass
            
    def convert_file(self, nameFile, newNameFile) -> None:
        self._filetxt = nameFile
        self._fileBat = newNameFile

        os.rename(self._filetxt, self._fileBat)
