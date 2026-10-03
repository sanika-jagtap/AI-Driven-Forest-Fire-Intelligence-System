import os
import requests
from tensorflow.keras.utils import load_img,img_to_array
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('model/svm_final.h5')


def isFireDetected(img):
  print("inside SVM")
  retsultstr="Fire"  
  test_image = load_img(img, target_size=(224,224))
 # plt.imshow(test_image)
  test_image = img_to_array(test_image)
  test_image=test_image/255
  test_image = np.expand_dims(test_image, axis = 0)
  result = model.predict(test_image)
  #print(result)
  if result[0]>0.3 and result[0]<1:
      retsultstr="No Fire Detected"
  else:
      retsultstr="Fire Detected"
      
  return retsultstr    
      
# image_path="Input_map.jpg"
# print("Image is Pulled ")
# resulststr=isFireDetected(image_path)  
# print("resulststr ",resulststr)    

