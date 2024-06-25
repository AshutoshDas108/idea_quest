import React, { useState } from "react";
import axios from "axios";

function App() {
  const [amount, setAmount] = useState("");
  const [merchant, setMerchant] = useState("");
  const [age, setAge] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [lat, setLat] = useState("");
  const [longi, setLongi] = useState("");
  const [hour, setHour] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      amount: parseFloat(amount),
      merchant: merchant,
      age: parseInt(age),
      city: city,
      state: state,
      lat: parseFloat(lat),
      longi: parseFloat(longi),
      hour: parseInt(hour)
    };

    const url = "http://localhost:8081/api/predict"; // Update the port if necessary

    try {
      const response = await axios.post(url, data);
      const responseData = response.data;
      setResponse(JSON.stringify(responseData, null, 2)); // Display response from Spring Boot API
    } catch (error) {
      console.error("Error:", error);
      setResponse("Error: " + error.message);
    }
  };

  return (
    <div className="App bg-gray-100 min-h-screen flex items-center justify-center">
      <div className="max-w-md w-full p-6 bg-white rounded-lg shadow-md">
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="flex flex-col">
            <label htmlFor="amount" className="text-gray-600">
              Amount
            </label>
            <input
              id="amount"
              type="number"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <div className="flex flex-col">
            <label htmlFor="merchant" className="text-gray-600">
              Merchant
            </label>
            <input
              id="merchant"
              type="text"
              value={merchant}
              onChange={(e) => setMerchant(e.target.value)}
              className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <div className="flex flex-col">
            <label htmlFor="age" className="text-gray-600">
              Age
            </label>
            <input
              id="age"
              type="number"
              value={age}
              onChange={(e) => setAge(e.target.value)}
              className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <div className="flex flex-col">
            <label htmlFor="city" className="text-gray-600">
              City
            </label>
            <input
              id="city"
              type="text"
              value={city}
              onChange={(e) => setCity(e.target.value)}
              className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <div className="flex flex-col">
            <label htmlFor="state" className="text-gray-600">
              State
            </label>
            <input
              id="state"
              type="text"
              value={state}
              onChange={(e) => setState(e.target.value)}
              className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <div className="flex flex-col">
            <label htmlFor="lat" className="text-gray-600">
              Latitude
            </label>
            <input
              id="lat"
              type="number"
              value={lat}
              onChange={(e) => setLat(e.target.value)}
              className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <div className="flex flex-col">
            <label htmlFor="long" className="text-gray-600">
              Longitude
            </label>
            <input
              id="longi"
              type="text"
              value={longi}
              onChange={(e) => setLongi(e.target.value)}
              className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <div className="flex flex-col">
            <label htmlFor="hour" className="text-gray-600">
              Hour
            </label>
            <input
              id="hour"
              type="number"
              value={hour}
              onChange={(e) => setHour(e.target.value)}
              className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded-md transition duration-300"
          >
            Predict
          </button>
        </form>

        {response && (
          <pre className="mt-4 text-green-600 text-sm">
            {response}
          </pre>
        )}
      </div>
    </div>
  );
}

export default App;
