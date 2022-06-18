from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

model = load_model('keras_model.h5')
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
image = Image.open('/PATH/TO/FILE')
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)
image_array = np.asarray(image)
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
data[0] = normalized_image_array
prediction = (model.predict(data) > 0.5).astype("int32")
#print(prediction)
predictiontolist = prediction.tolist()
listelements = predictiontolist[0]
if int(listelements[0]) == int('1'):
    print('Boat')
elif int(listelements[1]) == int('1'):
    print('Airplane')
elif int(listelements[2]) == int('1'):
    print('Car')
