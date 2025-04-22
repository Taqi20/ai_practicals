# Artificial Intelligence Viva Notes

## **Uninformed Search Algorithms (DFS & BFS)**

1. **What is the difference between informed and uninformed search?**  
   Uninformed (blind) search uses no heuristic information about the goal’s location; it explores the search space based solely on node expansions. Informed search uses heuristic estimates to guide exploration toward the goal.

2. **Explain how Depth‑First Search (DFS) works.**  
   DFS starts at the root and explores as far as possible along each branch before backtracking, using a stack (or recursion) to keep track of nodes.

3. **Explain how Breadth‑First Search (BFS) works.**  
   BFS starts at the root and explores all neighbors at the current depth before moving to the next level, using a queue to manage the frontier.

4. **In which scenarios is BFS preferred over DFS?**  
   When you need the shortest path (in steps) and the solution is likely at a shallow depth, because BFS is complete and optimal under equal step costs.

5. **What are the drawbacks of DFS?**  
   It can get stuck in infinite loops on cyclic graphs, does not guarantee finding the shortest path, and completeness is not guaranteed without cycle checks.

6. **Why is BFS considered optimal?**  
   Because it expands nodes in order of increasing path length (number of steps), it always finds the shallowest solution when all steps cost the same.

7. **What are the time and space complexities of DFS and BFS?**  
   - DFS: Time O(bᵐ), Space O(b·m)  
   - BFS: Time O(bᵈ), Space O(bᵈ)  
   where b = branching factor, m = maximum depth, d = depth of the shallowest solution.

8. **Can DFS be modified to avoid infinite loops?**  
   Yes—by maintaining a visited set of expanded nodes (or by limiting depth with depth‑limited search).

9. **What is the role of the visited set in these algorithms?**  
   To prevent revisiting the same nodes, avoiding cycles and redundant expansions.

10. **How do DFS and BFS differ in terms of memory usage?**  
    DFS uses memory proportional to the current path depth (stack), making it more memory‑efficient when the solution is deep; BFS stores all nodes at the current frontier level, which can grow exponentially.

---

## **A* Search**

1. **What is A* Search?**  
   An informed, optimal path‑finding algorithm that uses both the cost so far (g(n)) and a heuristic estimate (h(n)) to choose the next node.

2. **Write the A* evaluation function.**  
   `f(n) = g(n) + h(n)`, where g(n) is the exact cost from the start to n, and h(n) is the heuristic estimate from n to the goal.

3. **What makes a heuristic admissible?**  
   It never overestimates the true cost to reach the goal: h(n) ≤ actual cost from n to goal.

4. **Why is admissibility important?**  
   It guarantees that A* finds an optimal (least‑cost) path.

5. **Describe the data structures A* uses.**  
   - **Open list**: a priority queue of frontier nodes, ordered by f(n)  
   - **Closed list**: a set of already‑expanded nodes  
   - **g_cost** map: stores the best known g(n) for each node  
   - **parent** map: records predecessors for path reconstruction

6. **Outline the A* algorithm steps.**
   1. Add start to open list.  
   2. While open is not empty:  
      - Remove node n with lowest f(n).  
      - If n is goal, reconstruct and return path.  
      - Move n to closed list.  
      - For each neighbor m: compute tentative g(m).  
        - If m is new or tentative g(m) is better, update g(m), set parent, and add or reprioritize m in open.

7. **What are A*’s properties?**  
   - Complete (finds a path if one exists)  
   - Optimal (with admissible heuristic)  
   - Time complexity exponential in worst case (O(bᵈ))  
   - Space complexity high (stores all generated nodes)

8. **List A*’s main limitations.**  
   High memory usage (open + closed lists) and potential re‑expansion of nodes if costs improve.

---

## **Experiment 4: Classification & Attribute Selection (WEKA)**

1. **What was the aim of the experiment and which classification problem did you choose?**  
   To apply classification techniques on a dataset of your choice (e.g., customer churn, iris species).

2. **What is a “knowledge database” and how did you structure your ARFF file?**  
   A database in ARFF format lists `@relation`, defines each `@attribute` (with types/values), and provides data lines under `@data`.

3. **Why WEKA and which classification algorithm did you use?**  
   WEKA offers a GUI and implementations of standard algorithms. Common choices include J48 (decision tree) or Naive Bayes.

4. **What is feature selection and why is it needed? How do CFSEvaluator, Chi‑Squared, and SubsetEvaluator work?**  
   Feature selection removes irrelevant or redundant attributes to improve model performance.  
   - **CFSEvaluator**: selects subsets by correlation-based measures  
   - **Chi‑Squared**: ranks features by statistical association with the class  
   - **SubsetEvaluator**: evaluates subsets using cross-validation

5. **Define Accuracy, Precision, Recall, F1‑score, AUC. How did attribute selection impact these metrics?**  
   - **Accuracy**: (TP+TN)/total  
   - **Precision**: TP/(TP+FP)  
   - **Recall**: TP/(TP+FN)  
   - **F1‑score**: harmonic mean of precision and recall  
   - **AUC**: area under ROC curve  
   Removing irrelevant features often increases precision and reduces overfitting, improving these metrics.

