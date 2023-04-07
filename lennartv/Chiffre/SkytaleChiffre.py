import ChiffreBase

class SkytaleChiffre(ChiffreBase): # type: ignore
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
        
        return msg
    
    def Break(self, encryptedMsg: str) -> str:
        msg = ""
        return msg