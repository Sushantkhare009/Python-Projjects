import qrcode as qr

img = qr.make("https://maps.app.goo.gl/6abqZM9BfgTwJQDN6")
img.save("qr_code.png")