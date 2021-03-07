const path = require("path");
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
  entry: path.resolve(__dirname, "src", "main.ts"),
  plugins: [
    new CopyPlugin({
      patterns: [
        path.resolve(__dirname, "src", "static"),
        { from: path.resolve(__dirname, "src", "assets"), to: "assets" },
      ],
    }),
  ],
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
  output: {
    filename: "bundle.js",
    path: path.resolve(__dirname, "dist"),
  },
};
