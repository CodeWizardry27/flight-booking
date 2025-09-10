import qrcode
# taking upi id
upi_id='satyamjha88anand-1@okicici'
amount=10
Payment_url=f'upi://pay?pa={upi_id}&pn=ReceiverName&am={amount}'

#create qr code for each code
Payment_qr=qrcode.make(Payment_url)

#save the qr code 
Payment_qr.save('Payment_qr.png')


#showing qrsatyamjha88anand-1@okicici
Payment_qr.show()

    
