class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix=''
        for i in range(len(strs[0])):  
            character=strs[0][i] 
            for word in strs:
                                    
                if i>=len(word)or word[i]!=character:
                    return prefix              

            prefix+=character
        return prefix
