import random
import json
import math
import pandas as pd


def random_group(num):
    # generate min teams
    team_num = math.ceil(num/9)
    print('min team num is', team_num)
    # generate random num for team member
    team_map = {}
    for i in range(num):
        set_team_map_by_random(team_map, i + 1)
    print('team map is', json.dumps(team_map))
    # ordered by random number
    sorted_team_map = sorted(team_map.items(), key=lambda item: item[0])
    sorted_team_list = [item[1] for item in sorted_team_map]
    print('sorted team list is', sorted_team_list)
    final_team_map = {}
    for i in range(team_num):
        final_team_map[i + 1] = []
    for index, value in enumerate(sorted_team_list):
        final_team = index % team_num + 1
        final_team_map[final_team].append(value)
    print('final team map is', json.dumps(final_team_map))
    return final_team_map


def set_team_map_by_random(team_map, index):
    key = random.random()
    if key in team_map.keys():
        set_team_map_by_random(team_map, index)
    else:
        team_map[key] = index


def generate_team_csv(file_path):
    try:
        # read source data from csv file
        data = pd.read_csv(file_path)
        data_map = {}
        for _, row in data.iterrows():
            index, email = row['id'], row['email']
            data_map[index] = email
        print(data_map)
        # generate random order
        team_map = random_group(len(data))
        team_id_list = []
        team_member_list = []
        for (key, value) in team_map.items():
            team_id = 'Team_' + str(key)
            team_list = [team_id] * len(value)
            team_id_list.extend(team_list)
            replace_item = [data_map.get(x) for x in value]
            team_member_list.extend(replace_item)
            team_map[key] = replace_item
        print(team_map)
        # output to csv file
        dataframe = pd.DataFrame({'team_number': team_id_list, 'team_member': team_member_list})
        dataframe.to_csv("test.csv", index=False, sep=',')
    except Exception:
        print('error')


if __name__ == '__main__':
    generate_team_csv('mock-data.csv')