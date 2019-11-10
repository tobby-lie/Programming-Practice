class Solution:
    def lengthOfLongestSubstring(self, str: string) -> int:
        '''
        :type str: string
        :rtype: int
        '''
        n = len(str) # n is length of str passed in
        ans = 0 # ans is initialized to 0, this will ultimately be returned
        char_map = {} # in the format of char:indx to show each character's most recent index as the window slides
        i = 0 # i starts at 0, represents the start point of the sliding window
        
        # Overall complexity: O(n) * O(1) = O(n)
        
        # loop from j = 0 to j = n - 1
        for j in range(n): # complexity: O(n) -> go through all elements (0 - (n - 1))
            # if char_map contains str[j]
            if str[j] in char_map: # complexity: O(1) -> hashtable search
                i = max(char_map[str[j]], i) # i equals max of most recent index of str[j] and i, shift i to new start point if needed
            ans = max(ans, j - i + 1) # ans is equal to max of ans and j - i + 1 which is current window size (substring)
            char_map[str[j]] = j + 1 # most recent index of str[j] is equal to j + 1
        return ans