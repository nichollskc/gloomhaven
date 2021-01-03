from collections import OrderedDict
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

    all_attempts = OrderedDict()
    for scenario_num, attempt_info in completion_dict.items():
        print(attempt_info)
        attempts = re.findall(r'COLOR="#[\w]{6}">(\w+) (\d+/\d+/\d\d)', attempt_info)
        loot_left = re.findall(r'COLOR="#[\w]{6}">([\w ]+ left)', attempt_info)

        for attempt in attempts:
            print(attempt)
            attempt_dict = {
                "scenario": int(scenario_num),
            }
            if attempt[0] != "Completed":
                attempt_dict["failure"] = True
            attempt_date = attempt[1]
            all_attempts[attempt_date] = attempt_dict

    print(all_attempts)

    return all_attempts

ATTEMPTS = convert_completion_dict_yaml()
with open("tmp/scenario_info.yml", "w") as f:
    yaml.dump(ATTEMPTS, f)
