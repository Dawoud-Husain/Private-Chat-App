module.exports = {
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000",
        ws: false,
        changeOrigin: true
      }
    }
  }
};

// module.exports = {
//   devServer: {
//     proxy: {
//       "^/api": {
//         target: "http://localhost:3000",
//         changeOrigin: true,
//         secure: false,
//         pathRewrite: { "^/api": "/api" },
//         logLevel: "debug",
//       },
//     },
//   },
// };
