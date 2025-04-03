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
## proposed by AI
#def sorting_resultset(dict_result):
#    sorted_result=sorted(dict_result.items(), key=lambda x: x[1], reverse=True)
#    return sorted_result
def sort_on(dict):
    return dict["count"]
def sorting_results(list_working):
    return list_working.sort(reverse=True, key=sort_on)
def transform_dict(x_dict):
    list_dict=[]
    for i in x_dict:
        list_dict.append({"char":i,"count":x_dict[i]})
    sorting_results(list_dict)
    return list_dict
