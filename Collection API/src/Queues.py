import unittest
from collections import deque 
from queue import Queue


class Test(unittest.TestCase):

    def testCollectionsDeque(self):
        q = deque([1, 2, 3])

        q.append(4)
        self.assertEqual(list(q), [1, 2, 3, 4])
        
        q.appendleft(0)
        self.assertEqual(list(q), [0, 1, 2, 3, 4])

        result = q.pop()
        self.assertEqual(result, 4)
        self.assertEqual(list(q), [0, 1, 2, 3])
        
        result = q.popleft()
        self.assertEqual(result, 0)
        self.assertEqual(list(q), [1, 2, 3])

        q.insert(3, 4)
        self.assertEqual(list(q), [1, 2, 3, 4])

        q.remove(3)  # Remove a value, not at an index!
        self.assertEqual(list(q), [1, 2, 4])

        q.extend([5, 6])
        self.assertEqual(list(q), [1, 2, 4, 5, 6]) 
        
        q.extendleft(['a', 'b', 'c'])  # In reverse order of course...
        self.assertEqual(list(q), ['c', 'b', 'a', 1, 2, 4, 5, 6]) 

    def testQueueQueue(self):
        q = Queue(8)

        q.put(1)
        q.put(2)
        q.put(3)
        q.put(4)
        self.assertEqual(list(q.queue), [1, 2, 3, 4])
        
        result = q.get()  # Not pop
        self.assertEqual(result, 1)  # First item, not last
        self.assertEqual(list(q.queue), [2, 3, 4])
        

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
