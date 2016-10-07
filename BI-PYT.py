def qs(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        left  = [ x for x in a     if x <  pivot]
        right = [ x for x in a[1:] if x >= pivot]
        return qs(left) + [pivot] + qs(right)

# docstring: funkce pro test stringov : dostupne cez magic __doc__
def strings():

  s = "Ahoj, světe! Python 3"   # textový řetězec v kódování UTF-8
  bs =  b"bytes"         #byte stream
  print (s)
  print (bs)

def 中文():
  print("中文: 蟒科3 ")

def my_future_method():
  pass



def change_list( x ):
  x[0] = 1;

def change_tuple( x ):
  # x[0] = 1; impossible to change
  pass

def change_string( x ):
  # x[0] = 'c'; do not support (bytearray)
  x += "->add"
  print (x);


def mutable_immutable():

  a = [5,2,3]; # mutable  - {bytearray, list, set, dict }
  b = (5,2,3); # immutable
  s = "string"; # immutable
  change_list(a);  print(a)
  change_tuple(b); print(b)
  change_string(s);print(s)


if __name__ == '__main__':

  strings()
  中文()
  print( qs([5,4,4,2,45,3,8]) );

  mutable_immutable()
