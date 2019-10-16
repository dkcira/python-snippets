# find if two string are anagrams (formed by rearranging letters of each other)

from collections import Counter

str1, str2, str3 = 'pasadena', 'asapedna', 'nadepasa'
cnt1, cnt2, cnt3 = Counter(str1), Counter(str2), Counter(str3)

if cnt1 == cnt2:
    print (str1 + ' and ' + str2 + ' are anagrams')
if cnt1 == cnt3:
    print (str1 + ' and ' + str3 + ' are anagrams')