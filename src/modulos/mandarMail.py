import smtplib
from email.mime.text import MIMEText as MT
from email.mime.multipart import MIMEMultipart as MM
from email.mime.image import MIMEImage as MI
import time

class mail:
    def __init__ (self, to):
        self.to = to  # Destinatario
        self.From = 'ejemplo@email.com'  # Remitente
        self.password = 'contraseña1234'  # Contraseña
        self.minPer = 0  # minimo de personas permitidas
        self.puerto = 587  # Puerto SMTP
        self.direccion = 'smtp-mail.outlook.com'  # Dirección del servidor SMTP
        self.Ccamaras = 1  # Cantidad de camaras
        self.ruta = [] #Ruta de las imagenes

    def set_minPer(self, minPer):
        self.minPer = minPer

    def set_puertoDir(self, puerto, direccion):
        self.puerto = puerto
        self.direccion = direccion

    def set_from(self, From):
        self.From = From

    def set_ruta(self, ruta):
        self.ruta = ruta

    def set_Ccamaras(self, Ccamaras):
        self.Ccamaras = Ccamaras

    def mandarMail(self, cantidad):
        #  Cambiar asunto segun el numero de personas detectadas 
        if cantidad <= self.minPer:
            asunto = 'Faltan personas'
        else:
            asunto = 'Exceso de personas'

        # Guardar fecha y hora
        fecha = time.strftime('%d/%m/%Y')
        hora = time.strftime('%H:%M:%S')

        # Texto del email
        if cantidad == 1:
            linea = 'Se encontro 1 persona en la imagen'
        else:
            numero = str(cantidad)
            linea = 'Se encontratron ' + numero + ' personas en la imagen'

        # Contenido del email
        email_content = f"""
        <html Lang="es">
            <body>
                <p>{linea}</p>
                <p>Fecha de la captura: {fecha}</p>
                <p>Hora de la captura: {hora}</p>
            </body>
        </html>
        """

        # Adjuntar imagen
        if self.Ccamaras == 4:
            with open(self.ruta[0], 'rb') as file1:
                img1 = MI(file1.read())
                img1.add_header('Content-Disposition','attachment',filename=self.ruta[0])
            with open(self.ruta[1], 'rb') as file2:
                img2 = MI(file2.read())
                img2.add_header('Content-Disposition','attachment',filename=self.ruta[1])
            with open(self.ruta[2], 'rb') as file3:
                img3 = MI(file3.read())
                img3.add_header('Content-Disposition','attachment',filename=self.ruta[2])
            with open(self.ruta[3], 'rb') as file4:
                img4 = MI(file4.read())
                img4.add_header('Content-Disposition','attachment',filename=self.ruta[3])

        elif self.Ccamaras == 3:
            with open(self.ruta[0], 'rb') as file1:
                img1 = MI(file1.read())
                img1.add_header('Content-Disposition','attachment',filename=self.ruta[0])
            with open(self.ruta[1], 'rb') as file2:
                img2 = MI(file2.read())
                img2.add_header('Content-Disposition','attachment',filename=self.ruta[1])
            with open(self.ruta[2], 'rb') as file3:
                img3 = MI(file3.read())
                img3.add_header('Content-Disposition','attachment',filename=self.ruta[2])

        elif self.Ccamaras == 2:
            with open(self.ruta[0], 'rb') as file1:
                img1 = MI(file1.read())
                img1.add_header('Content-Disposition','attachment',filename=self.ruta[0])
            with open(self.ruta[1], 'rb') as file2:
                img2 = MI(file2.read())
                img2.add_header('Content-Disposition','attachment',filename=self.ruta[1])

        else:
            with open(self.ruta[0], 'rb') as file1:
                img1 = MI(file1.read())
                img1.add_header('Content-Disposition','attachment',filename=self.ruta[0])

        # Armado del email
        msg = MM("alternative")
        msg['Subject'] = asunto
        msg['From'] = self.From
        msg['To'] = self.to
        password = self.password
        parte_html = MT(email_content, "html")
        msg.attach(parte_html)
        if self.Ccamaras == 4:
            msg.attach(img1)
            msg.attach(img2)
            msg.attach(img3)
            msg.attach(img4)
        elif self.Ccamaras == 3:
            msg.attach(img1)
            msg.attach(img2)
            msg.attach(img3)
        elif self.Ccamaras == 2:
            msg.attach(img1)
            msg.attach(img2)
        else:
            msg.attach(img1)
        server = smtplib.SMTP(self.direccion, port=self.puerto)
        server.starttls()

        # Login
        server.login(msg['From'],password)
        # Mandar Mail
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        # Logout
        server.quit()
