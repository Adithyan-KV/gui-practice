import random
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class AppWindow(BoxLayout):

    def generate_sequence(self,length):
        """generates a DNA sequence using length parameter"""

        #possible base pairs in DNA
        bp=['A','T','G','C']
        sequence=""

        #to keep track of the time required to generate each sequence
        t_start=time.time()

        for i in range(length):
            index=random.randint(0,3)
            sequence+=bp[index]

        t_end=time.time()

        time_taken=t_end-t_start
        print(sequence+"\n")
        print("Time elapsed: "+ str(time_taken)+'\n')

        return sequence

    def btn_clk_generate(self):
        dna_seq= self.generate_sequence(100)
        print("Here:"+dna_seq)
        return(dna_seq)

class DnaApp(App):
    def build(self):
        return AppWindow()

def input_prompt():
    """ to input the size of DNA sequence to be generated """

    n=input("how many base pairs would you like to generate?\n")
    try:
        return(int(n))
    except:
        print("Error: Non integer value")
        return(0)



def repeat_prompt():
    """to check if the user wants to generate another sequence"""

    repeat=input("would you like to try again? (y/n)\n")
    if repeat.lower()=='y':
        main()
    elif repeat.lower()=='n':
        pass
    else:
        print("Please enter a valid response (y/n)\n")
        repeat_prompt()

def main():
    DnaApp().run()

#def main():
#    length=input_prompt()
#    generate_sequence(length)
#    repeat_prompt()

if __name__=="__main__":
    main()
