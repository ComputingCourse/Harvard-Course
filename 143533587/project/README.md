# TikTacToe
    #### Video Demo:  https://youtu.be/egF-yQm7vmI
    #### Description:
    My project contains 5 funstions:get_row, get_collum, winnnable, check_win and start which do as follows.
    get_row takes the mousey co-ordinate as a perameter and uses if statements to see what horozontal row the mouse is on (either 0,1,2 since their uses to index the GRID list)
    get_collum does the same as get row but uses the mouse x co-ordinate to finde out where the mouse is in relation to the grid collums.
    both previous functions are called when you click to see where to place your X or O depending on who's turn it is.
    The winnable function take the current Grid as a perameter and creates a second grid where it will go through each empty square and place and O and a X and use the check win function to see if that would result in a win then return where you would have to place the x or o to win.
    This function is used to determin where the ai should go, when theirs no possible win the ai will place randomly.
    check win goes through every way you could win and returns True if someone won.
    start desplays the start screen where you choise ai or 1v1 aand uses mousey and x to see what you chose.
    Thenthere is a while loop for the actual game where if you push a button it restarts using the start function. if you click it uses get_collum and get_row to see where you clicked and places a x or o there and updates the Grid array.
    then if your playing an ai it will play its turn automatically after 0.4 seconds as described above.
    After each turn it also check to see if theres been a win or a draw using check_win and shows the right message.
    ps it wouldn't work with the online CS50 website but as shown in teh video it does work.