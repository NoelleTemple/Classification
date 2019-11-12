from classification_pkg.classifcation import deepNet

obj = deepNet(img = "https://files.slack.com/files-pri/TMTRE2L81-FQ4CAU7FV/image_from_ios.png")
obj.eval()
print ("Object is {}, {} % sure".format(obj.getname(), obj.getPercent()))
