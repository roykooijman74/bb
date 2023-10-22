import pyautogui
import time
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
import signal
import pyttsx3

def enablectrlc():
    # KeyboardInterrupt: Ctrl-C
    # dependent on import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def zoekplaatje(plaatje,offset=0,confidencevalue=0.7):
    xpositie,ypositie=pyautogui.position()
    try:
        imagex,imagey = pyautogui.locateCenterOnScreen(plaatje, confidence=confidencevalue)
    except:
        status=False
        imagex=0
        imagey=0
    else:
        status=True
        x=imagex-2560
        y=imagey+offset
        pyautogui.moveTo(x,y)
        #print(pyautogui.locateCenterOnScreen(plaatje, confidence=confidencevalue))
        #time.sleep(0.2)
        pyautogui.click(button='left')
        #print(pyautogui.locateCenterOnScreen(plaatje, confidence=confidencevalue))
        time.sleep(0.5)
        #pyautogui.moveTo(xpositie,ypositie)
    finally:
        return status,imagex,imagey


def main():
    enablectrlc()

    totaal_teller=0
    invasie_teller=0
    groen_vernietigen_teller = 0
    bruin_vernietigen_teller = 0        
    false_counter = 0
    while True:

        print("====Invasie")
        invasie_status=zoekplaatje("images/npc-invasie.png",70)
        while invasie_status[0] == True:
                    invasie_teller = invasie_teller + 1
                    groen_vernietigen_teller = groen_vernietigen_teller + 1
                    bruin_vernietigen_teller = bruin_vernietigen_teller + 1
                    totaal_teller=totaal_teller+1
                    print(invasie_status, totaal_teller, invasie_teller, groen_vernietigen_teller, bruin_vernietigen_teller)
                    invasie_status=zoekplaatje("images/npc-invasie.png",70)
#        time.sleep(0.2)            
        print("====Bruin")
        while bruin_vernietigen_teller >0:
               bruin_status=zoekplaatje("images/npc-vernietigen-bruin.png")
               bruin_vernietigen_teller = bruin_vernietigen_teller - 1
               print(bruin_status ,totaal_teller, invasie_teller, groen_vernietigen_teller, bruin_vernietigen_teller)    
#        time.sleep(0.4)            
        print("====Groen")
        while groen_vernietigen_teller >0:
               groen_status=zoekplaatje("images/npc-vernietigen-groen.png")
               groen_vernietigen_teller = groen_vernietigen_teller -1
               print(groen_status ,totaal_teller, invasie_teller, groen_vernietigen_teller, bruin_vernietigen_teller)    
        invasie_teller = 0       
        engine = pyttsx3.init()
        engine.say("Next")
        engine.runAndWait()
        print("-----------------------------------next")
'''
        werkt niet want beloning wordt grijs... nog oplossing zoeken
        print("Beloning")
        beloning_status=zoekplaatje("images/npc-beloning.png",0)
        while beloning_status[0] == True:
                    print("beloning gevonden")
                    beloning_status=zoekplaatje("images/npc-beloning.png",0)
'''
        
if __name__ == '__main__':
    main()
