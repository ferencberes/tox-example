import math, operator
import numpy as np
import networkx as nx

### EDGE WEIGHTER CLASSES ###
class ConstantWeighter:
    """Gives each edge uniform weight"""
    def __init__(self, cons):
        self.constant = cons
    
    def getWeight(self, edge_with_data, current_node_num):
        return self.constant

    def toStr(self):
        return '{Constans: %.2f}' % self.constant


class LastIntervalWeighter:
    """Gives uniform weight for each edge that occured in the last interval with length delta"""
    def __init__(self, delta):
        self.delta_t = delta

    def getWeight(self, edge_with_data, current_node_num):
        arrival = edge_with_data[2]['weight']
        t = current_node_num - arrival
        if t < self.delta_t:
            edge_weight = 1.0
        else:
            edge_weight = 0.0
        return edge_weight

    def toStr(self):
        return '{LastInterval: %.2f}' % self.delta_t


### FUNCTION FOR WEIGHTED INDEGREE ###
def weighted_in_degree(graph, node_ids, current_node_num, weighter_obj):
    """Compute weighted indegree for node_ids according to weighter_obj"""
    if type(node_ids) is not list: node_ids = [ node_ids ]
    w_sums = {}
    for node_id in node_ids:
        in_edges = graph.in_edges(nbunch=[node_id], data=True)
        #print in_edges
        w_sum = 0.0
        for edge in in_edges:
            # edge data : [source_id, target_id, number_of_nodes_when_this_edge_occured]
            w_sum += weighter_obj.getWeight(edge, current_node_num)
        w_sums[node_id] = w_sum
    return w_sums


### GRAPH PROCESSOR ###
def weighted_indegree_graph_processor(node_time_sorted_data, weighter_obj, step_size):
    print 'Processing weighted indegrees by %i nodes STARTED...' % step_size
    num_of_nodes = len(node_time_sorted_data)
    weighted_indegrees = []
    G = nx.DiGraph()
    step_index = 0
    new_edges = []
    counter = 0
    for node_num in sorted(node_time_sorted_data):
        for edge in node_time_sorted_data[node_num]:
            new_edges.append((edge[0], edge[1], node_num))
        if step_index + step_size <= node_num or node_num == num_of_nodes-1:
            G.add_weighted_edges_from(new_edges)
            #print 'Number of nodes: %i' % G.number_of_nodes()
            #print 'Number of edges: %i' % G.number_of_edges()
            #print
            weighted_indegrees.append(weighted_in_degree(G, G.nodes(), node_num,  weighter_obj))
            new_edges = []
            step_index = node_num
            counter += 1
    print 'Processing weighted indegrees FINISHED.'
    print 'The number of total steps were: %i' % counter
    return weighted_indegrees
