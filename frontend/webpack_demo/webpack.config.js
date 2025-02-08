const path = require('path');

module.exports = {
  mode: 'development',
  entry: ['./src/index.js'], // Entry point of the application
  output: {
      path: path.resolve(__dirname, 'dist'), // Output directory
      filename: "[name].[hash:4].bundle.js", // Output file name
      // clean: true, // Clean the output directory before each build
  },
  // loader
  module:{
    rules:[
      {
      }
    ]
  }
  
};