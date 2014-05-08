import pygame
import TextureLoader
import HelperTexture

class IcnBasic:
	def __init__(self,x,y,w,h,textureID=-1,isTextureRescaled = False):
		self.isSelected = False
		self.pos = (x,y)
		self.size = (w,h)
		self.textureID = textureID
		self.rect = (0,0,0,0);
		self.mySurface = None
		if(self.textureID != -1):
			self.mySurface= TextureLoader.get(textureID)
			if(isTextureRescaled ) : self.mySurface =HelperTexture.scale(self.mySurface, self.size)
		pass
	def setSelect(s,value):
		s.isSelected = value
		
	def isUnder(self,pos):
		x, y = pos
		if (self.pos[0] < x and
			self.pos[0] + self.size[0] > x and
			self.pos[1] < y and
			self.pos[1] + self.size[1] > y
			):
			return pos
		else: return None
		
	def select(self):
		self.isSelected = not self.isSelected
		return self.isSelected
	def draw(self,screen):
		if(self.mySurface != None ): self.rect  = screen.blit(self.mySurface,self.pos)
		pass
	def drawEnd(self):
		pygame.display.update(self.rect )
		pass
	def drawUpdate(self, timeElapsed):
		pass