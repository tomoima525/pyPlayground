### find, if
str1="水金地火木"

str2=input("検索文字列:")

index= str1.find(str2)
if index != -1:
    print('{}が見つかりました!'.format(str2))
    print("index:",index)
else:
    print('見つかりませんでした')
