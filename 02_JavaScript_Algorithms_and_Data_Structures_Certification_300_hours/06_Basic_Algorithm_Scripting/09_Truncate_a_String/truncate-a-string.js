function truncateString(str, num) {
    return str === '' ? '' : str.length > num ? str.substr(0, num) + '...' : str;
}

truncateString("A-tisket a-tasket A green and yellow basket", 8);
