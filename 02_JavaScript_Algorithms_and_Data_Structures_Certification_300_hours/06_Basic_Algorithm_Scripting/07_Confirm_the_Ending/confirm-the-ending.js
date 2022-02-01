function confirmEnding(str, target) {
    return str === '' ? false : str.substr(-target.length) === target;
}

confirmEnding("Bastian", "n");
