import qrcode

# Cria o objeto QR code
link = "https://www.youtube.com/watch?v=e3SxwVcp3kY"

imagem = qrcode.make(link)

# Salva o QR code em um arquivo
imagem.save("qrCodeGerado.png")