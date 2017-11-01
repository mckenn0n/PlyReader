#from __future__ import division
import numpy as np
import re

class Parse():
	def __init__(self,name):
		self.name = name
		self.header = []
		self.vert_list = []
		self.face_list = []


	def parse(self):
		file_object  = open('../models/'+self.name, 'r')
		data = file_object.read()
		file_object.close()
		data = data.split("\n")
		end_header_index = data.index("end_header")

		# element_vertex_number_index = [i for i,val in enumerate(data) if val.startswith('element vertex ')]
		# element_vertex_number_index = element_vertex_number_index[0]
		# num_of_vertex = data[element_vertex_number_index].split(" ")
		# num_of_vertex = np.int32(num_of_vertex[2])

		# element_face_number_index = [i for i,val in enumerate(data) if val.startswith('element face ')]
		# element_face_number_index = element_face_number_index[0]
		# num_of_face = data[element_face_number_index].split(" ")
		# num_of_face = np.int32(num_of_face[2])

		self.header = data[0:end_header_index+1]

		element_vertex_number_index = [i for i,val in enumerate(self.header) if val.startswith('element vertex ')]
		element_vertex_number_index = element_vertex_number_index[0]
		num_of_vertex = self.header[element_vertex_number_index].split(" ")
		num_of_vertex = np.int32(num_of_vertex[2])

		body = data[end_header_index+1:]
		self.vert_list = body[0:num_of_vertex]
		for x in range(len(self.vert_list)):
			self.vert_list[x] = self.vert_list[x].split(" ")
			self.vert_list[x] = np.float32(self.vert_list[x])
		self.vert_list = [x for x in self.vert_list if x != '']

		self.face_list = body[num_of_vertex:]
		self.face_list = [x for x in self.face_list if x != '']
		for x in range(len(self.face_list)):
			self.face_list[x] = self.face_list[x].split(' ')
			self.face_list[x] = np.int32(self.face_list[x])


jim = Parse("model0.ply")
jim.parse()
print(jim.name,'\n\n\n\n', jim.header,'\n\n\n\n', jim.vert_list, '\n', len(jim.vert_list), '\n\n\n\n', jim.face_list,'\n',len(jim.face_list))