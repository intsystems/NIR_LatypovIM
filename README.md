# Balancing Efficiency and Interpretability: A New Approach to Multi-Objective Optimization with High Computation Costs in Lipschitz Functions

**Author:** Ilgam Latypov

**Advisor:** Yuriy Dorn

## Abstract

In practical engineering and optimization scenarios, tackling multi-objective optimization (MOO) problems often involves employing scalarization methods. Traditional approaches, while being effective, often entail significant computational overhead due to iterative computations. In this paper, we propose a novel method specifically tailored for Lipschitz objective functions aimed at computing function values only once, thus substantially reducing computational costs. This approach is advantageous in scenarios where function computation is expensive or where function values are computed once and then computation become unavailable. Our algorithm uses the Gembchiki scalarization method, is formulated as a convex optimization problem and offers efficient and practical solution to MOO problems. Additionally, we propose interpretable parameters selection for the scalarization method, enhancing the interpretability and practical applicability of the optimization results. Empirical evaluations, conducted on graph-based supply network problems, demonstrate the effectiveness and scalability of our approach, highlighting its potential to address computational challenges in MOO across various domains.

## Repository Structure

The repository is structured as follows:

- `paper`: This directory contains the main paper in PDF format (`main.pdf`) 
<!-- and the LaTeX source file (`main.tex`). Also there is a directory `figs` with images used in the paper. -->
- `code`: This directory contains the code used in the paper. 
<!-- It has its own `README.md` file providing a detailed description of the code files. -->