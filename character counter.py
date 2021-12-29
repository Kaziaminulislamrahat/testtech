#Length Count
x = input('Enter your name:')
y=str(x)
print("With space total character:", len(y))
#Word Count
word_list = y.split()
number_of_words = len(word_list)
print("Total Word:", number_of_words)
#Line Count
line_count=y.count('\n')+1
print("Line:", line_count)
#Letter Frequency
lower_case_string=y.lower()
dict_counter = {}  
                   
for char in lower_case_string:          
    if not dict_counter or char not in dict_counter.keys():                                             
        dict_counter.update({char: 1})                
    elif char in dict_counter.keys():                              
        dict_counter[char] += 1
        dict_counter.pop(' ', None)    #For white space remove
for key, val in dict_counter.items():
    print(key,":",  val)


