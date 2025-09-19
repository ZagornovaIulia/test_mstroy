class TreeStore:
    def __init__(self, items: list):
        self._items = items
        self._by_id = {item["id"]: item for item in items}
        self._children = {}
        self._parent = {}
        for item in items:
            parent = item["parent"]
            self._parent[item["id"]] = parent
            self._children.setdefault(parent, []).append(item)

    def getAll(self):
        return self._items

    def getItem(self, id: int):
        return self._by_id.get(id)

    def getChildren(self, id: int):
        return self._children.get(id, [])

    def getAllParents(self, id: int):
        parents = []
        current_parent = self._parent.get(id)
        while current_parent != "root":
            parent_item = self._by_id[current_parent]
            parents.append(parent_item)
            current_parent = parent_item["parent"]
        # добавляем корневой элемент
        parents.append(self._by_id[current_parent]
                       ) if current_parent != "root" else None
        return parents


if __name__ == "__main__":
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    ts = TreeStore(items)
    print(ts.getAll())
    print(ts.getItem(7))
    print(ts.getChildren(4))
    print(ts.getChildren(5))
    print(ts.getAllParents(7))
