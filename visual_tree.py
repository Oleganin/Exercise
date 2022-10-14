from hexlet import fs

def visual_tree(tree, deep = 0):
    logo = f'({fs.get_name(tree)})'
    if fs.get_meta(tree):
        logo += f'-{fs.get_meta(tree)}'
    print(logo)
    for node in fs.get_children(tree):
        if fs.is_file(node):
            print('  '*deep+'|_', end='')
            name_node = fs.get_name(node)
            if fs.get_meta(node):
                name_node += f'-{fs.get_meta(node)}'
            print(name_node)
        if fs.is_directory(node):
            print('  '*deep+'|_', end='')
            deep+=1
            visual_tree(node, deep)
            deep-=1
