# Leetcode 811 medium
import collections
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # T: O(N) * O(1)
        # S: O(N)
        # subdomain → visit count
        counts = collections.defaultdict(int)
        for domain in cpdomains:
            # .split() → ["9001", "discuss.leetcode.com"]
            count, domain = domain.split()
            print(count)

            # Convert the string "9001" into integer 9001
            count = int(count)
            # Break the domain by dots.
            # Example: "discuss.leetcode.com" → ["discuss", "leetcode", "com"].
            fragments = domain.split('.')

            # For each subdomain, add the visit count (9001) to counts
            for i in range(len(fragments)):
                subdomain = ".".join(fragments[i:])
                counts[subdomain] += count

        return [f"{count} {domain}" for domain, count in counts.items()]

# Step by step
#
# len(fragments) = 3 → so i = 0, 1, 2.
#
# Iteration 1 (i = 0):
#
# fragments[0:] = ["discuss", "leetcode", "com"]
# 
# ".".join(["discuss","leetcode","com"]) = "discuss.leetcode.com"
#
# Add 9001 to counts["discuss.leetcode.com"]
#
# Iteration 2 (i = 1):
#
# fragments[1:] = ["leetcode","com"]
#
# ".".join(["leetcode","com"]) = "leetcode.com"
#
# Add 9001 to counts["leetcode.com"]
#
# Iteration 3 (i = 2):
#
# fragments[2:] = ["com"]
#
# ".".join(["com"]) = "com"
#
# Add 9001 to counts["com"]
