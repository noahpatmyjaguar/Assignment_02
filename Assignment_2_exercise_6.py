#ALL CODE WAS COMPLETED BY NOAH PATTON-JENSEN

#imports
from psychopy import visual, event, core
import glob
import random                                                                    #importing everything I need

# setup / setting variables 
images = glob.glob('stimuli/stimulus*.jpg')                                      #this defines images as any stimulus.jpg
random.shuffle(images)                                                           #it means the images will always be suffled 

win = visual.Window(size=(1280, 720), fullscr=False,                             #creating the window of which everything will be displayed on
                    color='black', checkTiming=False)

n_correct = 0                                                                    #create the score counter variable

reset_cross = visual.TextStim(win, text="+", height=0.1, color="red")            #creates the fixation cross for later

stopwatch = core.Clock()                                                         #create the stopwatch

lion_rts = []                                                                    #create the lists that will contain the rts of lion and burrow 
burrow_rts = []


# defining functions
def msg(text):
    message = visual.TextStim(win, height=0.06, color="white", text=text)        #defining msg(text) with text being a name placeholder. it is a visual text stim painted on the window with the first text meaning the argument and the second being the msg(text) e.g. whatever we put after msg
    message.draw()                                                               # paint it backstage
    win.flip()                                                                   # curtain up
    event.waitKeys()

def show_stim(image):
    stim = visual.ImageStim(win, image=image)                                    # defining show_stim(image) on the window, the argument image = the image later defined in images
    stim.draw()                                                                  # paint it backstage
    win.flip()                                                                   # curtain up

# intro message
msg("The fleeing rabbit experiment.\n\n"
    "If you see a lion press the opposite arrow.\n\n"
    "If you see a burrow press the same direction arrow.\n\n"
    "Press any button to begin...")                                              #welcome text: it must teach the rule!

#here is the meat of the code, the loop that wraps the entire experiment 
for image in images:                                                             #images is just a name for the first item in the list defined by images and assigns it to the name image
    show_stim(image)                                                             #one call does prepare-draw-flip
    stopwatch.reset()

# collect the response (key / reaction time):
    keys = event.waitKeys(keyList=["left", "right", "escape"])                   #list of keys able to be pressed 
    key = keys[0]                                                                #when you press a key, it returns a list containing the keys that are pressed. key=the first key that is pressed
    rt = stopwatch.getTime()
    
    if key == "escape":
        win.close()
        core.quit()                                                              #adding an escape button

#analyse the response
    if "lion" in image:
        trial_type = "lion"                                                      #definine what the trial type was
    else:
        trial_type = "burrow"


    if image.endswith('_L.jpg'):                                                 #which response is correct for each image
        correct_key = 'left'
    else:
        correct_key = 'right'

#how to respond to the input 
    if key == correct_key:                                                       #if the correct key is pressed, show the success, add one to the correct counter, add the reaction time to the corresponding trial type
        show_stim('stimuli/success.jpg')
        n_correct = n_correct + 1                                                #add one to the correct counter

        if trial_type == "lion":
            lion_rts.append(rt)                                                  #add the reaction time to the list
        else: 
            burrow_rts.append(rt)

    else:
        show_stim('stimuli/failure.jpg')                                         #anything else show fail, no adding correct number, no adding reaction time
    
    print(f"Reaction time: {rt:.2f}, Pressed key: {key}, Correct Key: {correct_key}") #prints the reaction times/pressed key/correct key in the output 
    core.wait(2)
    
#adding the fixation cross
    reset_cross.draw()
    win.flip()
    core.wait(0.5)

#then the loop repeats itself for each image in images

mean_rt = (sum(burrow_rts) + sum(lion_rts)) / (len(burrow_rts) + len(lion_rts))  #after the loop so the zero division error doesn't happen...
#THEN it creates the goodbye message
msg(f"The rabbit escaped {n_correct} of {len(images)} times.\n\n"                #calculates the goodbye message inputs
f"Average reaction time for lion = {sum(lion_rts)/len(lion_rts):.2f}s\n\n"
f"Average reaction time for burrow = {sum(burrow_rts)/len(burrow_rts):.2f}s\n\n" 
f"Overall average reaction time = {mean_rt:.2f}\n\n"
f"Thank you for participating! Press any button to exit. \n\n")                  #msg defined as any button pressed to wait until a key is pressed

#exit cleanly
win.close()
core.quit()
