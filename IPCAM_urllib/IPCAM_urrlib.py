import urllib.request
import cv2
import numpy as np
import face_recognition
from PIL import Image, ImageDraw

url = 'http://192.168.10.1/media/?action=snapshot'
username = 'admin'
password = ''
p = urllib.request.HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)
imgResp = urllib.request.urlopen(url)

while 1 > 0:
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    test_image = cv2.imdecode(imgNp, -1)
    cv2.imshow('test', test_image)
    if ord('q') == cv2.waitKey(10):
        cv2.destroyallwindows()
        exit(0)
