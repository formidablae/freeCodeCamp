function titleCase(str) {
    return str === '' ? '' : str.toLowerCase().split(' ').map(word => word.charAt(0).toUpperCase() + word.substr(1)).join(' ');
}

console.log(titleCase("I'm a little tea pot"));
