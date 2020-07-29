import string
import random
from .models import Room

def id_generator(size=4, chars=string.ascii_uppercase + string.digits):
  code = ''.join(random.choice(chars) for _ in range(size))
  while Room.objects.filter(code=code):
    # loops until a unique code is found
    code = ''.join(random.choice(chars) for _ in range(size))
  return code
