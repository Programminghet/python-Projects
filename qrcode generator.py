#QR code generatation code.

import qrcode 

#taking UPI ID as a payment input
upi_id = input("Enter your UPI ID : ")

#upi : //pay?pa=UPI-ID&pn=NAME&an=Amount&cu=CURRENCY&tn=MESSAGE

#defining the payment URL based on the UPI id and payment app
#Modefiable according to your applocation's payment application support 

phonepay_url = f'upi://pay={upi_id}&pn=Recipient&cu=Rupees'
paytm_url = f'upi://pay={upi_id}&pn=Recipient&cu=Rupees'
googlepay_url = f'upi://pay={upi_id}&pn=Recipient&cu=Rupees'

#make qr code for each payment application 

phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)


#dispaly qr code (install PIL/pillow ,Library)
phonepay_qr.show()
paytm_qr.show()
googlepay_qr.show()