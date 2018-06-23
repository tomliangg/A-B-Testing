# python ab_analysis.py searches.json
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

OUTPUT_TEMPLATE = (
    '"Did more/less users use the search feature?" p-value: {more_users_p:.3g}\n'
    '"Did users search more/less?" p-value: {more_searches_p:.3g}\n'
    '"Did more/less instructors use the search feature?" p-value: {more_instr_p:.3g}\n'
    '"Did instructors search more/less?" p-value: {more_instr_searches_p:.3g}'
)

# Did more users use the search feature? (More precisely: did a different fraction of users have search count > 0?)

# Did users search more often? (More precisely: is the number of searches per user different?)

searchdata_file = sys.argv[1]
search_data = pd.read_json(searchdata_file, orient='records', lines=True)
"""
Users with an odd-numbered uid were shown a new-and-improved search box. Others were shown the original design.
format like:
        is_instructor  login_count  search_count   uid
0             True            1             2   6061521
1            False            4             0  11986457
2            False            1             0  15995765
...
679          False            2             0   6454817
680          False            2             3   9276990
"""

# Separate the users who use new search and who use original search
new_search_data = search_data[search_data['uid']%2==1]
old_search_data = search_data[search_data['uid']%2==0]

new_search_at_least_once = new_search_data[new_search_data['search_count']>0]['uid'].count()
new_search_never = new_search_data[new_search_data['search_count']==0]['uid'].count()

old_search_at_least_once = old_search_data[old_search_data['search_count']>0]['uid'].count()
old_search_never = old_search_data[old_search_data['search_count']==0]['uid'].count()

"""
contingency table:
                      Used at least once        Never used
New Search Engine:  new_search_at_least_once    new_search_never
Old Search Engine:  old_search_at_least_once    old_search_never
"""

contingency = [[new_search_at_least_once, new_search_never],
                [old_search_at_least_once, old_search_never]]

chi2, more_searches_p, dof, expected = stats.chi2_contingency(contingency)
# I am getting p (~0.168) > 0.05 so we might conclude that the new search makes no difference 


# Reading through the exercise documentation, it seems like we are expected to use chi-square to solve the searching problem only. As for login question, I just assume that we need to use nonparametric test to solve it
more_users_p = stats.mannwhitneyu(new_search_data['login_count'], old_search_data['login_count']).pvalue
# pvalue for users login is 0.107 > 0.05 so users use the new search as frequent as the old search


# Only looking at the instructors
new_search_data_instructors = new_search_data[new_search_data['is_instructor']==True]
old_search_data_instructors = old_search_data[old_search_data['is_instructor']==True]

new_search_at_least_once_instructors = new_search_data_instructors[new_search_data_instructors['search_count']>0]['uid'].count()
new_search_never_instructors = new_search_data_instructors[new_search_data_instructors['search_count']==0]['uid'].count()

old_search_at_least_once_instructors = old_search_data_instructors[old_search_data_instructors['search_count']>0]['uid'].count()
old_search_never_instructors = old_search_data_instructors[old_search_data_instructors['search_count']==0]['uid'].count()

contingency_instructors = [[new_search_at_least_once_instructors, new_search_never_instructors],
                [old_search_at_least_once_instructors, old_search_never_instructors]]

chi2_instr, more_instr_searches_p, dof_instr, expected_instr = stats.chi2_contingency(contingency_instructors)
# pvalue 0.052 > 0.05 so we still conclude that the new search usage is not different from the old search's among the instructors

more_instr_p = stats.mannwhitneyu(new_search_data_instructors['login_count'], old_search_data_instructors['login_count']).pvalue
# pvalue 0.449 > 0.05 so we conclude again that the new search's user login frequency is not different from the old search's among the instructors


print(OUTPUT_TEMPLATE.format(
    more_users_p=more_users_p,
    more_searches_p=more_searches_p,
    more_instr_p=more_instr_p,
    more_instr_searches_p=more_instr_searches_p,
))