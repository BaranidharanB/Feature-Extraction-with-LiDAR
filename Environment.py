import math
import pygame

class EnvironmentBuild():
    def __init__ (self,MapDim):
        pygame.init()
        self.pointCloud=[]
        self.externalMap = pygame.image.load("Plan.png")
        self.mapH,self.mapW = MapDim
        self.MapWindowName = "2D Lidar Visualization"
        pygame.display.set_caption(self.MapWindowName)
        self.map = pygame.display.set_mode((self.mapW,self.mapH))
        # Overlaying the Empty map with the image of house floor plan
        self.map.blit(self.externalMap,(0,0))
        self.black = (0,0,0)
        self.grey = (70,70,70)
        self.Blue = (0,0,255)
        self.Green = (0,255,0)
        self.Red = (255,0,0)
        self.White = (255,255,255)

    
    def Ad2Pos (self,distance,angle,robotpos):
        x = distance * math.cos(angle) + robotpos[0]
        y = -distance * math.sin(angle) + robotpos[1]
        return (int (x),int (y))
    
    def DataStorage(self,data):
        print(len(self.pointCloud))
        if data:
            for i in data:
                point = self.Ad2Pos(i[0],i[1],i[2])
                if point not in self.pointCloud:
                    self.pointCloud.append(point)
    def ShowSensorData(self):
        self.mapInfo = self.map.copy()
        for point in self.pointCloud:
            self.mapInfo.set_at((int(point[0]),int(point[1])),(255,0,0))


