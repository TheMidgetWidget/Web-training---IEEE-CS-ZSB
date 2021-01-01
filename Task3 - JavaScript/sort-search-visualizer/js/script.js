async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// array
var items = new Array(100);

for (var i = 0; i < 100; i++) {
    items[i] = Math.floor(Math.random() * 10 + 1)
}

// populate page
var draw = function () {
    items.forEach(i => {
        var div = document.createElement("div");
        div.style.height = (i * 10) + "%";
        div.setAttribute("class", "list-item");
        document.getElementById("list").appendChild(div);
    });
};

draw();

// quick sort
async function swap(items, leftIndex, rightIndex) {
    await sleep(10);
    console.log(items)
    var temp = items[leftIndex];
    items[leftIndex] = items[rightIndex];
    items[rightIndex] = temp;
    var list = document.getElementById("list");
    list.innerHTML = '';
    draw();
}

async function quickSort(array, left, right) {
    if (left < right - 1) {
        var pivot = left + right >> 1;
        pivot = await partition(array, left, right, pivot);
        await quickSort(array, left, pivot);
        await quickSort(array, pivot + 1, right);
    }
}

async function partition(array, left, right, pivot) {
    var pivotValue = array[pivot];
    await swap(array, pivot, --right);
    for (var i = left; i < right; ++i) {
        if (array[i] < pivotValue) {
            await swap(array, i, left++);
        }
    }
    await swap(array, left, right);
    return left;
}

document.getElementById("clicker").addEventListener("click", event => {
    quickSort(items, 0, items.length - 1);
});
