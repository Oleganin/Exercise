from hexlet import fs
from visual_tree import visual_tree

def generate():
    tree = fs.mkdir('python-package', [
        fs.mkfile('Makefile'),
        fs.mkfile('README.md'),
        fs.mkdir('dist'),
        fs.mkdir('tests', [
            fs.mkfile('test_solution.py')
        ]),
        fs.mkfile('pyproject.toml'),
        fs.mkdir('.venv',[
            fs.mkdir('lib', [
                fs.mkdir('python3.6', [
                    fs.mkdir('site-packages',[
                        fs.mkfile('hexlet-python-package.egg-link')
                    ])
                ])
            ])
        ],{'owner':'root','hidden':False})
    ], {'hidden':True})
    return tree

if __name__ == '__main__':
    tree = generate()
    visual_tree(tree)
