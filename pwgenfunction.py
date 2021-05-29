# function to generate the password

try:
    from string import ascii_letters, digits, punctuation, join
except ImportError:
    from string import ascii_letters, digits, punctuation
from random import choice, sample, randint

def is_even(integer):
    return integer % 2 == 0

# generator
def random_pass(size = 8):
    s0 = ascii_letters 
    s1 = digits
    s3 = "!$%^&*- _~"
    s = s0 + s1
    s_full = s + s3
    passlen = size.get()
    new_password = ""

    if is_even(passlen) == True:
        frnt = passlen // 3
    else:
        frnt = passlen // 2
    mid = 2
    bck = passlen - (frnt + mid) - 1

    p0 = "".join(choice(s0))
    p1 = "".join(sample(s_full,frnt ))
    p2 = "".join(sample(s3,mid))
    p3 = "".join(sample(s,bck ))
    if passlen != len(p0 + p1 + p2 + p3):
        p2 = "".join(sample(s3,passlen - (frnt+bck+1) ))

    if p3[:-1] == ' ':
        temp = list(p3)
        temp[:-1] = choice(s)
        p3 = ''.join(str(e) for e in temp)
    new_password = p0 + p1 + p2 + p3    
    
    # colors and strength
    if passlen <= 8:
        msg = 'VERY WEAK'
        color_val = "#6d0001"
    elif passlen <=10:
        msg = 'WEAK'
        color_val = "#cc0000"
    elif passlen <=12:
        msg = 'DECENT'
        color_val = "#fc8600"
    elif passlen <=14:
        msg = 'GOOD'
        color_val = "#eae200"
    elif passlen <=16:
        msg = 'STRONG'
        color_val = "#9ff400"
    elif passlen <=18:
        msg = 'VERY STRONG'
        color_val = "#007715"
    elif passlen >18:
        msg = 'EXCELLENT'
        color_val = "#001fef"
    else:
        pass

    return new_password, msg, color_val