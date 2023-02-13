import numpy as np


def find_the_next_candidate(dice_value_matrix_, used_indexes_, performances_):
    candidates = set(np.arange(len(dice_value_matrix_))) - set(used_indexes_)
    sum_corr = {cand: 0 for cand in candidates}
    for cand in candidates:
        for used_index in used_indexes_:
            sum_corr[cand] += (dice_value_matrix_[cand][used_index] + (1 - performances_[cand]))

    min_value = 100
    cand_index = -1
    for key, value in sum_corr.items():
        if value < min_value:
            min_value = value
            cand_index = key

    return cand_index

def dipe():
    result_dice_list = []  # List with the dice score for each model.
    used_indexes = [result_dice_list.argsort()[-1]]  # Select the best model.
    max_number_of_models_in_ensemble = 10  # The maximum number of models in the final ensemble.
    dice_value_matrix = np.zeros((20, 20))  # Compute the dice matrix between the models => Eq.6 from paper.
    for _ in range(1, max_number_of_models_in_ensemble):
        new_index = find_the_next_candidate(dice_value_matrix, used_indexes, result_dice_list)
        used_indexes.append(new_index)

    return used_indexes # the indices of the best ensemble.

if __name__ == '__main__':
    dipe()
