import os

def hasnum(s):
    return any(i.isdigit() for i in s)

def parse(num):
    found_chap = False
    global txt
    with open('ddj.txt', 'r') as file:
        txt = file.readlines()
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

def hanresp(msg) -> str:
    global num
    num = int(msg)
    cont = parse(num)
    if cont:
        pmsg = '**Chapter {0}**\n{1}'.format(num, "\n".join(cont))
        return pmsg
    else:
        pmsg = 'Chapter {0} not found'.format(num)
        return pmsg