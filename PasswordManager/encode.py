from cryptography.fernet import Fernet

class encode_decode:
    def encodepass(self,password):
        key = b'WYMBojcmFsh59plms9aXG4WCJG-nPcq-3q36IybNjzI='    
        self.fernet = Fernet(key)
        self.encPassword = self.fernet.encrypt(password.encode())
        return self.encPassword.decode()

    def decodepass(self,encPassword):
        key = b'WYMBojcmFsh59plms9aXG4WCJG-nPcq-3q36IybNjzI='
        self.fernet = Fernet(key)
        self.decPassword = self.fernet.decrypt(encPassword.encode()).decode()
        return self.decPassword