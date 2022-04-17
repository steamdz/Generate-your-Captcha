from captcha.image import ImageCaptcha

#Creat size of image captcha
image = ImageCaptcha(width=200 , height=90)

#Captcha Text
text = 'AYMEN DEV'

#Generate Captcha Text Given
data = image.generate(text)

#Result
image.write(text,"Aymen.PNG")
