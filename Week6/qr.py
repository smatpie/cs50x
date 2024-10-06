import qrcode

img = qrcode.make("https://www.youtube.com/watch?v=EHi0RDZ31VA")
img.save("qr.png", "PNG")
