# Reponse Handler for bot.py

def hasnum(s):
    """Checks if the string contains a number"""
    return any(i.isdigit() for i in s)


availtrans = {
    "sm": "Stephen Mitchell",
    "gia": "Gia-Fu Feng",
    "wtc": "Wing-Tsit Chan",
}


def parse(num: int, trans):
    """
    Parses the .txt files and adds each requested line
    to make up the final message
    sent to user.

    Parameters:
        num (int): The requested chapter from user.
        trans (str): The requested translation from user.
    Returns:
        str: The result of parsing the .txt file,
        i.e. contents of requested chapter.
    """
    found_chap = False
    global validtrans
    validtrans = True
    global txt
    req = "daodelightful/translations/{}ddj.txt".format(trans) # noqa
    try:
        with open(req, 'r') as file:
            txt = file.readlines()

    except FileNotFoundError:
        validtrans = False
        global errormsg
        errormsg = "Translation {} is not a valid translation.".format(trans)
        return errormsg

    res = []
    for line in txt:
        if hasnum(line):
            chap = ""
            in_digit_sequence = False

            for char in line:
                chap += char
                if char.isdigit():
                    in_digit_sequence = True
                else:
                    break

            if in_digit_sequence:
                chap = int(chap)
                if chap == num:
                    found_chap = True
                elif found_chap:
                    break

        if found_chap and not hasnum(line):
            res.append(line.strip())

    return res


def hanresp(chap: int, translation):
    """
    Handles the data from parse() and returns the
    final message to be sent by the bot.

    Parameters:
        chap (str): The requested chapter from user.
        translation (str): The requested translation from user.

    Returns:
        str: The message to be sent by the bot
        (error message or chapter content).
    """
    cont = parse(chap, translation)
    atrans = availtrans[str(translation)]
    if cont:
        if validtrans:
            pmsg = '**Chapter {0} - ({1})**\n{2}'.format(chap, atrans, "\n".join(cont))  # noqa
            return pmsg
        else:
            return errormsg
    else:
        pmsg = 'Chapter {0} not found'.format(chap)
        return pmsg
