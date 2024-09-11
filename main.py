def mean_vs_median(numbers: list[int]) -> str:

    def get_mean(data: list[int]) -> float:
        total_sum: int = 0
        for num in data:
            total_sum += num
        return total_sum / len(data)


    def get_median(data: list[int]) -> int:

        def sort(arr: list[int]) -> list[int]:
            for i in range(len(arr)):
                for j in range(i, len(arr)):
                    if arr[i] > arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]
            return arr

        sorted_nums: list[int] = sort(data)
        mid: int = (len(sorted_nums) // 2 )
        return sorted_nums[mid]

    mean:float = get_mean(numbers)
    median: int = get_median(numbers)

    if mean > median:
        return "mean"
    elif mean < median:
        return "median"
    else:
        return "same"

if __name__ == "__main__":
    print(mean_vs_median([7, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(mean_vs_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
    print(mean_vs_median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14]))

