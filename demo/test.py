from classification_pkg.classification import deepNet

obj = deepNet(img = "gr.jpg")
obj.eval()
print ("Object is {}, {} % sure".format(obj.getName(), obj.getPercent()))
