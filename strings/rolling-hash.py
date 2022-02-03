def polynomial_rolling_hash(str):
    p = 31
    m = 1e9 + 9
    power = 1
    curr_hash = 0
 
    for i in range(len(str)):
        curr_hash = ((curr_hash + (ord(str[i]) - ord('a') + 1) * power) % m)
        power = (power * p) % m
 
    return int(curr_hash)
 
text = "ante-test"

print(f"Hash of '{text}' = {polynomial_rolling_hash(text)}")
print(f"Hash of '{'AA'}' = {polynomial_rolling_hash('AA')}")