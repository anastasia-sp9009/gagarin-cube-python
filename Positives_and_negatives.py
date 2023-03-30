def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return [] 
    negatives = filter(lambda item: item < 0, arr)
    sumOfNegatives = sum(negatives)
    positives = list(filter(lambda item: item > 0, arr))
    countOfPositives = len(positives);
    return [countOfPositives, sumOfNegatives]
