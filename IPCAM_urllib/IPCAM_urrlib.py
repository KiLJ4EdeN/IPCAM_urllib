import urllib.request
import cv2
import numpy as np
import face_recognition
from PIL import Image, ImageDraw

# open the desired url to take a photo
# exapmle : (url = 'http://192.168.10.1/media/?action=snapshot')
url = 'http://camera_ip/snapshot_end'

# enter the username and password
# example : username, password = 'admin', 'admin'

username = 'username'
password = 'password'

# Set up password handling object
p = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# add user name and password for the url
p.add_password(None, url, username, password)

# use the auth handler class to open the url with the saved information
handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)
imgResp = urllib.request.urlopen(url)

while 1 > 0:
    # enter a loop to get image data from the url and display it
    
    imgResp = urllib.request.urlopen(url)
    # transform the image data from bytes to numpy array
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    
    # decode the image 
    test_image = cv2.imdecode(imgNp, -1)
    
    ##### any processing to the image can be done here ex: b & w  ######
    
    # display the image using open cv
    cv2.imshow('test', test_image)
    
    # set a criteria for the code to stop
    if ord('q') == cv2.waitKey(10):
        cv2.destroyallwindows()
        exit(0)
