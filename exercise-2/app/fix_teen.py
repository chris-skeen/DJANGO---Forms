def fix_teen(n):
  if n < 9:
    return n
  
  elif n >= 10 and n < 15:
    n = 0 
    return n
  
  elif n == 15 or n == 16:
    return n
  
  elif n>= 17 and n <= 19:
    n = 0
    return n
  
  else:
    return n