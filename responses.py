# Reponse Handler for bot.py
def hasnum(s):
    return any(i.isdigit() for i in s)

availtrans = {
    "sm": "Stephen Mitchell",
    "gia": "Gia-Fu Feng",
    "wtc": "Wing-Tsit Chan",
}

def parse(num, trans):
    found_chap = False
    global validtrans
    validtrans = True
    global txt
    req = "daodelightful/translations/{}ddj.txt".format(trans)
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

def hanresp(chap, translation) -> str:
    global num 
    num = int(chap)
    cont = parse(num, translation)
    atrans = availtrans[str(translation)]
    if cont:
        if validtrans:
            pmsg = '**Chapter {0} - ({1})**\n{2}'.format(num, atrans, "\n".join(cont))
            return pmsg
        else:
            return errormsg
    else:
        pmsg = 'Chapter {0} not found'.format(num)
        return pmsg