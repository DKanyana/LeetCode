##############

#Problem -
#Given a 32-bit signed integer, reverse digits of an integer.

#################

#Solution -

def reverseDigits(num):
  revnum = 0

  while num > 0:
      revnum = (revnum*10) + num%10
      num = num//10

  return revnum
