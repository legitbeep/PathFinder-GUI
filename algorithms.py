from queues import *
from random import shuffle
from multiprocessing import Process

class algo:

    def bfs(self,start,end):

        front = Queue()
        front.add(start)
        came_from = {start: None}
        success = False
        has_been_next = []

        while not front.empty():
            current = front.pop()
            current.visit()
            if current == end:
                success = True
                break

            for next_tile in current.neighbours:
                if next_tile not in has_been_next:
                    has_been_next.append(next_tile)
                if next_tile not in came_from:
                    front.add(next_tile)
                    came_from[next_tile] = current

        return came_from, success, has_been_next

    def aStar(self,start,end):

        front = PriorityQueue()
        front.put(start,0)
        cameFrom = {start:None}
        curCost = {start:0}
        beenNext = []
        done = False

        while not front.empty():
            cur = front.pop()
            cur.visit()

            if cur == end:
                done = True
                break

            for nextTile in cur.neighbours:

                if nextTile not in beenNext:
                    beenNext.append(nextTile)

                newCost = curCost[cur] + nextTile.weight

                if nextTile not in curCost or newCost < curCost[nextTile]: 
                    curCost[nextTile] = newCost
                    priority = newCost + self.distance(end,nextTile)
                    front.put(nextTile,priority)
                    cameFrom[nextTile] = cur
        return cameFrom , curCost , done , beenNext

    def distance(self,end,nextTile):
        return abs(end.x - nextTile.x) + abs(end.y - nextTile.y)

    def djikstra(self,start,end):

        front = PriorityQueue()
        front.put(start,0)
        cameFrom = {start:None}
        curCost = {start:0}
        beenNext = []
        done = False

        while not front.empty():

            cur = front.pop()
            cur.visit()
            if cur == end :
                done = True
                break

            for nextTile in cur.neighbours:

                newCost = curCost[cur] + nextTile.weight
                
                if nextTile not in beenNext or newCost < curCost[cur]:
                    if nextTile not in beenNext:
                        beenNext.append(nextTile)
                    curCost[nextTile] = newCost
                    priority = newCost
                    front.put(nextTile,priority)
                    cameFrom[nextTile] = cur
        return cameFrom , curCost, done , beenNext  




    def dfs(self,start,end):

        front = []
        front.append(start)
        came_from = {start: None}
        success = False
        has_been_next = []
    
        while not len(front)==0 and not success:
            current = front.pop()
            current.visit()
            if current == end:
                success = True
                break


            for next_tile in current.neighbours:
                if next_tile not in has_been_next:
                    has_been_next.append(next_tile)
                if next_tile not in came_from:
                    front.append(next_tile)
                    came_from[next_tile] = current
            
        return came_from, success, has_been_next      

