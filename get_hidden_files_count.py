from hexlet import fs
from visual_tree import visual_tree
def is_hidden(node):
    return fs.get_name(node)[0] == '.'

def get_hidden_files_count(node):
    if fs.is_file(node):
        if is_hidden(node):
            return 1
        else:
            return 0
    children = fs.get_children(node)
    counts = list(map(get_hidden_files_count, children))
    return sum(counts)

if __name__ == '__main__':
    tree = fs.mkdir('/', [
        fs.mkdir('etc', [
            fs.mkdir('apache'),
            fs.mkdir('nginx', [
                fs.mkfile('.ngnix.conf' , {'size': 800}),
            ]),
            fs.mkdir('.consul', [
                fs.mkfile('.config.json', {'size': 1200}),
                fs.mkfile('data', {'size': 8200}),
                fs.mkfile('raft', {'size': 80})
            ]),
        ]),
        fs.mkfile('.hosts', {'size': 3500}),
        fs.mkfile('resolve', {'size': 1000})
    ])
    visual_tree(tree)
    print('-'*5+f'Hidden files: {get_hidden_files_count(tree)}'+'-'*5)
