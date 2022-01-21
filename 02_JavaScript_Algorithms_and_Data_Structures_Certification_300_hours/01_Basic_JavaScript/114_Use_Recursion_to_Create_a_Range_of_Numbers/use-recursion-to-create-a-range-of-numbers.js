function rangeOfNumbers(startNum, endNum) {
    return startNum === endNum ? [startNum] : [startNum, ...rangeOfNumbers(startNum + 1, endNum)];
};
