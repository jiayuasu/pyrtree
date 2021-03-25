from pyrtree import Rect, RTree

DATA_SIZE = 100

# PyRTree Insert and Search Test. This PyRTree is query only index.

obj = []
for x in range(DATA_SIZE):
    # Create objects with rectangles for objs, Rect(0, 0, 1, 1), Rect(1, 1, 2, 2); name obj0, obj1, ...
    obj.append([Rect(0 + x, 0 + x, 1 + x, 1 + x), 'obj' + x.__str__()])

rtree = RTree() # tree creation

# pyrtree uses the Rect (x_min, y_min, x_max, y_max) notation
for x in range(DATA_SIZE):
    rtree.insert(obj[x], obj[x][0]) # element insertion with a given box

# Query the tree
rect_res = rtree.query_rect(Rect(1, 1, 4, 4) )

# Traverse the query result
for rtree_node in rect_res:
    if not rtree_node.is_leaf():
        continue
    t = rtree_node.leaf_obj()
    print(t[0].x, t[0].y, t[0].xx, t[0].yy, t[1])

# Get the internal nodes which are at the deepest level of the tree. Each internal contains a number of leaf nodes
for nodes in rtree.get_last_level():
    print(nodes)

# Print all
for nodes in rtree.get_last_level():
    for node in nodes:
        print(node[0].x, node[0].y, node[0].xx, node[0].yy, node[1])