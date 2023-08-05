import math 
import pygame
import numpy as np



def AddUncertain(Distance, Angle, Sigma ):
    Mean = np.array([Distance,Angle])
    Cov = np.diag (Sigma ** 2)  # Covariance Matrix
    Distance, Angle = np.random.multivariate_normal(Mean,Cov)
    Distance = max(Distance,0)
    Angle = max(Angle,0) # To ignore negative values
    return [Distance,Angle]



class LiDAR():
    def __init__(self, Range, Map, Uncertainty):
        self.Range = Range
        self.Speed = 4 
        self.Sigma = np.array([Uncertainty[0],Uncertainty[1]]) #Sensor Measurement noise
        self.initPos = (0,0)
        self.Map = Map
        self.W,self.H = pygame.display.get_surface().get_size()
        self.Obstacles = []
    
    def EquDis (self, ObstaclePos):
        px = (ObstaclePos[0]-self.initPos[0])**2
        py = (ObstaclePos[1]-self.initPos[1])**2
        return math.sqrt(px+py)
    
    def ObstacleSense(self):
        data = []
        x1,y1 = self.initPos[0],self.initPos[1] # X Y Co-Ordinates of the Robot
        for angle in np.linspace(0,2*math.pi,60, False): # This loop is to go through 360 around the robot to sense the obstacle in the environment
            x2,y2 = (x1 + self.Range * math.cos(angle),y1 - self.Range * math.sin(angle)) # End of line
            for i in range (0,101):
                u = i/100
                x =int(x1*u + x2 *(1-u)) 
                y =int (y1*u + y2 *(1-u))
                if 0 < x <self.W and 0<y<self.H:
                    color = self.Map.get_at((x,y))
                    if (color[0],color[1],color[2]) == (0,0,0):
                        Distance = self.Distance((x,y))
                        output = AddUncertain(Distance,angle,self.Sigma)
                        output.append(self.initPos)
                        data.append(output)
                        break
        
        if len(data)>0:
            return data
        else:
            return False