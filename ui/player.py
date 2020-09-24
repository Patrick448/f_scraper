import pygame
import logging

logger = logging.getLogger('app.player')

class Player:
    @classmethod
    def play(cls, file_path):

        logger.debug(f"Requested file path: {file_path}")
        file = open(file_path)
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick()

        file.close()