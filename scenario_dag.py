import itertools
import os
import re

from graphviz import Digraph

def build_labels():
    scenario_list = "1.G-10Black Barrow 2.G-11Barrow Lair 3.G-3Inox Encampment 4.E-11Crypt of the " \
                    "Damned 5.D-6Ruinous Crypt 6.F-10Decaying Crypt 7.C-12Vibrant Grotto " \
                    "8.C-18Gloomhaven Warehouse 9.L-2Diamond Mine 10.C-7Plane of Elemental Power " \
                    "11.B-16Gloomhaven Square A 12.B-16Gloomhaven Square B 13.N-3Temple of the " \
                    "Seer 14.C-10Frozen Hollow 15.B-11Shrine of Strength 16.B-6Mountain Pass " \
                    "17.K-17Lost Island 18.C-14Abandoned Sewers 19.M-7Forgotten Crypt " \
                    "20.H-13Necromancer’s Sanctum 21.C-7Infernal Throne 22.K-8Temple of the " \
                    "Elements 23.C-15Deep Ruins 24.C-6Echo Chamber 25.A-5Icecrag Ascent " \
                    "26.D-15Ancient Cistern 27.E-6Ruinous Rift 28.E-4Outer Ritual Chamber " \
                    "29.E-3Sanctuary of Gloom 30.N-15Shrine of the Depths 31.A-16Plane of Night " \
                    "32.L-11Decrepit Wood 49.N-7Rebel’s Stand 50.C-17Ghost Fortress 51.A-15The " \
                    "Void 52.D-14Noxious Cellar 53.F-11Crypt Basement 54.D-8Palace of Ice " \
                    "55.G-5Foggy Thicket 56.G-4Bandits Wood 57.D-14Investigation 58.E-15Bloody " \
                    "Shack 59.F-1Forgotten Grove 60.B-15Alchemy Lab 61.N-11Fading Lighthouse " \
                    "62.O-11Pit of Souls 63.M-1Magma Pit 64.K-16Underwater Lagoon 65.L-5Sulfur " \
                    "Mine 66.G-14Clockwork Cove 67.K-2Arcane Library 68.N-8Toxic Moor 69.F-8Well " \
                    "of the Unfortunate 70.J-17Chained Isle 71.K-5Windswept Highlands " \
                    "72.H-12Oozing Grove 73.N-5Rockslide Ridge 74.I-14Merchant Ship " \
                    "75.G-12Overgrown Graveyard 76.L-3Harrower Hive 77.B-17Vault of Secrets " \
                    "78.B-14Sacrifice Pit 79.K-12Lost Temple 80.K-1Vigil Keep 33.A-7Savvas Armory " \
                    "34.A-4Scorched Summit 35.A-14Gloomhaven Battlements A 36.B-14Gloomhaven " \
                    "Battlements B 37.G-18Doom Trench 38.G-2Slave Pens 39.B-11Treacherous Divide " \
                    "40.F-12Ancient Defense Network 41.F-13Timeworn Tomb 42.C-5Realm of the Voice " \
                    "43.D-4Drake Nest 44.F-3Tribal Assault 45.M-9Rebel Swamp 46.A-11Nightmare " \
                    "Peak 47.H-18Lair of the Unseeing Eye 48.E-1Shadow Weald 81.D-2Temple of the " \
                    "Eclipse 82.M-6Burning Mountain 83.C-15Shadows Within 84.D-12Crystalline Cave " \
                    "85.M-3Sun Temple 86.D-15Harried Village 87.I-9Corrupted Cove 88.D-16Plane of " \
                    "Water 89.C-17Syndicate Hideout 90.J-7Demonic Rift 91.E-2Wild Melee " \
                    "92.C-14Back Alley Brawl 93.N-17Sunken Vessel 94.F-12Vermling Nest " \
                    "95.G-12Payment Due "

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


