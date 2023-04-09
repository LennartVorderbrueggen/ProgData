from ChiffreBase import Chiffre

class SkytaleChiffre(Chiffre):
    def __init__(self, blockLength: int) -> None:
        self.Name = "Skytale Chiffre"
        self.stick = []
        self.blockLength = blockLength        
    
    def Encrypt(self, msg: str) -> str:
        res = ""
        for idx in range(0, self.blockLength):
            res += msg[idx::self.blockLength]
        return res
    
    def Decrypt(self, encryptedMsg: str) -> str:
        msg = ""
        for i in range(0, self.blockLength):
            self.stick.append([])
        for idx, char in enumerate(encryptedMsg):
            stickNo = (idx % self.blockLength)
            self.stick[stickNo].append(char)
        for line in self.stick:
            msg += line
        return msg
    
    def Break(self, encryptedMsg: str) -> str:
        msg = ""
        return msg