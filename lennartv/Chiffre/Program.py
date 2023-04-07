from ChiffreFactory import ChiffreFactory
from ChiffreFactory import ChiffreType

def ShowChiffre(type: ChiffreType, msg: str, blockLength: int = None, key: str = None) -> None: # type: ignore
    chiffre = ChiffreFactory.CreateChiffre(type, blockLength, key)
    print("Demonstrating: " + str(chiffre.Name))
    print("Message: " + msg)
    
    encryptedMsg = chiffre.Encrypt(msg)
    print("Encrypted Message: " + encryptedMsg)
    
    decryptedMsg = chiffre.Decrypt(encryptedMsg)
    %timeit chiffre.Decrypt(encryptedMsg) # type: ignore
    print("Decrypted Message: " + decryptedMsg)


msg = "This message is very important."
ShowChiffre(ChiffreType.SkytaleChiffre, msg)
ShowChiffre(ChiffreType.CaesarChiffre, msg)
ShowChiffre(ChiffreType.SkytaleChiffre, msg)