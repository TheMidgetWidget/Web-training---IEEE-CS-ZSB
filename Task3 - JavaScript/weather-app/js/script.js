var apiKey = "acd4c672ef3521374119e83b44cb562e";
var input = document.getElementById("city-input");

input.addEventListener("keyup", function (event) {
    if (event.key == "Enter") {
        fetch('http://api.openweathermap.org/data/2.5/weather?q=' + input.value + '&units=metric&appid=' + apiKey)
            .then(response => response.json())
            .then(data => {
                changeFieldValues(data['name'], Math.ceil(data['main']['temp']) + ' °C', data['weather']['0']['description']);
            })
            .catch(err => {
                changeFieldValues();
            });
        input.value = "";
    }
});

function changeFieldValues(name, temp, description) {
    if (name == undefined || temp == undefined || description == undefined) {
        name = temp = description = "city not found!"
    }
    document.getElementById("name").innerHTML = name;
    document.getElementById("temp").innerHTML = temp;
    document.getElementById("description").innerHTML = description;
}