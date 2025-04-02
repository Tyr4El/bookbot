def get_num_words(string_book):
    list_words=string_book.split()
    return len(list_words)

def counting_char(string_book):
    lwr_convert=string_book.lower()
    tmp_dict={}
    for i in range(len(lwr_convert)):
        if lwr_convert[i] in tmp_dict:
           tmp_dict[lwr_convert[i]] +=1
        else :
            tmp_dict[lwr_convert[i]]=1
    return tmp_dict