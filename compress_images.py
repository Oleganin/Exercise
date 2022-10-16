from hexlet import fs
import copy

def copy_meta(meta):
    return copy.deepcopy(meta)

def is_jpg(file):
    return fs.get_name(file).split('.')[-1] == 'jpg'

def compress_image(node, scale = 2):
    if fs.is_directory(node):
        return node
    if fs.is_file(node):
        if is_jpg(node):
            new_meta = copy_meta(fs.get_meta(node))
            new_meta['size'] = int(new_meta['size']/scale)
            return fs.mkfile(fs.get_name(node), new_meta)
        else:
            return node


def compress_images(tree, scale = 2):
    children = fs.get_children(tree)
    new_children = list(map(lambda child: compress_image(child, scale), children))
    new_meta = copy_meta(fs.get_meta(tree))
    return fs.mkdir(fs.get_name(tree), new_children, new_meta)

if __name__ == '__main__':
    from visual_tree import visual_tree
    tree = fs.mkdir(
        'my_documents',
        [
            fs.mkfile('avatar.jpg', {'size':100}),
            fs.mkfile('photo.jpg', {'size':150})
        ],
        {'hide': False}
    )
    visual_tree(tree)
    print('-'*10+'{AFTER COMPRESS}'+'-'*10)
    visual_tree(compress_images(tree))
