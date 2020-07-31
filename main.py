#IMPORTS
from termcolor import colored,cprint
import time
import statistics 
from statistics import mode
import random
#VARIABLES
twenty = (colored("~~~~~~~~~~~~~~~~~~~~","yellow"))
yes = ("yes", "YES", "Yes", "yEs", "yeS","YEs", "YeS", "YEs", "YeS", "YeS", "yES", "Y", "y")
no = ("no", "No", "NO", "nO", "N", "n")
VALUE = []
  


#FUNCTIONS
def randomnoworkmain(num_of_values,VALUE):
  print("RANDOMNOWORKMAIN")
  mensum = 0
  madsum = 0
  for i in VALUE:
    mensum = i + mensum
  print(twenty)
  print(twenty)
  VALUE.sort()
  print(colored("LIST SORTED FROM LEAST TO GREATEST:","blue"))
  print(twenty)
  print(VALUE)
  print(twenty)
  print(colored("The sum of these numbers: " + str(mensum), "blue"))
  print(twenty)
  time.sleep(3)
  median = statistics.median(VALUE)
  mode = most_common(VALUE)
  #rangea = VALUE[num_of_values] - VALUE[1]
  mean = mensum/num_of_values 
  print(calculating("CALCLATING MEAN..."))
  print(calculating("CALCLATING MODE..."))
  print(calculating("CALCLATING MEDIAN..."))
  print(calculating("CALCLATING RANGE...")) 
  print(calculating("CALCLATING MAD..."))
  if bool == False:
    print(the_is("N/A", "MODE"))
  elif bool == True:
    print(the_is(mode,"MODE"))
  else:
    pass  
  print(the_is(median,"MEDIAN"))
  print(the_is(mean,"MEAN"))
  #print(the_is(rangea,"RANGE"))
  for i in range(0, len(VALUE)):
    newval = abs(VALUE[i] - mean)
    madsum = newval + madsum
  MAD = madsum/num_of_values
  print(the_is(MAD,"MAD"))
  print('THIS IS STILL randomnoworkmain')
  


def randomworkmain(num_of_values,VALUE):

  print("RANDOMWORKMAIN")
  meansum = 0
  madsum = 0
  for number in VALUE:
    meansum = number+meansum
  print(twenty)
  print(twenty)
  VALUE.sort()
  print(colored("LIST SORTED FROM LEAST TO GREATEST:","blue"))
  print(twenty)
  print(VALUE)
  print(twenty)
  time.sleep(3)
  median = statistics.median(VALUE)
  mode = most_common(VALUE)
  mean = meansum/num_of_values
  #rangea = VALUE[num_of_values] - VALUE[1]
  print(calculating("CALCLATING MEAN..."))
  print(calculating("CALCLATING MODE..."))
  print(calculating("CALCLATING MEDIAN..."))
  print(calculating("CALCLATING RANGE...")) 
  print(calculating("CALCLATING MAD..."))
  if bool == False:
    print(the_is("N/A", "MODE"))
  elif bool == True:
    print(the_is(mode,"MODE"))
  else:
    pass  
  print(the_is(median,"MEDIAN"))
  print(the_is(mean,"MEAN"))
  print(colored("(Sum of " + str(VALUE) + " / " + str(len(VALUE)) + ")", "green"))
  print(twenty)
  #print(the_is(rangea,"RANGE"))
  for i in range(0, len(VALUE)):
    newval = abs(VALUE[i] - mean)
    madsum = newval + madsum
  MAD = madsum/num_of_values
  print(the_is(MAD,"MAD"))
  madsum2 = 0
  for i in range(0, len(VALUE)):
    newval2 = abs(VALUE[i] - mean)
    madsum2 = newval2 + madsum2
    print(colored("|" + str(VALUE[i]) + " - " + str(mean) + "| = " + str(newval2) + "(sum = " + str(madsum2) + ")", "green"))
  return(twenty)
  time.sleep(3)



