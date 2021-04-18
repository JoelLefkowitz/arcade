karma = require("./karma.conf")

module.exports = function (config) {
  config.set(karma(config));
};