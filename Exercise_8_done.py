#Noah Otto Patton-Jensen is responsible for participant ID, consent form, information pop up window and results collection. 
#Sophie Fogh and Maria Mihalka collaborated on the for loop and core code
#Amalie (AJ) is responsible for storage of data, CSV file, and results collection and has helped a little here and there

#imports
from psychopy import visual, event, core, gui, data
import glob
import random                                                                    #importing everything needed
import os
import pandas as pd 

participant_id = f"P{random.randint(10000,99999)}"

#1. display study information screen
study_welcome = gui.Dlg(title = "Reading Experiment", labelButtonOK = "OK")
study_welcome.addText(
"You are being invited to take part in a research study.\n"
"This experiment will measure how quickly you read.\n"
"You may ask at any point before or after if you require more information.\n"
"Noah Patton-Jensen, Email: au821002@uni.au.dk.\n"
"Press ok to continue.\n")
study_welcome.show()

study_consent = gui.Dlg(title = "Reading Experiment Informed Consent", labelButtonOK = "OK")
study_consent.addText(
"We are intrested in studying how participants process written language.\n"
"Including how long it takes to read surprise words compared to predictable words.\n"
"Participation is voluntary, estimated time around 10 minutes.\n"
"As participation is fully anonymous, it's not be possible to retract consent.\n"
"If you agree to give informed consent press 'OK' otherwise press 'Cancel'.\n")
study_consent.show()
if study_consent.OK:
    consent_status = "yes"
else:
    core.quit()

participant_info = gui.Dlg(title = "Participant information")
participant_info.addText("Please fill out the following information or withdraw consent via 'Cancel'")
participant_info.addField("Age")
participant_info.addField("Native language")
participant_info.show()
if participant_info.OK:
    language = participant_info.data["Native language"]
    age = participant_info.data["Age"]
else:
        core.quit()



story= """Lily’s alarm buzzed at 7:00 AM. She stretched, popped out of bed, and dashed to brush her teeth. Back in her room, she threw on her favorite yellow sweater and dark jeans, quickly pulling her hair into a neat ponytail.
She glanced at the clock and smiled, pleased that she was right on schedule. Outside her window, the birds were chirping, and the sunlight peeked through the curtains, promising a beautiful day.
Downstairs, the kitchen smelled of warm toast. Lily enjoyed a bowl of oatmeal with fresh berries while double-checking her morning routine. She packed her homework folder, water bottle, and pencil case into her backpack, zipped it tight, and slipped on her sneakers.
Before leaving, she checked that she had everything she needed for her classes. She was especially excited about her art lesson, where she hoped to finish the colorful painting she had been working on all week. After saying goodbye to her family, she picked up her lunchbox from the kitchen counter.
Checking her reflection in the hallway mirror, she grabbed her coat and stepped into the crisp morning air, completely ready to tackle the school day!"""

control_cond=story.split()

surprise_cond = control_cond.copy()

control_target = 'coat'

surprise_target = 'crocodile'

target_i = control_cond.index(control_target)

surprise_cond[target_i]=surprise_target

#AJ - the assigning of the participants
version=random.choice(['control', 'experimental'] )                 #the random.choice makes it so the participants are randomly assigned to the two groups
if version=='control':                                              #The following just tells the code whether to present the expected or the surprising word to the participant
    story_words=control_cond
else:
    story_words=surprise_cond

print(f'participant condition:{version}')

#No longer AJ
win = visual.Window(size=(1280, 720), fullscr=False,
                    color='black', checkTiming=False)

results = []

#Defining the opening text and explanation of the game
def msg(text):
    message=visual.TextStim(win, text=text, color='white', height=0.1)
    message.draw()
    win.flip()
    event.waitKeys()
    
msg("Welcome. A story will appear one word at a time. Press space to read the next word, press escape to close")


#Text
text = visual.TextStim(win, text='+', color='white', height=48, units='pix')

fixation = visual.TextStim(win, text='+', height=0.1)
fixation.draw()
win.flip()
core.wait(0.8)

# define a helper to display text in the window.
def show(message):
    text.text = message
    text.draw()
    win.flip()

stopwatch = core.Clock()

#The following chunk has been made by Sofie and Maria
for word_index in range(len(story_words)):      #AJ helped with this part
    event.clearEvents()
    text.text = story_words[word_index]
    text.draw()
    win.callOnFlip(stopwatch.reset)
    win.flip()
    keys = event.waitKeys(
        keyList=['space', 'escape'],
        timeStamped=stopwatch)
    key, reaction_time = keys[0]
    if key == 'escape':
        win.close()
        core.quit()
    results.append({"word": story_words[word_index], "rt": reaction_time, "id": participant_id, "language": language, "consent": consent_status})

    #print(results) could be added for testing, but to make it faster we won't, we have however added for the program to tell us which version the participant had
    

#AJ - the savings part
os.makedirs('Reading_test', exist_ok=True)                                     #This creates the folder 'Reading_test where we want out data stored in

Results_DF = pd.DataFrame(results)                                             #This makes it so out data is saved in a dataframe - using pandas

date = data.getDateStr()                                                       #This gives the date and time, which is used in the file name

Filename = f'Reading_test/results_{participant_id}_{date}.csv'                 #This is the filename of every document, ensuring annonymity
Results_DF.to_csv(Filename, index=False)                                        #This ensures that we don't bring along the numbering in the data fram from pandas to our data, since it doesn't belong with our data

#NP
msg("Thank you for participating!")
win.close()
core.quit()
