sentence=(input())
for i in range(500):
    sentence+=str(input())
print(sentence)
alfavit=('а|б|в|г|д|е|ё|ж|з|и|й|к|л|м|н|о|п|р|с|т|у|ф|х|ц|ч|ш|щ|ъ|ы|ь|э|ю|я'.split('|'))
for i in range(33):
    print(alfavit[i],';',sentence.count(alfavit[i]))
