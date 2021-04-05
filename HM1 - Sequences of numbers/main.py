'''
Implement a menu-driven console application that provides the following functionalities:
   1. Read a list of complex numbers (in z = a + bi form) from the console.
   2. Display the entire list of numbers on the console.
   3. Display on the console the longest sequence that observes a given property. Each student will receive 2 of the
     properties from the list provided below.
   4. Exit the application.
The source code will include:
   - Specifications for the functions related to point 3 above.
   - 10 complex numbers already available at program startup.


Sequence Properties : 7. The difference between the modulus of consecutive numbers is a prime number.
                     10. Sum of its elements is 10+10i.
'''



def print_menu():
    print("Chose an option from the list above:")
    print("1 - Add a complex number.")
    print("2 - Show the list with all the complex numbers.")
    print("3 - Display the longest sequence of the consecutive complex numbers whose difference between modules is a prime number. ")
    print("4 - Display the longest sequence of the complex numbers whose sum is 10 + 10i.")
    print("5 - Exit the application\n")
    option = int(input("The number of the chosen option is:"))
    print("")

    return option


def read_number ():
    x = int(input("The real part of the number is:"))
    y = int(input("the fractional part of the number is:"))
    z = complex(x, y)
    print("The added complex number is:", z, "\n")

    return z


def calc_dif_mod_cn (x, y):
    """ Check if the difference between the modulus of consecutive numbers is a prime number """

    modx = math.sqrt(x.real ** 2 + x.imag ** 2)  # modulus of the first complex number
    mody = math.sqrt(y.real ** 2 + y.imag ** 2)  # modulus of the second complex number
    dif = modx-mody
    d = 0   # the number of the divisors of dif
    if dif == int(dif):  # first, we check if the dif is an integer
        for i in range(2, int(int(dif)/2 + 1)):  # then, we check if it's a prime number

            if dif % i == 0:
                d = d + 1  # if d = 0, then dif is a prime number

        if (d == 0 or dif==2):
            return dif
        else:
            return 0

    else:
         return 0


def sequence_7 (list):
    """"
    Display the longest sequence of the consecutive complex numbers whose difference between modules is a prime number.

    """

    max = 0
    now = 0
    k = 0
    for i in range(1, len(list)):
          if int(calc_dif_mod_cn(list[i], list[i-1])) != 0:    # the dif is a prime number
                now = now + 1
          else:
              if (now > max):
                  max = now
                  first = k
                  last = i-1
              now = 0
              k = i
    if (now > max):
        max = now
        first = k
        last = len(list)-1
    print ("The longest sequence is formed by the following numbers: ")
    for i in range(first, last+1):
        print(list[i])


def sum_10r10i (len):
    """"
     Display the longest sequence of the complex numbers whose sum is 10 + 10i.

    """
    sum = complex(0, 0)
    max = 0
    now = 0

    for a in len (0,len):
        sum = sum + list_clx_nr[a]

        for i in range (a,len):
            if ((sum.imag > 10) or (sum.real > 10)) :
                k = a
            else:
                now = now + 1


if __name__ == '__main__':
    import math
    import cmath
    x = 0

    list_clx_nr = [complex(4, 0), complex(0, 1), complex(8, 0), complex(2, 10), complex(3, 5), complex(3, 0),
                            complex(1, 2), complex(7, 13), complex(5, 1), complex(1, 1)]
    while True:
         x = int(print_menu())
         if x == 5:
             break

         elif x == 1:
              y = int(input ("How many nr you want to add?") )
              for i in range (1, y+1):
                 list_clx_nr.append(read_number())

         elif x == 2:
             print ("The list with all the complex numbers is: ", (list_clx_nr))
             print ("")

         elif x == 3:
             sequence_7(list_clx_nr)

         elif x == 4:
             sum_10r10i()