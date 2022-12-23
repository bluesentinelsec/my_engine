import my_game

def main():
    game = my_game.MyGame()

    game.easy_init(320, 200, True)
    
    # ToDo: set starting scene
    
    game.run_game()

    game.quit_game()

if __name__ == "__main__":
    main()