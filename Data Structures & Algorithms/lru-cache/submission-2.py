class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.order = []

        

    def get(self, key: int) -> int:
        
        if key in self.hash_map:
            if key in self.order:
                self.order.remove(key)
                self.order.append(key)
            else:
                self.order.append(key)
            return self.hash_map[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.hash_map:
            self.hash_map[key] = value
            self.order.remove(key)
            self.order.append(key)

        elif len(self.hash_map) < self.capacity:
            
            self.order.append(key)
            self.hash_map[key] = value  
        
        else:
            remove = self.order[0]
            self.order.remove(remove)
            del self.hash_map[remove]
            self.order.append(key)
            self.hash_map[key] = value


             



        
