class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        result = []
        max_value = 0
        for x in input_list:
            if x > max_value:
                max_value = x
        for x in input_list:
            if x > 0:
                result.append(max_value)
            else:
                result.append(x)
        return result

    @staticmethod
    def search(input_list: list[int], query: int) -> int:

        def recursion(start: int, end: int) -> int:
            if start > end:
                return -1
            mid = (start + end) // 2
            if query == input_list[mid]:
                return mid
            if query < input_list[mid]:
                return recursion(start, mid - 1)
            else:
                return recursion(mid + 1, end)

        return recursion(0, len(input_list) - 1)
