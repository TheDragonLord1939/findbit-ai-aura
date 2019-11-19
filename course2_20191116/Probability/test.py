# -*- coding: utf-8 -*-

table_titles = ['症状', '职业', '疾病']
table = [['打喷嚏', '护士', '感冒'],
         ['打喷嚏', '农夫', '过敏'],
         ['头痛', '建筑工人', '脑震荡'],
         ['头痛', '建筑工人', '感冒'],
         ['打喷嚏', '教师', '感冒'],
         ['头痛', '教师', '脑震荡']]


def probability_cal(table, column, val):
    p = list(filter(lambda r: r[column] == val, table))
    p = len(p) / len(table)
    return p


if __name__ == "__main__":
    # ['打喷嚏', '建筑工人', '感冒']
    Pa = probability_cal(table, 0, '打喷嚏')
    Pb = probability_cal(table, 1, '建筑工人')
    Pc = probability_cal(table, 2, '感冒')
    print('Pa=%0.2f,Pb=%0.2f,Pc=%0.2f' % (Pa, Pb, Pc))

    table = list(filter(lambda r: r[2] == '感冒', table))
    Pa_c = probability_cal(table, 0, '打喷嚏')
    Pb_c = probability_cal(table, 1, '建筑工人')
    print('Pa_c=%0.2f,Pb_c=%0.2f' % (Pa_c, Pb_c))

    # Pc_ab = Pab_c * Pc / Pab
    Pc_ba = (Pa_c * Pb_c) * Pc / (Pa * Pb)
    print('Pc_ba=%0.2f' % (Pc_ba))
