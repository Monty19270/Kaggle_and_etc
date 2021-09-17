def news_dissemination(n: int, m: int, groups: list) -> list:
    dict_news = dict()
    dict_peoples = dict()
    check_list = list()
    for number_group in range(m):
        if len(groups[number_group][1:]) == 0:
            continue
        else:
            dict_news[number_group + 1] = groups[number_group][1:]

    for people in range(n):
        dict_peoples[people + 1] = []



    return check_list


# def init_talk_graph(dict_news: dict, dict_peoples: dict):
#     index = 0
#     for groups, peoples in dict_news.items():
#         if len(peoples) == 0:
#             continue
#         else:
#             check_list = peoples
#             while len(check_list) != 0:
#                 people = check_list.pop(index)
#                 for man in check_list:
#                     if man not in dict_peoples[people]:
#                         dict_peoples[people].append(man)
#                         dict_peoples[man].append(people)
#                     else:
#                         continue
#     return dict_peoples


# def find_all_native(linked_list: dict, people: int, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(people)
#     for next_people in set(linked_list[people]) - visited:
#         find_all_native(linked_list, next_people, visited)
#     return visited


