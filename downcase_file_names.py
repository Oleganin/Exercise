from hexlet import fs
import copy
from visual_tree import visual_tree

def downcase_file_names(node):
    name = fs.get_name(node)
    new_meta = copy.deepcopy(fs.get_meta(node))
    if fs.is_file(node):
        return fs.mkfile(name.lower(),new_meta)
    children = fs.get_children(node)
    new_children = list(map(downcase_file_names, children))
    return fs.mkdir(name, new_children, new_meta)

if __name__ == '__main__':
    tree = fs.mkdir('/', [
        fs.mkdir('etTc',[
            fs.mkdir('NgiNX', [], {'size':4000}),
            fs.mkdir('CONSUL', [
                fs.mkfile('config.JSON', {'uid':0})]
                  )
            ]),
        fs.mkfile('HOSTS')
    ])

    visual_tree(tree)
    new_tree = downcase_file_names(tree)
    new_file = fs.get_children(new_tree)[1]
    print(fs.get_name(new_file))
    print('-'*10+'{after downcase_file_names}'+'-'*10)
    visual_tree(new_tree)
