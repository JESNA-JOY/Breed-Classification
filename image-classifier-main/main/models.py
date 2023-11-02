from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.vgg16 import decode_predictions

model = VGG16()

def classify_image(image_path):
    # Load the image and preprocess it
    img = load_img(image_path, target_size=(224, 224))
    img = img_to_array(img)
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    img = preprocess_input(img)
    
    # Make a prediction using the model
    yhat = model.predict(img)
    
    # Decode the predictions
    label = decode_predictions(yhat)[0][0][1]
    
    # Return the label
    return label
