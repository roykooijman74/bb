                # #* invasion logic
                                
                # villagewindows=[]
                # for window in windows: 
                #     village_taken_status=WC.check_item_on_screen(window,village_taken)
                #     if village_taken_status: 
                #         villagewindows.append(window)
                #     for villagewindow in villagewindows:
                #         print("!!!!!!"*100,villagewindow[4])
                #     for villagewindow in villagewindows:
                #         WC.check_item_on_screen(window,destroy_brown)
                #     for villagewindow in villagewindows:
                #         WC.check_item_on_screen(window,destroy_green)
                # if len(window)<=2:
                #     time.sleep(0.2)
                # time.sleep(0.3)



        # TODO :" insert chest logic"


                


        # for window in windows: WC.check_item_on_screen(window,collect_reward)
        # for window in windows: WC.check_item_on_screen(window,village_taken)
        # for window in windows: 
        #     invasion_state=False
        #     invasion_state=WC.check_item_on_screen(window,invasion,offset_y=70,delay=0.5)
        #     if invasion_state:
        #         brown_state=False
        #         time.sleep(0.2)
        #         while brown_state==False:
        #             brown_state=WC.check_item_on_screen(window,destroy_brown)
        #             time.sleep(0.2)
        #             if brown_state:
        #                 green_state=False
        #                 while green_state==False:
        #                     green_state=WC.check_item_on_screen(window,destroy_green)
        #                     time.sleep(0.2)




        # valid_rois = [roi for roi in SMURFWINDOWS if pyautogui.locateOnScreen("images/npc-invasie2.png", confidence=0.7, region=(roi[0], roi[1], roi[2], roi[3]))]

        # if valid_rois:
        #     npc_counter, status, found_x, found_y = search_image("images/npc-invasie2.png", npc_counter, 70, rois=valid_rois, wait=0.1)

        #     if status > 0:
        #         for smurf_info in valid_rois:
        #             x1, y1, _, _, smurf_name = smurf_info
        #             print(smurf_name, "detected at", found_x, found_y)

        #     sleep_time = 1.5 if len(valid_rois) == 1 else 0.5
        #     time.sleep(sleep_time)

        #     for smurf_info in valid_rois:
        #         x1, y1 = smurf_info[:2]
        #         brown_coords = (x1 + 498, y1 + 206)
        #         green_coords = (x1 + 433, y1 + 310)

        #         for coords in [brown_coords, green_coords]:
        #             pyautogui.moveTo(*coords)
        #             pyautogui.click(button='left')
        #             time.sleep(sleep_time)
