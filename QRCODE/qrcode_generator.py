import qrcode

informacoes = 'EF501VA21\n202130273\nLUIS AUGUSTO SOUZA DE MACEDO'

qr = qrcode.QRCode(
        version=1,
        box_size=4,
        border=5)

qr.add_data(informacoes)
qr.make(fit=True)

# cria imagem: https://

img = qr.make_image(fill='black',back_color='white')
img.show()