karma = require("./karma.conf")

module.exports = function (config) {
    config.set(
    {
      ...karma(config),
      ...{
        proxies: {
          '/api/': 'http://localhost:8000/api/',
        },
        client: {
          clearContext: false,
          jasmine: {timeoutInterval: 5000}
        },
      }
    }
  );
};




