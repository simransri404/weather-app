const input = document.getElementById("cityInput");
const button = document.getElementById("searchBtn");
const result = document.getElementById("result");

async function getWeather() {
  const city = input.value.trim();

  if (city === "") {
    result.innerHTML = "<p>Please enter a city name</p>";
    return;
  }

  result.innerHTML = "<p>Loading...</p>";

  try {
    const response = await fetch("/weather?city=" + city);
    const data = await response.json();

    if (!response.ok) {
      result.innerHTML = "<p>" + data.error + "</p>";
      return;
    }

    result.innerHTML =
      "<h2>" + data.city + "</h2>" +
      "<img src='https://openweathermap.org/img/wn/" + data.icon + "@2x.png'>" +
      "<p>Temperature: " + data.temp + " °C</p>" +
      "<p>Humidity: " + data.humidity + " %</p>" +
      "<p>Condition: " + data.description + "</p>";
  } catch (error) {
    result.innerHTML = "<p>Something went wrong. Try again.</p>";
  }
}

button.addEventListener("click", getWeather);
input.addEventListener("keypress", function (e) {
  if (e.key === "Enter") getWeather();
});