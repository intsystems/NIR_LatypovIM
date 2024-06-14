"""
Здесь реализован класс для загрузки и обработки графа
"""
from typing import Any
from paper_code.multicommodity_flow.process_graph import read_graph, read_traffic, solve_problem_with_flow



class GraphFunc:    
    def __init__(self, graph, cost, traffic_mat, additional_cost) -> None:
        self.graph = graph
        self.cost = cost
        self.traffic_mat = traffic_mat
        self.additional_cost = additional_cost
    def __call__(self, bandwidth, *args: Any, **solver_kwargs: Any) -> Any:
        dat = {'graph': self.graph, 'cost': self.cost, 'bandwidth': bandwidth}
        try:
            rez = solve_problem_with_flow(dat, self.traffic_mat, 
                                          self.additional_cost,
                                          **solver_kwargs)                                        
            self.rez = rez
            return rez['flow_cost']
        except Exception as e:
            print(e)
            return float("inf")