# FinaL Project
#
# Python file name: CIT_95_Final.py
#
# Date: 10-30-2023
#
# Programmer's name: Matthew Gutierrez

import numpy as np
import pygame
import sys

def main():
    # Program Intro
    print("\n** Welcome to Mac Mac's Program for creating a 3D environment. **\n")

    def start():
        start_game = input("Would you like to play the game? Y/N: ").lower()
        if start_game == "y":
            def game_window():
                running = True
                resolution = (1366, 768)
                white = (255, 255, 255)
                black = (0, 0, 0)
                dungeon_lily = pygame.image.load("Lily's Dungeon Floor.png")
                player_cursor_image = pygame.image.load('angle-crosshair.png')
                player_position = [693, 725]
                player_speed = 10

                screen = pygame.display.set_mode(resolution)
                pygame.display.set_caption("Warrior's Diatribe")

                clock = pygame.time.Clock()
                user_input_clock = pygame.time.Clock()  # Clock for handling user input
                minimap_clock = pygame.time.Clock()

                # Calculate scaled cursor size before using it
                original_cursor_size = player_cursor_image.get_size()
                scaled_cursor_size = (int(original_cursor_size[0] * 0.05), int(original_cursor_size[1] * 0.05))

                def mini_map():
                    # Mini-map setup
                    mini_map_size = (int(resolution[0] * 0.2), int(resolution[1] * 0.2))
                    mini_map_surface = pygame.Surface(mini_map_size, pygame.SRCALPHA)  # Use SRCALPHA for transparency

                    # Scale the dungeon image for mini-map
                    scaled_mini_dungeon = pygame.transform.scale(dungeon_lily, mini_map_size)
                    mini_map_surface.blit(scaled_mini_dungeon, (0, 0))

                    # Scale the player cursor for mini-map
                    scaled_mini_cursor = pygame.transform.scale(player_cursor_image,
                                                                (scaled_cursor_size[0] // 10, scaled_cursor_size[1] // 10))
                    mini_map_surface.blit(scaled_mini_cursor, (player_position[0] // 10, player_position[1] // 10))

                    # Display the minimap with transparency
                    screen.blit(mini_map_surface, (resolution[0] - mini_map_size[0], resolution[1] - mini_map_size[1]))

                    # Update the display for the minimap
                    pygame.display.flip()
                    # Frame rate cap for the minimap
                    minimap_clock.tick(30)

                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            print("\nThank you for testing my 3D environment.\nProgram terminated.")
                            running = False
                            pygame.quit()
                            sys.exit()

                    keys = pygame.key.get_pressed()

                    # Get the current mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Move the player cursor to the mouse position
                    player_position[0] = mouse_x - scaled_cursor_size[0] / 2
                    player_position[1] = mouse_y - scaled_cursor_size[1] / 2

                    # Handle user input independently
                    user_input_clock.tick(60)

                    # Fill the background with white
                    screen.fill(white)

                    # Scale the dungeon image to fit the entire map window
                    # scaled_dungeon = pygame.transform.scale(dungeon_lily, resolution)
                    # screen.blit(scaled_dungeon, (0, 0))

                    # Scale the player cursor image
                    scaled_cursor = pygame.transform.scale(player_cursor_image, scaled_cursor_size)

                    # Display the scaled player cursor at the current position
                    screen.blit(scaled_cursor, player_position)

                    # Hide the system mouse cursor
                    pygame.mouse.set_visible(False)

                    # Update the main game window
                    pygame.display.flip()
                    # Frame rate cap for the main window
                    clock.tick(60)

                    # Call the minimap function
                    mini_map()

            game_window()

        else:
            print('\nThis program is designed to render a three-dimensional environment, and you don\'t want to see my hard work?')
            return_to_start = input("\nTHEN WHAT AM I GOOD FOR?!!!!!\nDo you want to see it, please? Y/N: \n")
            if return_to_start[0] == "y":
                start()
            else:
                print("\nK Bye.")
                exit(1)

    start()

main()
