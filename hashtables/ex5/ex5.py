class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def finder(paths, queries):
    file_paths = {}
    result = []
    
    for path in paths:
        path_split = path.split('/')
        name_index = len(path_split) - 1
        file_name = path_split[name_index]

        if file_paths.get(file_name) is not None:
            node = file_paths[file_name]
            while node.next is not None:
                node = node.next
            node.next = LinkedList(path)
        else:
            file_paths[file_name] = LinkedList(path)
    
    for query in queries:
        path = file_paths.get(query)
        if path is None:
            continue
        else:
            while path is not None:
                result.append(path.value)
                path = path.next

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
