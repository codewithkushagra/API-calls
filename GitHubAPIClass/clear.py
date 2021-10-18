from os import system, name

class Clear():
    def __init__(self) -> None:
        pass

    def clear():
      
        if name == 'nt':
            _ = system('cls')
    
        else:
            _ = system('clear')