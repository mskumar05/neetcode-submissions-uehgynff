class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        from collections import Counter
        
        # Count characters in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Sliding window pointers
        left = 0
        right = 0
        formed = 0
        
        # Character count in current window
        window_counts = {}
        
        # Result tracking
        ans = float("inf"), None, None  # (length, left, right)
        
        while right < len(s):
            # Expand window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if this character helps complete required characters
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # Contract window when we have all characters
            while left <= right and formed == required:
                char = s[left]
                
                # Update result
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove leftmost character from window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]