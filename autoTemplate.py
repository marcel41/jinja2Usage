from jinja2 import Environment, FileSystemLoader
import os

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('index.html')


course = os.path.join(root, 'testCourse')
dirList = [item for item in os.listdir(course) if os.path.isdir(os.path.join(course, item))]
listWithFiles = []
for i in dirList:
    tempDict = {}
    #print (i)
    moduleToLookAt = os.path.join(course,i)
    txtFile = [itemtxt for itemtxt in os.listdir(moduleToLookAt) if itemtxt.endswith('txt')]
    pyFile = [itempy for itempy in os.listdir(moduleToLookAt) if itempy.endswith('py')]
    tempDict['module'] = i
    tempDict['lectures'] = txtFile[0]
    tempDict['pathLecture'] = './testCourse/' +  i + "/" + txtFile[0]
    tempDict['labs'] = pyFile
    tempDict['pathXD'] = []
    listOfPaths = []
    for pathToDownloadPy in pyFile:
      #print(os.path.join(i,pathToDownloadPy))
      #tempDict['pathXD'] = os.path.join(i,pathToDownloadPy)
      #listOfPaths.append(os.path.join('\\testCourse',i,pathToDownloadPy))

      listOfPaths.append('./testCourse/' +  i + "/" + pathToDownloadPy)
    print(listOfPaths)
    tempDict['pathXD'] = listOfPaths
    if(len(tempDict['labs']) != len(tempDict['pathXD'])):
      print("ERROR")
    for XDXD in tempDict['pathXD']:
      print(XDXD)
    listWithFiles.append(tempDict)
    #print(txtFile)
    #print(pyFile)

# for file in listWithFiles:
#     print(file['labs'])
filename = os.path.join(root, 'index.html')
# templateXD = template.render(h1 = "Hello Jinja2",
#                             show_one = True,
#                             show_two = False,
#                             names2    = ["Foo", "", "Qux"],
#                             names    = dirList,
#                             modulesToPrint = listWithFiles,)
#
# with open(filename, 'w') as fh:
#     fh.write(templateXD)
#print(templateXD)
with open(filename, 'w') as fh:
    fh.write(template.render(
        h1 = "Hello Jinja2",
        modulesToPrint = listWithFiles,
    ))
