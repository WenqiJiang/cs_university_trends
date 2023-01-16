from rank import get_university_ranking

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import FuncFormatter

plt.style.use('ggplot')

if __name__ == "__main__":


    """ Asia """

    uni_list_hk = ['University of Hong Kong', 
        'HKUST',
        'Chinese University of Hong Kong']

    uni_list_cn = ['Tsinghua University', 
        'Peking University',
        'Shanghai Jiao Tong University',
        'Zhejiang University',
        'HUST']

    """ EU """
    uni_list_eu = ['ETH Zurich', 
        'EPFL',
        'Max Planck Society',
        'TU Munich']

    uni_list_uk = [
        'University of Cambridge',
        'University of Oxford',
        'Imperial College London',
        'University of Edinburgh']

    """ NA  """

    uni_list_ca = ['University of Toronto',
        'University of British Columbia',
        'University of Waterloo',
        'Simon Fraser University']

    uni_list_us = [
        'Massachusetts Institute of Technology',
        'Stanford University',
        'Univ. of California - Berkeley',
        'Carnegie Mellon University', 
        'University of Washington',
        'Univ. of Illinois at Urbana-Champaign', 
        'University of Michigan',
        'Cornell University',
        'University of Chicago',
        'Columbia University',
        'Princeton University',
        'Univ. of California - Los Angeles',
        'University of Pennsylvania',
        'University of Texas at Austin',
        'University of Wisconsin - Madison',
        'Univ. of California - San Diego',
        'Georgia Institute of Technology', 
        'Purdue University', 
        'Yale University',
        'Harvard University',
        'Brown University']

    university_names = uni_list_us
    # university_names = uni_list_hk + uni_list_cn + uni_list_eu + uni_list_uk + uni_list_ca + uni_list_us

    html_list = ['./html/csrankings_systems_1990_1999.html', 
        './html/csrankings_systems_2000_2009.html', 
        './html/csrankings_systems_2010_2019.html', 
        './html/csrankings_systems_2020_2022.html']
    year_tags = ['1990~1999', '2000~2009', '2010~2019', '2020~2022']
    assert len(html_list) == len(year_tags)

    rank_trend_dict = dict()
    for university_name in university_names:
        rank_trend_dict[university_name] = [np.nan] * len(html_list)

    for i, html_dir in enumerate(html_list):
        rank_dict = get_university_ranking(html_dir, university_names)
        for key in rank_dict:
            rank_trend_dict[key][i] = rank_dict[key]
        print('\n', html_dir)
        # print(rank_dict)
        # ranks = []
        # for key in rank_dict:
        #     if key in uni_list_us:
        #         rank = rank_dict[key]
        #         print("{}\trank: {}".format(key, rank))
        #         ranks.append(rank)
        # print("average rank: {}".format(np.average(ranks)))

    print(rank_trend_dict)

    fig, ax = plt.subplots(1, 1, figsize=(8, 3))

    label_font = 16
    markersize = 8
    tick_font = 14

    plots = []
    for university_name in university_names:
        plot = ax.plot(year_tags, rank_trend_dict[university_name], markersize=markersize)
        plots.append(plot)

    ax.legend([plot[0] for plot in plots], university_names, loc=(0, 1.1), fontsize=label_font)
    ax.tick_params(top=False, bottom=True, left=True, right=False, labelleft=True, labelsize=tick_font)
    ax.get_xaxis().set_visible(True)
    ax.set_xlabel('year', fontsize=label_font)
    ax.set_ylabel('rank', fontsize=label_font)

    ax.set_ylim([1, 150])
    ax.invert_yaxis()

    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)

    plt.rcParams.update({'figure.autolayout': True})

    plt.savefig('./img/plot.png', transparent=False, dpi=200, bbox_inches="tight")
    plt.show()