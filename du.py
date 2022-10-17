from hexlet import fs
from visual_tree import visual_tree

def du(node):
    children = fs.get_children(node)
    result = list(map(lambda child: (
            fs.get_name(child), get_size_of_node(child)
        ), children)
    )
    return sorted(result, key=(lambda child: child[-1]), reverse=True)

def get_size_of_node(node):
    if fs.is_file(node):
        return fs.get_meta(node)['size']
    children = fs.get_children(node)
    all_size = list(map(get_size_of_node, children))
    return sum(all_size)

if __name__ == '__main__':
    tree = fs.mkdir('/', [
        fs.mkdir('etc', [
            fs.mkdir('apache'),
            fs.mkdir('nginx', [
                fs.mkfile('nginx.conf', {'size':800}),
            ]),
            fs.mkdir('consul', [
                fs.mkfile('.config.json', {'size':1200}),
                fs.mkfile('data', {'size':8200}),
                fs.mkfile('raft', {'size':80}),
            ]),
        ]),
        fs.mkfile('hosts', {'size' : 3500}),
        fs.mkfile('resolve', {'size': 1000}),
    ])
    visual_tree(tree)
    print('-'*20)
    print(du(tree))
