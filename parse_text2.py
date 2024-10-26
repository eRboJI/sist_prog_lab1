from collections import Counter
import os
import sys


def clean_text(text_list):
    '''
    Input:
        text_list - list with all symbols
    Output:
        clean_text_list - cleaned list, words only from letters, digits and -, no zero-len words
    '''
    letters = "йцукенгшщзхъфывапролджэячсмитьбю"
    digits = "0123456789-"
    all_signs = letters + digits
    clean_text_list = list()
    
    for word in text_list:
        clean_word = "".join([i for i in word if i in all_signs])
        '''
        for i in word:
            if i in all_signs:
                clean_word += i
        '''
        if len(clean_word) > 0:
           clean_text_list.append(clean_word)
           
    return clean_text_list

def count_words_dict(text_list):
    '''
    Input:
        text_list - list with all symbols
    Output:
        text_dict - dict with words counter
    '''
    result_dict = dict()
    for word in set(text_list):
        result_dict[word] = text_list.count(word)
    return result_dict   
	
def count_words_counter(text_list):
    '''
    Input:
        text_list - list with all symbols
    Output:
        text_dict - dict with words counter
    '''
    counter = Counter(text_list)
    return dict(counter)

def output_result(file_name,text_dict):
    '''
    Input:
        file_name - file name to output result
        text_dict - dict to output
    '''
    result_text = ''
    for res in text_dict.keys():
        result_text += str(res) + ": " + str(text_dict[res]) + "\n" 
    with open (file_name, "tw") as file:
        file.write(result_text)
       

def count_stat(text,text_dict):
    '''
    Input:
        text - input text
        text_dict - counted on text_dict
    Output:
        result_dict - dict on signs and word lens
    '''
    sign_list = ['.',',',';','?','!','"']
    max_len = max([len(i) for i in text_dict.keys()])

    lens_list = list(range(1,max_len+1))
    result_dict = dict()
    
    for i in sign_list:
        result_dict[i] = text.count(i)
    
    for ln in lens_list:
        word_len_counter = 0
        for i in text_dict.keys():
            if len(i) == ln:
                word_len_counter += text_dict[i]
        print(ln," *** ",word_len_counter)
        result_dict[ln] = word_len_counter
    
    print(result_dict)
    iter_list = list(result_dict.keys())
    for i in iter_list:
        print(i,result_dict[i] )
        if result_dict[i] == 0:
            print('***')
            del result_dict[i] 
    return result_dict
    
def output_stat():	
	pass 
    
if __name__ == "__main__":
    arg_list = sys.argv
    print(arg_list)
    file_name = sys.argv[-1]
    with open (file_name, "tr") as file:
        text = file.read()
    print(os.getcwd())
    print("INITIAL TEXT",text)
    text = text.lower()
    text_list = text.split()
    clened_text_list = clean_text(text_list)
    print("CLEANED TEXT LIST",clened_text_list)
    
    word_counter = count_words_counter(clened_text_list)
    print("WORD COUNTER",word_counter)
    output_result("word_stat.txt",word_counter)
    
    result_stat_dict = count_stat(text,word_counter)
    print("RESULT STAT DICT ",result_stat_dict)
    output_result("final_stat.txt",result_stat_dict)
    
    
    