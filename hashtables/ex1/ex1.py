from collections import defaultdict 

# initialize hash table as built-in 
ht = defaultdict()


def get_indices_of_item_weights(weights, length, limit):
  # my code here 
  global ht
  
  #  store each weight in weights input list as a key in ht
  # with each key, find another key whos sum equals limit and store as value
  for i in range(length):
    ht.fromkeys(weights[i])
    
  print(f"hash table keys: {ht}")
  # return None


get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)