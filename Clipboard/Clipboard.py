import pyperclip
import re
from Macro import Macro

def pdf_edit():
    """
    Function that removes most extraneous newline characters from the clipboard when triggered. 

    """
    current_clip = pyperclip.paste()
    output = re.sub(r"([^\\.])\r\n", r"\1 ", current_clip)
    pyperclip.copy(output)


if __name__=="__main__":
    Macro(pdf_edit)