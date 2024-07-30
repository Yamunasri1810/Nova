import face_recognition
import cv2

# Load the known faces
known_faces = []
known_names = []

# Load the face recognition model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Define a function to recognize faces
def recognize_face(frame):
    # Convert the frame to RGB
    rgb_frame = frame[:, :, ::-1]
    
    # Find all the faces in the frame
    faces = face_cascade.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5)
    
    # Loop through each face
    for (x, y, w, h) in faces:
        # Extract the face ROI
        face_roi = rgb_frame[y:y+h, x:x+w]
        
        # Recognize the face
        face_encoding = face_recognition.face_encodings(face_roi)[0]
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        
        # If a match is found, greet the user
        if True in matches:
            index = matches.index(True)
            name = known_names[index]
            print(f"Hello, {name}!")
