from tkinter import*
import random
from PIL import ImageTk, Image


global questions_answers
names_list = []
asked = []
score=0

questions_answers = {
 1: ["Who is the youngest player to score 10,000 points in the NBA?", 'Kobe Bryant','Michael Jordan','Steph Curry','LeBron James', '21',4],
 2: ["What is Usain Bolt's world record time?", '10.03','9.21','9.43','9.58', '9.58',4],
 3: ["The olympic are held every how many years?", '5 Years', '2 Years', '3 Years', '4 Years', '4 Years',4],
 4: ["How many points are a touchdown worth in the NFL?", '5 points', '7 points', '8 points', '6 points', '6 points',4],
 5: ["What team holds the longest winning streak in NBA history?", 'Chicago Bulls', 'Milwaukee Bucks', 'Dallas Mavericks', 'Los Angeles Lakers',  'Los Angeles Lakers',4],
 6: ["How many rings are there on an olympic flag?", '6', '7', '3', '5', '5',4],
 7: ["Who is the president of the UFC?", 'Joe Rogan', 'Jon Jones', 'Michael Bisping', 'Dana White', 'Dana White',4]

}

def randomiser():
  global qnum
  qnum = random.randint(1,7)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()


class QuizStarter:
  def __init__(self, parent):
    background_color="yellow"

    #frame set up
    self.quiz_frame = Frame(parent, bg = background_color, padx=10, pady=10)
    self.quiz_frame.grid()

    #Label widget for heading
    self.heading_label = Label (self.quiz_frame, text = "SPORTS", font=("Helvetica", "30",), bg=background_color)
    self.heading_label.grid(row=0, padx=5, pady=5)
    
  
    #Start button
    self.start_button = Button (self.quiz_frame, text = "START", bg="steelblue", command=self.start)
    self.start_button.grid(row=2, padx=5, pady=5) 
   
   #Exit button
    self.exit_button = Button (self.quiz_frame, text = "EXIT", bg="red", command=self.quiz_frame.destroy)
    self.exit_button.grid(row=4, padx=5, pady=5)

    #Picture resize
    self.picture_image = Image.open("Sports.jpeg")
    self.picture_image = self.picture_image.resize((500, 200), Image.ANTIALIAS)
    self.picture_image = ImageTk.PhotoImage(self.picture_image)
    self.image_label= Label(self.quiz_frame, image=self.picture_image)
    self.image_label.grid(row=1, pady=5, padx=5)
    
  
  def start(self):
    self.quiz_frame.destroy()  
    NameEnter(root)


class NameEnter:
  def __init__(self, parent):
    background_color="Yellow"

    #Quiz Frame
    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    self.user_label = Label (self.quiz_frame, text = "Please enter your username", font=("Helvetica", "20"), bg=background_color)
    self.user_label.grid(row=0, padx=5, pady=5)
  
    #Name Enter
    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=1, pady=5, padx=5)
 
   #Exit button
    self.continue_button = Button (self.quiz_frame, text = "CONTINUE", bg="steelblue", command=self.name_collection)
    self.continue_button.grid(row=4, pady=5, padx=5)





  def name_collection(self):
    name=self.entry_box.get()
    if name.strip () != "" and len (name) <= 15:
       names_list.append(name)
       self.quiz_frame.destroy()
       Quiz(root)
    elif len(name) >15:
      self.user_label.config(text="Please enter name of 1-15 charcters", fg="red")
    elif len(name) ==0 :
      self.user_label.config(text="Must enter at least 1 character", fg="red")

      
    
    

class Quiz:
  def __init__(self, parent):
    #color selections
    background_color="yellow"
    self.quiz_frame = Frame(parent, bg = background_color, padx=50, pady=50)
    self.quiz_frame.grid()

    #continue Button
    self.quiz_instance = Button(self.quiz_frame, text="CONFIRM", bg="steelblue", command=self.test_progress)
    self.quiz_instance.grid(row=8, pady=5) 

    #score label to show score
    self.score_label = Label(self.quiz_frame,font=("Tw Cen MT", "16"), bg=background_color)
    self.score_label.grid(row=9) 

    randomiser()

    #questions
    self.question_label = Label(self.quiz_frame, text=questions_answers[qnum][0], font=("Tw Cen MT","14"),bg=background_color)
    self.question_label.grid(row=0, padx=10, pady=10)

    #holds value of ratio buttons
    self.var1=IntVar()

#radio button 1
    self.rb1 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], font=("Helvetica","12"), bg=background_color, value=1, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light grey")
    self.rb1.grid(row=1, pady=5)

#radio button 2
    self.rb2 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], font=("Helvetica","12"), bg=background_color, value=2, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light grey")
    self.rb2.grid(row=2, pady=5)

#radio button 3
    self.rb3 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], font=("Helvetica","12"), bg=background_color, value=3, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light grey")
    self.rb3.grid(row=3, pady=5)

#radio button 4
    self.rb4 = Radiobutton(self.quiz_frame, text=questions_answers[qnum][4], font=("Helvetica","12"), bg=background_color, value=4, padx=10, pady=10, variable = self.var1, indicator = 1, background = "light grey")
    self.rb4.grid(row=4, pady=5)


  #Set questions setup
  def questions_setup(self):
    randomiser()
    self.var1.set(0)
    self.question_label.config(text=questions_answers[qnum][0])
    self.rb1.config(text=questions_answers[qnum][1])
    self.rb2.config(text=questions_answers[qnum][2])
    self.rb3.config(text=questions_answers[qnum][3])
    self.rb4.config(text=questions_answers[qnum][4])
 

  #confirm button command, could be enchanced  
  def test_progress(self):
      global score
      scr_label=self.score_label
      choice=self.var1.get()
      if len(asked)>6:
        if choice == questions_answers[qnum][6]:  
          score +=1
          scr_label.configure(text="Correct")
          self.quiz_instance.config(text="CONFIRM")
          self.endscreen()
        else:
            score+=0
            scr_label.configure(text="The correct answer was " + questions_answers[qnum][4]) 
            self.quiz_instance.config(text="CONFIRM")
            self.endscreen()
      else:
         if choice == 0:
             scr_label.configure(text="Please pick an answer before advancing")
             choice=self.var1.get()
         else:
           if choice == questions_answers[qnum][6]:#If user picks right answer
              score +=1
              scr_label.configure(text="Correct")
              self.quiz_instance.config(text="CONFIRM")
              self.questions_setup()
           else:
               score+=0
               scr_label.configure(text="The correct answer was " + questions_answers[qnum][4])
               self.quiz_instance.config(text="CONFIRM")
               self.questions_setup()

  def endscreen(self):
    root.withdraw()
    open_endscrn=End()
 


class End:
  def __init__ (self):
    background="Yellow"
    self.end_box = Toplevel(root)# top level widgets work as windows  that are directly managed by the window manager 
    self.end_box.title("End Box")

    self.end_frame = Frame (self.end_box, width=250, height=250, bg=background)
    self.end_frame.grid(row=0)

    self.end_heading = Label (self.end_frame, text="Well done, You have reached the end of the quiz", font=("Helvetica", 18), bg=background, pady=60, padx=50)
    self.end_heading.grid(row=0)

    self.exit_button = Button (self.end_frame, text="Exit", width=10, bg="red", font=("Helvetica", 12), command=self.close_end)
    self.exit_button.grid(row=4, pady=20)

  def close_end(self):
    self.end_box.destroy()
    root.withdraw()
       

#************Starting point program************#

if __name__ == "__main__":
  root = Tk()
  root.title("SPORTS")
  quizStarter_object = QuizStarter(root)
  root.mainloop()