const users = {
    Alan: {
        online: false
    },
    Jeff: {
        online: true
    },
    Sarah: {
        online: false
    }
}

function countOnline(usersObj) {
    // Only change code below this line
    let count = 0;
    for (let user in usersObj) {
        if (usersObj[user].online) {
            count++;
        }
    }
    return count;
    // Only change code above this line
}

console.log(countOnline(users));
