def shuffle( nums: List[int], n: int) -> List[int]:
        new_lst = []
        for i in range(n):
            new_lst.append(nums[i])
            new_lst.append(nums[i+n])
        return new_lst
