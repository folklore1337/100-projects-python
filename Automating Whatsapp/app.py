import pywhatkit

phone_number = input("Enter phone number: ")
pywhatkit.sendwhatmsg(phone_number, 'Hello', 0, 57)

# group_id = input("Enter group id: ")
# pywhatkit.sendwhatmsg_to_group(group_id, "Test", 10, 25) 
