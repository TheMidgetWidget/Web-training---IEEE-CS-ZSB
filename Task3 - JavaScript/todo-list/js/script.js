// DELETE LISTENER
document.getElementsByName("li").forEach(e => e.addEventListener("click", removeChild));

// INPUT LISTENER
inputField = document.getElementById("list-input");
inputField.addEventListener("keyup", function (event) {
    if (event.key == "Enter" && inputField.value.length > 0) {
        var li = document.createElement("li");
        li.appendChild(document.createTextNode(inputField.value));
        li.addEventListener("click", removeChild);
        document.getElementById("todo-list").appendChild(li);
        inputField.value = "";
    }
});

// helper function
function removeChild() {
    this.parentNode.removeChild(this);
}