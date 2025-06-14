class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("John", 30)
print(p.__dict__)

print(help(Person))


# help(str)
# Help on class str in module builtins:

class str(object)
   str(object='')
   str(bytes_or_buffer[, encoding[, errors]]) -> str
 
#   Create a new string object from the given object. If encoding or
#   errors is specified, then the object must expose a data buffer
#   that will be decoded using the given encoding and error handler.
#   Otherwise, returns the result of object.__str__() (if defined)
#   or repr(object).
#   encoding defaults to sys.getdefaultencoding().
#   errors defaults to 'strict'.