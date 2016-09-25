from collections import defaultdict
class Solution(object):

    def DFS(self, dt, s, tickets, visited, curitr, i, totalvisited):
        if totalvisited == len(tickets):
            return True


        if s not in dt:
            print s
            return False

        for n in dt[s]:
            if not visited[n[1]]:
                visited[i] = 1
                curitr.append(tickets[n[1]][1])
                print "visiting", tickets[n[1]][1], totalvisited
                if self.DFS(dt, tickets[n[1]][1], tickets, visited, curitr, n[1], totalvisited+1) == True:
                    return True
                visited[i] = 0
                del curitr[-1]
        return False

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        _dict = defaultdict(list)
        for i in range(len(tickets)):
            _dict[tickets[i][0]].append((tickets[i][1], i))

        for key, value in _dict.iteritems():
             _dict[key] = sorted(value)

        print _dict
        size = len(tickets)

        for n in _dict["JFK"]:
            curitr = ["JFK"]
            visited = [0 for i in range(size)]
            curitr.append(tickets[n[1]][1])
            print "visiting", tickets[n[1]][1]
            if self.DFS(_dict, tickets[n[1]][1], tickets, visited, curitr, n[1], 1) == True:
                return curitr

        return []



