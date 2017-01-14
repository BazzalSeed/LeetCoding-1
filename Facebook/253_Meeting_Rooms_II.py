
"""
Description
____________
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.

Approach
______________
The core is to calculate the overlap.
Have a map where
1. key is the start and end time
2. initial value is 1 for start and -1 for end
3. +1, -1 for identical start, end time

Loop through the map
record
current_rooms === current opened rooms
rooms === maximum rooms opened

return rooms

Complexity
_______________
O(Nlog(N))
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        dic = {}
        for i in intervals:
            if dic.has_key(i.start):
                dic[i.start] += 1
            else:
                dic[i.start] = 1
            if dic.has_key(i.end):
                dic[i.end] -= 1
            else:
                dic[i.end] = -1
        dic = sorted(dic.items())
        current_rooms, rooms = 0, 0
        for i in dic:
            current_rooms += i[1]
            rooms = max(rooms, current_rooms)
        return rooms
