const path = require('path');
const webpack = require('webpack');

/*
 * Webpack Plugins
 */
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

// take debug mode from the environment
const debug = (process.env.NODE_ENV !== 'production');

// Development asset host (webpack dev server)
const publicHost = debug ? 'http://localhost:2992' : '';

const rootAssetPath = path.join(__dirname, 'assets');

module.exports = {
  // configuration
  context: __dirname,
  entry: {
    main_js: './assets/js/main',
    main_css: [
      path.join(__dirname, 'node_modules', 'font-awesome', 'css', 'font-awesome.css'),
      path.join(__dirname, 'node_modules', 'bootstrap', 'dist', 'css', 'bootstrap.css'),
      path.join(__dirname, 'assets', 'css', 'style.css'),
    ],
  },
  output: {
    path: path.join(__dirname, '{{cookiecutter.app_name}}', 'static', 'build'),
    publicPath: `${publicHost}/static/build/`,
    filename: '[name].[hash].js',
    chunkFilename: '[id].[hash].js',
  },
  resolve: {
    extensions: ['.js', '.jsx', '.css'],
  },
  devtool: 'source-map',
  devServer: {
    headers: { 'Access-Control-Allow-Origin': '*' },
  },
  module: {
    loaders: [
      { test: /\.html$/, loader: 'raw-loader' },
      { test: /\.less$/, loader: ExtractTextPlugin.extract({ fallback: 'style-loader', use: 'css-loader!less-loader' }) },
      { test: /\.css$/, loader: ExtractTextPlugin.extract({ fallback: 'style-loader', use: 'css-loader' }) },
      { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: 'url-loader?limit=10000&mimetype=application/font-woff' },
      { test: /\.(ttf|eot|svg|png|jpe?g|gif|ico)(\?.*)?$/i,
        loader: `file-loader?context=${rootAssetPath}&name=[path][name].[hash].[ext]` },
      { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader', query: { presets: ['env'], cacheDirectory: true } },
    ],
  },
  plugins: [
    new ExtractTextPlugin('[name].[hash].css'),
    new webpack.ProvidePlugin({ $: 'jquery', jQuery: 'jquery' }),
    new ManifestRevisionPlugin(path.join(__dirname, '{{cookiecutter.app_name}}', 'webpack', 'manifest.json'), {
      rootAssetPath,
      ignorePaths: ['/js', '/css'],
    }),
  ].concat(debug ? [] : [
    // production webpack plugins go here
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production'),
      }
    }),
  ]),
};
