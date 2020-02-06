is_old = True
has_licence = True

if is_old: 
  print('you are old enough to drive!')
elif has_licence: 
  print('you can drive now')
else: 
  print('You cant drive')

if is_old and has_licence: 
  print('you are old enough to drive!')
else: 
  print('You cant drive')

# Ternary Op

# starts at if, and works backwards if true
# condition_if_true if condition else condition_if_else

is_friend = True
can_message = "message allowed" if is_friend else "not friends"

print(can_message)

def sum1(num1, num2):
  '''
  Sum up the numbers
  '''
  return num1 + num2

print(sum1(5, 4))

sum1(1,2)


# *args **kwargs 

# def super_fun(args):
#   return sum(arg)

# super_fun(1,2,3,4) # Will fail because it expects one argument

def super_fun(*args):
  return sum(args)

print(super_fun(1,2,3,4)) # Will pass because accepts mulitple args

# **kwarg is to sent informaition in 

# Rule: paramas, *arg, default paras, **kwargs


# Global Scope keyword

total = 0 

def count():
  '''
  info
  '''
  global total
  total += 1
  return total

print(count())
print(count())
print(count())

