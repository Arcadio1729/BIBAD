def get_forms(sentence):
    SPECIAL_CHARACTERS = [".",",","?","\\r\\n","b\'","\'","!",":","-","\"","(",")",";","$"]
    for sc in SPECIAL_CHARACTERS:
        sentence = str(sentence).replace(sc, " ")
    return sentence.split()


def count_forms(words):
    forms_amount = {}
    last_word = words[0]
    current_word_amount = 0
    for w in words:
        if w != last_word:
            forms_amount[str(last_word)] = current_word_amount
            current_word_amount = 1
            last_word = w
        else:
            last_word = w
            current_word_amount += 1
    forms_amount[str(last_word)] = current_word_amount
    return forms_amount


def get_digrams(words):
    digrams=[]
    for i in range(len(words) - 1):
        digrams.append(words[i:(i+2)])
    return digrams

def get_trigrams(words):
    trigrams=[]
    for i in range(len(words) - 2):
        trigrams.append(words[i:(i + 3)])
    return trigrams


def generate_forms(path):
    forms = []
    with open(path) as infile:
        for line in infile:
            forms.append(get_forms(line))
    return forms


def generate_forms_from_txt(path):
    with open(path,'rb') as infile:
        for line in infile:
            for current_form in get_forms(line):
                yield clean_polish(current_form)

def clean_polish(word):
    polish_dict={"\\xc3\\xb3":"ó","\\xc4\\x84":"Ą","\\xc4\\x85":"ą","\\xc4\\x86":"Ć","\\xc4\\x87":"ć","\\xc4\\x98":"Ę","\\xc4\\x99":"ę","\\xc5\\x81":"Ł","\\xc5\\x82":"ł","\\xc5\\x83":"Ń","\\xc5\\x84":"ń","\\xc5\\x9a":"Ś","\\xc5\\x9b":"ś","\\xc5\\xb9":"Ź","\\xc5\\xba":"ź","\\xc5\\xbb":"Ż","\\xc5\\xbc":"ż"}
    for pd in polish_dict.keys():
        word=word.replace(pd,polish_dict[pd])

    return word

def sort_insertion(A):
    for j in range(1,len(A),1):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key
    return A


def find_minimum_index(A,start_position):
    minimum_index=start_position
    for i in range(start_position,len(A),1):
        if A[i]<A[minimum_index]:
            minimum_index=i
    return minimum_index

def sort_selection(A):
    for current_index in range(len(A)):
        minimum_index=find_minimum_index(A,current_index)
        A[current_index],A[minimum_index]=A[minimum_index],A[current_index]
    return A

def print_first_n_from_dict(working_dict,n):
    last_value=""
    counter=0
    for key in working_dict:
        if counter>n and last_value==key:
            print(key+"-"+str(working_dict[key]))
            last_value=key
            counter=counter+1
        else:
            if counter<=n:
                print(key + "-" + str(working_dict[key]))
                last_value = key
                counter = counter + 1


if __name__ == "__main__":

    #zad1
    sample_list = [6, 50, 11, 8, 20, 20, 5, 98, 36]
    sorted_by_insertion=sort_insertion(sample_list)

    #zad2
    sample_list = [6, 50, 11, 8, 20, 20, 5, 98, 36]
    sorted_by_insertion = sort_selection(sample_list)

    #zad3
    forms=[]
    path = "potop.txt"
    for mg in generate_forms_from_txt(path):
       forms.append(str(mg))

    #zad4 https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value used for sorting dict by value
    digrams=get_digrams(forms)
    digrams.sort()
    counted_digrams=count_forms(digrams)
    sorted_counted_digrams={k: v for k, v in sorted(counted_digrams.items(), key=lambda item: item[1],reverse=True)}
    print_first_n_from_dict(sorted_counted_digrams,20)
    trigrams=get_trigrams(forms)
    trigrams.sort()
    counted_trigrams=count_forms(trigrams)
    sorted_counted_trigrams={k: v for k, v in sorted(counted_trigrams.items(), key=lambda item: item[1],reverse=True)}
    print_first_n_from_dict(sorted_counted_trigrams,20)
    #print_first_n_from_dict(sorted_counted_trigrams,20)