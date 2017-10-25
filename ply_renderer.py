#from __future__ import division
import numpy as np
import re

class Parse():
	def __init__(self,name):
		self.name = name


	def parse():
		file_object  = open(self.name, 'r')
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

		header = data[0:end_header_index+1]

		element_vertex_number_index = [i for i,val in enumerate(header) if val.startswith('element vertex ')]
		element_vertex_number_index = element_vertex_number_index[0]
		num_of_vertex = header[element_vertex_number_index].split(" ")
		num_of_vertex = np.int32(num_of_vertex[2])

		body = data[end_header_index+1:]
		vert_list = body[0:num_of_vertex]
		face_list = body[num_of_vertex:]
