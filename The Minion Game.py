def minion_game(string):
    vowel='AEIOU'
    str_len=len(string)
    k_scr=0
    s_scr=0

    for i in range(str_len):
        if s[i] in vowel:
            k_scr +=(str_len-i)
        else:
            s_scr +=(str_len -i)


    if k_scr > s_scr:
        print("Kevin",k_scr)
    elif k_scr < s_scr:
        print("Stuart",s_scr)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
