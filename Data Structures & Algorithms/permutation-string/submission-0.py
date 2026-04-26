class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # Frequency arrays for 26 lowercase letters
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Initialize first window and s1 counts
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        # Check first window
        if s1_count == s2_count:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character to window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove old character from window
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            # Check if current window matches
            if s1_count == s2_count:
                return True
        
        return False