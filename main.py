from ply_renderer import Parse as p
from ply_renderer import Render as r
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame


test = p("model0.ply")
test.parse()
vl = test.vert_list
fl = test.face_list
print('vl ',len(vl), vl[2])
print('fl ',len(fl), fl[2])
# print('test ', vl[2][fl[2][3]])
class GLContext():
	def __init__(self, screen):
		self.screen=screen

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
		glBegin(GL_TRIANGLES)

		glColor3f(1.0, 0.0, 1.0)
		for x in range(len(fl)): #x starts at 1
			print(x)
			glVertex2f(vl[fl[x][1]], vl[fl[x][2]])
			glVertex2f(vl[fl[x][2]], vl[fl[x][3]])
			glVertex2f(vl[fl[x][3]], vl[fl[x][1]])


		glEnd()
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

