
## This 2D python game on firefighter simulation for FOET term project.

### How to run

1. Install anaconda for your respective system
    https://docs.anaconda.com/anaconda/install/

2. Clone this repository

3. Create a conda environment with requirements as stated in requirements.txt

    #### $ conda create --name <env> --file requirements.txt
    This command line should do the job

4. Once, environment is created, run:
    
   #### $ python roomDesign.py
   (This would replace existing room.csv file)
    
   OR 
    
   #### $ python roomDesign.py --name <name of room>.csv
    
6. ### NOTE: Press 's' after you finish drawing the obstacles to save them, the window would close automatically.
  
5. Once the custom room is created, run
   
   #### $ python game_final.py
   (to run a game with custom room as room.csv)
   
   OR
   
   #### $ python game_final --customRoom <custom room name>.csv
   (This would use the specified customRoom)
    
   OR
   
   #### $ python game4.py --customRoom <custom_room_name>.csv
   (for full game)
  
By default, there are 5 rooms arranged in a circular manner (- 1st - 2nd - 3rd - 4th - 5th - 1st -). And only 5th room is customizable. To customize other rooms and keep number of rooms dynamic, pyQt additions are required.

