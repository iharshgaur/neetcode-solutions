class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded_str = "";
        for (let word of strs) {
            encoded_str += `${word.length}#${word}`;
        }
        return encoded_str;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let i = 0;
        const result = [];
        // If str is "", the loop never starts, returning an empty array []
        while (i < str.length) {
            let j = str.indexOf("#", i);
            let length = parseInt(str.substring(i, j));
            // ... logic to extract content
            i = nextPosition;
        }
        return result;
    }
}
