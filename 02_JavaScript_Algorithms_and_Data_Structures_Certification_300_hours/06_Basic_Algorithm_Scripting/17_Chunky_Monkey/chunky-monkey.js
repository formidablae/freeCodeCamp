function chunkArrayInGroups(arr, size) {
    return arr.reduce((acc, cur, i) => {
        if (i % size === 0) {
            acc.push([])
        }
        acc[acc.length - 1].push(cur)
        return acc
    }, []);

}

chunkArrayInGroups(["a", "b", "c", "d"], 2);
