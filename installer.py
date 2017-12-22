import pip

def install(package):
    pip.main(['install', package])

# Example
if __name__ == '__main__':
    install('numpy')
    install('tensorflow')
    install('pandas')
    install('scipy')
    install('sklearn')
    install('matplotlib')