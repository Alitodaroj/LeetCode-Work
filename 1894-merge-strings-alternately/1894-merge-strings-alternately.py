class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        a=0
        b=0
        st=[]
        while a < len(word1) and b < len(word2):
            st.append(word1[a])
            st.append(word2[b])
            a+=1
            b+=1
        while b < len(word2):
            st.append(word2[b])
            b+=1
        while a < len(word1):
            st.append(word1[a])
            a+=1
        return "".join(st)