from oswhich import linux, windows
#pylint: disable=function-redefined


@linux
def main(*args, **kwargs):
    print('in linux:')
    print('args:', args)
    print('kwargs', kwargs)

@windows
def main(*args, **kwargs):
    print('in windows:')
    print('args:', args)
    print('kwargs', kwargs)

if __name__ == '__main__':
    main(1, 2, 3, 'a', 'b', 'c', x=0, y=-1, z=-2)