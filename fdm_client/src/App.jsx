import React, { useState } from "react";
import axios from "axios";

function App() {
  const [amount, setAmount] = useState("");
  const [oldBalance, setOldBalance] = useState("");
  const [newBalance, setNewBalance] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      amount: parseFloat(amount),
      oldBalance: parseFloat(oldBalance),
      newBalance: parseFloat(newBalance)
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
    <div className="App">
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
              <label htmlFor="oldBalance" className="text-gray-600">
                Old Balance
              </label>
              <input
                id="oldBalance"
                type="number"
                value={oldBalance}
                onChange={(e) => setOldBalance(e.target.value)}
                className="mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
              />
            </div>

            <div className="flex flex-col">
              <label htmlFor="newBalance" className="text-gray-600">
                New Balance
              </label>
              <input
                id="newBalance"
                type="number"
                value={newBalance}
                onChange={(e) => setNewBalance(e.target.value)}
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
    </div>
  );
}

export default App;
