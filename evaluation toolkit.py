import random
class EM:
    def __init__(self):
        total = int(input("Total number of documents:"))
        ret = int(input("Total number of retrieved documents:"))
        rel = int(input("Total number of relevant documents:"))
        self.docs = set([f"d{x+1}" for x in range(total)])
        print("Documents:", self.docs)
        self.ret_set = set(random.sample(list(self.docs), ret))
        print("Retrieved documents:", self.ret_set)
        self.rel_set = set(random.sample(list(self.docs), rel))
        print("Relevant documents:", self.rel_set)
    def cal_metrics(self):
        tp = len(self.ret_set.intersection(self.rel_set))
        tn = len(self.docs.difference(self.ret_set.union(self.rel_set)))
        fp= len(self.ret_set.difference(self.rel_set)) 
        fn = len(self.rel_set.difference(self.ret_set))
        print("True Positive:", tp)
        print("True Negative:", tn)
        print("False Positive:", fp)
        print("False Negative:", fn)
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f_measure = 2 * precision * recall / (precision + recall)
        accuracy = (tp + tn) / (tp + tn + fp + fn)
        print("Precision:", precision)
        print("Recall:",  recall)
        print("F-measure:", f_measure)
        print("Accuracy:", accuracy)
em = EM()
em.cal_metrics()
from sklearn.metrics import average_precision_score
y_true = [0, 1, 1, 0, 1, 1]
y_score = [0.1, 0.4, 0.35, 0.8, 0.65, 0.9]
avg_precision = average_precision_score(y_true, y_score)
print(f"Average precision-recall score: {avg_precision:.6f}")
