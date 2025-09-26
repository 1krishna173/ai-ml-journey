# with open('example.txt','r') as file:
    # print(file.read()) This helps in reading the file
    
# with open('example.txt','w') as file:
    # file.write('this overwrites which is an issue') 
    
# with open ('example.txt','a') as file:
#     file.write("THis will append Directly to file")
    
# lst=['First line\n','second line\n']
# with open ('example.txt','a') as file:
#     file.writelines(lst)

# read a file and count the number of lines words and chareceters
# cnt_line=0
# cnt_words=0
# cnt_ch=0
# with open('example.txt','r') as file:
#     for line in file:
#         # print(word.strip())
#         cnt_line+=1
#         cnt_ch+=len(line)
#         cnt_words+=len(line.split())

# print(cnt_line,cnt_words,cnt_ch)
    
# with open('new.txt','w+')as file:  # in this mode if the file is not created it creates and then overwrites it
#     file.write("Hello WOrld!\n this was my first program in C")
#     file.seek(0)# moves the cursor to the begining
#     content=file.read()
#     print(content)

import os 
# items=os.listdir('.')
# print(items)
new_direc="folder"
new_file="file.txt"
print(os.path.join(os.getcwd(),new_direc,new_file))


    