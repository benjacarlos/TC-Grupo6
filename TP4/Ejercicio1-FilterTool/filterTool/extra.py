def printTransferFunctionInput(numberList):
    myNumString = ""

    print ("VENGO A IMRPIMIT JEJE")
    # Representación en unicode para potencias de 2,3,4,5,6,7,8,9 #

    unicodes = ['', '', '\u00B2', '\u00B3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079']
    for i in range(len(numberList)):
        if (numberList[i]) > 0 and i == 0 and len(numberList) == 1:
            myNumString += (f"{(numberList[i]):.3}")
        elif (numberList[i]) > 0 and i == 0:
            myNumString += ((f"{(numberList[i]):.3}") + "S" + str(unicodes[len(numberList) - i - 1]))
        elif (numberList[i] > 0) and i == (len(numberList) - 1):
            myNumString += ("+" + (f"{(numberList[i]):.3}"))
        elif (numberList[i] < 0) and i == (len(numberList) - 1):
            myNumString += ((f"{(numberList[i]):.3}"))
        elif (numberList[i]) > 0 and i != 0:
            myNumString += ("+" + (f"{(numberList[i]):.3}") + "S" + str(unicodes[len(numberList) - i - 1]))
        elif numberList[i] < 0:
            myNumString += ((f"{(numberList[i]):.3}") + "S" + str(unicodes[len(numberList) - i - 1]))
    return str(myNumString)