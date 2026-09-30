import re
from Extract import extract_text
# For cleaning the text 
def clean_text(text):

    #Remove the Extra Spaces
    text = re.sub(r"[ \t]+"," ",text)

     #Remove excessive new lines
    text = re.sub(r"\n","\n",text)

    # Remove spaces at the beginning/end of each line
    text = "\n".join(
        line.strip()
        for line in text.splitlines()
    )
    #Remove Empty Line
    text = "\n".join(
        line 
        for line in text.splitlines() if line
    )

    return text.strip()

