const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: './assets/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname, 'sato', 'static'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        enforce: 'pre',
        use: ['source-map-loader'],
      },
      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.s[ac]ss$/i,
        use: [
          "style-loader",
          "css-loader",
          "sass-loader",
        ],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif|ico)$/i,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]',
          outputPath: (url, resourcePath, context) => {
            // For email backwards compatibility, logos must be in 'logos' directory.
            if (/logos/.test(resourcePath)) {
              return `img/logos/${url}`;
            }

            return `img/${url}`;
          },
        },
      },
      {
        test: /\.(woff|woff2|eot|ttf|otf)$/i,
        loader: 'file-loader',
        options: {
          name: 'fonts/[name].[ext]',
        },
      },
    ],
  },
  plugins: [
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      jquery: 'jquery'
    }),
  ],
  watch: true,
};
