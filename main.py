from story import *
from storyline import *
from classes import *
user = User()
user.name = "Simon"#input("Hello Adventurer! What is your name?")
main_story = Story()
main_dialogue = Dialogue()
#main_story.intro(user)
main_dialogue.shop()
main_story.forest(user)
main_dialogue.impDialogue()
main_story.reed(user)
main_dialogue.trollDialogue()
main_story.wolf_story(user)
main_dialogue.WolfDialogue()
main_story.lich_story(user)
main_dialogue.BoneDialogue()
main_story.wizard_story(user)
main_dialogue.LichDialogue()
main_story.worm_story(user)
main_dialogue.WizardDialogue()
main_story.medusa_story(user)
main_dialogue.wormDialogue()
main_story.kary_story(user)
main_dialogue.medusaDialogue()
main_story.kraken_story(user)
main_dialogue.karyDialogue()
main_story.tiamat_story(user)
main_dialogue.krakenDialogue()
main_story.tiamat_story(user)
main_dialogue.tiamatDialogue()
main_story.chaos_story(user)
main_dialogue.chaosDialogue()
main_story.end(user)