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
        if (str === "") return [""];
        let decoded_str = [];
        let i = 0;
        while (i < str.length) {
            let j = str.indexOf("#", i);
            let length = parseInt(str.substring(i, j));
            i = j + 1;
            let content = str.substring(i, i + length);
            decoded_str.push(content);
            i += length;
        }
        return decoded_str;
    }
}
