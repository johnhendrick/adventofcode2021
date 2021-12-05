nums = [[int(z) for z in y] for y in [x.replace('\n', '')
                                      for x in open('./input/day3.txt').readlines()]]

###Part 1:###
l = len(nums)
h = l//2
w = len(nums[0])
sums = [1 if sum([nums[j][i] for j in range(l)]) > h else 0 for i in range(w)]
gamma = int(''.join(str(y) for y in sums), 2)
epsilon = int(''.join(str(y) for y in [0 if x == 1 else 1 for x in sums]), 2)
print(gamma*epsilon)

###Part 2:###


def findnum(inputnums, mode):
    nums = inputnums.copy()
    w = len(nums[0])
    while len(nums) > 1:
        for i in range(w):
            h = len(nums)/2
            keep = 1 if sum([x[i] for x in nums]) >= h else 0
            if mode == 0:
                keep = (keep+1) % 2
            for n in inputnums:
                if len(nums) > 1 and n[i] != keep and n in nums:
                    nums.remove(n)
            print(len(nums))
    out = int(''.join(str(x) for x in nums[0]), 2)
    print('found: ', ''.join(str(x) for x in nums[0]))
    return(out)


print(findnum(nums, 1)*findnum(nums, 0))
