from selenium import webdriver



driver = webdriver.Chrome('enter chrome driver path')


driver.get('https://web.whatsapp.com/')


name = raw_input('enter name of user or group: ')


msg = raw_input('enter your message')


count = int(input('enter the count'))



raw_input('enter anything after scanning qr code')


user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))


user.click()


msg_box = driver.find_element_by_class_name('input-container')

for i in range(count):

	msg_box.send_keys(msg)
	 
        
	button =  driver.find_element_by_class_name('compose-btn-send')

     
	button.click()
