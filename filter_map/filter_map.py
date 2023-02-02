from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []
        for x in input_array:
            func_res = func(x)
            if func_res[0]:
                result.append(func_res[1])
        return result
