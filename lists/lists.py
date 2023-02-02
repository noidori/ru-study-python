class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        result = []
        for x in input_list:
            if x > 0:
                x = max(input_list)
                result.append(x)
            else:
                result.append(x)
        return result

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        start = 0
        end = len(input_list) - 1
        while start <= end:
            mid = (start + end) // 2
            if query == input_list[mid]:
                return mid
            if query < input_list[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
