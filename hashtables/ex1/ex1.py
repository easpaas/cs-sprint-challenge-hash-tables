from collections import defaultdict 

# initialize hash table as built-in 
# ht = defaultdict()


def get_indices_of_item_weights(weights, length, limit):
  ht = {}

  #  store each weight in weights input list as a key in ht
  # with each key, find another key whos sum equals limit and store as value
  for i in range(length):
    # determines difference needed to reach limit
    remaining = limit - weights[i]
    
    # check if remaining exists in ht
    if remaining in ht:
      # output: ht[remaining]
      output = ht[remaining]
      result = [i,output]
      result.sort(reverse=True)
      # print(f"result: {result}")
      return result
    else:
      ht[weights[i]] = i
  # print(f"hash table keys: {ht}")
  return None

