from hexlet import fs

def generate():
    tree = fs.mkdir('python-package', [
        fs.mkfile('Makefile'),
        fs.mkfile('README.md'),
        fs.mkdir('dist'),
        fs.mkdir('tests', [
            fs.mkdir('test_solution.py')
        ]),
        fs.mkfile('pyproject.toml'),
        fs.mkdir('.venv',[
            fs.mkdir('lib', [
                fs.mkdir('site-packages',[
                    fs.mkfile('hexlet-python-package.egg-link')
                ])
            ]),
            {'owner':'root','hidden':False}
        ])
    ], {'hidden':True})
    return tree
