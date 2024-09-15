class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        """Find the node with the given id using depth-first traversal."""
        return self._dfs(self.root, id)

    def _dfs(self, node, id):
        """Helper method for depth-first search."""
        if node is None:
            return None
        
        if node['id'] == id:
            return node
        
        # Search in the children nodes recursively
        for child in node.get('children', []):
            result = self._dfs(child, id)
            if result:
                return result

        return None  # Return None if no match is found
