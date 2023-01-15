import numpy as np
import re

def get_university_ranking(html_file_dir, university_names):
    """
    
    Input: 
        html_file_dir of the csranking file (saved by Chrome, scroll down to make sure
         more than the first 20 universities are shown)
        university_names: a list of univerisity names, has to be the same as csrankings

    Preprocess univerisity name input: 
        e.g., >Georgia Institute of Technology</span>

    Example rank by grep:
        <tr><td>40&nbsp;&nbsp;
        here 40 is the ranking 
    """

    rank_dict = dict() # key = name, value = rank

    university_names_preprocessed = []
    for university_name in university_names:
        university_names_preprocessed.append(">" + university_name + "</span>")

    with open(html_file_dir, "r") as file:

        for line in file:
            for i, university_name_preprocessed in enumerate(university_names_preprocessed):
                if re.search(university_name_preprocessed, line):
                    rank_search = re.search('<tr><td>([0-9]+)&nbsp;', line)
                    # print(university_name)
                    # print(line)
                    rank = int(rank_search.group(1))
                    # print("University: {}\trank:{}".format(university_name, rank))

                    university_name = university_names[i]
                    if university_name in rank_dict:
                        print("A university is found multiple times... exit")
                        raise ValueError
                    else:
                        rank_dict[university_name] = rank

    for university_name in university_names:
        if university_name not in rank_dict:
            print("{} not found in the html".format(university_name))

    return rank_dict

if __name__ == '__main__':



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

    university_names = uni_list_hk + uni_list_cn + uni_list_eu + uni_list_uk + uni_list_ca + uni_list_us

    html_list = ['./html/csrankings_systems_1990_1999.html', 
        './html/csrankings_systems_2000_2009.html', 
        './html/csrankings_systems_2010_2019.html', 
        './html/csrankings_systems_2020_2022.html']

    for html_dir in html_list:
        rank_dict = get_university_ranking(html_dir, university_names)
        print('\n', html_dir)
        # print(rank_dict)
        ranks = []
        for key in rank_dict:
            if key in uni_list_us:
                rank = rank_dict[key]
                print("{}\trank: {}".format(key, rank))
                ranks.append(rank)
        print("average rank: {}".format(np.average(ranks)))

