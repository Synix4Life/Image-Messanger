from ops.generator import generate
from ops.degenerator import degenerate

def main() -> None:
    filename = input("Please give me the filename (*.png): ")
    if not filename.endswith(".png"):
        raise NameError("Given incorrect filename")
    
    message = input("Please now give me the message: ")
    generate(message, filename)
    
    try:
        result = degenerate(filename)
    except ValueError as e:
        print(e)
        return
    
    print(f"Message is: {result}")

if __name__ == '__main__':
    main()