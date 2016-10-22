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

  a = [5,2,3]; # mutable  - {bytearray, list, set, dict }  -  ( passed by reference )
  b = (5,2,3); # immutable - ( passed by value )
  s = "string"; # immutable
  change_list(a);  print(a)
  change_tuple(b); print(b)
  change_string(s);print(s)

def format():
  print (1)
  print ( "Prvek {0} by měl mít průměr {1:.3} cm.".format( 'cosi', 2/3 ) )
  print ( "Prvek {jmeno} by měl mít průměr {prumer:.3} cm.".format(
                                                    jmeno='cosi',
                                                    prumer=1/3 ,
                                                  ))

def tuple_test():
  t = ('ahoj', 234, ['a', 3, 5],);
  t = 'ahoj', 234, ['a', 3, 5],; # the same
  print( dir(t) )
  ##a, b = b, a # swap(a,b)

  a, *b, c = 'první', 1, 2, 'ahoj', 'poslední'
  print(a)
  print(b)
  print(c)

def dict_test():
  d = { 'a': 1, 'b': [1,2,3], 'c': "ahoj", }
  d['a'] = "svet"
  d[123] = (1, 'tuple')
  del d['c']
  print(d)
  for i in d:
    print(i)

  for (key, val) in d.items():
    print( key, val, sep=': ' )


def sorting():
  xs = [ ('Láďa', 2), ('Jana', 2), ('Jana', 1), ('Karel', 3) ]
  print(sorted(xs)) #Python obecně bude třídit všechny objekty, které interně implementují „magickou“ metodu __lt__(), tedy menší než, pro porovnání svých prvků. Ve výchozím stavu to znamená všechny předdefinované typy.
  print( sorted( xs, key = lambda c: c[0] ) )
  print( sorted( xs, key = lambda c: c[1] ) )
  ## xs.sort()  -- change the list.

def generators():
  xs = range(1, 9)
  # list(xs) # to list
  print(  [2**n for n in xs] )
  print(  [n for n in xs if n % 2 == 0] )

def for_test():

  for i in range(10): ## for else -- similar while
    if i > 2 : break
    print(i)
  else:
    print ("print only if for runs till end")

  #####

  for i, word in enumerate(["welcome", "to", "python"]):
    print(i, word)

  x = (2,5,4,3,6);
  for i in reversed(x):
    print(i)

  print( list( range(5) ) )
  print( list( range(4,6) ) )
  print( list( range(1,7,2) ) )

def with_test():
  #with -> netreba zatvarat subor, nie je treba riesit vynimky
  with open('README.md', mode='r', encoding='utf-8') as soubor:
    for i, řádka in enumerate(soubor):
        print(i, řádka)

def print_test():
  s1, s2, s3 = 'ahoj', 'světe', 'jak se máš'
  print( s1, s2, s3, sep='; ', end='\n')

def input_test():
  answer = input('Zadej text: ')
  print('Zadal si', answer )


def super_sum( a, b ,c):
    return a+b+c

def operator_star():
    a = 1,2,3
    b = [1,2,3]
    print( super_sum(*a) )
    print( super_sum(*b) )


### class MojeTridaEx( Exception ):   # dedeni
'''
# atributy, jejichž jméno začíná alespoň dvěma podtržítky a končí podtržítkem nejvýše jedním se budou jako privátní tvářit
__call__()
uvedené třídy (jejich instance) se budou chovat jako funkce (půjde je zavolat)
__enter__()
__exit__()
uvedené třídy bude možné použít uvnitř bloku with
__len__()
__contains__(x)
uvedené třídy se budou chovat jako množiny (tedy bude možné na ně aplikovat množinové operace)
__iter__()
__next__()
__reversed__()
uvedené třídy se budou chovat jako iterátory
'''

class MyClass:

  pass



if __name__ == '__main__':

  strings()
  中文()
  print( qs([5,4,4,2,45,3,8]) );

  mutable_immutable()
  format()
  tuple_test()
  dict_test();
  sorting()
  generators()
  print( 'it is true' if 2 == 3 else 'it is false'  )  #ternar operator
  for_test()
  with_test()
  print_test()
  #input_test()

  print( dir( 'ahoj' ) )  ## GET all methods and magic methods

  operator_star()


