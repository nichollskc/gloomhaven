# Gloomhaven scenario graph

The python file scenario_dag.py contains a description of the nodes and edges that should be added to the scenario graph.

When you complete a scenario, take the following steps:

1) Add the scenario number to a scenario block, or to the other_scenarios list
2) Add a line to completion_dict giving the date of completion and extra details such as 'Side rooms left'
3) Add a call to add_edge to add edges from the completed scenario to any that were obtained during the scenario
4) Run python3 scenario_dag.py (using a conda environment containing dot - on my mac `conda activate graphics` should work.)

The file locations_route.gv.pdf should now contain the scenario graph.