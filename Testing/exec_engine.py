from xml.dom import minidom

'''
testCode = minidom.parse('test.xml')
testList = testCode.getElementsByTagName('item1')
print(len(testList))
for x in testList:
    print(x)
    print(x.firstChild.nodeValue)
'''



buttermilkSource = minidom.parse('Light_PIR_Dusk_Temp_Buttermilk.xml')
actionsList = buttermilkSource.getElementsByTagName('action')
print(actionsList)
