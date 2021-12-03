#Import Modules ...
import random
import string
import pandas as pd

class gen:
    def generatepass(self,len,radio):
        self.length = len
        self.lower = "abcdefghijklmnopqrstuvwxyz"
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
        self.digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*_/?"
        self.password = ""
    
        # if strength selected is low
        if radio=='low':
            for _ in range(0,self.length):
                self.password += random.choice(self.lower)
            return self.password
    
        # if strength selected is medium
        elif radio=='medium':
            for _ in range(0, self.length):
                self.password += random.choice(self.upper)
            return self.password
    
        # if strength selected is strong
        elif radio=='strong' :
            for _ in range(0,self.length):
                self.password += random.choice(self.digits)
            return self.password

    def copy1(self,password):
        self.df=pd.DataFrame([password])
        self.df.to_clipboard(index=False,header=False)
