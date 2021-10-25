class Solution:
  def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    # This solution takes note of each level as I iterate through.
    # `before_pop` is needed because I want to store the last queue
    # before the queue is reset to the next level to remove.

    # The solution is fairly easy to understand. Queue is the current queue,
    # and next_level represents the next `bastion` of sorts.
    # Usually we don't need to use another array for the next level, but
    # we need to keep track of the level.
    
    queue = [ root ]
    level = 0
    next_level = []
    before_pop = []
    
    while queue:
        # pop from last value
        level += 1
        before_pop = queue
        for node in queue:
            if not node == None:
                if not node.left == None: next_level.append(node.left)
                if not node.right == None: next_level.append(node.right)
        
        queue, next_level = next_level, []
    
    return sum([x.val for x in before_pop])

class Solution:
  # This is the classic way to iterate though the BFS way. Actually not too hard.
  def deepestLeavesSum(self, root: Optional[TreeNode]) -> int: 
    queue = [] 
    queue.append(root) 
    while queue: 
      # pop from last value 
      node = queue.pop(0) 
      if not node == None: 
        queue.append(node.left) 
        queue.append(node.right) 


# https://leetcode.com/problems/deepest-leaves-sum