def build_graph():
    dot = Digraph(comment = 'Gloomhaven Scenarios')
    dot.attr(newrank = 'true')

    scenario_blocks = [{'name': 'jekserah',
                        'desc': 'Jekserah the Valrath merchant',
                        'scenarios': [1, 2, 3, 8, 9, 7, 13, 14, 20, 28]},
                       {'name': 'hail',
                        'desc': 'Hail the Aesther Enchantress',
                        'scenarios': [19, 31, 43, 26, 37, 47]},
                       {'name': 'gloom',
                        'desc': 'The Gloom',
                        'scenarios': [4, 5, 6, 10, 21, 22, 35, 36, 39, 51]},
                       {'name': 'voice',
                        'desc': 'The Voice',
                        'scenarios': [24, 32, 30, 33, 40, 41]},
                       {'name': 'drake',
                        'desc': 'The Drake',
                        'scenarios': [16, 25, 33, 34]},
                       {'name': 'help',
                        'desc': 'Help the Captain of the Guards',
                        'scenarios': [18]},
                       {'name': 'Orchids',
                        'desc': 'Help the Orchids',
                        'scenarios': [38, 44, 48]},
                       ]
    other_scenarios = [15, 17, 61, 64, 68, 71, 82]

    scenarios = other_scenarios + list(itertools.chain.from_iterable([d['scenarios'] for d in scenario_blocks]))

    scenario_names, coordinate_labels = build_labels()

    completion_dict = dict([(str(i), '') for i in scenarios])
    completion_dict.update({
        '1': '<TR><TD><b><FONT COLOR="#BF111D">Completed 13/2/19</FONT></b></TD></TR>',
        '2': '<TR><TD><b><FONT COLOR="#BF111D">Completed 14/2/19</FONT></b></TD></TR>'
             '<TR><TD><i><FONT COLOR="#BF111D">Side rooms left</FONT></i></TD></TR>',
        '3': '<TR><TD><b><FONT COLOR="#A9A9A9">Attempted 15/2/19</FONT></b></TD></TR>'
             '<TR><TD><b><FONT COLOR="#BF111D">Completed 16/2/19</FONT></b></TD></TR>'
             '<TR><TD><i><FONT COLOR="#BF111D">Side rooms left</FONT></i></TD></TR>',
        '8': '<TR><TD><b><FONT COLOR="#BF111D">Completed 17/2/19</FONT></b></TD></TR>'
             '<TR><TD><i><FONT COLOR="#BF111D">Chest left</FONT></i></TD></TR>',
        '82': '<TR><TD><b><FONT COLOR="#BF111D">Completed 19/2/19</FONT></b></TD></TR>',
        '14': '<TR><TD><b><FONT COLOR="#BF111D">Completed 2/3/19</FONT></b></TD></TR>',
        '43': '<TR><TD><b><FONT COLOR="#BF111D">Completed 9/3/19</FONT></b></TD></TR>'
              '<TR><TD><i><FONT COLOR="#BF111D">Side rooms left</FONT></i></TD></TR>',
        '7': '<TR><TD><b><FONT COLOR="#BF111D">Completed 23/3/19</FONT></b></TD></TR>',
        '20': '<TR><TD><b><FONT COLOR="#BF111D">Completed 7/4/19</FONT></b></TD></TR>',
        '16': '<TR><TD><b><FONT COLOR="#BF111D">Completed 25/5/19</FONT></b></TD></TR>',
        '24': '<TR><TD><b><FONT COLOR="#A9A9A9">Attempted 9/6/19</FONT></b></TD></TR>'
              '<TR><TD><b><FONT COLOR="#BF111D">Completed 23/6/19</FONT></b></TD></TR>',
        '25': '<TR><TD><b><FONT COLOR="#BF111D">Completed 27/6/19</FONT></b></TD></TR>',
        '34': '<TR><TD><b><FONT COLOR="#BF111D">Completed 29/6/19</FONT></b></TD></TR>',
        '4': '<TR><TD><b><FONT COLOR="#BF111D">Completed 30/6/19</FONT></b></TD></TR>',
        '5': '<TR><TD><b><FONT COLOR="#BF111D">Completed 7/7/19</FONT></b></TD></TR>',
        '10': '<TR><TD><b><FONT COLOR="#BF111D">Completed 14/7/19</FONT></b></TD></TR>',
        '21': '<TR><TD><b><FONT COLOR="#BF111D">Completed 31/7/19</FONT></b></TD></TR>',
        '68': '<TR><TD><b><FONT COLOR="#BF111D">Completed 18/9/19</FONT></b></TD></TR>',
        '32': '<TR><TD><b><FONT COLOR="#BF111D">Completed 21/9/19</FONT></b></TD></TR>',
        '33': '<TR><TD><b><FONT COLOR="#A9A9A9">Attempted 30/9/19</FONT></b></TD></TR>'
              '<TR><TD><b><FONT COLOR="#BF111D">Completed 6/10/19</FONT></b></TD></TR>',
        '40': '<TR><TD><b><FONT COLOR="#BF111D">Completed 9/11/19</FONT></b></TD></TR>',
        '41': '<TR><TD><b><FONT COLOR="#BF111D">Completed 16/11/19</FONT></b></TD></TR>',
        '37': '<TR><TD><b><FONT COLOR="#BF111D">Completed 14/12/19</FONT></b></TD></TR>',
        '47': '<TR><TD><b><FONT COLOR="#BF111D">Completed 11/01/20</FONT></b></TD></TR>'
              '<TR><TD><i><FONT COLOR="#BF111D">Chest left</FONT></i></TD></TR>',
        '17': '<TR><TD><b><FONT COLOR="#BF111D">Completed 12/01/20</FONT></b></TD></TR>',
        '13': '<TR><TD><b><FONT COLOR="#BF111D">Completed 16/01/20</FONT></b></TD></TR>',
        '15': '<TR><TD><b><FONT COLOR="#A9A9A9">Attempted 01/02/20</FONT></b></TD></TR>',
        '22': '<TR><TD><b><FONT COLOR="#BF111D">Completed 15/02/20</FONT></b></TD></TR>',
        '31': '<TR><TD><b><FONT COLOR="#BF111D">Completed 16/02/20</FONT></b></TD></TR>',
        '38': '<TR><TD><b><FONT COLOR="#A9A9A9">Attempted 23/02/20</FONT></b></TD></TR>'
              '<TR><TD><b><FONT COLOR="#BF111D">Completed 01/03/20</FONT></b></TD></TR>',
        '44': '<TR><TD><b><FONT COLOR="#BF111D">Completed 08/03/20</FONT></b></TD></TR>',
        # Unsure of dates for these two
        '48': '<TR><TD><b><FONT COLOR="#A9A9A9">Attempted 16/03/20</FONT></b></TD></TR>'
              '<TR><TD><b><FONT COLOR="#BF111D">Completed 23/03/20</FONT></b></TD></TR>',
    })

    for block in scenario_blocks:
        with dot.subgraph(name=f"cluster_{block['name']}") as cluster:
            cluster.attr(label=block['desc'], fontsize='40')
            for i in block['scenarios']:
                image_file = f"locations/location_{i}.png"
                assert os.path.isfile(image_file), f"Expected image file {image_file}"
                label = f"""<<TABLE BORDER="0">
                            <TR><TD><IMG SCALE="TRUE" SRC="{image_file}"/></TD></TR>
                            <TR><TD><b>{scenario_names[str(i)]}</b></TD></TR>
                            <TR><TD><b>{coordinate_labels[str(i)]}</b></TD></TR>
                            {completion_dict[str(i)]}
                            </TABLE>>"""
                print(label)
                cluster.node(name=str(i),
                         label=label,
                         fontname='times',
                         fontsize='30',
                         penwidth='0')

    for i in other_scenarios:
        image_file = f"locations/location_{i}.png"
        assert os.path.isfile(image_file), f"Expected image file {image_file}"
        label = f"""<<TABLE BORDER="0">
                    <TR><TD><IMG SCALE="TRUE" SRC="{image_file}"/></TD></TR>
                    <TR><TD><b>{scenario_names[str(i)]}</b></TD></TR>
                    <TR><TD><b>{coordinate_labels[str(i)]}</b></TD></TR>
                    {completion_dict[str(i)]}
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

    # dot.edge('1', '1to2', arrowhead='none')
    # dot.node(name='1to2', penwidth='0', label='Continue through the lair')
    # dot.edge('1to2', '2')

    add_edge(dot, 1, 2, "Continue", linked=True)
    add_edge(dot, 1, 68, "Chest loot", unusual=True)
    add_edge(dot, 2, 3, "Help Jekserah")
    add_edge(dot, 2, 4, "Investigate Gloom")
    add_edge(dot, 3, 82, "Road event", unusual=True)
    add_edge(dot, 3, 8, "Help Jekserah")
    add_edge(dot, 3, 9, "Spy on Jekserah")
    add_edge(dot, 8, 7, "Find Jekserah")
    add_edge(dot, 8, 13, "Ask enchanter for help")
    add_edge(dot, 8, 14, "Ask enchanter for help")
    add_edge(dot, 8, 7, "Spy on Jekserah")
    add_edge(dot, 14, 7, "Help from Hail")
    add_edge(dot, 14, 19, "Help from Hail")
    add_edge(dot, 14, 31, "Help from Hail")
    add_edge(dot, 14, 43, "Help from Hail")
    add_edge(dot, 43, 26, "Use water-breathing")
    add_edge(dot, 43, 37, "Use water-breathing")
    add_edge(dot, 7, 20, "Fight Jekserah")
    add_edge(dot, 20, 28, "Jekserah's warning")
    add_edge(dot, 20, 16, "Help Captain")
    add_edge(dot, 20, 18, "Help Captain")
    add_edge(dot, 16, 24, "Follow the Voice")
    add_edge(dot, 16, 25, "Continue ascent", linked=True)
    add_edge(dot, 24, 64, "Chest loot", unusual=True)
    add_edge(dot, 24, 32, "Help the Voice")
    add_edge(dot, 24, 30, "Investigate the Voice")
    add_edge(dot, 25, 34, "Fight the Drake", linked=True)
    add_edge(dot, 25, 33, "Help the Drake")
    add_edge(dot, 4, 5, "Disrupt cult")
    add_edge(dot, 4, 6, "Help cult")
    add_edge(dot, 5, 10, "Enter the void", linked=True)
    add_edge(dot, 5, 14, "Close the void")
    add_edge(dot, 5, 19, "Close the void")
    add_edge(dot, 10, 21, "Fight the Demon", linked=True)
    add_edge(dot, 10, 22, "Find artifact")
    add_edge(dot, 32, 61, "Pyper's Personal Quest")
    add_edge(dot, 32, 33, "Find vessel")
    add_edge(dot, 32, 40, "Find vessel")
    add_edge(dot, 40, 41, "Continue", linked=True)
    add_edge(dot, 37, 47, "Continue", linked=True)
    add_edge(dot, 37, 17, "Chest loot", unusual=True)
    add_edge(dot, 47, 51, "End corruption")
    add_edge(dot, 17, 71, "Chest loot", unusual=True)
    add_edge(dot, 13, 15, "Gain power")
    add_edge(dot, 22, 35, "Fight for evil")
    add_edge(dot, 22, 36, "Fight against evil")
    add_edge(dot, 22, 31, "Artifact to Hail")
    add_edge(dot, 31, 38, "Find evil")
    add_edge(dot, 31, 39, "Find evil")
    add_edge(dot, 38, 44, "Help Orchid village")
    add_edge(dot, 38, 48, "Find evil in forest")

    dot.render('Gloomhaven_scenario_route.gv', view=True)


if __name__ == "__main__":
    build_graph()
