from ops.generator import generate
from ops.reconstructor import reconstruct

def _file():
    filename = input("Please give me the filename (*.png): ")
    if not filename.endswith(".png"):
        raise NameError("Given incorrect filename")
    return filename

def main() -> None:
    choice = input("Please tell me if you want to (a) encode a string into an image or (b) reconstruct the string from an image: ")
    
    if(choice.lower().strip() == "a"):
        filename = _file()
        message = input("Please now give me the message: ")
        generate(message, filename)
    elif (choice.lower().strip() == "b"):
        try:
            filename = _file()
            print(f"Message is: {reconstruct(filename)}")
        except FileNotFoundError as e:
            print(e)
    else:
        raise ValueError(f"{choice} not recognized!")

if __name__ == '__main__':
    main()