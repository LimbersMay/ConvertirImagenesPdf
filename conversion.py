import os
import img2pdf
from io import open
from PIL import Image

class PngToJpg:
    def __init__(self, ruta_origen: str, ruta_destino: str, extension: str = "jpg") -> None:
        self.ruta_origen = ruta_origen
        self.ruta_destino = ruta_destino

        self.extension = extension

    def realizar_conversion(self):
        listado_pngs = [archivo for archivo in os.listdir(self.ruta_origen) if archivo.endswith(".png")]
        convertir_jpg = [archivo[:-3] + self.extension for archivo in listado_pngs]

        # Recorremos todos los ficheros y convertimos uno a uno cada fichero
        for contador in range(len(listado_pngs)):
            img = Image.open(self.ruta_origen + listado_pngs[contador])

            if img.mode in ("RGBA", "P"): 
                img = img.convert("RGB")

            # Guardamos la imagen en jpg en la ruta de origen y eliminamos la original en png
            img.save(self.ruta_origen + convertir_jpg[contador])
            os.remove(self.ruta_origen + listado_pngs[contador])


class ImgToPdf:
    def __init__(self, ruta_origen: str, ruta_destino: str, nombre: str = "unido.pdf") -> None:
        self.ruta_origen = ruta_origen
        self.ruta_destino = ruta_destino

        self.nombre = nombre

        self.listado_origen: list[str]
        self.nombres_pdf: list[str]
    
    def obtener_informacion(self):
        self.listado_origen = os.listdir(self.ruta_origen)
        self.nombres_pdf = [archivo[:-3] + "pdf" if archivo.endswith(".jpg") else archivo[:-5] + ".pdf" for archivo in self.listado_origen]
    
    def convertir_separado(self):
        self.obtener_informacion()

        for contador in range(len(self.listado_origen)):
            with open(self.ruta_destino + self.nombres_pdf[contador], "wb") as fichero:
                fichero.write(img2pdf.convert(self.ruta_origen + self.listado_origen[contador]))

    def convertir_unido(self):
        self.obtener_informacion()

        # rutas_ordenadas = ordenar_lista(self.listado_origen)
        listado_rutas = [self.ruta_origen + archivo for archivo in self.listado_origen]
        
        with open(self.ruta_destino + self.nombre, "wb") as fichero:
            fichero.write(img2pdf.convert(listado_rutas))
