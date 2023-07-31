import os
import tensorflow as tf
import cv2
import numpy as np

def getIndex(oneHotEncodedTab):
    index = 0
    for i in range(len(oneHotEncodedTab)):
        if oneHotEncodedTab[i] == 1:
            index = i
    return index

size =128
categories = ['Bacterial_spot', 'Early_blight', 'Healthy', 'Late_blight', 'Leaf_Mold', 'Mosaic_virus', 'Powdery_mildew', 'Rust', 'Spider_mites', 'Target_Spot']

loaded_model = tf.keras.models.load_model('modelPlantPal01')

images = []

for image in os.listdir("testData"):
    print(image)
    img_array = cv2.imread(os.path.join("testData", image))
    img_resized = cv2.resize(img_array, (size, size))
    print(img_resized.shape)
    images.append(img_resized)

images = np.array(images)
pred = loaded_model.predict(images)

for i in range(len(images)):
    getIndex(pred[i])
    print(categories[getIndex(pred[i])])
print("done !")