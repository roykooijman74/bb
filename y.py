import time

import pyautogui
#vars
from variables import * # yes import all the variables
from functions import enable_ctrl_c
from functions import WindowsChecker as WC

#from PIL import ImageGrab
#ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

def main():
    enable_ctrl_c()

    # #* close sync if enabled
    # print("="*40," ","check if sync button is active windows")
    # sync_check=True
    # while sync_check:
    #     pyautogui.moveTo(369, 18)
    #     sync_check=WC.check_item_on_screen(smurfwindows[0],sync_stop_button)
        

    #! prep
    #* check which smurfs are active
    print("="*40," ","check active windows")
    windows = WC.check_active_windows(smurfwindows)
    print("="*40," ","sync stop button")
    time.sleep(0.2)
    print(smurfwindows[0])


    #* close chat menu if open
    print("="*40," ","close chat menu")
    for window in windows: 
        check=WC.check_item_on_screen(window,close_chat_menu)
        if check: time.sleep(0.3)

    #* compas open
    print("="*40," ","click on compas to go to island view")
    for window in windows: 
        WC.check_item_on_screen(window,compas)
    time.sleep(0.5)

    #* close attack menu
    for window in windows: WC.check_item_on_screen(window=window,item=close_attack_menu_item)
    time.sleep(0.5)


    #! end prep
    
    #! loop it a couple of times
    loopcounter = 1
        
    while loopcounter <=3:
        print("#"*40," ","loopcounter: ",loopcounter)

        print("="*40," ","check dr t")
        for window in windows:
            state=True
            while state:
                state=WC.check_item_on_screen(window,dr_t_talking)
                time.sleep(0.2)
                print(window[3],state)

        #* open attack menu
        for window in windows: WC.check_item_on_screen(window,open_attack_menu_item)
        time.sleep(0.5)

        # TODO :" insert chest logic"
        for window in windows: WC.check_item_on_screen(window,collect_reward)

        for window in windows: WC.check_item_on_screen(window,village_taken)
        for window in windows: 
            invasion_state=False
            invasion_state=WC.check_item_on_screen(window,invasion,offset_y=70,delay=0.5)
            if invasion_state:
                brown_state=False
                time.sleep(0.2)
                while brown_state==False:
                    brown_state=WC.check_item_on_screen(window,destroy_brown)
                    time.sleep(0.2)
                    if brown_state:
                        green_state=False
                        while green_state==False:
                            green_state=WC.check_item_on_screen(window,destroy_green)
                            time.sleep(0.2)


        # TODO END :" inster chest logic"

        #* close attack menu
        for window in windows: WC.check_item_on_screen(window=window,item=close_attack_menu_item)
        time.sleep(0.5)

        #* check if chest claimen is possible
        for window in windows: 
            print("="*40," ",window[3],"claim check")

            claim_state=WC.check_item_on_screen(window=window,item=claimen_text)
            if claim_state:
                time.sleep(0.1)
                reward_state=False
                while reward_state==False:
                    reward_state=WC.check_item_on_screen(window=window,item=select_supply_chest_reward)
                    print("="*40," ",window[3],"reward check")

                greyed_out_state=False
                while greyed_out_state==False:
                    greyed_out_state=WC.check_item_on_screen(window,close_reward_textbox)
                    print("="*40," ",window[3],"close_reward_textbox check")

        loopcounter = loopcounter +1
        #! end op loop




    




if __name__ == '__main__':
    main()
