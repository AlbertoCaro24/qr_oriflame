import qrcode
import os

# Crear carpeta si no existe
os.makedirs("qr_generado_oriflame", exist_ok=True)

base_url = "https://albertocaro24.github.io/qr_oriflame/"

# Generar el código QR
img = qrcode.make(base_url)

# Guardar la imagen en la carpeta
img.save("qr_generado_oriflame/oriflame_qr.png")