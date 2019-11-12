from classification_pkg.classification import deepNet
import sys

#maybe this works? maybe it doesn't?
image = sys.argv[1]
obj = deepNet(img = image)
obj.eval()
print ("Object is {}, {} % sure".format(obj.getName(), obj.getPercent()))
