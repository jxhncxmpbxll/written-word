const webpack = require('webpack');
const path = require('path');
const SRC_DIR = path.resolve(__dirname, './src/index.js');
const PUBLIC_DIR = path.resolve(__dirname, './dist');

module.exports = {
    entry: ['@babel/polyfill', SRC_DIR],
    output: {
      path: PUBLIC_DIR,
      filename: 'bundle.js'
    },
    module: {
      rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: ['babel-loader']
        },
        {
          test: /\.(?:ico|gif|png|jpg|jpeg)$/i,
          type: 'asset/resource'
        },
        {
          test: /\.(woff(2)?|eot|ttf|otf|svg)$/,
          type: 'asset/inline'
        },
        {
          test: /\.css$/,
          use: [
            {loader: 'style-loader'},
            {loader: 'css-loader', options: {modules: true}}
          ]
        }
      ],
    },
    mode: 'development'
}