def randomnums(LIST):
    global num_of_values
    print(twenty)
    num_of_values = int(input(colored("How many numbers do you want generated?",'red')))
    print(twenty)
    #THERE REALLY WASN'T A POINT TO ADD THE FOLLOWING LINE CUZ THE CONTINUE FUNCTION HANDLES THE REPETITION
    #times = int(input(colored("How many times do you want to generate random lists?", 'red')))
    #MAKES CODE SLOPPY AND INCONSISTENT CUZ 'times' IS NO LONGER THERE.
    #print(twenty)
    rangehigh = float(input(colored("What is the maxinimum number for the generated numbers?",'red')))
    print(twenty)
    rangelow = float(input(colored("What is the minimum number for the generated numbers?","red")))
    for i in range(0,num_of_values):
      number = random.randint(rangelow, rangehigh)
      LIST.append(number)
      if i % 15 == 0:
        print(colored("GENERATING NUMBERS...",'green'))
        print(twenty)
    else:
        pass
    print(twenty)
    #WHY DID I ADD THESE TWO LINES SO MUCH DEBUGGING PAIN FOR NO REASON!!(I DIDN'T PUT THE DIFFERENT RANDOM FUNCTIONS)
    """
    if times > 1:
      print(randomworkmain(num_of_values,VALUE))
    else:
    	print(randomworkmain(num_of_values,VALUE))
    """


def instructions():
  print(twenty)
  print(colored("MEASURES OF CENTER CALCULATOR. \nINSTRUCTIONS:\n1.Enter the number of values being entered.\n2.ENTER THE VALUES(in any order - press \"ENTER\" after entering each value).\n3.That's it.","red"))
  return(twenty)


def get_q1(LIST):
  number = float(len(LIST))
  if number % 2 == 0:
    lowernum = number/2
    uppernum = lowernum + 1
    q13 = LIST(lowernum)
    q12 = LIST(uppernum)
    q1 = float((q12 + q13)/2)
    q1 = int(q1)
    print(colored("OOP, THIS IS MEDIAN"))
    return(q1)
  if number % 2 != 0:
   print("sigh")

def the_is(WORD, ACTUALWORD):
  print(colored("The " + str(ACTUALWORD) + " IS:","red"))
  print((WORD))
  return(twenty)




def calculating(word):
  for i in range(0,3):
    print(colored(str(word),"green"))
    time.sleep(.1)
    return(twenty)


def most_common(List):
  global bool
  bool = True
  try:
    return(mode(List))
  except statistics.StatisticsError:
    bool = False
  except AttributeError:
    pass
  finally:
    bool = bool


def noworkmain(num_of_values,VALUE):
  mensum = 0
  madsum = 0
  for i in range(1, (num_of_values + 1)):
    valuem = float(input(colored("ENTER VALUE " + str(i),"red")))
    mensum = valuem + mensum
    VALUE.append(valuem)
  print(twenty)
  print(twenty)
  VALUE.sort()
  print(colored("LIST SORTED FROM LEAST TO GREATEST:","blue"))
  print(twenty)
  print(VALUE)
  print(twenty)
  print(colored("The sum of these numbers: " + str(mensum), "blue"))
  print(twenty)
  time.sleep(3)
  median = statistics.median(VALUE)
  mode = most_common(VALUE)
  #rangea = VALUE[num_of_values] - VALUE[1]
  mean = mensum/num_of_values 
  print(calculating("CALCLATING MEAN..."))
  print(calculating("CALCLATING MODE..."))
  print(calculating("CALCLATING MEDIAN..."))
  print(calculating("CALCLATING RANGE...")) 
  print(calculating("CALCLATING MAD..."))
  if bool == False:
    print(the_is("N/A", "MODE"))
  elif bool == True:
    print(the_is(mode,"MODE"))
  else:
    pass  
  print(the_is(median,"MEDIAN"))
  print(the_is(mean,"MEAN"))
  #print(the_is(rangea,"RANGE"))
  for i in range(0, len(VALUE)):
    newval = abs(VALUE[i] - mean)
    madsum = newval + madsum
  MAD = madsum/num_of_values
  return(the_is(MAD,"MAD"))


