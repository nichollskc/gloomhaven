import itertools
import os
import re
import yaml

from graphviz import Digraph

def build_labels():
    with open("scenario_list.txt", "r") as f:
        scenario_list = f.read()

    extracted_coordinates = re.findall(r'(\d+).([A-Z]\-\d+)', scenario_list)
    extracted_names = re.findall(r'(\d+).[A-Z]\-\d\d?([A-Za-z ]+)', scenario_list)
    return dict(extracted_names), dict(extracted_coordinates)


def add_edge(graph, first_node, second_node, explanation, linked=False, unusual=False):
    if linked:
        graph.edge(str(first_node), str(second_node), label=f"    {explanation}   ", color="#008300")
    elif unusual:
        graph.edge(str(first_node), str(second_node), label=f"    {explanation}   ", color="#A9A9A9", style="dashed")
    else:
        graph.edge(str(first_node), str(second_node), label=f"    {explanation}   ")

def format_line(text, color, style):
    return f"<TR><TD><{style}><FONT COLOR=\"{color}\">{text}</FONT></{style}></TD></TR>"

def format_attempt(attempt_info, date):
    if attempt_info.get("failure", False):
        main_line = format_line(f"Attempted {date}", "#A9A9A9", "b")
    else:
        main_line = format_line(f"Completed {date}", "#BF111D", "b")

    if "loot_left" in attempt_info:
        loot_line = format_line(attempt_info["loot_left"], "#BF111D", "i")
    else:
        loot_line = ""

    return main_line + loot_line

def build_graph():
    dot = Digraph(comment = 'Gloomhaven Scenarios')
    dot.attr(newrank = 'true')

    with open("scenario_info.yml", "r") as f:
        scenario_info = yaml.load(f, Loader=yaml.FullLoader)

    print(scenario_info["attempts"])
    all_open_scenarios = set()
    all_labelled_scenarios = set()
    scenario_labels = {}
    for date, attempt in scenario_info["attempts"].items():
        scenario_num = str(attempt["scenario"])

        try:
            existing_label = scenario_labels[scenario_num]
        except KeyError:
            existing_label = ""

        label = existing_label + format_attempt(attempt, date)

        scenario_labels[scenario_num] = label

        all_labelled_scenarios.add(scenario_num)
        all_open_scenarios.add(scenario_num)
        try:
            for linked in attempt["links"].keys():
                all_open_scenarios.add(linked)
        except:
            pass

    for unlabelled in all_open_scenarios.difference(all_labelled_scenarios):
        scenario_labels[unlabelled] = ""

    scenario_blocks = scenario_info["scenario_clusters"]
    included_in_cluster = set()

    scenario_names, coordinate_labels = build_labels()

    for name, block in scenario_blocks.items():
        with dot.subgraph(name=f"cluster_{name}") as cluster:
            cluster.attr(label=block['description'], fontsize='40')
            for i in block['scenarios']:
                included_in_cluster.add(i)

                image_file = f"locations/location_{i}.png"
                assert os.path.isfile(image_file), f"Expected image file {image_file}"
                label = f"""<<TABLE BORDER="0">
                            <TR><TD><IMG SCALE="TRUE" SRC="{image_file}"/></TD></TR>
                            <TR><TD><b>{scenario_names[str(i)]}</b></TD></TR>
                            <TR><TD><b>{coordinate_labels[str(i)]}</b></TD></TR>
                            {scenario_labels[str(i)]}
                            </TABLE>>"""
                print(label)
                cluster.node(name=str(i),
                         label=label,
                         fontname='times',
                         fontsize='30',
                         penwidth='0')

    for i in all_open_scenarios.difference(included_in_cluster):
        image_file = f"locations/location_{i}.png"
        assert os.path.isfile(image_file), f"Expected image file {image_file}"
        label = f"""<<TABLE BORDER="0">
                    <TR><TD><IMG SCALE="TRUE" SRC="{image_file}"/></TD></TR>
                    <TR><TD><b>{scenario_names[str(i)]}</b></TD></TR>
                    <TR><TD><b>{coordinate_labels[str(i)]}</b></TD></TR>
                    {scenario_labels[str(i)]}
                    </TABLE>>"""
        print(label)
        dot.node(name=str(i),
                 label=label,
                 fontname='times',
                 fontsize='30',
                 penwidth='0')

    dot.edge_attr = {'penwidth': '5',
                     'arrowhead': 'normal',
                     'fontsize':'25',
                     'weight': '10',
                     'fontname':'times'}


    for attempt_date, attempt in scenario_info["attempts"].items():
        links = attempt.get("links", {})
        for link, link_info in links.items():
            add_edge(dot,
                     int(attempt["scenario"]),
                     int(link),
                     link_info["description"],
                     linked=link_info.get("linked", False),
                     unusual=link_info.get("unusual", False))

    dot.render('Gloomhaven_scenario_route.gv', view=True)


if __name__ == "__main__":
    build_graph()
