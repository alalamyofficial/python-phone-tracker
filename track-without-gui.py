import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone 

number="+201068864143"


ch_number = phonenumbers.parse(number,"CH")

print(geocoder.description_for_number(ch_number,"en"))

service_number = phonenumbers.parse(number,"RO")

print(carrier.name_for_number(service_number,"en"))


isvalid = phonenumbers.parse(number)

valid = phonenumbers.is_valid_number(isvalid) 

print("The Number is "+ str(valid))


phoneNumber = phonenumbers.parse(number) 
  
timeZone = timezone.time_zones_for_number(phoneNumber) 

print(timeZone)