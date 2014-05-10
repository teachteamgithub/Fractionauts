from IcnBasic import IcnBasic 
import HelperTexture
import HelperVec2

class IcnTextBox(IcnBasic):
	@staticmethod 
	def setFont(font):
		IcnTextBox.FONT =  font

	def __init__(s,x,y,w,h, content):
		IcnBasic.__init__(s,x,y,w,h)
		s.posInit = (x,y)
		s.content = str(content)
		s.setContent(content)
		s.mySurface =  IcnTextBox.FONT.render(s.content , 1, (255,255,255))
	def setContent(s, c):
		s.content = str(c)
		s.mySurface =  IcnTextBox.FONT.render(s.content , 1, (255,255,255))
		size = (s.mySurface.get_width(),s.mySurface.get_height())
		ratio_1 =  s.size[0] / s.mySurface.get_width()
		ratio_2 =  s.size[1] / s.mySurface.get_height()
		ratio = ratio_1 if ratio_1 < ratio_2 else ratio_2

		s.mySurface= HelperTexture.scale(s.mySurface ,HelperVec2.mult( size,(ratio,ratio) ))
		size = (s.mySurface.get_width(),s.mySurface.get_height())
		
		extraSpace = HelperVec2.mult(HelperVec2.sub(s.size, size),(.5,.5) )
		s.pos = HelperVec2.add(s.posInit , extraSpace)
	


