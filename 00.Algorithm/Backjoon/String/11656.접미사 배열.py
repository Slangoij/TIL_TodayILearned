s = input().strip()
suffix = [s[i:] for i in range(len(s))]
suffix.sort()
print("\n".join(suffix))