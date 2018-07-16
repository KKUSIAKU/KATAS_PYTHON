def longest_repetition(chars):
    chars_list = list(chars)
    print(chars_list)
    chars_dic = {}
    key=''
    for c in chars_list:
        if chars_dic.get(c) != None:
            chars_dic[c] += 1
        else:
            chars_dic[c]=0
    
    
    return chars_dic