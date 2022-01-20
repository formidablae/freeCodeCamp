function findLongestWordLength(str) {
    return str.length === 0 ? 0 : Math.max(...str.split(' ').map(word => word.length));
}

findLongestWordLength("The quick brown fox jumped over the lazy dog");