def workmain(num_of_values,VALUE):
  mensum = 0
  madsum = 0
  for i in range(1, (num_of_values + 1)):
    valuem = float(input(colored("ENTER VALUE " + str(i),"red")))
    mensum = valuem + mensum
    VALUE.append(valuem)
  print(twenty)
  print(twenty)
  VALUE.sort()
  print(colored("LIST SORTED FROM LEAST TO GREATEST:","blue"))
  print(twenty)
  print(VALUE)
  print(twenty)
  time.sleep(3)
  median = statistics.median(VALUE)
  mode = most_common(VALUE)
  #rangea = VALUE[num_of_values] - VALUE[1]
  mean = mensum/num_of_values 
  print(calculating("CALCLATING MEAN..."))
  print(calculating("CALCLATING MODE..."))
  print(calculating("CALCLATING MEDIAN..."))
  print(calculating("CALCLATING RANGE...")) 
  print(calculating("CALCLATING MAD..."))
  if bool == False:
    print(the_is("N/A", "MODE"))
  elif bool == True:
    print(the_is(mode,"MODE"))
  else:
    pass  
  print(the_is(median,"MEDIAN"))
  print(the_is(mean,"MEAN"))
  print(colored("(Sum of " + str(VALUE) + " / " + str(len(VALUE)) + ")", "green"))
  print(twenty)
  #print(the_is(rangea,"RANGE"))
  for i in range(0, len(VALUE)):
    newval = abs(VALUE[i] - mean)
    madsum = newval + madsum
  MAD = madsum/num_of_values
  print(the_is(MAD,"MAD"))
  madsum2 = 0
  for i in range(0, len(VALUE)):
    newval2 = abs(VALUE[i] - mean)
    madsum2 = newval2 + madsum2
    print(colored("|" + str(VALUE[i]) + " - " + str(mean) + "| = " + str(newval2) + "(sum = " + str(madsum2) + ")", "green"))
  return(twenty)
  time.sleep(3)



def CONTINUEmain(CONTINUE,function):
  global VALUE
  VALUE=[]
  while CONTINUE in yes:
    num_of_values = int(input(colored("HOW MANY VALUES ARE YOU ENTERING:\n","blue")))  
    VALUE = []
    return(function(num_of_values,VALUE))
    CONTINUE = str(input(colored("WOULD YOU LIKE TO CONTINUE?\n[Y/N]","red")))
  print(colored("Thanks For Using My Calculator.", 'red', 'on_blue'))

def CONTINUErandommain(CONTINUE,LIST,function0,function1):
  global VALUE
  VALUE=[]
  while CONTINUE in yes:
    #num_of_values = int(input(colored("HOW MANY VALUES DO YOU WANT GENERATED:\n","blue")))
    VALUE = []
    print(function0(LIST))
    return(function1(num_of_values,LIST))
    CONTINUE = str(input(colored("WOULD YOU LIKE TO CONTINUE?\n[Y/N]","red")))
  print(colored("Thanks For Using My Calculator.", 'red', 'on_blue'))





#RUNNING
print(twenty)
print(twenty)
print(colored("CAPS SENSITIVE! THANKS, MS. LAYNE","green"))
print(twenty)
print(twenty)
work = str(input(colored("WOULD YOU LIKE TO SHOW THE WORK(not recommended for large number of values)?\n[Y/N]: ","yellow")))
print(twenty)
randombool = str(input(colored("WOULD YOU LIKE TO GENERATE RANDOM NUMBERS INSTEAD OF ENTERING YOUR OWN?",'yellow')))

if work in no and randombool in no:
  print(instructions())
  num_of_values = int(input(colored("HOW MANY VALUES ARE YOU ENTERING:\n","blue")))
  print(noworkmain(num_of_values,VALUE))
  CONTINUE = str(input(colored("WOULD YOU LIKE TO CONTINUE?\n[Y/N]","red")))
  #what was i doing at next line
  #print(get_q1)
  print(CONTINUEmain(CONTINUE,noworkmain(num_of_values,VALUE)))
  while CONTINUE in yes:
    num_of_values = int(input(colored("HOW MANY VALUES ARE YOU ENTERING:\n","blue")))  
    VALUE = []
    print(noworkmain(num_of_values,VALUE))
    CONTINUE = str(input(colored("WOULD YOU LIKE TO CONTINUE?\n[Y/N]","red")))
  print(colored("Thanks For Using My Calculator.", 'red', 'on_blue'))
