#Facial Detection
import face_recognition
image = face_recognition.load_image_file("your_file.jpg")
face_locations = face_recognition.face_locations(image)
face_locations = face_recognition.face_locations(image)
top, right, bottom, left = face_locations[0]
face_image = image[top:bottom, left:right]

#Facial Recognition
encoding_1 = face_recognition.face_encodings("your_file.jpg")[0]

encoding_2 = face_recognition.face_encodings("your_file.jpg")[0]

results = face_recognition.compare_faces([encoding_1], encoding_2,tolerance=0.50)

#Emotion Detection
import numpy as np
model = face_recognition.load_model("./emotion_detector_models/model.hdf5")
predicted_class = np.argmax(model.predict(face_image)




################I have to train the model with certain epochs so that the model will be trained better than the past. 