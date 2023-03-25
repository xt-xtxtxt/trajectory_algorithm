# Simple-trajectory-algorithm



Simple trajectory algorithms are implemented in python

Due to my limited English, so there may be grammatical or semantic errors in the description.If you find any errors in the code or description, please contact me for modification.Thank you very much.

This is my email address: taoxu22@mails.jlu.edu.cn

I will upload the algorithms and codes I have learned one after another and add simple comments for reading and understanding.

This library is mainly used to implement breadth-first algorithm, Dijkstra algorithm and Astar algorithm, and visualize their results.

This library is mainly used to record my learning trajectory algorithm process, mainly using python to chieve the algorithm.

If I have extra time, I try to refactor the algorithms in c++ code.

Reference : https://www.redblobgames.com/pathfinding/a-star/introduction.html

-----------------------------------------------------------------------------------------------------------------------------------------------
# Modify log:


2023.3.25

1.Reassemble the file and modify some of its code.

2.If everything goes well, this is the last update to the library.In my humble opinion.There are still some problems.

  1)The code time complexity is high,If you run the code,you can see that it takes longer than you expected.More than 70 percent of time is spent generating visual maps.Python's long runtime is also a factor.C++ is still the first choice.
  
  2)No random obstacle map is created.You need to manually add obstacles.And I didn't add a function to determine whether the starting and ending points are in obstacles.I think it's a very simple question for you.
  
This library is just to implement the basic ideas of various tracking algorithms, so I didn't spend a lot of time optimizing and improving my code.If you have any better ideas to share with me.
  
2023.3.21

1.Upload the newly modified Astar algorithm.Previous versions of Astar had major logic problems.Please refer to new version.

2.This version of Astar algorithm is still not perfect.It's not looking for the shortest path.It is affected by heuristic function and moving cost.You can modify its parameters yourself.

2023.3.20

1.The breadth-first algorithm was modified to add diagonal movement.Increase the number of obstacles on the map.

2.Dijkstra algorithm and Astar algorithm were added.Dijkstra algorithm has a good performance, but Astar alogrithm still has some problem.I will modify the Astar algorithm in the following time.

3.Package and sort all files for runtime and error correction.


2023.3.19

First version of breadth-first algorithm.You need to manually add obstacles.And can only move in four directions.
