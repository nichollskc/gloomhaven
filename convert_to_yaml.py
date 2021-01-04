import re
import yaml

def convert_completion_dict_yaml():
    completion_dict = {
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
        '48': '<TR><TD><b><FONT COLOR="#A9A9A9">Attempted 14/03/20</FONT></b></TD></TR>'
              '<TR><TD><b><FONT COLOR="#BF111D">Completed 21/03/20</FONT></b></TD></TR>',
        '39': '<TR><TD><b><FONT COLOR="#A9A9A9">Attempted 22/11/20</FONT></b></TD></TR>',
        '64': '<TR><TD><b><FONT COLOR="#BF111D">Completed 20/12/20</FONT></b></TD></TR>',
        '61': '<TR><TD><b><FONT COLOR="#BF111D">Completed 24/12/20</FONT></b></TD></TR>',
        '62': '<TR><TD><b><FONT COLOR="#BF111D">Completed 26/12/20</FONT></b></TD></TR>',
    }

    all_attempts = {}
    scenario_to_completion_date = {}
    for scenario_num, attempt_info in completion_dict.items():
        print(attempt_info)
        attempts = re.findall(r'COLOR="#[\w]{6}">(\w+) (\d+)/(\d+)/(\d\d)', attempt_info)
        loot_left = re.search(r'COLOR="#[\w]{6}">([\w ]+ left)', attempt_info)
        print(loot_left)

        for attempt in attempts:
            print(attempt)
            attempt_dict = {
                "scenario": int(scenario_num),
            }
            day = attempt[1]
            if len(day) == 1:
                day = "0" + day
            month = attempt[2]
            if len(month) == 1:
                month = "0" + month
            year = "20" + attempt[3]
            attempt_date = f"{year}/{month}/{day}"

            if attempt[0] == "Completed":
                scenario_to_completion_date[scenario_num] = attempt_date
            else:
                attempt_dict["failure"] = True

            all_attempts[attempt_date] = attempt_dict

        if loot_left:
            attempt_dict["loot_left"] = loot_left[1]


    print(all_attempts)

    return all_attempts, scenario_to_completion_date

def construct_yaml():
    edges = [
        (1, 2, "Continue", True),
        (1, 68, "Chest loot", False, True),
        (2, 3, "Help Jekserah"),
        (2, 4, "Investigate Gloom"),
        (3, 82, "Road event", False, True),
        (3, 8, "Help Jekserah"),
        (3, 9, "Spy on Jekserah"),
        (8, 7, "Find Jekserah"),
        (8, 13, "Ask enchanter for help"),
        (8, 14, "Ask enchanter for help"),
        (8, 7, "Spy on Jekserah"),
        (14, 7, "Help from Hail"),
        (14, 19, "Help from Hail"),
        (14, 31, "Help from Hail"),
        (14, 43, "Help from Hail"),
        (43, 26, "Use water-breathing"),
        (43, 37, "Use water-breathing"),
        (7, 20, "Fight Jekserah"),
        (20, 28, "Jekserah's warning"),
        (20, 16, "Help Captain"),
        (20, 18, "Help Captain"),
        (16, 24, "Follow the Voice"),
        (16, 25, "Continue ascent", True),
        (24, 64, "Chest loot", False, True),
        (24, 32, "Help the Voice"),
        (24, 30, "Investigate the Voice"),
        (25, 34, "Fight the Drake", True),
        (25, 33, "Help the Drake"),
        (4, 5, "Disrupt cult"),
        (4, 6, "Help cult"),
        (5, 10, "Enter the void", True),
        (5, 14, "Close the void"),
        (5, 19, "Close the void"),
        (10, 21, "Fight the Demon", True),
        (10, 22, "Find artifact"),
        (32, 61, "Pyper's Personal Quest"),
        (32, 33, "Find vessel"),
        (32, 40, "Find vessel"),
        (40, 41, "Continue", True),
        (37, 47, "Continue", True),
        (37, 17, "Chest loot", False, True),
        (47, 51, "End corruption"),
        (17, 71, "Chest loot", False, True),
        (13, 15, "Gain power"),
        (22, 35, "Fight for evil"),
        (22, 36, "Fight against evil"),
        (22, 31, "Artifact to Hail"),
        (31, 38, "Find evil"),
        (31, 39, "Find evil"),
        (38, 44, "Help Orchid village"),
        (38, 48, "Find evil in forest"),
        (48, 51, "End corruption"),
        (61, 74, "City event", False, True),
        (61, 62, "Lighthouse basement", True),
        (62, 72, "Town records", False, True),
    ]

    attempts_dict, scenario_to_completion_date = convert_completion_dict_yaml()
    for edge in edges:
        from_id = str(edge[0])
        to_id = str(edge[1])
        description = edge[2]
        linked = False
        unusual = False
        try:
            linked = edge[3]
        except IndexError:
            pass
        try:
            unusual = edge[4]
        except IndexError:
            pass

        attempt = scenario_to_completion_date[from_id]
        link = {"description": description}
        if unusual:
            link["unusual"] = True
        if linked:
            link["linked"] = True

        attempt_info = attempts_dict[attempt]
        if "links" in attempt_info:
            attempt_info["links"][to_id] = link
        else:
            attempt_info["links"] = {to_id: link}

    return {"attempts": attempts_dict}

ATTEMPTS = construct_yaml()
with open("tmp/scenario_info.yml", "w") as f:
    yaml.dump(ATTEMPTS, f)
