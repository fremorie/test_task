if __name__ == '__main__':
    import os
    import os.path as osp

    import sys
    import subprocess

    try:
        source, target = sys.argv[1], sys.argv[2]
        if len(sys.argv) > 3:
            sass = sys.argv[3]
        else:
            sass = 'sass'
    except:
        print('Usage: %s <sass root> <css root> [path to sass]')
        sys.exit(0)

    def walk(path):
        if osp.isfile(path):
            yield path
        elif osp.isdir(path):
            for item in os.listdir(path):
                item_path = osp.join(path, item)
                for x in walk(item_path):
                    yield x

    for f in walk(source):
        rel_path = osp.relpath(osp.abspath(f), osp.abspath(source))
        target_path = '.'.join(osp.join(target, rel_path).split('.')[:-1]) + '.css'

        if not f.endswith('.scss'):
            continue

        print('%s %s %s' % (sass, f, target_path))
        process = subprocess.Popen([sass, f, target_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print('Failed to compile %s' % rel_path)
            print(stdout)
            print(stderr)
