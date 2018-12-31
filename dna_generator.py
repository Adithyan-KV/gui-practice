import random
import time
import pyperclip
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
import os

class AppWindow(BoxLayout):

    output_sequence= StringProperty()

    def generate_sequence(self,length):
        """generates a DNA sequence using length parameter"""

        #possible base pairs in DNA
        bp=['A','T','G','C']
        sequence=""

        #to keep track of the time required to generate each sequence
        t_start=time.time()

        #generating the random sequence
        for i in range(length):
            index=random.randint(0,3)
            sequence+=bp[index]

        t_end=time.time()

        time_taken=t_end-t_start
        print(sequence+"\n")
        print("Time elapsed: "+ str(time_taken)+'\n')

        return sequence

    def btn_clk_generate(self,length):

        #catching exceptions for non-integer,negative integer and no input seperately
        try:
            if length=="":
                raise TypeError
            try:
                int(length)
                try:
                    if int(length)<=0:
                        raise TypeError
                except:
                    self.output_sequence="Please enter a positive integer value"
                    return self.output_sequence
            except:
                self.output_sequence="Please enter an integer value"
                return self.output_sequence
        except:
            self.output_sequence="Please fill up the length of sequence field"
            return self.output_sequence

        self.output_sequence=self.generate_sequence(int(length))

    def btn_clk_copy(self,sequence):
         pyperclip.copy(sequence);

    def btn_clk_save(self,sequence):
        fin=open("./saved file/sequence.txt","w")
        fin.write(sequence)
        print("file saved")

class DnaApp(App):
    def build(self):
        return AppWindow()

#for CLI only
def input_prompt():
    """ to input the size of DNA sequence to be generated """

    n=input("how many base pairs would you like to generate?\n")
    try:
        return(int(n))
    except:
        print("Error: Non integer value")
        return(0)

#for CLI only
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
