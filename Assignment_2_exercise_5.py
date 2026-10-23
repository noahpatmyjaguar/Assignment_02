from psychopy import visual, event, core
import glob
import random
#All code in this document made by Sofie Skovlyst

#setup of the stimulus and window
images = glob.glob('stimuli/stimulus*.jpg')
print(images)

win = visual.Window(size=(1280, 720), fullscr=False,
                    color='black', checkTiming=False)

#Defining the opening text and explanation of the game
def msg(text):
    message=visual.TextStim(win, text=text, color='white', height=0.1)
    message.draw()
    win.flip()
    event.waitKeys()

msg('Welcome to the rabbit game! When you see a lion, press the arrow opposite to the side with the lion to make the rabbit run away. When you see a burrow press the arrow that makes the rabbit run towards it. Press any button to start')

win = visual.Window(size=(1280, 720), fullscr=False,
                    color='black', checkTiming=False)

#Defining the stimulus
def show_stim(image):
    img=visual.ImageStim(win, image=image, size=2.0)
    img.draw()
    win.flip()

#Creating a for loop to repeat the stimulus and show succes or faliure with a fixation cross between trials 
for image in images:
    show_stim(image)
    keys=event.waitKeys(keyList=['left', 'right', 'escape'])
    key=keys[0]
    
    if key == 'escape':
        win.close()
        core.quit()
    
    if image.endswith('_L.jpg'):
        correct_key = 'left'
    else:
        correct_key = 'right'

    if key == correct_key:
        feedback = visual.ImageStim(win, image='stimuli/success.jpg')
    else:
        feedback = visual.ImageStim(win, image='stimuli/failure.jpg')
    feedback.draw()
    win.flip()
    core.wait(2)
    fixation = visual.TextStim(win, text='+', height=0.1)
    fixation.draw()
    win.flip()
    core.wait(0.5)

#Last window with a goodbye message, that dissapears when you press any button
msg("Thank you for participating!")
event.waitKeys()
win.close()
core.quit()