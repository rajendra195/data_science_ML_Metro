class Statictics:
    def mean(self, data):
        
        for item in data:
            sums = sum(item)
            no_of_items = len(item)
        mean = sums / no_of_items
        return mean
    
    def median(self, data):
        
        for item in data:
            n = len(item)

        if n % 2 != 0:
            median_item = (n + 1) / 2
            median = data[int(median_item) - 1]
            return median
        else:
            median_item = (n + 1) // 2
            median = (data[median_item - 1] + data[median_item]) / 2
            return median

stats = Statictics()
median = stats.median(3, 2, 5, 2, 2, 1, 1, 3)
print(median)