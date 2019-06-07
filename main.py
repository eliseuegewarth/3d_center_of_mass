from random import randint

from graph import Graph
from node import Node
from edge import Edge

def get_rand_rgb_pixel(value_range=[0, 4]):
	k = (255//value_range[1])
	# return {
	# 	"r": randint(value_range[0], value_range[1])*k,
	# 	"g": randint(value_range[0], value_range[1])*k,
	# 	"b": randint(value_range[0], value_range[1])*k
	# 	}
	return (randint(value_range[0], value_range[1])*k*1000^2 +
		randint(value_range[0], value_range[1])*k*1000 +
		randint(value_range[0], value_range[1])*k
		)

def get_pixels(x_range=100, y_range=100, z_range=100, value_range=[0,255]):
	x_lines = []
	for x in range(0, x_range):
		y_lines = []
		for y in range(0, y_range):
			z_lines = []
			for z in range(0, z_range):
				pixel = get_rand_rgb_pixel()
				z_lines.append(Node(pixel))
			y_lines.append(z_lines)
		x_lines.append(y_lines)
	return x_lines

def get_edges(pixels):
	edges = []
	for x in range(1,len(pixels)):
		for y in range(1,len(pixels[x])):
			for z in range(1,len(pixels[x][y])):
				if pixels[x][y][z].value == pixels[x][y][z-1].value:
					edges.append(
						Edge(pixels[x][y][z], pixels[x][y][z-1])
					)
				if len(pixels[x][y]) > z + 1:
					if pixels[x][y][z].value == pixels[x][y][z+1].value:
						edges.append(
							Edge(pixels[x][y][z], pixels[x][y][z+1])
							)
				if pixels[x][y][z].value == pixels[x][y-1][z].value:
					edges.append(
						Edge(pixels[x][y][z], pixels[x][y-1][z])
						)
				if len(pixels[x]) > y + 1:
					if pixels[x][y][z].value == pixels[x][y+1][z].value:
						edges.append(
							Edge(pixels[x][y][z], pixels[x][y+1][z])
						)
				if pixels[x][y][z].value == pixels[x-1][y][z].value:
					edges.append(
						Edge(pixels[x][y][z], pixels[x-1][y][z])
						)
				if len(pixels) > x + 1:
					if pixels[x][y][z].value == pixels[x+1][y][z].value:
						edges.append(
							Edge(pixels[x][y][z], pixels[x+1][y][z])
							)
	return edges

def print_nodes(graph):
	for node in sorted(graph.nodes.keys()):
		print(graph.nodes[node])

if __name__ == '__main__':

	pixels = get_pixels(50,50,50)
	edges = get_edges(pixels)
	graph = Graph("3d image Graph", is_directional=False)
	graph.build_nodes(pixels)
	graph.build_edges(edges)
	bfs = graph.bfs()
	for node in bfs:
		print(node)
	print("=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=")
	import ipdb ;ipdb.set_trace()

	# nodes.sort(key=lambda x:x.value)

	# edges = get_edges(nodes)
	# edges.sort(key=lambda x:x.origin.value)

	# print("----------------------------------------------------------------------")
	# graph = Graph("Second Graph", is_directional=True)
	# graph.build_nodes(nodes)
	# graph.build_edges(edges)
	
	# print_nodes(graph)
	# print("======================================================================")
	# print("=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=")
	# bfs_from_origin = graph.bfs(edges[0].origin.value)[edges[0].origin.value]
	# for node in bfs_from_origin:
	# 	print(node)
	# print("=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=")
	# bfs_complete = graph.bfs()
	# for reachable in bfs_complete.keys():
	# 	print(reachable)
	# 	for node in bfs_complete[reachable]:
	# 		print(node)
	# 	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	# print("=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=+-=")
	# print("======================================================================")
	# reverse_graph = graph.reverse()
	# print_nodes(reverse_graph)
	# print("----------------------------------------------------------------------")