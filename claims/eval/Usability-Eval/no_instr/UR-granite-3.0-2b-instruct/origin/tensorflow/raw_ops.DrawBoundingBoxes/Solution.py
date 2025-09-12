import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

# Load a pre-trained model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Load an image
img_path = 'path_to_your_image.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = tf.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make a prediction
preds = model.predict(x)

# Decode the predictions
decoding_preds = decode_predictions(preds, top=3)[0]

# Draw bounding boxes on the image
for i, (i, pred) in enumerate(decoding_preds):
    color = (0, 255, 0) if i == 0 else (255, 0, 0)
    y1, x1, y2, x2 = pred[1] * 224, pred[0] * 224, pred[1] * 224 + pred[2] * 224, pred[0] * 224 + pred[3] * 224
    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
    cv2.putText(img, f'Class: {decoding_preds[i][1]}', (int(x1), int(y1) - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
