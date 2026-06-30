int lengthOfLongestSubstring(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    
    
    bool seen[256] = {false};
    int maxLen = 0;
    int left = 0;
    
    for (int right = 0; right < n; right++) {
        
        while (seen[s[right]]) {
            seen[s[left]] = false;
            left++;
        }
        
        
        seen[s[right]] = true;
        
        
        int currentLen = right - left + 1;
        if (currentLen > maxLen) {
            maxLen = currentLen;
        }
    }
    
    return maxLen;
}