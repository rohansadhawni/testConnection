//server.js

const express = require("express");
const app = express();

// Define the /testConnection endpoint
app.get("/testConnection", (req, res) => {
  res.status(200).json({ status: "OK" });
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
