# FinaL Project
#
# Python file name: CIT_95_Final.py
#
# Date: 10-30-2023
#
# Programmer's name: Matthew Gutierrez
import pygame


def main():
    # Program Intro
    print("\n** Welcome to Mac Mac's Program for creating a 3D environment. **\n")

    def start():
        start_game = input("Would you like to see play the game. Y/N: ", ).lower()
        if start_game == "y":
            resolution = (500, 400)
            dungeon_lily = pygame.image.load("Lily's Dungeon Floor.png")
            white = (255, 255, 255)
            black = (0, 0, 0)
            red = (255, 0, 0)
            screen = pygame.display.set_mode(resolution)
            while True:
                #screen.fill(white)
                screen.blit(dungeon_lily, (0, 0))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("\nThank you for testing my 3D environment.\nProgram terminated.")
                        pygame.quit()
                        exit(1)
        else:
            print(
                '\nThis program is designed to render a three dimensional environment and you don\'t want to see my hard work?')
            return_to_start = input(
                "\nTHEN WHAT AM I GOOD FOR?!!!!!\nDo you want to see it, please? Y/N: \n")
            if return_to_start[0] == "y":
                start()
            else:
                print("\nK Bye.")
                exit(1)
    start()
main()
