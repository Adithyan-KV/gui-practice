import random
import matplotlib.pyplot as plt
import time

def input_prompt():
    n=input("how many base pairs would you like to generate?\n")
    try:
        return(int(n))
    except:
        print("Error: Non integer value")
        return(0)
def generate_sequence(length):

    #possible base pairs in DNA
    bp=['A','T','G','C']
    sequence=""

    t_start=time.time()
    
    for i in range(length):
        index=random.randint(0,3)
        sequence+=bp[index]

    t_end=time.time()

    time_taken=t_end-t_start
    print(sequence+"\n")
    print("Time elapsed: "+ str(time_taken)+'\n')

def repeat_prompt():
    repeat=input("would you like to try again? (y/n)\n")
    if repeat.lower()=='y':
        main()
    elif repeat.lower()=='n':
        pass
    else:
        print("Please enter a valid response (y/n)\n")
    

def main():
    length=input_prompt()
    generate_sequence(length)
    repeat_prompt()

if __name__=="__main__":
    main()
