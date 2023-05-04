def loadHuto(huto = []):
    inp = input("Mi van még a hütőben?\n")
    while inp != "":
        huto.append(inp)
        inp = input("Mi van még a hütőben?\n")
    return huto

def askForOperation():
    return input("---\n\nMit szeretnél csinálni?\n1. Ételek listázása\n2.Ételek kivétele a hütőből\n3. Étel berakasa a hűtőbe\n4. Takatítás - hűtő kiüritése\n5. kilépés\nCH:")

def writeList(huto):
    print(f"{huto}")
    return True

def removeItem(huto):
    item = input(f"Melyik elemet szeretnéd kivenni? [{huto}]")
    for i in huto:
        if i == item:
            huto.remove(i)
    return True

def addItem(huto):
    item = input(f"Addj hozzá egy új elemet\nÚj elem:")
    huto.append(item)
    return True

def reset(huto):
    huto.clear()
    return True

def validOption(ch, huto):
    match ch:
        case "1":
            return writeList(huto)
        case "2":
            return removeItem(huto)
        case "3":
            return addItem(huto)
        case "4":
            return reset(huto)
        case "5":
            return False

def main():
    huto = loadHuto()
    ch = askForOperation()
    while validOption(ch, huto):
        ch = askForOperation()
            
main()