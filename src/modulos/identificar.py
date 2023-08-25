import math
import cvzone
from ultralytics import YOLO

class perDec:
    def __init__(self, yolo):
        self.model = YOLO(yolo)  # Modelo de detección 
        self.classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                           "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                           "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
                           "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
                           "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
                           "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
                           "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
                           "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
                           "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
                           "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"] # Clases
        self.confMeta = 0.4  # Nivel de confianza meta
        self.bC = 0  # Azul esquina
        self.gC = 0  # Verde esquina
        self.rC = 255  # Rojo esquina
        self.bR = 255  # Azul rectangulo
        self.gR = 0  # Verde rectangulo
        self.rR = 0  # Rojo rectangulo
        
    def set_model(self, model, classNames):  # Cambiar modelo y clase
        self.model = YOLO(model)  # Model = ruta del archivo
        self.classNames = classNames  # Lista de clases que se detectan

    def set_confMeta(self, confMeta):
        self.confMeta = confMeta

    def set_colorC(self, b, g, r):  # Cambiar color de esquina formato BGR
        self.bC = b
        self.gC = g
        self.rC = r

    def set_ColorR(self, b, g, r):  # Cambiar color de rectangulo formato BGR
        self.bR = b
        self.gR = g
        self.rR = r

    def get_cPerson(self, foto):  # Contar personas en la imagen
        model = self.model  # importar modelo
        classNames = self.classNames
        bC, gC, rC = self.bC, self.gC, self.rC
        bR, gR, rR = self.bR, self.gR, self.rR
        personC = 0 # Personas contadas
        img = foto

        # Procesar imagen y detectar coincidencias con las clases del modelo
        results1 = model(img, stream=True)
        for r1 in results1:
            boxes = r1.boxes
            for box in boxes:
                #  Área en la que hay una bounding box
                x1, y1, x2, y2 = box.xyxy[0]  # x, y ,w, h
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Pasa float a int
                w, h = x2 - x1, y2 - y1  # Obtener ancho y alto de la bounding box
                #  Nivel de confianza
                conf = math.ceil((box.conf[0] * 100)) / 100
                #  Nombre de la clase
                cls = int(box.cls[0])
                currentClass = classNames[cls]
                # Poner bounding box, etiqueta y nivel de confiaza a las deteccinones validas
                if currentClass == "person" and conf > self.confMeta:
                    cvzone.cornerRect(img, (x1, y1, w, h), colorC=(bC, gC, rC), colorR=(bR, gR, rR))
                    personC += 1
        
        return personC, img