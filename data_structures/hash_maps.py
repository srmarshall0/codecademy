class HashMap:
    def __init__(self, array_size = None):
        self.array_size = array_size
        self.array = [None for i in range(array_size)]
    def hash(self, key, number_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + number_collisions
    def compressor(self, hash_code):
        return hash_code % self.array_size
    def assign(self, key, value):
        index = self.compressor(self.hash(key))
        current_array_value = self.array[index]
        if current_array_value is None:
            self.array[index] = [key, value]
            return 
        if current_array_value is not None:
            if current_array_value[0] == key:
                self.array[index] = [key, value]
            return 
        # collision 
        count_collisions = 1 
        while current_array_value[0] != key:
            new_hash_code = self.hash(key, count_collisions)
            new_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_index]
            if current_array_value is None:
                self.array[new_index] = [key, value]
                return 
            if current_array_value is not None:
                if current_array_value[0] == key:
                    self.array[new_index] = [key, value]
                    return 
            else:
                count_collisions += 1
        return 
    def retrieve(self, key):
        index = self.compressor(self.hash(key))
        possible_return_value = self.array[index]
        if possible_return_value is None:
            return None
        if possible_return_value is not None:
            if possible_return_value[0] == key:
                return possible_return_value[1]
        # retrieval collision 
        retrieval_collisions = 1
        while possible_return_value[0] != key:
            new_hash_code = self.hash(key, retrieval_collisions)
            new_index = self.compressor(new_hash_code)
            possible_return_value = self.array[new_index]
            if possible_return_value is None:
                return None
            if possible_return_value is not None:
                if possible_return_value[0] == key:
                    return possible_return_value[1]
            else:
                retrieval_collisions += 1
        return 
    

# testing 
hash_map = HashMap(15)
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")


print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))