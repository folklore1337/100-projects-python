import random
import string

def get_string(letters_count, digits_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    # convert list to string
    final_string = ''.join(sample_list)
    print('Random string with', letters_count, 'letters', 'and', digits_count, 'digits', 'is:', final_string)

get_string(5, 4)