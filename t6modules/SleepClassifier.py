# This module is to predict status of user's bed taken at a picture.

import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

class SleepClassifier():
    
    def __init__(self):
        self.model = self.loadModel()
    
    def loadModel(self):
        with open('model2.json') as json_file:
            json_config = json_file.read()
        status_model = tf.keras.models.model_from_json(json_config)
        # print(status_model.layers)
        status_model.load_weights('model_weights2.h5')
        return status_model
    
    
    def imgLoad(self, img_path):
        try:
            print("Loading Imange")
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            print("Image Processing")
            expanded_img_array = np.expand_dims(img_array, axis=0)
            preprocessed_img = expanded_img_array / 255.  # Preprocess the image
            return  preprocessed_img
        except:
            return []
    
    
    def getStatus(self, img_path):
        preprocessed_img = self.imgLoad(img_path)
        print("Get processed image")
        prediction = self.model.predict(preprocessed_img)

        print('non: %f, not sleeping %f, sleeping: %f\n\n' %(prediction[0][0],prediction[0][1],prediction[0][2]))

        status = ""
        threshold = 0.5
        if prediction[0][0] > threshold:
            status = 'non'
        elif prediction[0][1] > threshold:
            status = 'not sleeping'
        elif prediction[0][2] > threshold:
            status = 'sleeping'
        else:
            status = 'chaos'
            
        print('Now status is that: ' + str(status))
        return status

    
print("Module Loaded : sleep classifier")