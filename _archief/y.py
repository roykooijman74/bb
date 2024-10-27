import time
import pyautogui
#vars
from variables import * # yes import all the variables
from functions import enable_ctrl_c
from functions import WindowsChecker as WC

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
    scroll_counter = 0

    while scroll_counter <=0:

        #* check if dr t is on screen, if so get rid of him
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

        #* go to the attack menu page
        print("#"*40," ","scroll_counter: ",scroll_counter)
        for _ in range(scroll_counter):
            for window in windows:
                
                pyautogui.moveTo(window[0]+100,window[1]+448)
                pyautogui.mouseDown()
                pyautogui.moveTo(window[0]+100,window[1]+100, duration=1.0)
                pyautogui.mouseUp()
                pyautogui.mouseDown()
                pyautogui.moveTo(window[0]+100,window[1]+100, duration=0.2)
                pyautogui.mouseUp()

                #pyautogui.leftClick

        #* collect chests
        for y in range(80, 440, 30):
            for window in windows:
                pyautogui.leftClick(window[0]+2670-2560, window[1]+y)
                if len(window)<=2:
                    time.sleep(0.5)
                time.sleep(1.0)
                    
                #* collect chests
                for window in windows: WC.check_item_on_screen(window,collect_reward)



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

        scroll_counter = scroll_counter +1
        time.sleep(1.0)
        #! end op loop


if __name__ == '__main__':
    main()
