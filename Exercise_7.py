#The following is build on exercise 6, meaning that most of it is the work of Noah Patton-Jensen (NP), and then there's add ons made by Amalie Jacobsen (AJ)

#importing scripts - NP and AJ - AJ added the gui, data, os and pandas
from psychopy import visual, event, core, gui, data
import glob
import random
import os
import pandas as pd     


#participant script - part 1 AJ

box = gui.Dlg(title='The Fleeing Rabbit')                                    #Gives the participant a name to the game
box.addField('Native language')                                              #Gives us the Native language of the participant - important for reaction time
box.addField('Handedness', choices=['Right-handed', 'Left-handed'])          #Gives us an idea of whether they're left handed or right handed - could matter in terms of where on the keyboard they have to press
box.show()

#this next part allows the participant to exit the experiment / to change their mind before starting NP
if box.OK:
    language = box.data['Native language']
    handedness = box.data['Handedness']
else:
    core.quit()

participant_id = f'P{random.randint(10000, 99999)}'                          #This gives the participant a random participant ID (number) so they're annonymous


# setup - first part is new, and the rest is like in exercise 6

#AJ - part 2
os.makedirs('logfiles', exist_ok=True)                                       #This ensures that the logfiles folder is created, exists and then you eon't lose the data due to a missing folder
date = data.getDateStr()                                                     #This gets the date and time as a string, so every file can get a new name
logfile_name = f'logfiles/logfile_{participant_id}_{date}.csv'               #This names the file 'logfiles/logfile_..._....csv' where the first ... is the randomized ID for the participant and the second ... is the date and time from the line above

rows = []

#NP
images = glob.glob('stimuli/stimulus*.jpg')                                      #this defines images as any stimulus.jpg
random.shuffle(images)                                                           #it means the images will always be suffled 

win = visual.Window(size=(1280, 720), fullscr=False,                              #creating the window of which everything will be displayed on
                    color='black', checkTiming=False)

n_correct = 0                                                                    #create the score counter variable

reset_cross = visual.TextStim(win, text="+", height=0.1, color="red")            #creates the fixation cross for later

stopwatch = core.Clock()                                                         #create the stopwatch

lion_rts = []                                                                    #create the lists that will contain the rts of lion and burrow 
burrow_rts = []

# defining functions NP
def msg(text):
    message = visual.TextStim(win, height=0.06, color="white", text=text)        #defining msg(text) with text being a name placeholder. it is a visual text stim painted on the window with the first text meaning the argument and the second being the msg(text) e.g. whatever we put after msg
    message.draw()                                                               # paint it backstage
    win.flip()                                                                   # curtain up
    event.waitKeys()

def show_stim(image):
    stim = visual.ImageStim(win, image=image)                                    # defining show_stim(image) on the window, the argument image = the image later defined in images
    stim.draw()                                                                  # paint it backstage
    win.flip()                                                                   # curtain up

# intro message NP
msg("The fleeing rabbit experiment.\n\n"
    "If you see a lion press the opposite arrow.\n\n"
    "If you see a burrow press the same direction arrow.\n\n"
    "Press any button to begin...")                                              #welcome text: it must teach the rule!

#here is the meat of the code, the loop that wraps the entire experiment NP
for image in images:                                                             #images is just a name for the first item in the list defined by images and assigns it to the name image
    show_stim(image)                                                             #one call does prepare-draw-flip
    stopwatch.reset()

# collect the response (key / reaction time): NP
    keys = event.waitKeys(keyList=["left", "right", "escape"])                   #list of keys able to be pressed 
    key = keys[0]                                                                #when you press a key, it returns a list containing the keys that are pressed. key=the first key that is pressed
    rt = stopwatch.getTime()
    
    if key == "escape":
        win.close()
        core.quit()                                                              #adding an escape button

#analyse the response NP
    if "lion" in image:
        trial_type = "lion"                                                      #definine what the trial type was
    else:
        trial_type = "burrow"


    if image.endswith('_L.jpg'):                                                 #which response is correct for each image
        correct_key = 'left'
    else:
        correct_key = 'right'

#how to respond to the input - Mainly NP but AJ changed it from print to append (marked above the line)
    if key == correct_key:                                                       #what did happen vs what should.
        show_stim('stimuli/success.jpg')
        n_correct = n_correct + 1                                                #add one to the correct counter

        if trial_type == "lion":
            lion_rts.append(rt)                                                  #add the reaction time to the list
        else: 
            burrow_rts.append(rt)

    else:
        show_stim('stimuli/failure.jpg')
    
    #instead of saving all the data in different lists, we will want them all in one dictionary, so we change the print to append - part 3 of exercise 7 - AJ
    rows.append({'id': ____, 'language': language, 'handedness': handedness, 'stimulus': ____, 'key': key, 'correct_key': correct_key, 'rt': ____})
    
#adding the fixation cross NP
    reset_cross.draw()
    win.flip()
    core.wait(0.5)

#then the loop repeats itself for each image in images

#AJ - part 4, adding the save
logfile = pd.DataFrame(rows)                           #This makes so the data is kept in a table using pandas, so the keys becomes the columns (reaction time, trial number...) and the different participants get each their own row
logfile.to_csv(logfile_name, index=False)              #the 'index=false' keeps the numbers that belongs to pandas and not our data out of the data set when saved

#THEN it creates the goodbye message NP
msg(f"The rabbit escaped {n_correct} of {len(images)} times.\n\n"                #calculates the goodbye message inputs
f"Average reaction time for lion = {sum(lion_rts)/len(lion_rts):.2f}s\n\n"
f"Average reaction time for burrow = {sum(burrow_rts)/len(burrow_rts):.2f}s\n\n" 
f"Thank you for participating! \n\n")                                            #msg defined as any button pressed to wait until a key is pressed

#exit cleanly NP
win.close()
core.quit()
