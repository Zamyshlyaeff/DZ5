# Дана строка(возможно,пустая), состоящая из букв AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB
# BBBBBBBBBBBBBBBBBBBBBBB, написать функцию RLE которая выдаст строку вида: A4B3C2X1 и тд
str1='AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBB'
def RLE(str1):
    count=0 
    str2=''
    for i in range(1,len(str1)):
      if str1[i-1]==str1[i]:
         count+=1
      else: 
         str2+=str1[i-1]
         if count>0:
            str2+=str(count)
            count=0
         

    return str2


print(RLE(str1))

