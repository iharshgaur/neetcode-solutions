class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isAlphaNumeric(char) {
        const code = char.charCodeAt(0);
        return (
            (code >= 48 && code <= 57) || // 0-9
            (code >= 65 && code <= 90) || // A-Z
            (code >= 97 && code <= 122)   // a-z
        ); 
    }

    isPalindrome(s) {
        let left = 0;
        let right = s.length - 1;
        
        while (left < right) {
            // Notice the use of 'this.' here
            if (!this.isAlphaNumeric(s[left])) {
                left++;
                continue;
            }
            // And here
            if (!this.isAlphaNumeric(s[right])) {
                right--;
                continue;
            }
            
            if (s[left].toLowerCase() !== s[right].toLowerCase()) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}