import numpy as np
class Statictics:
    def mean(self, data):
        total_sum = sum(data)
        no = len(data)
        return total_sum / no
        
    def quartiles(self, datas, quartile):
        data = sorted(datas)
        length = len(data)
        
        if (quartile * (length + 1)) % 4 == 0:
            q = data[((quartile * (length + 1)) // 4) - 1]
            print(q)

        else:
            th_item = quartile * (length + 1) // 4
            q = (data[th_item - 1] + data[th_item]) / 2
        return q

stats = Statictics()
median = stats.quartiles([3, 4, 2, 5, 2, 5, 2, 5, 2, 4, 2], 3)
print(median)
print(np.percentile([3, 4, 2, 5, 2, 5, 2, 5, 2, 4, 2], 3))


# print(stats.mean([3, 3, 5, 2, 4, 2]))