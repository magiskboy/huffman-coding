# encoding=utf-8

from graphviz import Digraph, nohtml



def node_render(node, g):
    label = str(node.key)
    name = str(id(node))
    if node.val:
        g.node(name, nohtml(f'<f0> {label}|<f1> {node.val}'), shape='record')
    else:
        g.node(name, nohtml(label))
    if node.left:
        node_render(node.left, g)
        g.edge(name, str(id(node.left)), label='0')
    if node.right:
        node_render(node.right, g)
        g.edge(name, str(id(node.right)), label='1')


def viz_tree(tree, filename='tree'):
    g = Digraph('g', filename=f'{filename}.gv',
                node_attr={'shape': 'circle', 'height': '.1'})

    node_render(tree, g)
    g.view()

