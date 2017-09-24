const path = require('path');
const webpack = require('webpack');
const ManifestPlugin = require('webpack-manifest-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');

// input dir
const APP_DIR = path.resolve(__dirname, './');

// output dir
const BUILD_DIR = path.resolve(__dirname, './dist');

const config = {
  node: {
    fs: 'empty'
  },
  entry: {
    dashboard: ['babel-polyfill', APP_DIR + '/javascripts/dashboard.jsx']
  },
  output: {
    path: BUILD_DIR,
    filename: '[name].bundle.js',
    chunkFilename: '[name].[chunkhash].entry.js',
  },
  resolve: {
    extensions: ['.js', '.jsx', '.css']
  },
  module: {
    loaders: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: APP_DIR + '/node_modules'
      },
      {
        test: /\.jsx$/,
        loader: 'babel-loader',
        exclude: APP_DIR + '/node_modules',
        query: {
          presets: [
            'es2015',
            'react'
          ]
        }
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader'
      }
    ]
  },
  plugins: [
    new ManifestPlugin(),
    new CleanWebpackPlugin(['dist']),
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify(process.env.NODE_ENV),
      },
    }),
  ]
};

module.exports = config;
