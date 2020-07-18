class LinkedList:
    __init__(self, value):
        self.value = value
        self.next = None

def finder(paths, queries):
    file_paths = {}
    
    for path in paths:
        path_split = path.split('/')
        name_index = len(path_split) - 1
        file_name = path_split[name_index]
        file_paths[file_name] = path

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