elif work in yes and randombool in no:
  print(instructions())
  num_of_values = int(input(colored("HOW MANY VALUES ARE YOU ENTERING:\n","blue")))
  print(workmain(num_of_values, VALUE))
  CONTINUE = str(input(colored("WOULD YOU LIKE TO CONTINUE?\n[Y/N]","red")))
  print(CONTINUEmain(CONTINUE,workmain(num_of_values,VALUE)))
  """
  while CONTINUE in yes:
    num_of_values = int(input(colored("HOW MANY VALUES ARE YOU ENTERING:\n","blue")))  
    VALUE = []
    print(workmain(num_of_values,VALUE))
    CONTINUE = str(input(colored("WOULD YOU LIKE TO CONTINUE?\n[Y/N]","red")))
  """
  print(colored("Thanks For Using My Calculator.", 'red', 'on_blue'))
elif work in no and randombool in yes:
  print(randomnums(VALUE))
  print(randomnoworkmain(num_of_values,VALUE))
  CONTINUE = str(input(colored("WOULD YOU LIKE TO CONTINUE?\n[Y/N]","red")))
  if CONTINUE in yes:
    print(CONTINUErandommain(CONTINUE,VALUE,randomnums(VALUE),randomnoworkmain(num_of_values,VALUE)))
  elif CONTINUE in no:
    print(twenty)
    print(twenty)
    print(colored("MADE BY NOAH"))
    print(twenty)
    print(twenty)
  else:
    print(colored("THIS IS A BUG",'green'))
elif work in yes and randombool in yes:
  print(randomnums(VALUE))
  print(randomworkmain(num_of_values,VALUE))
  CONTINUE = str(input(colored("WOULD YOU LIKE TO CONTINUE?\n[Y/N]","red")))
  if CONTINUE in yes:
    print(CONTINUErandommain(CONTINUE,VALUE,randomnums(VALUE),randomworkmain(num_of_values,VALUE)))
  elif CONTINUE in no:
    print(twenty)
    print(twenty)
    print(colored("MADE BY NOAH"))
    print(twenty)
    print(twenty)
  else:
    print(colored("THIS IS A BUG",'green'))





#print(MAD(num_of_values, mean,VALUE,sum))

"""
def workmain(num_of_values,VALUE):
  mensum = 0
  madsum = 0
  for i in range(1, (num_of_values + 1)):
    valuem = float(input(colored("ENTER VALUE " + str(i),"red")))
    mensum = valuem + mensum
    VALUE.append(valuem)
  print(twenty)
  print(twenty)
  VALUE.sort()
  median = statistics.median(VALUE)
  if num_of_values % 2 == 0:
    median 
    print("1")
  else:
    print("asdf")
  for i in range(0,5):
    print(colored("CALCLATING MEAN...","green"))
    time.sleep(.2)
    print(twenty)
  mean = mensum/num_of_values  
  print(colored("The Mean IS:\n\n","red"))
  print(mean)
  for i in range(0, len(VALUE)):
    newval = abs(VALUE[i] - mean)
    madsum = newval + madsum
  MAD = madsum/num_of_values
  for i in range(0,5):
    print(colored("CALCLATING MAD...","green"))
    time.sleep(.2)
    print(twenty)
  print(colored("The MAD IS:\n\n","red"))
  print(MAD)



def MAD(num_of_values,VALUE,sum):
  for i in range(1, (num_of_values + 1)):
    valuex = float(input(colored("ENTER VARIABLE " + str(i),"red")))
    valuex = abs(valuex - mean)
    print(sum)
    sum = valuex + sum
    print(sum)
    #VALUE.append(valuex)
  for i in range(0,5):
    print(colored("CALCLATING...","green"))
    time.sleep(.5)
    print(twenty)
  MAD = sum/num_of_values
  print(colored("The IQR IS:\n\n","red"))
  print(MAD)
"""



