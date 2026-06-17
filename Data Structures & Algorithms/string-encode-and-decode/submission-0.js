class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let encoded_str = strs.join("#")
        return encoded_str
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let decoded_str = str.split("#")
        return decoded_str
    }
}
