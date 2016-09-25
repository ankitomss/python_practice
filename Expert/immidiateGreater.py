def immidiateGreater(nums):
    n = len(nums)
    st = [nums[n-1]]
    out = [nums[n-1]]
    for i in range(len(nums)-2, -1, -1):
        while st and st[-1] < nums[i]:
            st.pop()

        out.insert(0, st[-1] if st else nums[i])
        st.append(nums[i])
    return out

nums = [5,6,3,10,9,12]
print immidiateGreater(nums)