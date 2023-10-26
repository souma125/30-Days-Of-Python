def random_user_id():
    return 'iosdfgl'

import string
import random
def user_id_gen_by_user(num_characters,num_ids):
    if num_characters <= 0 or num_ids <= 10:
        return 'Please enter valid characters and valid numbers'
    