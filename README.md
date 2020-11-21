# COMP 251 - Assignment 3 Test Cases

## **IMPORTANT**

- Even though we tried making the most appropriate testcases for this assignment, there still may be some errors in them, do not hesitate to point them out.

- Having everything right in the following tests does not mean in any way that you will obtain 100% on the assignment.

---

## Contribute

You are more than welcome to fork this repository and add more test cases.

---

## To do's

### Question 1

[ ] Add tester file for pathDFS

[ ] CLRS p. 728 : transcribe worst case scenario for FF

[ ] Internet : Find examples of max-flow (bigger graphs)

### Question 2

[ ] Test cases for Question 2 : Bellman-Ford

---

## Question 1 : _Ford-Fulkerson_

### Running tests

You must pass **FFTest _i_ .txt** as argument to **FordFulkerson.java** to run the tests, where **_i_** is the number of the test.

For example, to run the first example you should do the following :

```b
$ javac FordFulkerson.java
$ java FordFulkerson FFTest1.txt
```

### Sample output should look like:

```b
1
0 5
6
0 1 1
1 2 1
2 3 1
3 4 1
4 5 1
```

The result should match **FFRes _i_ .txt**, where **_i_** is the number of the test. For example if you run **`java FordFulkerson FFTest1.txt`** , your output should be exactly the contents of **`FFRes1.txt`**.

**Note : All test files are located in the [FordFulkerson folder](https://github.com/tomsarry/COMP251_A3_TestCases/tree/main/FordFulkerson).**

### Precisions on Graphs

| Graph                                                  | Purpose of test                                                            |
| ------------------------------------------------------ | -------------------------------------------------------------------------- |
| FFTest1                                                | Trivial path from s to t (one iteration)                                   |
| FFTest2                                                | No path from s -> t                                                        |
| FFTest3                                                | Same file as ff2.txt (provided by instructor)                              |
| FFTest4                                                | Same graph as FFTest3, but source is 5, target is 0 (no path)              |
| [FFTest5](https://www.youtube.com/watch?v=Tl90tNtKvxs) | Multiple solutions (Res5-1 / [Res5-2](https://youtu.be/Tl90tNtKvxs?t=269)) |

## Question 2 : _Bellman-Ford_

_WIP_
