def countWordsfromFile():
    fileName= input('Enter File Name:- ')
    noOfWords = 0
    file = open(fileName,'r')
    for fileData in file:
        words = fileData.split(',')
        noOfWords = noOfWords + len(words)
    print('Number Of Words- ')
    print(noOfWords)

countWordsfromFile()