6. **Which attributes turned out most relevant and why? What general lessons did you learn?**  
   The highest‑scoring features (e.g., customer age or income) often align with domain knowledge. Lesson: proper feature selection speeds up training and yields simpler, more generalizable models.

---

## **Experiment 5: Prolog Family‑Tree Program**

1. **What was the aim of the experiment and what is Prolog?**  
   To model family relationships declaratively. Prolog is a logic programming language based on facts and rules.

2. **Define a fact vs. a rule and give examples.**  
   - **Fact**: a basic assertion, e.g., `parent(alice, bob).`  
   - **Rule**: a conditional relationship, e.g., `grandparent(X,Z) :- parent(X,Y), parent(Y,Z).`

3. **How do you pose a query and how does Prolog find solutions?**  
   Use `?-` prefix, e.g., `?- grandparent(alice, Who).` Prolog uses backtracking to explore all variable bindings that satisfy the query.

4. **What logical operators are used?**  
   - Conjunction: `,` (and)  
   - Disjunction: `;` (or)  
   - Negation: `\+ Goal` or `not(Goal)`  
   - Inequality: `\=`

5. **How are arithmetic and comparisons handled?**  
   Use `is` to evaluate expressions, e.g., `X is Y + 1`, and comparison operators `>`, `<`, `>=`, `=<`.

6. **How would you define extended relationships and handle negation for “bachelor”?**  
   - **Uncle**: `uncle(X,Y) :- parent(Z,Y), sibling(X,Z).`  
   - **Ancestor**: recursive rule similar to grandparent.  
   - **Bachelor**: `bachelor(X) :- male(X), \+ married(X).`

---

## **Monkey‑and‑Banana Problem**

1. **What is the Monkey and Banana problem?**  
   A planning problem where a monkey must move a box to reach bananas hanging out of reach.

2. **How do you represent the state?**  
   As a tuple: `(monkey_pos, box_pos, monkey_status, banana_status)`.

3. **What actions can the monkey perform, and what are their preconditions/effects?**  
   - **Go(X)**: no precondition → moves monkey to X  
   - **Push(Box,X)**: monkey at box → moves both to X  
   - **Climb(Box)**: monkey at box on floor → monkey on box  
   - **Grasp**: monkey on box at banana → banana status becomes “has_banana”

4. **How do you define the goal state?**  
   `banana_status == has_banana`

5. **How would you solve it via uninformed search vs. A*?**  
   - **BFS/DFS**: explore states until goal  
   - **A***: heuristic = Manhattan distance from box to banana plus one climb step

6. **Walk through a Python implementation.**  
   Use `if`‑blocks to check preconditions, generate successor states, maintain a frontier (stack/queue/priority queue), and a visited set.

7. **What is the size of the state space and how does it scale?**  
   For N positions: O(N²) combinations of monkey and box positions times statuses; grows rapidly with more items or larger grids.

8. **How would you model it in Prolog?**  
   Define facts for initial state, rules for actions generating new states, and use Prolog’s backtracking to search.

9. **How would you extend the problem for multiple boxes/bananas?**  
   Include lists of positions and iterate action definitions over each item; the state tuple grows accordingly.

10. **What real‑world scenarios relate to this problem?**  
   Basic robotics tasks involving moving obstacles, stacking, and object retrieval.

---

## **N‑Queens Problem (8‑Queens)**

1. **What is the N‑Queens problem?**  
   Place N queens on an N×N board so that none attack each other (no shared row, column, or diagonal).

2. **Why can’t two queens share a row, column, or diagonal?**  
   Because queens move any number of squares vertically, horizontally, or diagonally and would threaten each other.

3. **Why is it called a backtracking problem?**  
   You place a queen, recurse to the next row, and if no safe position exists, remove (backtrack) and try another.

4. **How do you check if placing a queen is safe?**  
   Verify no other queen is in the same column, or on either diagonal above the current row.

5. **What are the base and recursive cases?**  
   - **Base**: row == N → all queens placed → record solution  
   - **Recursive**: try each column in the current row, place queen if safe, recurse to next row

6. **What is the time complexity?**  
   Worst‑case O(N!) because each row tries N columns.

7. **How is backtracking applied?**  
   After a recursive call, remove the queen (`board[row][col] = '.'`) to try the next column.

8. **What does the `is_safe()` function do?**  
   Checks the column and both diagonals above the current cell for existing queens.

9. **Why remove the queen after recursion?**  
   To undo the move (backtrack) and explore alternative placements in the same row.

10. **What happens when `row == N`?**  
    A valid solution is found; you print or store the board configuration.

11. **How many solutions does 8‑Queens have?**  
    92 distinct solutions (not counting rotational/reflection symmetries).

12. **Can you explain the code in your own words?**  
    You iterate row by row, place queens safely, recurse, and backtrack until all rows are filled, collecting each valid arrangement.
