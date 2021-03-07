const path = require("path");
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
  entry: path.resolve(__dirname, "src", "main.ts"),
  plugins: [
    new CopyPlugin({
      patterns: [
        { from: path.resolve(__dirname, "src", "static"), to: "" },
        { from: path.resolve(__dirname, "src", "assets"), to: "assets" },
        { from: path.resolve(__dirname, "src", "python"), to: "python" },
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
