from scipy.spatial.distance import cosine
import mtcnn
from keras.models import load_model
from utils import *
import pyfirmata

puerto = "\\.\COM9"  # Puerto COM de emulación en USB
LedRed = (13)  # PIN donde va conectado el LED Rojo
LedGreen = (12)  # PIN donde va conectado el LED Verde

# Conexión con placa Arduino
print("Conectando con Arduino por USB...")
tarjeta = pyfirmata.Arduino(puerto)
print("Conectado a Arduino por USB...")

def recognize(img,
              detector,
              encoder,
              encoding_dict,
              recognition_t=0.5,
              confidence_t=0.99,
              required_size=(160, 160), ):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = detector.detect_faces(img_rgb)
    for res in results:
        if res['confidence'] < confidence_t:
            continue
        face, pt_1, pt_2 = get_face(img_rgb, res['box'])
        encode = get_encode(encoder, face, required_size)
        encode = l2_normalizer.transform(encode.reshape(1, -1))[0]
        name = 'unknown'

        distance = float("inf")
        for db_name, db_encode in encoding_dict.items():
            dist = cosine(db_encode, encode)
            if dist < recognition_t and dist < distance:
                name = db_name
                distance = dist

        if name == 'unknown':
            cv2.rectangle(img, pt_1, pt_2, (0, 0, 255), 2)
            cv2.putText(img, name, pt_1, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)

            print("Encendiendo LED Rojo...")
            tarjeta.digital[LedRed].write(1)
            print("Encendido LED Rojo...")
            tarjeta.pass_time(3)
            print("Apagando LED Rojo...")
            tarjeta.digital[LedRed].write(0)
            print("Apagado LED Rojo...")
            tarjeta.pass_time(3)

        else:
            cv2.rectangle(img, pt_1, pt_2, (0, 255, 0), 2)
            cv2.putText(img, name + f'__{distance:.2f}', (pt_1[0], pt_1[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (0, 200, 200), 2)

            print("Encendiendo LED Verde...")
            tarjeta.digital[LedGreen].write(1)
            print("Encendido LED Verde...")
            tarjeta.pass_time(3)
            print("Apagando LED Verde...")
            tarjeta.digital[LedGreen].write(0)
            print("Apagado LED Verde...")
            tarjeta.pass_time(3)

    return img


if __name__ == '__main__':
    encoder_model = 'data/model/facenet_keras.h5'
    encodings_path = 'data/encodings/encodings.pkl'

    face_detector = mtcnn.MTCNN()
    face_encoder = load_model(encoder_model)
    encoding_dict = load_pickle(encodings_path)

    vc = cv2.VideoCapture(0)
    while vc.isOpened():
        ret, frame = vc.read()
        if not ret:
            print("no frame:(")
            break
        frame = recognize(frame, face_detector, face_encoder, encoding_dict)
        cv2.imshow('camera', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
