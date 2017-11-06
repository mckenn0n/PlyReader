from ply_renderer import Parse as p
from ply_renderer import Render as r
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


test = p("model0.ply")
test.parse()
vl = test.vert_list
fl = test.face_list
print('vl ',len(vl), vl[0], vl[len(vl)-1])
print('fl ',len(fl), fl[0], fl[len(fl)-1])
# print('test ', vl[2][fl[2][3]])
class GLContext():
	def __init__(self, screen):
		glEnable(GL_DEPTH_TEST)
		glDepthFunc(GL_LEQUAL)
		self.screen=screen
		self.aspect = screen.get_width()/screen.get_height()
		gluPerspective(45.0, self.aspect, 0.1, 200.0)

		glClearColor(0.0, 0.0, 0.0, 1.0)
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		return

	
	def check_events(self):
 		for event in pygame.event.get():
 			if event.type == pygame.QUIT:
 				exit()
 				if event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
 					exit()
 		return


	def display(self):

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glPushMatrix()
		glTranslatef(0.0, 0.0, -5.0) 
		glRotatef(45.0, 1, 0, 0)  
		glRotatef(15, 0, 1, 0) 
		glRotatef(0.0, 0, 0, 1) 
		
		glBegin(GL_TRIANGLES)
		
		glColor3f(1.0, 0.0, 1.0)
		for x in range(len(fl)): #x starts at 0
			glVertex3f(vl[fl[x][1]][0], vl[fl[x][1]][1], vl[fl[x][1]][2])
			glVertex3f(vl[fl[x][2]][0], vl[fl[x][2]][1], vl[fl[x][2]][2])
			glVertex3f(vl[fl[x][3]][0], vl[fl[x][3]][1], vl[fl[x][3]][2])


		
		glPopMatrix()
		return
def main():
	pygame.init() 
	screen = pygame.display.set_mode((600,600), pygame.OPENGL|pygame.DOUBLEBUF) 
	context=GLContext(screen) 

	
	while True:
		context.check_events() 
		context.display() 
		pygame.display.flip() 


if __name__ == '__main__':
	try:
		main()
	finally:
		pygame.quit()

