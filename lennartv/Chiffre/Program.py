from ChiffreFactory import ChiffreFactory
from ChiffreFactory import ChiffreType

def ShowChiffre(type: ChiffreType, msg: str) -> None:
    chiffre = ChiffreFactory.CreateChiffre(type)
    print("Demonstrating: " + str(chiffre.Name))
    print("Message: " + msg)
    
    encryptedMsg = chiffre.Encrypt(msg)
    print("Encrypted Message: " + encryptedMsg)
    
    decryptedMsg = chiffre.Decrypt(encryptedMsg)
    print("Decrypted Message: " + decryptedMsg)


