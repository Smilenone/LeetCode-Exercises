def lengthOfLongestSubstring(s):
    count_dict = {}
    if s == "":
        return 0
    if len(s) == 1:
        return 1
    for i in range(len(s)):
        count_str = s[i]
        for j in range(i+1, len(s)):
            if s[j] not in count_str:
                count_str = count_str + s[j]
            elif (s[j] in count_str):
                count_dict[count_str] = len(count_str)
                break
            if j == len(s)-1:
                count_dict[count_str] = len(count_str)
    return max(count_dict.values())

s = "jbpnbwwd"
print(lengthOfLongestSubstring(s))
#######
#1、注意由于max函数不能对空值使用，所以当s=""时，要单独考虑，并且写在前面
#2、如果没有len(s) == 1这一段，那么当s='c'单字符串时，会没有返回值，导致错误
#3、 1，2两点说明，程序debug时要多试几个特殊的例子，防止低级错误
