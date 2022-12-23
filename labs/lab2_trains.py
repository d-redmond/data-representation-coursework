# Get the data
import requests
import csv
from xml.dom.minidom import parseString
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)

# Store all the names of tags we want to retrieve
retrieveTags=['TrainStatus',
'TrainLatitude',
'TrainLongitude',
'TrainCode',
'TrainDate',
'PublicMessage',
'Direction'
]

# Check it works, outputs to console
# print(doc.toprettyxml())

# To store the xml in a file
# with open("lab2_trains.xml","w") as xmlfp:
#   doc.writexml(xmlfp)

# Print out each of the traincodes
# objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
# for objTrainPositionsNode in objTrainPositionsNodes:
#     traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
#     traincode = traincodenode.firstChild.nodeValue.strip()
#     print(traincode)

# Print out the latitudes
# objTrainLongitudeNodes = doc.getElementsByTagName("objTrainLongitude")
# for objTrainLongitudeNode in objTrainLongitudeNodes:
#     traincodenode = objTrainLongitudeNode.getElementsByTagName("TrainCode").item(0)
#     traincode = traincodenode.firstChild.nodeValue.strip()
#     print(traincode)

# Store property into CSV
with open('week02_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        dataList = []
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)

# Only store the trains whose traincode starts with "D"