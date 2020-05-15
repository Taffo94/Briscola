import random, turtle, dealer, graphics
background = turtle.Screen()
background.bgcolor("grey")
background.addshape("retro2.gif")

penny = turtle.Turtle()
penny.hideturtle()
penny.speed(0)
penny.penup()
penny.pensize(5)


setup_play_area(penny)

print("Would you like to turn on betting?")
betting_on = input("Type Yes if so:")
print("")
if betting_on == 'Yes':
    betting = True
    player_wallet = 100
else:
    betting = False

# game setup
keep_playing = True
while keep_playing:
    # this block here copies a new deck into the playing_deck variable, and resets the other playing variables
    playing_deck = [("Ace of Hearts", 11, "ace-of-hearts.png"), ("2 of Hearts", 2, "two-of-hearts.png"), \
                    ("3 of Hearts", 3, "three-of-hearts.png"), ("4 of Hearts", 4, "four-of-hearts.png"), \
                    ("5 of Hearts", 5, "five-of-hearts.png"), ("6 of Hearts", 6, "six-of-hearts.png"), \
                    ("7 of Hearts", 7, "seven-of-hearts.png"), ("8 of Hearts", 8, "eight-of-hearts.png"), \
                    ("9 of Hearts", 9, "nine-of-hearts.png"), ("10 of Hearts", 10, "ten-of-hearts.png"), \
                    ("Jack of Hearts", 10, "jack-of-hearts.png"), ("Queen of Hearts", 10, "queen-of-hearts.png"), \
                    ("King of Hearts", 10, "king-of-hearts.png"), ("Ace of Spades", 11, "ace-of-spades.png"), \
                    ("2 of Spades", 2, "two-of-spades.png"), ("3 of Spades", 3, "three-of-spades.png"), \
                    ("4 of Spades", 4, "four-of-spades.png"), ("5 of Spades", 5, "five-of-spades.png"), \
                    ("6 of Spades", 6, "six-of-spades.png"), ("7 of Spades", 7, "seven-of-spades.png"), \
                    ("8 of Spades", 8, "eight-of-spades.png"), ("9 of Spades", 9, "nine-of-spades.png"), \
                    ("10 of Spades", 10, "ten-of-spades.png"), ("Jack of Spades", 10, "jack-of-spades.png"), \
                    ("Queen of Spades", 10, "queen-of-spades.png"), ("King of Spades", 10, "king-of-spades.png"), \
                    ("Ace of Diamonds", 11, "ace-of-diamonds.png"), ("2 of Diamonds", 2, "two-of-diamonds.png"), \
                    ("3 of Diamonds", 3, "three-of-diamonds.png"), ("4 of Diamonds", 4, "four-of-diamonds.png"), \
                    ("5 of Diamonds", 5, "five-of-diamonds.png"), ("6 of Diamonds", 6, "six-of-diamonds.png"), \
                    ("7 of Diamonds", 7, "seven-of-diamonds.png"), ("8 of Diamonds", 8, "eight-of-diamonds.png"), \
                    ("9 of Diamonds", 9, "nine-of-diamonds.png"), ("10 of Diamonds", 10, "ten-of-diamonds.png"), \
                    ("Jack of Diamonds", 10, "jack-of-diamonds.png"),
                    ("Queen of Diamonds", 10, "queen-of-diamonds.png"), \
                    ("King of Diamonds", 10, "king-of-diamonds.png"), ("Ace of Clubs", 11, "ace-of-clubs.png"), \
                    ("2 of Clubs", 2, "two-of-clubs.png"), ("3 of Clubs", 3, "three-of-clubs.png"), \
                    ("4 of Clubs", 4, "four-of-clubs.png"), ("5 of Clubs", 5, "five-of-clubs.png"), \
                    ("6 of Clubs", 6, "six-of-clubs.png"), ("7 of Clubs", 7, "seven-of-clubs.png"), \
                    ("8 of Clubs", 8, "eight-of-clubs.png"), ("9 of Clubs", 9, "nine-of-clubs.png"), \
                    ("10 of Clubs", 10, "ten-of-clubs.png"), ("Jack of Clubs", 10, "jack-of-clubs.png"), \
                    ("Queen of Clubs", 10, "queen-of-clubs.png"), ("King of Clubs", 10, "king-of-clubs.png")]
    player_hand = []
    player_score = 0
    dealer_hand = []
    dealer_score = 0
    reset_turtles()

    # this block draws the player's starting hand, and tells them what they have
    player_hand.append(draw_card(playing_deck))
    create_card_image(player_hand, "player")
    player_hand.append(draw_card(playing_deck))
    create_card_image(player_hand, "player")
    player_score = compute_score(player_hand)
    print("Starting hand: " + cards_in_hand(player_hand))
    print("Starting score: " + str(player_score))
    if betting == True:
        print("Player Credits: " + str(player_wallet))
    print("")

    player_bet = 0
    if betting == True:
        while player_bet == 0:
            try:
                player_bet = int(input("How many credits would you like to wager?"))
                if player_bet > player_wallet:
                    print("You don't have that many credits to wager, try again!")
                    player_bet = 0
            except:
                print("That's not a number, try again!")
                player_bet = 0
    print("")
    # this is the start of the proper game loop
    in_game = True
    player_wins = None
    while in_game:
        print("Would you like to draw a card?")
        keep_going = input("Type 'hit' to draw, type 'stay' to end.")
        print('')
        if keep_going == "hit":
            player_hand.append(draw_card(playing_deck))
            create_card_image(player_hand, "player")
            player_score = compute_score(player_hand)
            if player_score > 21:
                print("Current hand: " + cards_in_hand(player_hand))
                print("Current score: " + str(player_score))
                print('')
                print("Oh no!  You went bust!")
                player_wins = False
                in_game = False
            elif len(player_hand) > 4:
                print("Wow!  You got a 'Five Card Charlie'!  You Win!")
                player_wins = True
                in_game = False
            else:
                print("Current hand: " + cards_in_hand(player_hand))
                print("Current score: " + str(player_score) + "\n")
        elif keep_going == "stay":
            print("Now the dealer will draw.")
            dealer_hand.append(draw_card(playing_deck))
            create_card_image(dealer_hand, "dealer")
            dealer_hand.append(draw_card(playing_deck))
            create_card_image(dealer_hand, "dealer")
            dealer_score = compute_score(dealer_hand)
            while dealer_score < 16:
                dealer_hand.append(draw_card(playing_deck))
                create_card_image(dealer_hand, "dealer")
                dealer_score = compute_score(dealer_hand)
            print("The dealer's hand is: " + cards_in_hand(dealer_hand))
            print("The dealer's score is: " + str(dealer_score))
            print('')
            if dealer_score > 21:
                print("The dealer went bust!  You win!")
                player_wins = True
                in_game = False
            elif len(dealer_hand) > 4:
                print("The dealder got a 'Five Card Charlie'.  You lose!")
                player_wins = False
                in_game = False
            elif dealer_score >= player_score:
                print("The dealer beat you!  You lose!")
                player_wins = False
                in_game = False
            else:
                print("You beat the dealer!  You win!")
                player_wins = True
                in_game = False
    if betting == True:
        if player_wins == True:
            player_wallet = player_wallet + player_bet
        elif player_wins == False:
            player_wallet = player_wallet - player_bet
        if player_wallet < 1:
            print("You've run out of credits!\nGame Over!")
            break
    check_continue = input("\nPress Enter if you would like to keep playing; type 'No' to stop.")
    if check_continue == "No":
        print("Thanks for playing!")
        keep_playing = False
    else:
        print('\n````` NEW GAME `````\n')
