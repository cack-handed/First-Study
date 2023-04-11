**1041. 困于环中的机器人**<br>
题目思路：<br>
收获技巧：学习答案；<br>
· 其中规定了4个方向，每个方向用各个方向数轴的单位向量表示；<br>
· 旋转对应于下标；只有四个数字+1的补码是+3，+1 = -(+3)。所以逆时针的-1与顺时针+3是同一个东西；<br>
· 模拟的过程，感觉很复杂。实际上就是暴力枚举数值，根据读取到的所有情况做出响应；<br>
相关理论：[群论](https://en.wikipedia.org/wiki/Group_theory)<br>
题外话：本人不懂什么群论。从结果上看，只是用到了一个同余理论，不论是旋转90°、180°、270°，经过一定的循环一定是可以被360度整除。回到原点进入循环。<br>
唯一的例外就是（方向不变&&位移改变），此种情况下，只会沿着一个方向移动，不会回到原点。