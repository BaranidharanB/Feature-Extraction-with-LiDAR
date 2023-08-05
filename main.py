from Environment import EnvironmentBuild
from Sensor import LiDAR
import pygame
import math

env = EnvironmentBuild((600,900))


env.OriginalMap = env.map.copy() 
Laser = LiDAR(200,env.OriginalMap,Uncertainty=(0.5,0.01))
env.map.fill ((0,0,0))
env.mapInfo = env.map.copy() 

running = True  

# while running:
#     LidarON = False
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             running = False
#         if pygame.mouse.get_focused():
#             LidarON = True 
#         elif not pygame.mouse.get_focused():
#             LidarON = False
#     if LidarON:
#         position = pygame.mouse.get_pos()
#         Laser.position = position
#         Lidar_data = Laser.ObstacleSense()
#         env.DataStorage(Lidar_data)
#         env.ShowSensorData()
#     env.map.blit(env.mapInfo,(0,0))
#     pygame.display.update()     

while running:
    LidarON = False
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = True
        if pygame.mouse.get_focused():
            LidarON = True 
        elif not pygame.mouse.get_focused():
            LidarON = False
    if LidarON:
        position = pygame.mouse.get_pos()
        Laser.position = position
        Lidar_data = Laser.ObstacleSense()
        env.DataStorage(Lidar_data)
        env.ShowSensorData()
    env.map.blit(env.mapInfo,(0,0))
    pygame.display.update()   

